# Student Grade System

A comprehensive Python-based student grade management system that tracks academic performance across multiple students, year levels, and semesters.

## Features

- **Multi-Student Management**: Create and manage multiple student records
- **Academic Period Tracking**: Track courses for different year levels (1-4) and semesters (1-2)
- **Course Management**: Add courses with units and grades per academic period
- **GWA Calculation**: Automatic computation of General Weighted Average (GWA) per period and overall
- **Grade Descriptions**: Descriptive labels for numeric grades (Excellent, Very Good, Good, etc.)
- **Data Persistence**: Save and load student data using JSON format
- **Unit Limit Validation**: Maximum of 21 units per academic period

## Grade Scale

| Grade | Description |
|-------|-------------|
| 1.00 - 1.25 | Excellent |
| 1.50 - 1.75 | Very Good |
| 2.00 - 2.25 | Good |
| 2.50 - 2.75 | Satisfactory |
| 3.0 | Passed |
| 4.0 | Conditional |
| 5.0 | Failed |
| INC | Incomplete |

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only standard library)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system
3. No additional installation required!

## Usage

### Running the Program

```bash
python student_grade_system.py
```

### Main Menu Options

1. **Create New Student** - Add a new student to the system
2. **Select Existing Student** - Manage an existing student's records
3. **List All Students** - View all students in the system
4. **Save Data** - Manually save all data to JSON file
5. **Exit** - Exit the program (prompts to save)

### Managing a Student

After selecting a student, you can:

1. **Select Academic Period** - Choose or create a year-semester combination
2. **View All Periods** - List all academic periods for the student
3. **Show Complete Summary** - Display full academic record with overall GWA
4. **Back to Main Menu** - Return to main menu

### Managing an Academic Period

Within a specific period (e.g., Year 1, Semester 1):

1. **Add Course** - Add a new course with units and grade
2. **Show Courses** - Display all courses in this period
3. **Show Period Summary** - View courses and GWA for this period
4. **Back to Student Menu** - Return to student management

## Data Structure

### Student Information
- Student Name
- Student ID (numeric)
- Multiple Academic Periods

### Academic Period
- Year Level (1-4)
- Semester (1-2)
- List of Courses
- Period GWA

### Course Information
- Course Name
- Units (credit hours)
- Grade (1.0-5.0 or "INC")

## File Storage

All data is automatically saved to `students_data.json` in the same directory as the program. The file is created automatically on first save.

### JSON Structure
```json
{
  "202412301": {
    "name": "Merry",
    "id": 202412301,
    "periods": [
      {
        "year_level": 1,
        "semester": 1,
        "courses": [
          {
            "name": "Math 101",
            "units": 3,
            "grade": 1.5
          }
        ]
      }
    ]
  }
}
```

## Example Workflow

1. **Start the program**
   ```
   python student_grade_system.py
   ```

2. **Create a new student**
   - Choose option 1
   - Enter name: "Merry Grace"
   - Enter ID: 202412301

3. **Add courses for Year 1, Semester 1**
   - Select student (option 2)
   - Select Academic Period (option 1)
   - Enter Year: 1, Semester: 1
   - Add courses with grades

4. **Add courses for Year 1, Semester 2**
   - Select Academic Period again
   - Enter Year: 1, Semester: 2
   - Add different courses

5. **View complete summary**
   - Choose option 3 to see all periods and overall GWA

6. **Save and exit**
   - Choose option 5
   - Confirm save when prompted

## Features in Detail

### GWA Calculation
- **Period GWA**: Calculated using only numeric grades from courses in that period
- **Overall GWA**: Weighted average across all periods and courses
- Formula: `GWA = Σ(Grade × Units) / Σ(Units)`
- Incomplete (INC) grades are excluded from calculations

### Unit Limits
- Maximum 21 units per academic period
- System prevents adding courses that would exceed this limit

### Input Validation
- Year level: Must be 1-4
- Semester: Must be 1-2
- Grade: Must be 1.0-5.0 or "INC"
- Units: Must be positive integers
- Student ID: Must be unique numeric values

## Error Handling

The system handles common errors:
- Duplicate student IDs
- Invalid grade inputs
- Exceeding unit limits
- Missing or corrupted data files
- Invalid menu selections

## Future Enhancements

Potential features for future versions:
- Delete/edit courses and students
- Export reports to PDF or CSV
- Academic standing calculation
- Course prerequisites tracking
- Transcript generation
- Search and filter functionality
- Password protection for student records

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Support

For issues or questions, please open an issue in the repository.

---

**Version**: 2.0  
**Last Updated**: December 18, 2025  
**Author**: Merry Grace Potot