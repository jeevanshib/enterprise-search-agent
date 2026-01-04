from fastapi import FastAPI
from pydantic import BaseModel

from core.orchestrator import build_graph
from core.state import AgentState

app = FastAPI(
    title="Intelligent Enterprise Search API",
    description="Agentic enterprise search with grounded answers and citations",
    version="1.0.0"
)

# Build graph once (important)
graph = build_graph()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    initial_state = AgentState(query=request.query)

    final_state = graph.invoke(initial_state)

    return {
        "answer": final_state["answer"],
        "sources": final_state.get("citations", [])
    }
