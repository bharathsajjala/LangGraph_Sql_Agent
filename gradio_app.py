import gradio as gr
from app import run_agent
from config import db

def process_question(question):
    schema = db.get_table_info()

    result = run_agent(question, schema)

    return (
        result.get("sql_query", ""),
        result.get("execution_result", ""),
        result.get("final_answer", "No answer")
    )

with gr.Blocks(title="NL → SQL Agent (LangGraph)") as demo:
    gr.Markdown(
        """
        # 🧠 NL → SQL Agent (LangGraph)
        Convert natural language questions into **safe SQL queries**  
        and get **explanations in plain English**.
        """
    )

    with gr.Row():
        question_input = gr.Textbox(
            label="Ask a question",
            placeholder="e.g. Which department has highest average salary?"
        )

    with gr.Row():
        submit_btn = gr.Button("Generate Answer", variant="primary")

    with gr.Row():
        sql_output = gr.Code(
            label="Generated SQL",
            language="sql"
        )

    with gr.Row():
        execution_output = gr.Textbox(
            label="SQL Execution Result",
            lines=5
        )

    with gr.Row():
        explanation_output = gr.Markdown(
            label="Explanation"
        )

    submit_btn.click(
        fn=process_question,
        inputs=[question_input],
        outputs=[
            sql_output,
            execution_output,
            explanation_output
        ]
    )

demo.launch()
