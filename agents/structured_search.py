from core.state import AgentState

def structured_search_agent(state: AgentState) -> AgentState:
    """
    Simulates structured data retrieval (e.g. tickets, CSV, Jira).
    """

    mock_results = [
        {
            "field": "probation_period_months",
            "value": 6,
            "source": "HR_DB"
        }
    ]

    state.retrieved_structured = mock_results
    return state
