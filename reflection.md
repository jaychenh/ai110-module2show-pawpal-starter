# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
- My initial UML design centered on a simple pet-care planning system with five main classes: Owner, Pet, CareTask, Scheduler, and DailyPlan. The Owner class would store basic owner information and preferences, the Pet class would hold the pet’s profile and care needs, and the CareTask class would represent tasks such as walks, feeding, or medication with attributes like duration, priority, and type. The Scheduler class would take the available tasks and constraints and decide which tasks should be included in the day’s plan, while the DailyPlan class would store the final schedule and explanation.

**b. Design changes**

- Did your design change during implementation?
- Yes, the design changed a bit during implementation. I simplified it by keeping the scheduler focused on a single pet and a one-day plan rather than trying to support more complex multi-pet or recurring-task behavior right away. I also decided not to create a separate explanation class, because a simple list of scheduling reasons attached to each task was enough for the first version. This made the implementation easier to build and test while still meeting the project goals.
---

**Brainstorm**

- **Owner**
  - **Attributes:** name, available_time_per_day, preferences
  - **Methods:** add_preference(), update_available_time(), get_preferences()

- **Pet**
  - **Attributes:** name, species, age, health_notes, care_needs
  - **Methods:** update_profile(), add_care_need(), get_care_summary()

- **CareTask**
  - **Attributes:** title, type, duration_minutes, priority, preferred_time, recurring
  - **Methods:** update_task(), mark_complete(), get_priority_score()

- **Scheduler**
  - **Attributes:** tasks, owner_constraints, pet_profile, available_time
  - **Methods:** sort_tasks(), filter_tasks(), build_daily_plan(), resolve_conflicts()

- **DailyPlan**
  - **Attributes:** date, scheduled_tasks, total_time_used, explanation_notes
  - **Methods:** add_task(), remove_task(), generate_explanation(), display_plan()
```

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- My scheduler considers task priority, task duration, scheduled time, and whether a task belongs to a specific pet. I treated priority and time as the most important constraints because they directly affect whether the plan feels helpful and realistic for a busy owner.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- One tradeoff is that it prioritizes simpler, fast-to-compute rules over more advanced scheduling logic. For example, it sorts by priority and time but does not yet model detailed time windows or long-term recurring patterns in a highly sophisticated way.
- Why is that tradeoff reasonable for this scenario?
- This tradeoff is reasonable because the app is meant to provide a practical daily plan quickly and clearly, rather than simulate a full scheduling system. In this scenario, a simple, understandable approach is more useful than an overly complex one.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
