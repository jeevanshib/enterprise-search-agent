from core.state import AgentState
from agents.structured_search import structured_search_agent

state = AgentState(query="What is the probation duration?")
state = structured_search_agent(state)

print(state.retrieved_structured)
