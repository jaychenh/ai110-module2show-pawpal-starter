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
    I used AI tools to help brainstorm the class structure, refine the scheduler behavior, and debug implementation issues while building the project. I also used AI to suggest better ways to structure the Streamlit UI and to turn the initial object model into working Python code.
- What kinds of prompts or questions were most helpful?
    The most helpful prompts were specific ones such as: “Help me design a simple scheduler class for pet care tasks,” “Show me how to connect this backend logic to a Streamlit app,” and “Write tests for recurring tasks and conflict detection.” These prompts produced useful starting points that I could verify and adjust.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
    One time I did not accept an AI suggestion when it proposed a more complex recurrence model than the project needed. I evaluated it by checking whether the simpler approach still met the requirements and whether it was easy to test and explain.
- How did you evaluate or verify what the AI suggested?
    I verified the AI’s suggestions by running the code and pytest, and by comparing the behavior against the project goals. This helped me keep the implementation simple, reliable, and consistent with the assignment.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
    I tested task completion, recurring task creation, task ordering, filtering by pet and completion status, and conflict detection. These behaviors were important because they represent the core scheduling logic that makes the app useful.
- Why were these tests important?
    I also verified that the app’s backend still worked after connecting it to the Streamlit interface, which helped confirm that the UI was using the same scheduler behavior.

**b. Confidence**

- How confident are you that your scheduler works correctly?
    I am highly confident that the current scheduler works correctly for the scope of this project because the test suite passed successfully and the main demo behavior was verified.
- What edge cases would you test next if you had more time?
    If I had more time, I would test edge cases such as tasks with no scheduled time, very long task durations, overlapping weekly recurring tasks, and multiple pets with similar schedules.
---

## 5. Reflection

**a. What went well**

    I am most satisfied with how the scheduler logic and the Streamlit UI came together into a cohesive experience. The project went from a simple concept to a working demo with meaningful scheduling behavior.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
    In a future iteration, I would improve the scheduler by supporting more realistic constraints, such as time windows, task durations that affect availability, and better multi-pet planning. I would also add persistence so tasks and pets are saved between sessions.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
    One important lesson was that simple, well-defined classes and clear responsibilities make it much easier to build and test a system incrementally. I also learned that AI is most useful when it is used as a collaborator for brainstorming and scaffolding, while the final decisions should still be verified by running the code.

## 6. Testing PawPal+
platform win32 -- Python 3.13.0, pytest 8.4.4, django 5.2.0
rootdir: ...\ai110\ai110-module2show-pawpal-starter
collected 6 items

tests/test_pawpal.py .....                                                                                                                                                     [100%]
6 passed in 0.03s

Confidence Level: 5/5 stars