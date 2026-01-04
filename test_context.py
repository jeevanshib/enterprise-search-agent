from core.state import AgentState
from agents.context_manager import context_manager_agent

state = AgentState(query="What is the leave policy during probation?")
state.intent = "policy"

state = context_manager_agent(state, session_id="user_1")

print(state.context)
