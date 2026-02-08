# 🎓 Py High School Registration System

A console-based student registration and evaluation system built with Python.

This project simulates a high school admission process by collecting student information, validating inputs, evaluating academic performance, skills, and personality traits, and finally deciding whether a student is accepted or rejected.

No frameworks. No databases. Just Python doing the work.

---

## 📌 Features

- **Student Registration**
  - Collects personal information with input validation
  - Only allows students aged **14 to 19**

- **Academic Score Evaluation**
  - Subjects: Math, Physics, Chemistry, Geometry, English
  - Scores must be between **0 and 20**
  - Automatically calculates the average score

- **Skill Selection System**
  - Main skills: Programming, Art, Sports, Other
  - Each main skill includes multiple sub-skills
  - Supports adding multiple skills per student

- **Personality Test**
  - 10 yes/no questions
  - Evaluates leadership, motivation, and planning habits

- **Admission Logic**
  A student is accepted only if:
  - No subject score is below 10
  - Average score is at least 14
  - More than 2 skills are selected
  - Personality test score is 5 or higher

- **Data Storage**
  - Student data is saved in a `student.json` file
  - Supports viewing and deleting registered students

---

## 🧪 Technologies Used

- Python 3
- Built-in libraries:
  - `json`
  - `os`

---

## ▶️ How to Run

1. Make sure Python 3 is installed
2. Clone the repository
3. Run the program:

```bash
python main.py
