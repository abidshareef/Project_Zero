# Project Zero — Frontend Brief

## Screen 1 — Command Center
- Active incident
- Memory count
- Historical matches
- Last learned experience

## Screen 2 — Incident Intake
Fields:
- machine
- machine type
- symptoms
- measurements
- environment
- description

Primary CTA: `Diagnose with Experience`

## Screen 3 — Memory Evidence
Show:
- match count
- successful cases
- failed/contradictory cases
- case IDs
- timeline

Do not show a fake similarity percentage unless the backend actually provides one.

## Screen 4 — Diagnostic Decision
Sections:
- likely cause
- supporting evidence
- conflicting evidence
- recommended next check
- confidence
- source memories

## Screen 5 — Capture Outcome
Fields:
- confirmed root cause
- intervention
- outcome
- lesson learned

CTA: `Add to Experience`

The interface should make the closed loop visually obvious:
CURRENT INCIDENT → REMEMBER → REASON → ACT → LEARN.
