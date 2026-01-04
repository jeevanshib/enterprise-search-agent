from core.state import AgentState

def evidence_aggregation_agent(state: AgentState) -> AgentState:
    """
    Aggregates evidence from vector and structured retrieval,
    normalizes it, ranks it, and prepares citations.
    """

    aggregated_evidence = []

    # Vector search evidence
    for doc in state.retrieved_docs:
        aggregated_evidence.append({
            "content": doc["content"],
            "source": doc["source"],
            "confidence": doc.get("score", 0.0)
        })

    # Structured search evidence
    for item in state.retrieved_structured:
        aggregated_evidence.append({
            "content": f"{item['field']} = {item['value']}",
            "source": item["source"],
            "confidence": 1.0
        })

    # Rank by confidence (highest first)
    aggregated_evidence.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    # Attach to state
    state.context["evidence"] = aggregated_evidence
    state.citations = list({e["source"] for e in aggregated_evidence})

    return state
