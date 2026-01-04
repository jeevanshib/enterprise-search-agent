from core.orchestrator import build_graph
from core.state import AgentState

graph = build_graph()

initial_state = AgentState(
    query="What is the leave policy during probation?"
)

final_state = graph.invoke(initial_state)

print("\nFINAL ANSWER:\n")
print(final_state["answer"])

