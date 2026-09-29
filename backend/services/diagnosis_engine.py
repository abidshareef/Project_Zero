from backend.models import Incident
from backend.services.hindsight import memory


def incident_to_query(incident: Incident) -> str:
    measurements = ", ".join(
        f"{key}={value}" for key, value in incident.measurements.items()
    ) or "no structured measurements"
    environment = ", ".join(incident.environment) or "no environment details"
    return (
        f"Current incident on {incident.machine_type} {incident.machine_id}. "
        f"Symptoms: {', '.join(incident.symptoms)}. "
        f"Measurements: {measurements}. Environment: {environment}. "
        f"Description: {incident.description}. "
        "Find historical incidents with similar symptoms, especially cases where "
        "an intervention succeeded or failed under similar conditions."
    )


def diagnose(incident: Incident, budget: str = "mid"):
    query = incident_to_query(incident)
    recalled = memory.recall(query=query, budget=budget)

    response = memory.reflect(
        query=(
            f"{query}\n\n"
            "Act as an evidence-driven diagnostic assistant. "
            "Compare successful and failed historical interventions. "
            "Do not invent measurements or outcomes. "
            "State the strongest diagnosis, the evidence supporting it, "
            "conflicting historical evidence, and the safest next diagnostic action. "
            "If evidence is insufficient, say so explicitly."
        ),
        budget=budget,
    )

    evidence = []
    for item in getattr(recalled, "results", [])[:6]:
        text = getattr(item, "text", None)
        if text:
            evidence.append(text)

    based_on = getattr(response, "based_on", None)
    for item in getattr(based_on, "memories", []) or []:
        text = getattr(item, "text", None)
        if text and text not in evidence:
            evidence.append(text)

    return {
        "diagnosis": response.text,
        "evidence": evidence[:8],
        "recommendation": "Review the evidence-backed diagnosis before intervention.",
        "confidence_note": (
            "Qualitative confidence only. Quantitative diagnostic performance "
            "will be reported from the evaluation suite."
        ),
        "raw_reasoning": response.text,
    }
