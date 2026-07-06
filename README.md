# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
#Daily plan for Jordan:
#  01:00 — Give medicine (5 min) [priority: high]
#  02:00 — Morning feeding (10 min) [priority: high]
#  03:00 — Evening walk (25 min) [priority: high]
#  04:00 — Clean litter box (15 min) [priority: medium]
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Orders tasks by scheduled time so the plan is chronological. |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks by pet name and/or completion status. |
| Conflict handling | `Scheduler.detect_conflicts()` | Warns when two tasks share the same scheduled time. |
| Recurring tasks | `Task.clone_for_next_occurrence()` and `Scheduler.complete_task()` | Creates a new task for the next occurrence when a daily or weekly task is completed. |

## 📸 Demo Walkthrough

Follow this example to see how a user would interact with PawPal+:

1. Launch the app with `streamlit run app.py` and open the local Streamlit URL.
2. Enter an owner name, add a pet, and choose its species.
3. Create one or more care tasks for that pet, such as a walk, feeding, or medication reminder.
4. Review the pending task list, which is filtered by pet and sorted by time when a time is available.
5. Click "Generate schedule" to view a daily plan and see any conflict warnings if two tasks overlap.
6. Complete a recurring task to confirm that a new task is created automatically for the next day or week.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
