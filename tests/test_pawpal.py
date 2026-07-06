import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pawpal_system import Pet, Task


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
