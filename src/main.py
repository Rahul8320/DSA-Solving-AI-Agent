import asyncio

from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

from agents.code_executor_agent import DockerCodeExecutorAgent


async def main():
    content: str = '''Here is some code
```python
def add(a:int, b:int)->int:
    return a+b
    
print('Hello world')
result = add(5,3)
print(f"Sum of 5 and 3 is: {result}")
```
'''
    task = TextMessage(content=content, source="user")
    code_executor = DockerCodeExecutorAgent()

    try:
        await code_executor.docker.start()
        response = await code_executor.agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print("Response: ", response.chat_message)
    except Exception as e:
        print(f"Error occurred: ", e)
    finally:
        await code_executor.docker.stop()

if __name__ == "__main__":
    asyncio.run(main())
