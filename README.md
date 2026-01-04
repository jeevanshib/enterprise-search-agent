# 🔍 Intelligent Enterprise Search (Agentic AI)

An **agentic enterprise search system** that goes beyond traditional semantic search by combining **intent-aware routing, multi-source retrieval, evidence aggregation, and grounded answer generation with citations**.

This project demonstrates how autonomous agents can collaborate via orchestration to produce **context-aware, reliable, and explainable answers** over enterprise knowledge.

---

## 🚀 Key Features

- 🧠 **Query Understanding Agent** – detects intent and prepares query context  
- 🔀 **Context Router Agent** – dynamically routes queries to the right data sources  
- 📄 **Vector Retrieval Agent** – document-style knowledge (PDFs, policies)  
- 📊 **Structured Retrieval Agent** – structured enterprise data (CSV / DB-like)  
- 🧩 **Evidence Aggregation Agent** – merges, ranks, and deduplicates evidence  
- ✅ **Grounded Answer Synthesis** – answers generated strictly from evidence  
- 📚 **Citations Included** – every answer includes source references  
- 🔗 **LangGraph Orchestration** – deterministic multi-agent execution  
- ⚡ **FastAPI Backend** + **Streamlit UI**

---

## 🏗️ Architecture Overview

The system is designed as a **multi-agent pipeline** orchestrated using **LangGraph**.  
Each agent has a **single responsibility**, and all agents share a common state.

### 🔁 Agent Flow

1. **Query Understanding Agent**  
   - Detects user intent (policy, ticket, general, etc.)
   - Normalizes and prepares query

2. **Context Manager Agent**  
   - Maintains conversational and session context

3. **Context Router Agent**  
   - Decides retrieval strategy: `vector`, `structured`, or `hybrid`

4. **Retrieval Agents**
   - Vector Search Agent (documents, policies)
   - Structured Search Agent (CSV / DB-style data)

5. **Evidence Aggregation Agent**
   - Merges results from all retrieval agents
   - Ranks evidence by confidence
   - Attaches source metadata

6. **Answer Synthesis Agent**
   - Generates answers **only from aggregated evidence**
   - Ensures grounding and prevents hallucinations

---

## 🔗 Agent Orchestration (LangGraph)

LangGraph is used to:

- Maintain a shared state across agents  
- Enable deterministic routing based on context  
- Ensure evidence aggregation occurs **before** answer generation  
- Make the system easily extensible (new agents, new data sources)

---

## 🖥️ Tech Stack

- **Backend**: FastAPI  
- **Agent Orchestration**: LangGraph  
- **State Management**: Pydantic  
- **Frontend**: Streamlit  
- **Retrieval (MVP)**: Mocked Vector + Structured sources  
- **LLM**: Mocked for deterministic local execution (pluggable in production)

---

## ▶️ How to Run the Project

### 1️⃣ Start Backend (FastAPI)

bash
uvicorn api.server:app --reload

API Docs:

http://127.0.0.1:8000/docs

## 2️⃣ Start Frontend (Streamlit)

Open a new terminal (same virtual environment):

streamlit run app.py

UI:

http://localhost:8501

##📌 Example Query
###Input
What is the leave policy during probation?

Output

Employees on probation are entitled to 6 casual leaves per year

Probation period lasts for 6 months from joining date

Sources

HR_Policy_Leave.pdf

HR_Policy_Probation.pdf

## ⚠️ Design Notes & Tradeoffs

- Document ingestion and vector DB persistence are intentionally mocked in this MVP.

- The focus is on agent orchestration, routing logic, and grounded answer generation.

- The architecture cleanly supports plugging in:

- Chroma / FAISS / Elasticsearch

- OpenAI / Azure OpenAI

- Jira, SQL, internal enterprise systems

## 🔮 Future Enhancements

- Real document ingestion & embedding pipelines**

- Authentication and role-based access control**

- Feedback-driven answer re-ranking

- Streaming responses

- Multi-turn conversational memory

- Observability and tracing for agents

## 🧪 Testing

The repository includes test scripts for:

- Context management

- Routing logic

- Retrieval agents

- Evidence aggregation

- End-to-end pipeline execution

## ✅ Project Status

✔ Backend working

✔ UI working

✔ End-to-end agent pipeline functional

✔ Ready for submission and demo
