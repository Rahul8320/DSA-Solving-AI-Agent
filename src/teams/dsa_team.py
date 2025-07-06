from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_core.code_executor import CodeExecutor
from autogen_core.models import ChatCompletionClient

from agents.code_executor_agent import get_code_executor_agent
from agents.problem_solver_agent import get_problem_solver_agent
from configs.settings import Settings


def get_dsa_team(model_client: ChatCompletionClient, executor: CodeExecutor) -> RoundRobinGroupChat:
    """
        Get dsa team with problem solver and code executor participants

        Parameters:
            model_client: An instance of Chat Completion Client to be used in problem solver agent
            executor: An instance of Code Executor to be used in Code Executor agent

        Return:
            An instance of Round Robin Group Chat
    """
    problem_solver_agent = get_problem_solver_agent(model_client=model_client)
    code_executor_agent = get_code_executor_agent(executor=executor)

    termination_condition = TextMentionTermination(Settings.TERMINATION_KEYWORD)

    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=Settings.TEAM_MAX_TURNS
    )

    return team