from core.state import AgentState

def context_router_agent(state: AgentState) -> AgentState:
    """
    Decides which retrieval path to use.
    """

    if state.intent in ["policy", "document", "general"]:
        state.context["route"] = "vector"
    elif state.intent in ["ticket", "status", "metrics"]:
        state.context["route"] = "structured"
    else:
        state.context["route"] = "hybrid"

    return state
