# Project Zero — Architecture

## Design principle

The product must demonstrate a closed experience loop:

1. A new incident arrives.
2. Hindsight recalls relevant historical experience.
3. The system identifies supporting and conflicting cases.
4. Hindsight Reflect synthesizes an evidence-backed diagnostic response.
5. A human reviews the recommendation.
6. The actual outcome is retained as new experience.

## Hindsight responsibilities

- **Retain:** incident reports, interventions, outcomes and lessons.
- **Recall:** retrieve relevant historical cases.
- **Reflect:** reason across memories and produce a grounded response.

Project Zero should not claim that Hindsight itself performs deterministic diagnosis. The application layer defines the diagnostic workflow and the human-review boundary.

## Prototype boundary

The first demo uses synthetic maintenance incidents. This is deliberate: it allows deterministic before/after demonstrations without claiming access to proprietary industrial data.

## Evaluation

The evaluation suite will compare:

- baseline LLM response without historical memory
- Project Zero with Hindsight memory

Measure retrieval of relevant cases, identification of contradictory outcomes, evidence attribution and recommendation consistency. Do not publish fabricated accuracy numbers.
