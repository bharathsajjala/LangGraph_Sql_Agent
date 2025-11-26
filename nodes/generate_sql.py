from langchain_core.prompts import ChatPromptTemplate
from config import llm

prompt = ChatPromptTemplate.from_template("""
You are an expert SQL developer.

Given the database schema:
{schema}

Convert the question into SAFE, READ-ONLY SQL.
Do NOT use INSERT, UPDATE, DELETE.

Question: {question}
""")

def generate_sql(state):
    response = prompt | llm
    sql = response.invoke({
        "schema": state["schema"],
        "question": state["question"]
    })
    state["sql_query"] = sql.content.strip()
    return state
