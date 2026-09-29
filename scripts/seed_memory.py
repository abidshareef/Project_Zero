import json
from pathlib import Path

from backend.services.hindsight import memory

DATA = Path(__file__).resolve().parents[1] / "backend" / "data" / "seed_incidents.json"


def main():
    memory.ensure_bank()
    cases = json.loads(DATA.read_text(encoding="utf-8"))

    for case in cases:
        content = (
            f"Historical incident {case['incident_id']}. "
            f"Machine: {case['machine_id']} ({case['machine_type']}). "
            f"Symptoms: {', '.join(case['symptoms'])}. "
            f"Measurements: {case['measurements']}. "
            f"Environment: {', '.join(case['environment'])}. "
            f"Diagnosis: {case['diagnosis']}. "
            f"Intervention: {case['intervention']}. "
            f"Outcome: {case['outcome']}. "
            f"Lesson: {case['lesson']}."
        )
        memory.retain(
            content,
            context="Synthetic Project Zero maintenance case",
        )
        print(f"retained {case['incident_id']}")


if __name__ == "__main__":
    main()
