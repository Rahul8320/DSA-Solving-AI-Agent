from autogen_agentchat.agents import CodeExecutorAgent
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor


class DockerCodeExecutorAgent:
    """Initialize a code executor agent with docker command line code executor"""

    def __init__(self):
        self.docker = DockerCommandLineCodeExecutor(
            image= "python:3-slim",
            work_dir= "/tmp",
            timeout= 120
        )

        self.agent = CodeExecutorAgent(
            name= "CodeExecutorAgent",
            code_executor= self.docker
        )