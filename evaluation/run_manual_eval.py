import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cases = json.loads((ROOT / "evaluation" / "test_cases.json").read_text())

print("PROJECT ZERO — MANUAL EVALUATION")
print("=" * 60)
for case in cases:
    print(f"\n{case['id']}")
    print(f"Query: {case['query']}")
    print(f"Expected cases: {', '.join(case['expected_case_ids'])}")
    print(f"Expected behavior: {case['expected_behavior']}")
    print("\nFill after running baseline and memory-enabled conditions:")
    print("[ ] Baseline answer recorded")
    print("[ ] Hindsight answer recorded")
    print("[ ] Relevant case found")
    print("[ ] Contradiction identified")
    print("[ ] Evidence cited")
    print("[ ] Recommendation matches expected behavior")
