from planner.claude_planner import plan
from execution.codex_runner import run_codex
from agents.review_agent import review_code

def run_workflow(requirement):

    plan_result = plan(requirement)

    code = run_codex(requirement)

    review = review_code(code)

    return {
        "plan": plan_result,
        "code": code,
        "review": review
    }
