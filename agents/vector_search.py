from core.state import AgentState

def vector_search_agent(state: AgentState) -> AgentState:
    """
    Simulates vector-based document retrieval.
    """

    # Mock retrieved documents (MVP)
    mock_docs = [
        {
            "content": "Employees on probation are entitled to 6 casual leaves per year.",
            "source": "HR_Policy_Leave.pdf",
            "score": 0.92
        },
        {
            "content": "Probation period lasts for 6 months from joining date.",
            "source": "HR_Policy_Probation.pdf",
            "score": 0.85
        }
    ]

    state.retrieved_docs = mock_docs
    return state
