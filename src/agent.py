from typing import Dict, List, TypedDict

from langgraph.graph import END, START, StateGraph

from src.heuristics import (
    calculate_quality_score,
    calculate_recommendation,
    generate_risks,
    score_criterion_against_diff,
)
from src.llm_client import real_llm_summary
from src.loaders import load_json, load_text
from src.report import build_markdown_report, save_report


class ReviewState(TypedDict, total=False):
    jira_path: str
    pr_diff_path: str
    output_path: str
    jira_ticket: Dict
    pr_diff: str
    findings: List[Dict[str, str]]
    risks: List[str]
    recommendation: str
    quality_score: int
    llm_summary: str
    final_report: str


def load_inputs_node(state: ReviewState) -> ReviewState:
    jira_ticket = load_json(state["jira_path"])
    pr_diff = load_text(state["pr_diff_path"])
    return {
        "jira_ticket": jira_ticket,
        "pr_diff": pr_diff,
    }


def analyze_criteria_node(state: ReviewState) -> ReviewState:
    jira_ticket = state["jira_ticket"]
    pr_diff = state["pr_diff"]
    criteria = jira_ticket.get("acceptance_criteria", [])

    findings = [score_criterion_against_diff(criterion, pr_diff) for criterion in criteria]
    return {"findings": findings}


def evaluate_result_node(state: ReviewState) -> ReviewState:
    findings = state["findings"]
    risks = generate_risks(findings)
    recommendation = calculate_recommendation(findings)
    quality_score = calculate_quality_score(findings)
    return {
        "risks": risks,
        "recommendation": recommendation,
        "quality_score": quality_score,
    }


def llm_summary_node(state: ReviewState) -> ReviewState:
    summary = real_llm_summary(
        jira_ticket=state["jira_ticket"],
        findings=state["findings"],
        pr_diff=state["pr_diff"],
    )
    return {"llm_summary": summary}


def build_report_node(state: ReviewState) -> ReviewState:
    final_report = build_markdown_report(
        jira_ticket=state["jira_ticket"],
        findings=state["findings"],
        risks=state["risks"],
        recommendation=state["recommendation"],
        quality_score=state["quality_score"],
        llm_summary=state["llm_summary"],
    )
    save_report(final_report, state["output_path"])
    return {"final_report": final_report}


def build_review_graph():
    workflow = StateGraph(ReviewState)

    workflow.add_node("load_inputs", load_inputs_node)
    workflow.add_node("analyze_criteria", analyze_criteria_node)
    workflow.add_node("evaluate_result", evaluate_result_node)
    workflow.add_node("llm_summary", llm_summary_node)
    workflow.add_node("build_report", build_report_node)

    workflow.add_edge(START, "load_inputs")
    workflow.add_edge("load_inputs", "analyze_criteria")
    workflow.add_edge("analyze_criteria", "evaluate_result")
    workflow.add_edge("evaluate_result", "llm_summary")
    workflow.add_edge("llm_summary", "build_report")
    workflow.add_edge("build_report", END)

    return workflow.compile()


def run_review(jira_path: str, pr_diff_path: str, output_path: str) -> ReviewState:
    graph = build_review_graph()
    result = graph.invoke(
        {
            "jira_path": jira_path,
            "pr_diff_path": pr_diff_path,
            "output_path": output_path,
        }
    )
    return result
