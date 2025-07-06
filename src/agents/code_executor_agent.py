from autogen_agentchat.agents import CodeExecutorAgent
from autogen_core.code_executor import CodeExecutor


def get_code_executor_agent(executor: CodeExecutor) -> CodeExecutorAgent:
    """
    Get an instance of Code Executor agent

    Parameters:
        executor: An instance of Code Executor to be used in Code Executor agent

    Return:
        An instance of Code Executor Agent
    """

    agent = CodeExecutorAgent(
        name= "CodeExecutorAgent",
        code_executor= executor
    )
    return agent