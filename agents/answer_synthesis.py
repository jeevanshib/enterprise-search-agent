from core.state import AgentState

def answer_synthesis_agent(state: AgentState) -> AgentState:
    """
    Mock answer synthesis agent.
    Uses aggregated evidence to generate a grounded response with citations.
    """

    evidence = state.context.get("evidence", [])

    if not evidence:
        state.answer = "Insufficient data"
        return state

    bullet_points = []
    for e in evidence:
        bullet_points.append(f"- {e['content']}")

    sources = ", ".join(state.citations)

    state.answer = (
        "Here is the relevant information based on available enterprise data:\n\n"
        + "\n".join(bullet_points)
        + f"\n\nSources: [{sources}]"
    )

    return state
