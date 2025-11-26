from graph import app as graph_app

def run_agent(question: str, schema: str):
    response = graph_app.invoke(
        {
            "question": question,
            "schema": schema,
            "sql_query": None,
            "execution_result": None,
            "error": None,
            "retries": 0
        }
    )
    return response
