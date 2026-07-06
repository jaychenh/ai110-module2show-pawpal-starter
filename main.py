from pawpal_system import Owner, Pet, Task, Scheduler


if __name__ == "__main__":
    owner = Owner(name="Jordan")

    mocha = Pet(name="Mochi", species="cat", age=3, notes="Loves cuddles")
    buddy = Pet(name="Buddy", species="dog", age=5, notes="Needs evening walk")

    owner.add_pet(mocha)
    owner.add_pet(buddy)

    morning_feed = Task(description="Morning feeding", duration_minutes=10, frequency="high")
    walk = Task(description="Evening walk", duration_minutes=25, frequency="high")
    litter_box = Task(description="Clean litter box", duration_minutes=15, frequency="medium")
    meds = Task(description="Give medicine", duration_minutes=5, frequency="high")

    mocha.add_task(morning_feed)
    mocha.add_task(litter_box)
    buddy.add_task(walk)
    buddy.add_task(meds)

    scheduler = Scheduler(owner)
    today_plan = scheduler.build_daily_plan(limit_minutes=60)

    print(f"Daily plan for {owner.name}:")
    for idx, task in enumerate(today_plan, start=1):
        print(f"  {idx:02d}:00 — {task.description} ({task.duration_minutes} min) [priority: {task.frequency}]")
