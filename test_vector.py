from core.state import AgentState
from agents.vector_search import vector_search_agent

state = AgentState(query="What is the leave policy during probation?")
state = vector_search_agent(state)

print(state.retrieved_docs)
