import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "students_data.json")

# The class Course
class Course:
    def __init__(self, name, units, grade):
        self.name = name
        self.units = units
        self.grade = grade # float between 1.0 and 5.0

    def is_numeric_grade(self):
        return isinstance(self.grade, float)
    
    def to_dict(self):
        # Convert course details to dictionary for JSON
        return {
            "name": self.name,
            "units": self.units,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        # Create a Course object from a dictionary
        return Course(data['name'], data['units'], data['grade'])

# The class for Academic Period 
class AcademicPeriod:
    max_units = 21

    def __init__(self, year_level, semester):
        self.year_level = year_level
        self.semester = semester
        self.courses = []
    
    def get_period_name(self):
        return f"Year {self.year_level} - Semester {self.semester}"
    
    def total_units(self):
        return sum(course.units for course in self.courses)
    
    def add_course(self, name, units, grade):
        if self.total_units() + units > AcademicPeriod.max_units:
            print(f"Cannot add course {name}. Exceeds maximum allowed units.")
            return
        
        self.courses.append(Course(name, units, grade))
        print(f"Course {name} added successfully.")
        return True
    
    def compute_gwa(self):
        total_weighted = 0
        total_units = 0

        for course in self.courses:
            if course.is_numeric_grade():
                total_weighted += course.grade * course.units
                total_units += course.units

        if total_units == 0:
            return 0.0
        
        return total_weighted / total_units
    
    def grade_description(self, grade):
        if grade == "INC":
            return "Incomplete"
        if grade == 5.0:
            return "Failed"
        if grade == 4.0:
            return "Conditional"
        if 1.00 <= grade <= 1.25:
            return "Excellent"
        if 1.50 <= grade <= 1.75:
            return "Very Good"
        if 2.00 <= grade <= 2.25:
            return "Good"
        if 2.50 <= grade <= 2.75:
            return "Satisfactory"
        if grade == 3.0:
            return "Passed"
        return "Invalid grade"
    
    def show_courses(self):
        if not self.courses:
            print(f"No courses enrolled in {self.get_period_name()}.")
            return

        print(f"\n--- Enrolled Courses for {self.get_period_name()} ---")
        for i, course in enumerate(self.courses, start=1):
            print(f"{i}, {course.name}")
            print(f"   Units: {course.units}")
            print(f"   Grade: {course.grade} ({self.grade_description(course.grade)})")

    def to_dict(self):
        # Convert academic period details to dictionary for JSON
        return {
            "year_level": self.year_level,
            "semester": self.semester,
            "courses": [course.to_dict() for course in self.courses]
        }
    
    @staticmethod
    def from_dict(data):
        # Create an AcademicPeriod from a dictionary
        period = AcademicPeriod(data['year_level'], data['semester'])
        period.courses = [Course.from_dict(c) for c in data['courses']]
        return period

# The class Student
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.periods = {}

    def get_or_create_period(self, year_level, semester):
        # Get existing or create new academic period
        key = (year_level, semester)
        if key not in self.periods:
            self.periods[key] = AcademicPeriod(year_level, semester)
        return self.periods[key]

    def get_period(self, year_level, semester):
        # Get existing academic period
        key = (year_level, semester)
        return self.periods.get(key)
    
    def list_periods(self):
        # List all academic periods
        if not self.periods:
            print("No academic periods registered yet.")
            return

        print("\n--- Academic Periods ---") # Study this
        sorted_periods = sorted(self.periods.items(), key=lambda x: (x[0][0], x[0][1]))
        for i, (key, period) in enumerate(sorted_periods, start=1):
            gwa = period.compute_gwa()
            gwa_str = f"{gwa:.2f}" if gwa > 0 else "N/A"
            print(f"{i}. {period.get_period_name()} - Units: {period.total_units()} - GWA: {gwa_str}")
        
        return sorted_periods
    
    def compute_overall_gwa(self):
        # Compute overall GWA across all periods
        total_weighted = 0
        total_units = 0

        for period in self.periods.values():
            for course in period.courses:
                if course.is_numeric_grade():
                    total_weighted += course.grade * course.units
                    total_units += course.units

        if total_units == 0:
            return 0.0
        
        return total_weighted / total_units
    
    def show_summary(self):
        print(f"\n{'='*50}")
        print(f"\n--- Student Summary for {self.name} ---")
        print(f"\n{'='*50}")
        print(f"Student Id: {self.id}")
        print(f"Total Academic Periods: {len(self.periods)}")

        if not self.periods:
            print("No academic periods registered yet.")
            return

        # Show each period's courses
        sorted_periods = sorted(self.periods.items(), key=lambda x: (x[0][0], x[0][1]))
        for key, period in sorted_periods:
            print(f"\n{'-'*50}")
            period.show_courses()
            gwa = period.compute_gwa()
            if gwa > 0:
                print(f"Period GWA: {gwa:.2f}")
        
        # Show overall GWA
        print(f"\n{'='*50}")
        overall_gwa = self.compute_overall_gwa()
        if overall_gwa > 0:
            print(f"OVERALL GWA: {overall_gwa:.2f}")
        else:
            print("OVERALL GWA: N/A")
        print(f"{'='*50}")

    def to_dict(self):
        """Convert student to dictionary for JSON serialization"""
        return {
            'name': self.name,
            'id': self.id,
            'periods': [period.to_dict() for period in self.periods.values()]
        }
    
    @staticmethod
    def from_dict(data):
        """Create student from dictionary"""
        student = Student(data['name'], data['id'])
        for period_data in data['periods']:
            period = AcademicPeriod.from_dict(period_data)
            key = (period.year_level, period.semester)
            student.periods[key] = period
        return student

# This is the student management system
class StudentSystem:
    def __init__(self, filename=FILE_NAME):
        self.students = {}
        self.filename = filename
        self.load_data()
    
    def add_student(self, name, student_id):
        # Add a new student to the system)
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists!")
            return
        
        student = Student(name, student_id)
        self.students[student_id] = student
        print(f"Student {name} added successfully.")
        return student
    
    def get_student(self, student_id):
        # Get student by ID
        return self.students.get(student_id)
    
    def list_students(self):
        # List all students
        if not self.students:
            print("No students registered yet.")
            return

        print("\n--- All Students ---")
        for student_id, student in self.students.items():
            period_count = len(student.periods)
            print(f"ID: {student_id} | Name: {student.name} | Periods: {period_count}")

    def save_data(self):
        # Save all students data to JSON file 
        data = {
            student_id: student.to_dict() 
            for student_id, student in self.students.items()
        } 
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        # Load students data from JSON file
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)

            self.students = {int(student_id): Student.from_dict(student_data) for student_id, student_data in data.items()}
            print(f"Loaded {len(self.students)} student(s) from {self.filename}")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.students = {}


