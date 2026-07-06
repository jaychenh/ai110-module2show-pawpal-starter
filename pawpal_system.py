from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Owner:
    name: str
    available_time_per_day: int = 240
    preferences: List[str] = field(default_factory=list)

    def add_preference(self, preference: str) -> None:
        if preference and preference not in self.preferences:
            self.preferences.append(preference)

    def update_available_time(self, minutes: int) -> None:
        self.available_time_per_day = max(0, minutes)

    def get_preferences(self) -> List[str]:
        return list(self.preferences)


@dataclass
class Pet:
    name: str
    species: str
    age: int = 0
    health_notes: List[str] = field(default_factory=list)
    care_needs: List[str] = field(default_factory=list)

    def update_profile(self, species: Optional[str] = None, age: Optional[int] = None) -> None:
        if species is not None:
            self.species = species
        if age is not None:
            self.age = max(0, age)

    def add_care_need(self, need: str) -> None:
        if need and need not in self.care_needs:
            self.care_needs.append(need)

    def get_care_summary(self) -> str:
        return f"{self.name} ({self.species}, age {self.age})"


@dataclass
class CareTask:
    title: str
    task_type: str
    duration_minutes: int
    priority: str = "medium"
    preferred_time: Optional[str] = None
    recurring: bool = False

    def update_task(self, duration_minutes: Optional[int] = None, priority: Optional[str] = None) -> None:
        if duration_minutes is not None:
            self.duration_minutes = max(1, duration_minutes)
        if priority is not None:
            self.priority = priority

    def mark_complete(self) -> None:
        self.priority = "completed"

    def get_priority_score(self) -> int:
        priority_map = {"low": 1, "medium": 2, "high": 3, "completed": 0}
        return priority_map.get(self.priority, 2)


@dataclass
class DailyPlan:
    date: str
    scheduled_tasks: List[CareTask] = field(default_factory=list)
    total_time_used: int = 0
    explanation_notes: List[str] = field(default_factory=list)

    def add_task(self, task: CareTask) -> None:
        self.scheduled_tasks.append(task)
        self.total_time_used += task.duration_minutes

    def remove_task(self, task: CareTask) -> None:
        if task in self.scheduled_tasks:
            self.scheduled_tasks.remove(task)
            self.total_time_used -= task.duration_minutes

    def generate_explanation(self) -> List[str]:
        return [f"Scheduled {task.title} because it is a {task.priority} priority task." for task in self.scheduled_tasks]

    def display_plan(self) -> str:
        if not self.scheduled_tasks:
            return "No tasks scheduled."
        lines = [f"Plan for {self.date}:"]
        for task in self.scheduled_tasks:
            lines.append(f"- {task.title} ({task.duration_minutes} min)")
        return "\n".join(lines)


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet, tasks: Optional[List[CareTask]] = None):
        self.owner = owner
        self.pet = pet
        self.tasks = tasks or []

    def sort_tasks(self) -> List[CareTask]:
        return sorted(self.tasks, key=lambda task: (-task.get_priority_score(), task.duration_minutes))

    def filter_tasks(self, available_minutes: Optional[int] = None) -> List[CareTask]:
        limit = available_minutes if available_minutes is not None else self.owner.available_time_per_day
        planned: List[CareTask] = []
        used = 0
        for task in self.sort_tasks():
            if used + task.duration_minutes <= limit:
                planned.append(task)
                used += task.duration_minutes
        return planned

    def build_daily_plan(self, available_minutes: Optional[int] = None) -> DailyPlan:
        plan = DailyPlan(date="today")
        for task in self.filter_tasks(available_minutes):
            plan.add_task(task)
        plan.explanation_notes = plan.generate_explanation()
        return plan

    def resolve_conflicts(self, available_minutes: Optional[int] = None) -> DailyPlan:
        return self.build_daily_plan(available_minutes)
