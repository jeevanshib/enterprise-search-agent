from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class AgentState(BaseModel):
    query: str

    rewritten_query: Optional[str] = None
    intent: Optional[str] = None
    entities: Dict[str, Any] = {}

    context: Dict[str, Any] = {}

    retrieved_docs: List[Dict[str, Any]] = []
    retrieved_structured: List[Dict[str, Any]] = []

    answer: Optional[str] = None
    citations: List[str] = []
