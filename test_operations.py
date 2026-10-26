
"""Tests for the student record operations."""

import unittest

from record_manager.operations import (
    create_student,
    delete_student,
    list_students,
    search_student,
)


class TestStudentOperations(unittest.TestCase):
    """Test student record creation, search, listing and deletion."""

    def setUp(self) -> None:
        """Create fresh records before each test."""
        self.students = []

    def test_create_student(self) -> None:
        student = create_student(self.students, "101", "Ravi")
        self.assertEqual(student["name"], "Ravi")
        self.assertEqual(len(self.students), 1)

    def test_reject_empty_name(self) -> None:
        with self.assertRaises(ValueError):
            create_student(self.students, "101", "   ")

    def test_reject_duplicate_id(self) -> None:
        create_student(self.students, "101", "Ravi")

        with self.assertRaises(ValueError):
            create_student(self.students, "101", "Priya")

    def test_search_missing_student(self) -> None:
        result = search_student(self.students, "999")
        self.assertIsNone(result)

    def test_list_empty_records(self) -> None:
        self.assertEqual(list_students(self.students), [])

    def test_delete_student(self) -> None:
        create_student(self.students, "101", "Ravi")
        deleted = delete_student(self.students, "101")

        self.assertEqual(deleted["name"], "Ravi")
        self.assertEqual(self.students, [])

    def test_delete_missing_student(self) -> None:
        with self.assertRaises(ValueError):
            delete_student(self.students, "999")


if __name__ == "__main__":
    unittest.main()
