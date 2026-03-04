from openclaw.llm_client import call_llm

def run_codex(task):

    prompt = f"generate code for {task}"

    return call_llm("coding",prompt)
