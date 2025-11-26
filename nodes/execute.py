from config import db
def execute_sql(state):
    try:
        result = db.run(state["sql_query"])
        state["execution_result"] = result
        state["error"] = None
    except Exception as e:
        state["error"] = str(e)
    return state
