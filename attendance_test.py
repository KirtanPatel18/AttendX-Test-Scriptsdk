
import unittest

def mark_attendance(student_id, present):
    if not student_id:
        return "Student ID required"
    if present:
        return "Attendance marked"
    return "Student is absent"


class AttendanceTest(unittest.TestCase):

    def test_mark_present(self):
        self.assertEqual(
            mark_attendance("ST101", True),
            "Attendance marked"
        )

    def test_empty_student_id(self):
        self.assertEqual(
            mark_attendance("", True),
            "Student ID required"
        )

    def test_absent_student(self):
        self.assertEqual(
            mark_attendance("ST102", False),
            "Student is absent"
        )


if __name__ == "__main__":
    unittest.main()
