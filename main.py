from pawpal_system import Owner, Pet, Task, Scheduler


if __name__ == "__main__":
    owner = Owner(name="Jordan")

    mocha = Pet(name="Mochi", species="cat", age=3, notes="Loves cuddles")
    buddy = Pet(name="Buddy", species="dog", age=5, notes="Needs evening walk")

    owner.add_pet(mocha)
    owner.add_pet(buddy)

    morning_feed = Task(description="Morning feeding", duration_minutes=10, frequency="high", scheduled_time="09:00", pet_name="Mochi")
    walk = Task(description="Evening walk", duration_minutes=25, frequency="high", scheduled_time="18:00", pet_name="Buddy")
    litter_box = Task(description="Clean litter box", duration_minutes=15, frequency="medium", scheduled_time="07:00", pet_name="Mochi")
    meds = Task(description="Give medicine", duration_minutes=5, frequency="high", scheduled_time="12:00", pet_name="Buddy")
    overlap = Task(description="Overlap task", duration_minutes=10, frequency="high", scheduled_time="12:00", pet_name="Mochi")

    mocha.add_task(morning_feed)
    mocha.add_task(litter_box)
    mocha.add_task(overlap)
    buddy.add_task(walk)
    buddy.add_task(meds)

    scheduler = Scheduler(owner)
    all_tasks = owner.get_all_tasks()
    ordered_tasks = scheduler.sort_by_time(all_tasks)
    filtered_tasks = scheduler.filter_tasks(ordered_tasks, completed=False, pet_name="Mochi")
    today_plan = scheduler.build_daily_plan(limit_minutes=60)
    conflict_warning = scheduler.detect_conflicts(all_tasks)

    print(f"Daily plan for {owner.name}:")
    print("Ordered tasks:")
    for task in ordered_tasks:
        print(f"- {task.description} ({task.scheduled_time})")

    print("\nFiltered Mochi tasks:")
    for task in filtered_tasks:
        print(f"- {task.description} ({task.scheduled_time})")

    print("\nConflict check:")
    print(conflict_warning)

    print("\nScheduled plan:")
    for idx, task in enumerate(today_plan, start=1):
        print(f"  {idx:02d}:00 — {task.description} ({task.duration_minutes} min) [priority: {task.frequency}]")
