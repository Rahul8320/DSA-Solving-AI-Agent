import asyncio

from agents.code_executor import CodeExecutor


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
    await CodeExecutor.run(content=content)


if __name__ == "__main__":
    asyncio.run(main())
