from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from configs.settings import Settings


class DockerExecutor:
    """
        Create and maintained docker executor
    """
    def __init__(self):
        self.__docker__ = DockerCommandLineCodeExecutor(
            image=Settings.DEFAULT_PYTHON_IMAGE,
            work_dir=Settings.DOCKER_WORK_DIR,
            timeout=Settings.CODE_EXECUTION_TIMEOUT
        )

    def get(self) -> DockerCommandLineCodeExecutor:
        """
        Get an instance of Docker command line code executor

        Return:
            An instance of Docker command line code executor
        """
        return self.__docker__

    async def start(self) -> None:
        """
        Start docker executor container
        """
        await self.__docker__.start()

    async def stop(self) -> None:
        """
        Stop docker executor container
        """
        await self.__docker__.stop()