# 🧠 NL → SQL Agent using LangGraph

A **production-style Natural Language to SQL (NL → SQL) agent** built using **LangGraph + LangChain**, with **validation, retries, safety guards, and a Gradio UI**.

This project is designed specifically for **GenAI / LLM Engineer interviews** and demonstrates **stateful agent workflows**, not just simple prompt chaining.

----------

## 🚀 Features

✅ Natural language → SQL conversion  
✅ Schema-aware query generation  
✅ Read-only SQL safety enforcement  
✅ Validation + retry loop using LangGraph  
✅ SQL execution on SQLite database  
✅ Human-readable explanation of results  
✅ Interactive Gradio UI

----------

## 🧩 System Architecture

```text
┌──────────────┐
│   User / UI  │  (Gradio)
└──────┬───────┘
       │  NL Question
       ▼
┌─────────────────────┐
│   LangGraph Agent   │
│ (Stateful Workflow) │
└──────┬──────────────┘
       ▼
┌──────────────────────────────────────────────┐
│ LangGraph Nodes (with shared state)           │
│                                              │
│ 1. Understand Intent                          │
│ 2. Generate SQL                               │
│ 3. Validate SQL  ─────┐                       │
│ 4. Execute SQL       │   (Retry Loop)         │
│ 5. Explain Result ◄──┘                        │
│                                              │
└──────────────┬───────────────────────────────┘
               ▼
        ┌────────────┐
        │ SQLite DB  │  (company.db)
        └────────────┘

```

----------

## 🧠 Why LangGraph?

NL → SQL is **not a linear task**.

-   SQL generation may fail
    
-   Validation may reject unsafe queries
    
-   Execution may throw errors
    

👉 LangGraph allows us to model this as a **state machine with loops and guards**, which is **not possible with simple chains**.

> _“I chose LangGraph because SQL generation requires retries, validation, and deterministic control flow.”_

----------

## 🗂️ Project Structure

```text
nl-sql-langgraph/
├── app.py                  # LangGraph runner interface
├── graph.py                # Graph definition
├── state.py                # Typed shared state
├── config.py               # LLM + DB configuration
├── conditions.py           # Retry conditions
├── nodes/
│   ├── intent.py           # Intent understanding
│   ├── generate_sql.py     # NL → SQL generation
│   ├── validate.py         # SQL safety checks
│   ├── execute.py          # SQL execution
│   └── explain.py          # Natural language explanation
├── ui/
│   └── gradio_app.py       # Gradio UI
├── db/
│   └── company.db          # SQLite database
└── README.md

```

----------

## 🗄️ Database Schema

### departments

-   `department_id` (PK)
    
-   `department_name`
    

### employees

-   `employee_id` (PK)
    
-   `name`
    
-   `department_id` (FK)
    
-   `title`
    
-   `salary`
    
-   `hire_date`
    

This schema enables:

-   Joins
    
-   Aggregations
    
-   Group-by queries
    

----------

## 🔁 LangGraph Workflow (State Flow)

```text
START
  ↓
[Understand Intent]
  ↓
[Generate SQL]
  ↓
[Validate SQL]
  ├── Unsafe / Error → Retry → Generate SQL
  ▼
[Execute SQL]
  ├── Execution Error → Retry → Generate SQL
  ▼
[Explain Result]
  ↓
END

```

----------

## 🧱 State Definition

```python
class SQLAgentState(TypedDict):
    question: str
    schema: str
    sql_query: Optional[str]
    execution_result: Optional[str]
    error: Optional[str]
    retries: int

```

✅ Shared across nodes  
✅ Enables retries and deterministic execution

----------

## 🖥️ Gradio UI

The Gradio interface provides:

-   Natural language input
    
-   Generated SQL view
    
-   SQL execution output
    
-   Plain English explanation
    

```bash
python ui/gradio_app.py

```

App runs at: **[http://localhost:7860](http://localhost:7860/)**

----------

## 🧪 Example Questions

-   "Who is the highest paid employee?"
    
-   "Which department has the highest average salary?"
    
-   "Top 3 employees hired after 2020"
    
-   "Average salary per department"
    

----------

## 🔐 Safety & Reliability

✅ Read-only SQL enforcement  
✅ Banned operations: INSERT, UPDATE, DELETE, DROP  
✅ Max retry count  
✅ Schema-based grounding  
✅ Deterministic LLM (temperature=0)

----------

### ⭐ If this project helps you, consider starring the repo!