def print_menu():
    print("\n--- Student Grade System ---")
    print("1. Create New Student")
    print("2. Select Existing Student")
    print("3. List All Students")
    print("4. Save Data")
    print("5. Exit")

def print_student_menu(student):
    print(f"\n=== Managing: {student.name} (ID: {student.id}) ===")
    print("1. Select Academic Period")
    print("2. View All Periods")
    print("3. Show Complete Summary")
    print("4. Back to Main Menu")

def print_period_menu(student, period):
    print(f"\n=== {student.name} - {period.get_period_name()} ===")
    print("1. Add Course")
    print("2. Show Courses")
    print("3. Show Period Summary")
    print("4. Back to Student Menu")

def get_valid_int(prompt, min_val=None, max_val=None):
    # Helper function to get valid integer input
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def create_new_student(system):
    # Add a new student in the system
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    student_id = get_valid_int("Enter student ID: ", min_val=1)

    return system.add_student(name, student_id)

def select_period(student):
    # Select or create an academic period for the student
    print("\n--- Select Academic Period ---")
    year_level = get_valid_int("Enter year level (1-4): ", min_val=1, max_val=4)
    semester = get_valid_int("Enter semester (1-2): ", min_val=1, max_val=2)

    period = student.get_or_create_period(year_level, semester)
    print(f"Selected period: {period.get_period_name()}")
    return period

def manage_period(student, period):
    # Manage a specific academic period
    while True:
        print_period_menu(student, period)
        choice = input("Choose an option: ")

        if choice == '1':
            course_name = input("Enter course name: ")
            units = get_valid_int("Enter course units: ", min_val=1)
            grade_input = input("Enter course grade (numeric or 'INC'): ")
            try:
                grade = float(grade_input)
                if grade < 1.0 or grade > 5.0:
                    print("Grade must be between 1.0 and 5.0")
                    continue
            except ValueError:
                if grade_input.upper() == "INC":
                    grade = "INC"
                else:
                    print("Invalid grade input. Use numeric value or 'INC'.")
                    continue
            period.add_course(course_name, units, grade)
        
        elif choice == '2':
            period.show_courses()
        
        elif choice == '3':
            gwa = period.compute_gwa()
            if gwa > 0:
                print(f"Period GWA: {gwa:.2f}")
            else:
                print("No numeric grades available to compute GWA.")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

def manage_student(student, system):
    # Manage a specific student
    while True:
        print_student_menu(student)
        choice = input("Choose an option: ")

        if choice == '1':
            period = select_period(student)
            manage_period(student, period)
        
        elif choice == '2':
            student.list_periods()
        
        elif choice == '3':
            student.show_summary()
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    system = StudentSystem()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            create_new_student(system)
        
        elif choice == '2':
            system.list_students()
            if system.students:
                student_id = get_valid_int("Enter student ID to select: ")
                student = system.get_student(student_id)
                if student:
                    manage_student(student, system)
                else:
                    print(f"No student found with ID {student_id}.")
        
        elif choice == '3':
            system.list_students()
        
        elif choice == '4':
            system.save_data()
        
        elif choice == '5':
            system.save_data()
            print("Data saved automatically and exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
