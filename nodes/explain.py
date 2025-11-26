from langchain_core.prompts import ChatPromptTemplate
from config import llm
explain_prompt = ChatPromptTemplate.from_template("""
Explain the SQL result in plain English.

Question: {question}
SQL: {sql}
Result: {result}
""")

def explain_result(state):
    chain = explain_prompt | llm
    explanation = chain.invoke({
        "question": state["question"],
        "sql": state["sql_query"],
        "result": state["execution_result"]
    })
    return {"final_answer": explanation.content}
