import asyncio

import streamlit as st
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.teams import RoundRobinGroupChat

from teams.dsa_team import get_dsa_team
from utils.docker_executor import DockerExecutor
from utils.model_client import get_ollama_client


async def run(docker:DockerExecutor, team: RoundRobinGroupChat, problem_statement: str):
    try:
        await docker.start()
        print(f"❇️ Docker container started")
        async for message in team.run_stream(task=problem_statement):
            if isinstance(message, TextMessage):
                print(msg:= f"💬 {message.source} : {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"🚫 Stop Reason: {message.stop_reason}")
                yield msg

        print("✅ Task Completed")
    except Exception as e:
        print(msg:= f"⚠️ Error occurred: {e}")
        yield msg
    finally:
        await docker.stop()
        print(f"🛑 Docker container stopped")



st.title("DSA Problem Solver Agent")
st.write("Welcome to our AI Agent, your personal DSA problem solver!. Here you can ask solutions to various DSA problems")

docker_executor = DockerExecutor()
ollama_client = get_ollama_client()
dsa_team = get_dsa_team(model_client=ollama_client, executor=docker_executor.get())

task = st.text_input(
    label="Give me a problem statement or question",
    value="Write a Python function to check if the given input number is odd or even number"
)

if st.button("Run"):
    st.write("⚙️ Running the Task...")

    async def prettify_message():
        async for msg in run(docker=docker_executor, team=dsa_team, problem_statement=task):
            st.markdown(msg)
            if isinstance(msg, str):
                if msg.startswith("user:"):
                    with st.chat_message(name="user", avatar="user"):
                        st.markdown(msg)
                elif msg.startswith("DSAProblemSolverAgent:"):
                    with st.chat_message(name="assistant", avatar="assistant"):
                        st.markdown(msg)
                elif msg.startswith("CodeExecutorAgent:"):
                    with st.chat_message(name="assistant", avatar="assistant"):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                st.markdown(f"🚫 Stop Reason: {msg.stop_reason}")

    asyncio.run(prettify_message())
