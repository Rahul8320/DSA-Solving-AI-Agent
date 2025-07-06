from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor


class CodeExecutor:
    """Code executor class to create and run code executor agent in docker"""

    @classmethod
    async def run(cls, content: str, image: str = "python:3-slim") -> None:
        """Run code using code executor agent in docker

            :parameter
                - content: code content in string
                - image: respected docker image to run this code, default "python:3-slim"
        """

        docker = DockerCommandLineCodeExecutor(
            image= image,
            work_dir= "/tmp",
            timeout= 120
        )
        agent = CodeExecutorAgent(
            name= "CodeExecutorAgent",
            code_executor= docker
        )
        task = TextMessage(content= content, source= "user")

        try:
            await docker.start()
            response = await agent.on_messages(
                messages= [task],
                cancellation_token= CancellationToken()
            )
            print("Response: ", response.chat_message)
        except Exception as e:
            print(f"Error occurred: ", e)
        finally:
            await docker.stop()