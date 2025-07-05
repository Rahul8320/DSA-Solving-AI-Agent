from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.ollama import OllamaChatCompletionClient
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()
ollama_url: str = os.getenv("OLLAMA_URL", "")

if not ollama_url:
    raise ValueError("Please set the OLLAMA Host Url into 'OLLAMA_URL' environment variable")

# Initialize the OLLAMA model client
ollama_client = OllamaChatCompletionClient(model="llama3.2:1b", host=ollama_url)

# Initialize Assistant Agent
assistant = AssistantAgent(
    name="Assistant",
    description="A helpful assistance that can write poetry.",
    model_client=ollama_client,
    system_message="You are a helpful assistant."
)

# Initialize the User Proxy Agent
user_proxy_agent = UserProxyAgent(
    name="UserProxy",
    description="A proxy agent that represents the user.",
    input_func=input
)

# Termination condition
termination = TextMentionTermination("APPROVE")

# Create a team with the assistant and user proxy agent
team = RoundRobinGroupChat(
    participants=[assistant, user_proxy_agent],
    termination_condition=termination
)

async def main():
    stream = team.run_stream(task="Write a 4 line poem about the ocean")

    await Console(stream=stream)

if __name__=="__main__":
    asyncio.run(main())