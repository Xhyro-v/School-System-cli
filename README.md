Mini School System (CLI)
A simple school management system built with Python — straight from the terminal, no fancy UI, just clean logic and real functionality.
This project was created as a learning journey, not just to “make it work”, but to understand how data, logic, and user interaction come together in a real program.

✨ About This Project
Mini School System is a command-line application that helps manage basic school data:
Student information
Student scores per subject
Automatic final score calculation
Data stored safely using JSON
Everything runs in the terminal. Fast, lightweight, and focused.
This project is perfect if you like:
CLI-based programs
Learning Python by building real stuff
Understanding how systems work behind the scenes

🚀 Features
Add new students by grade and class
Assign automatic attendance numbers
Input student scores (NH, PTS, PAS)
Automatic final score calculation
Letter grading system (A – D)
Clean terminal UI with colors and alignment
Persistent data using JSON files
No database. No frameworks. Just Python doing its job.

🗂 Project Structure
Salin kode

Mini-School-System/
│
├── Main.py                 # Main program & menu
├── Datamanager/
│   ├── DataEditor.py       # Student data manager
│   └── Graders.py          # Score & grading logic
│
├── Utility/
│   └── Utility.py          # Colors, UI, input validation
│
├── Datacenter/
│   ├── Students.json       # Student data storage
│   └── StudentsScore.json  # Student scores storage
│
└── README.md
Everything is separated by responsibility, so the code stays readable and scalable.

🧠 How It Works (Short Version)
Students are stored by grade and class
Each student has a unique NISN
Scores are saved per subject
Final score is calculated automatically:
Salin kode

Final = 40% NH + 30% PTS + 30% PAS
Scores are converted into letter grades
Simple logic, but realistic.

▶️ How To Run
Make sure you have Python 3.x installed.
Salin kode
Bash
python Main.py
That’s it. No setup drama.

🛠 Built With
Python
JSON (for data storage)
Pure logic (no external libraries)

📌 Why I Built This
This project isn’t about being perfect.
It’s about:
Practicing clean logic
Learning file-based data management
Understanding how real systems are structured
Building confidence by finishing something real
Every feature here exists because it needed to exist.

🔮 Future Ideas
Student data editing
Delete students or scores
Export reports
Better UI layout
Authentication system
Slowly but surely.

👤 Author
Naufal Azhar
Student • Builder • Learning by doing
