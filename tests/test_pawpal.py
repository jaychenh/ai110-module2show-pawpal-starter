import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete_changes_task_status():
    task = Task(description="Morning feeding", duration_minutes=10, frequency="high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="cat")
    task = Task(description="Evening walk", duration_minutes=20, frequency="medium")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Evening walk"


def test_sort_by_time_orders_tasks_by_scheduled_time():
    pet = Pet(name="Mochi", species="cat")
    morning = Task(description="Morning feeding", duration_minutes=10, frequency="high", scheduled_time="09:00")
    afternoon = Task(description="Afternoon meds", duration_minutes=5, frequency="high", scheduled_time="15:00")
    early = Task(description="Early walk", duration_minutes=20, frequency="medium", scheduled_time="07:00")

    pet.add_task(afternoon)
    pet.add_task(early)
    pet.add_task(morning)

    scheduler = Scheduler()
    ordered = scheduler.sort_by_time(pet.tasks)

    assert [task.description for task in ordered] == ["Early walk", "Morning feeding", "Afternoon meds"]


def test_filter_tasks_by_completion_status_and_pet_name():
    scheduler = Scheduler()
    mochi = Pet(name="Mochi", species="cat")
    buddy = Pet(name="Buddy", species="dog")

    completed_task = Task(description="Give meds", duration_minutes=5, frequency="high", completed=True, pet_name="Mochi")
    pending_task = Task(description="Walk", duration_minutes=20, frequency="high", pet_name="Buddy")

    mochi.add_task(completed_task)
    buddy.add_task(pending_task)

    filtered = scheduler.filter_tasks([completed_task, pending_task], completed=False, pet_name="Buddy")

    assert filtered == [pending_task]


def test_complete_task_creates_next_occurrence_for_daily_task():
    pet = Pet(name="Mochi", species="cat")
    task = Task(description="Morning feeding", duration_minutes=10, frequency="daily")
    pet.add_task(task)

    scheduler = Scheduler()
    next_task = scheduler.complete_task(task, pet)

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.description == "Morning feeding"
    assert next_task.frequency == "daily"
    assert len(pet.tasks) == 2


def test_detect_conflicts_returns_warning_for_overlapping_tasks():
    scheduler = Scheduler()
    task_one = Task(description="Morning feeding", duration_minutes=10, frequency="daily", scheduled_time="09:00", pet_name="Mochi")
    task_two = Task(description="Morning walk", duration_minutes=20, frequency="daily", scheduled_time="09:00", pet_name="Buddy")

    warning = scheduler.detect_conflicts([task_one, task_two])

    assert "conflict" in warning.lower()
