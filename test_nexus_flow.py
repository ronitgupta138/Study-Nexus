"""
Automated Integration Test for Study-Nexus Multi-Agent Workflow.
Verifies concept ingestion, Socratic drill generation, answer evaluation,
and formatted note archival.
"""

import json
from mcp_nexus_tools import (
    ingest_concept,
    generate_socratic_drill,
    evaluate_comprehension,
    archive_study_note,
)


def test_study_nexus_end_to_end():
    # 1. Curator ingests topic
    ingest_res = json.loads(ingest_concept("distributed-consensus", "Raft consensus paper"))
    assert ingest_res["status"] == "READY_FOR_SOCRATIC_DRILL"

    # 2. Tutor generates active recall question
    drill = json.loads(generate_socratic_drill("distributed-consensus"))
    assert "Raft" in drill["question"]
    assert drill["id"] == "DRILL-RAFT-01"

    # 3. Student answers
    student_ans = (
        "The new leader must contain all committed entries because a leader election requires "
        "a majority vote, and any majority intersects with the majority that committed the previous entry. "
        "Uncommitted entries from previous terms are never committed directly by count."
    )
    eval_res = json.loads(evaluate_comprehension(drill["id"], student_ans))
    assert eval_res["conceptual_understanding"] == "STRONG"
    assert eval_res["mastery_score"] >= 90

    # 4. Scribe compiles note
    note = json.loads(
        archive_study_note(
            "Raft Distributed Consensus",
            ["Leader Election Safety", "Log Matching Invariant", "Leader Completeness"],
            [
                {
                    "q": "What is the Leader Completeness property in Raft?",
                    "a": "If a log entry is committed in a given term, that entry will be present in the logs of the leaders for all higher-numbered terms.",
                }
            ],
        )
    )
    assert note["status"] == "SUCCESS"
    assert "Leader Completeness" in note["preview"]
    print("\n✅ Study-Nexus end-to-end active recall & note generation test PASSED!")


if __name__ == "__main__":
    test_study_nexus_end_to_end()
