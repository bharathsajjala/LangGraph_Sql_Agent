def validate_sql(state):
    sql = state["sql_query"]
    banned = ["insert", "update", "delete", "drop"]

    if any(b in sql.lower() for b in banned):
        state["error"] = "Unsafe SQL detected"
    else:
        state["error"] = None

    return state
