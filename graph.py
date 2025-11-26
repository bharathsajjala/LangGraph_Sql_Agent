from langgraph.graph import StateGraph
from state import SQLAgentState
from nodes.intent import understand_intent
from nodes.generate_sql import generate_sql
from nodes.validate import validate_sql
from nodes.execute import execute_sql
from nodes.explain import explain_result
from conditions import should_retry
from config import db, llm

graph = StateGraph(SQLAgentState)

graph.add_node("intent", understand_intent)
graph.add_node("generate", generate_sql)
graph.add_node("validate", validate_sql)
graph.add_node("execute", execute_sql)
graph.add_node("explain", explain_result)

graph.set_entry_point("intent")

graph.add_edge("intent", "generate")
graph.add_edge("generate", "validate")

graph.add_conditional_edges(
    "validate",
    should_retry,
    {
        "retry": "generate",
        "finish": "execute"
    }
)

graph.add_conditional_edges(
    "execute",
    should_retry,
    {
        "retry": "generate",
        "finish": "explain"
    }
)

app = graph.compile()

q='Which department has the highest average salary?'

response = app.invoke({
    "question": "Top 5 highest paid employees",
    "schema": db.get_table_info(),
    "sql_query": None,
    "execution_result": None,
    "error": None,
    "retries": 0
})

print(response["final_answer"])
