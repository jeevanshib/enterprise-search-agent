from langgraph.graph import StateGraph, END

from core.state import AgentState
from agents.query_understanding import query_understanding_agent
from agents.context_manager import context_manager_agent
from agents.context_router import context_router_agent
from agents.vector_search import vector_search_agent
from agents.structured_search import structured_search_agent
from agents.evidence_aggregator import evidence_aggregation_agent
from agents.answer_synthesis import answer_synthesis_agent


def build_graph():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("query_understanding", query_understanding_agent)
    graph.add_node("context_manager", context_manager_agent)
    graph.add_node("context_router", context_router_agent)
    graph.add_node("vector_search", vector_search_agent)
    graph.add_node("structured_search", structured_search_agent)
    graph.add_node("evidence_aggregation", evidence_aggregation_agent)
    graph.add_node("answer_synthesis", answer_synthesis_agent)

    # Edges (fixed flow)
    graph.set_entry_point("query_understanding")
    graph.add_edge("query_understanding", "context_manager")
    graph.add_edge("context_manager", "context_router")

    # Conditional routing
    # Conditional routing
    graph.add_conditional_edges(
        "context_router",
        lambda state: state.context.get("route"),
        {
            "vector": "vector_search",
            "structured": "structured_search",
            "hybrid": "vector_search",
        }
    )   


    # Retrieval → aggregation
    graph.add_edge("vector_search", "evidence_aggregation")
    graph.add_edge("structured_search", "evidence_aggregation")

    # Final answer
    graph.add_edge("evidence_aggregation", "answer_synthesis")
    graph.add_edge("answer_synthesis", END)

    return graph.compile()
