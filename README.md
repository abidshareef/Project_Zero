# Project Zero

> **Experience-based diagnostic intelligence powered by persistent memory.**

Project Zero turns historical incidents, interventions, and outcomes into reusable operational experience. A new incident is matched against past cases, the system reasons over successful and failed interventions, produces an evidence-backed diagnostic plan, and stores the final outcome as new experience.

## Core loop

```text
Current Incident
      ↓
Hindsight Recall
      ↓
Similar + contradictory experience
      ↓
Hindsight Reflect
      ↓
Evidence-backed diagnostic plan
      ↓
Recommended action
      ↓
Observed outcome
      ↓
Hindsight Retain
      ↓
Experience improves
```

## MVP status

- [x] Backend scaffold
- [x] Hindsight client wrapper
- [x] Incident API models
- [x] Synthetic incident seed data
- [x] Retain / recall / reflect endpoints
- [ ] Live Hindsight integration test
- [ ] Frontend command center
- [ ] Evaluation benchmark
- [ ] Demo recording

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env
uvicorn backend.main:app --reload
```

Configure either Hindsight Cloud or a local Hindsight server in `.env`.

**Important:** demo data is synthetic. Do not present synthetic evaluation as real-world diagnostic accuracy.
