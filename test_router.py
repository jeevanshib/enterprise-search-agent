from core.state import AgentState
from agents.context_router import context_router_agent

state = AgentState(query="What is the leave policy during probation?")
state.intent = "policy"
state.context = {}

state = context_router_agent(state)

print(state.context)
