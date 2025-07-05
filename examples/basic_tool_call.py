from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
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

# Define a custom function to reverse a string
def reverse_string(text: str) -> str:
    """Reverse the given text"""
    return text[::-1]

# Register the custom function as a tool
reverse_tool = FunctionTool(func=reverse_string, description="A tool to reverse a string")

# Create an agent with custom tool
agent = AssistantAgent(
    name="ReverseAgent",
    model_client=ollama_client,
    system_message="You are a helpful assistant that can reverse text using the reverse_string tool",
    tools=[reverse_tool]
)

async def main():
    # Define a Task
    task = "Reverse the text 'Hello, How are you?"

    # Run the agent
    response = await  agent.run(task=task)
    print(f"Agent Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())