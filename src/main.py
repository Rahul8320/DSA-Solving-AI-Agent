from autogen_agentchat.ui import Console

import asyncio

from teams.dsa_team import get_dsa_team
from utils.docker_executor import DockerExecutor
from utils.model_client import get_ollama_client


async def main():
    docker_executor = DockerExecutor()
    ollama_client = get_ollama_client()

    dsa_team = get_dsa_team(model_client=ollama_client, executor=docker_executor.get())

    try:
        await docker_executor.start()
        task = input("Please give me a problem statement: ")

        stream = dsa_team.run_stream(task=task)
        await Console(stream=stream)
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        await docker_executor.stop()

if __name__ == "__main__":
    asyncio.run(main())
