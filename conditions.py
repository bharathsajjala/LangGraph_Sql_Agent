def should_retry(state):
    if state["error"] and state["retries"] < 3:
        state["retries"] += 1
        return "retry"
    return "finish"
