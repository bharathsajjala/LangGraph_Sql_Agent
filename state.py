from typing import TypedDict, Optional

class SQLAgentState(TypedDict):
    question: str
    schema: str
    sql_query: Optional[str]
    execution_result: Optional[str]
    error: Optional[str]
    retries: int
