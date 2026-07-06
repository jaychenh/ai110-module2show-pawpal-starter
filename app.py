import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

owner = st.session_state.owner

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value=owner.name)
if owner_name != owner.name:
    owner.name = owner_name
    st.session_state.owner = owner

st.markdown("### Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    if pet_name.strip():
        new_pet = Pet(name=pet_name.strip(), species=species)
        owner.add_pet(new_pet)
        st.session_state.owner = owner
        st.success(f"Added {new_pet.name} to {owner.name}'s pets.")
    else:
        st.warning("Please enter a pet name.")

if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Add a Task")
st.caption("Attach a task to one of your pets and let the scheduler plan it.")

if owner.pets:
    selected_pet_name = st.selectbox("Select pet", [pet.name for pet in owner.pets])
    selected_pet = owner.get_pet(selected_pet_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        if task_title.strip() and selected_pet is not None:
            task = Task(
                description=task_title.strip(),
                duration_minutes=int(duration),
                frequency=priority,
                pet_name=selected_pet.name,
            )
            selected_pet.add_task(task)
            st.session_state.owner = owner
            st.success(f"Added task to {selected_pet.name}.")
        else:
            st.warning("Please enter a task title.")

    scheduler = Scheduler(owner)
    st.write("Current tasks:")
    for pet in owner.pets:
        pet_tasks = scheduler.filter_tasks(pet.tasks, completed=False, pet_name=pet.name)
        sorted_pet_tasks = scheduler.sort_by_time(pet_tasks)
        if sorted_pet_tasks:
            st.success(f"{pet.name} has {len(sorted_pet_tasks)} pending task(s) ready to review.")
            task_rows = [
                {
                    "Task": task.description,
                    "Time": task.scheduled_time or "Unscheduled",
                    "Duration": f"{task.duration_minutes} min",
                    "Priority": task.frequency.capitalize(),
                }
                for task in sorted_pet_tasks
            ]
            st.table(task_rows)
        else:
            st.warning(f"{pet.name} has no pending tasks yet.")
else:
    st.info("Add a pet before creating tasks.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generate a daily plan from the tasks you added.")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    plan = scheduler.build_daily_plan(limit_minutes=240)
    sorted_plan = scheduler.sort_by_time(plan)
    conflict_message = scheduler.detect_conflicts(sorted_plan)

    if sorted_plan:
        st.write("### Today's Schedule")
        plan_rows = [
            {
                "#": idx,
                "Task": task.description,
                "Time": task.scheduled_time or "Unscheduled",
                "Duration": f"{task.duration_minutes} min",
                "Priority": task.frequency.capitalize(),
            }
            for idx, task in enumerate(sorted_plan, start=1)
        ]
        st.table(plan_rows)

        if conflict_message != "No conflicts detected.":
            st.warning(conflict_message)
        else:
            st.success(conflict_message)
    else:
        st.info("No tasks available to schedule yet.")
