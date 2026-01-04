from core.state import AgentState

def query_understanding_agent(state: AgentState) -> AgentState:
    """
    Mock query understanding agent.
    Determines intent and rewrites query.
    """

    query = state.query.lower()

    if "leave" in query or "policy" in query:
        state.intent = "policy"
    elif "ticket" in query or "status" in query:
        state.intent = "ticket"
    else:
        state.intent = "general"

    state.rewritten_query = state.query
    state.entities = {}

    return state
