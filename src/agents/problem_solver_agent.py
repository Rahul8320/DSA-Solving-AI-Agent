from autogen_agentchat.agents import AssistantAgent
from autogen_core.models import ChatCompletionClient

from configs.settings import Settings

def get_problem_solver_agent(model_client: ChatCompletionClient) -> AssistantAgent:
    """
        Get an instance of DSA Problem Solver Agent

        Parameters:
            model_client: An instance of Chat Completion Client to be used in problem solver agent

        Return:
            An instance of Assistance Agent
    """

    agent = AssistantAgent(
        name= "DSAProblemSolverAgent",
        description= "An agent that solves DSA problems from the given problem statement",
        model_client= model_client,
        system_message = f'''
            You are a problem solver agent that is an expert in solving DSA problems.
            You will be working with code executor agent to execute code.
            You will be given a task and you should solved it in Python language by following bellow instruction:
                1. At the beginning of your response you have to specify your plan to solve the task.
                2. Then you should give the code in a code block (Python).
                3. You should write code in a one code block at a time and then pass it to code executor agent to execute it.
                4. Also, You should write 3 test cases for the problem statement.
                4. Once the code is executed successfully, check if all 3 test case passed.If yes, then you have the results.
                5. You should explain the code execution result.
                
            In the end once the code is executed successfully, you have to say {Settings.TERMINATION_KEYWORD} to stop the conversation. 
            '''
    )

    return agent