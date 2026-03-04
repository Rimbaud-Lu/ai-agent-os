from openclaw.llm_client import call_llm

def review_code(code):

    prompt = f"review code\n{code}"

    return call_llm("review",prompt)
