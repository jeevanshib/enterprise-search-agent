from core.state import AgentState

# Simple in-memory context store (MVP)
SESSION_MEMORY = {}

def context_manager_agent(state: AgentState, session_id: str = "default") -> AgentState:
    """
    Maintains conversational context across turns.
    """

    previous_context = SESSION_MEMORY.get(session_id, {})

    # Update context
    updated_context = {
        "last_query": state.query,
        "intent": state.intent,
        "entities": state.entities,
        "history": previous_context.get("history", []) + [state.query]
    }

    SESSION_MEMORY[session_id] = updated_context
    state.context = updated_context

    return state
