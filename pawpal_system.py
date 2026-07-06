from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    duration_minutes: int = 15
    frequency: str = "daily"
    completed: bool = False
    notes: str = ""

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False

    def update_details(
        self,
        description: Optional[str] = None,
        duration_minutes: Optional[int] = None,
        frequency: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> None:
        """Update the task's description, duration, frequency, or notes."""
        if description is not None:
            self.description = description
        if duration_minutes is not None:
            self.duration_minutes = max(1, duration_minutes)
        if frequency is not None:
            self.frequency = frequency
        if notes is not None:
            self.notes = notes

    def to_dict(self) -> dict:
        """Return the task as a dictionary for easy serialization."""
        return {
            "description": self.description,
            "duration_minutes": self.duration_minutes,
            "frequency": self.frequency,
            "completed": self.completed,
            "notes": self.notes,
        }


@dataclass
class Pet:
    name: str
    species: str
    age: int = 0
    notes: str = ""
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a new task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """Return tasks filtered by completion state if requested."""
        if completed is None:
            return list(self.tasks)
        return [task for task in self.tasks if task.completed is completed]

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks for this pet."""
        return self.get_tasks(completed=False)

    def get_completed_tasks(self) -> List[Task]:
        """Return all completed tasks for this pet."""
        return self.get_tasks(completed=True)

    def update_profile(self, species: Optional[str] = None, age: Optional[int] = None, notes: Optional[str] = None) -> None:
        """Update the pet's profile details."""
        if species is not None:
            self.species = species
        if age is not None:
            self.age = max(0, age)
        if notes is not None:
            self.notes = notes


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a new pet to the owner's collection."""
        if pet not in self.pets:
            self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's collection."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pet(self, pet_name: str) -> Optional[Pet]:
        """Find a pet by name."""
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                return pet
        return None

    def get_all_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        """Collect tasks from all pets for the owner."""
        tasks: List[Task] = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks(completed=completed))
        return tasks

    def get_pending_tasks(self) -> List[Task]:
        """Return all pending tasks across the owner's pets."""
        return self.get_all_tasks(completed=False)

    def get_completed_tasks(self) -> List[Task]:
        """Return all completed tasks across the owner's pets."""
        return self.get_all_tasks(completed=True)


class Scheduler:
    def __init__(self, owner: Optional[Owner] = None) -> None:
        self.owner = owner

    def set_owner(self, owner: Owner) -> None:
        """Attach an owner to the scheduler."""
        self.owner = owner

    def collect_tasks(self, owner: Optional[Owner] = None) -> List[Task]:
        """Gather pending tasks from the provided owner or the current owner."""
        active_owner = owner or self.owner
        if active_owner is None:
            return []
        return active_owner.get_all_tasks(completed=False)

    def organize_tasks(self, tasks: Optional[List[Task]] = None) -> List[Task]:
        """Sort tasks by completion state, priority, and duration."""
        source = tasks if tasks is not None else self.collect_tasks()
        return sorted(
            source,
            key=lambda task: (
                0 if not task.completed else 1,
                self._priority_score(task),
                task.duration_minutes,
                task.description.lower(),
            ),
        )

    def build_daily_plan(self, owner: Optional[Owner] = None, limit_minutes: Optional[int] = None) -> List[Task]:
        """Build a simple daily plan from the highest-priority pending tasks."""
        pending_tasks = self.organize_tasks(self.collect_tasks(owner))
        plan: List[Task] = []
        used_minutes = 0

        for task in pending_tasks:
            if limit_minutes is not None and used_minutes + task.duration_minutes > limit_minutes:
                continue
            plan.append(task)
            used_minutes += task.duration_minutes

        return plan

    def complete_task(self, task: Task) -> None:
        """Mark a task as completed."""
        task.mark_complete()

    @staticmethod
    def _priority_score(task: Task) -> int:
        priority_map = {"high": 0, "medium": 1, "low": 2}
        return priority_map.get(task.frequency.lower(), 1)

