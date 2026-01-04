from core.state import AgentState
from agents.answer_synthesis import answer_synthesis_agent

state = AgentState(query="What is the leave policy during probation?")

state.context = {
    "evidence": [
        {
            "content": "probation_period_months = 6",
            "source": "HR_DB",
            "confidence": 1.0
        },
        {
            "content": "Employees on probation are entitled to 6 casual leaves per year.",
            "source": "HR_Policy_Leave.pdf",
            "confidence": 0.92
        }
    ]
}

state = answer_synthesis_agent(state)

print(state.answer)
