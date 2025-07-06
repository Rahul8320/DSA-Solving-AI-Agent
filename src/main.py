import asyncio

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

from agents.code_executor_agent import DockerCodeExecutorAgent
from agents.problem_solver_agent import DSAProblemSolverAgent


async def main():
    code_executor = DockerCodeExecutorAgent()
    problem_solver_agent = DSAProblemSolverAgent().load()

    termination_condition = TextMentionTermination("STOP")

    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor.agent],
        termination_condition= termination_condition,
        max_turns= 10
    )

    try:
        await code_executor.docker.start()
        task = "Write a Python code to add two numbers."

        async for message in team.run_stream(task=task):
            print(message)
    except Exception as e:
        print(f"Error occurred: ", e)
    finally:
        await code_executor.docker.stop()

if __name__ == "__main__":
    asyncio.run(main())
