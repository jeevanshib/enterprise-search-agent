from core.state import AgentState
from agents.evidence_aggregator import evidence_aggregation_agent

state = AgentState(query="What is the leave policy during probation?")

state.retrieved_docs = [
    {
        "content": "Employees on probation are entitled to 6 casual leaves per year.",
        "source": "HR_Policy_Leave.pdf",
        "score": 0.92
    }
]

state.retrieved_structured = [
    {
        "field": "probation_period_months",
        "value": 6,
        "source": "HR_DB"
    }
]

state.context = {}

state = evidence_aggregation_agent(state)

print(state.context["evidence"])
print("Citations:", state.citations)
