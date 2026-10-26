
"""Functions for managing student records."""

from typing import TypedDict


class Student(TypedDict):
    """Describe the fields stored in one student record."""

    id: str
    name: str


def create_student(
    students: list[Student], student_id: str, name: str
) -> Student:
    """Create and store a student after validating the details."""
    student_id = student_id.strip()
    name = name.strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty.")

    if not name:
        raise ValueError("Student name cannot be empty.")

    if search_student(students, student_id) is not None:
        raise ValueError(f"Student ID '{student_id}' already exists.")

    student: Student = {"id": student_id, "name": name}
    students.append(student)
    return student


def list_students(students: list[Student]) -> list[Student]:
    """Return all student records."""
    return students.copy()


def search_student(
    students: list[Student], student_id: str
) -> Student | None:
    """Find a student by ID, or return None when not found."""
    student_id = student_id.strip()

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def delete_student(students: list[Student], student_id: str) -> Student:
    """Delete and return a student, or raise an error if missing."""
    student_id = student_id.strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty.")

    student = search_student(students, student_id)

    if student is None:
        raise ValueError(f"Student ID '{student_id}' was not found.")

    students.remove(student)
    return student
