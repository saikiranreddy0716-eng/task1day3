
"""Command-line interface for the student record manager."""

from record_manager.operations import (
    Student,
    create_student,
    delete_student,
    list_students,
    search_student,
)


def show_menu() -> None:
    """Display the available operations."""
    print("\n===== Student Record Manager =====")
    print("1. Create student")
    print("2. List students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")


def main() -> None:
    """Run the interactive student management menu."""
    students: list[Student] = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")

                student = create_student(students, student_id, name)
                print(f"Student '{student['name']}' created successfully.")

            elif choice == "2":
                records = list_students(students)

                if not records:
                    print("No student records found.")
                else:
                    print("\nStudent records:")
                    for student in records:
                        print(f"ID: {student['id']} | Name: {student['name']}")

            elif choice == "3":
                student_id = input("Enter student ID to search: ")
                student = search_student(students, student_id)

                if student is None:
                    print(f"No student found with ID '{student_id.strip()}'.")
                else:
                    print(f"ID: {student['id']} | Name: {student['name']}")

            elif choice == "4":
                student_id = input("Enter student ID to delete: ")
                student = delete_student(students, student_id)
                print(f"Student '{student['name']}' deleted successfully.")

            elif choice == "5":
                print("Thank you for using the Student Record Manager.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
