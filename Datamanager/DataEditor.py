import json, os
from Utility.Utility import Color, Center


class BaseManager:
    def __init__(self, filepath):
        self.filepath = filepath

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.db = json.load(f)
        else:
            self.db = {}

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self.db, f, indent=4)


class StudentDataEditor(BaseManager):
    def __init__(self, filepath):
        super().__init__(filepath)

        if "Student" not in self.db:
            self.db["Student"] = {
                "7": {},
                "8": {},
                "9": {}
            }

    def add(self, Grade, Subgrade, Name, Age, Gender, NISN):
        Grade = str(Grade)
        Subgrade = Subgrade.upper()
        NISN = str(NISN)

        self.db["Student"].setdefault(Grade, {})
        self.db["Student"][Grade].setdefault(Subgrade, {})

        kelas = self.db["Student"][Grade][Subgrade]

        absen = max(
            [v["Absen"] for v in kelas.values()],
            default=0
        ) + 1

        kelas[NISN] = {
            "Nama": Name,
            "Umur": Age,
            "Jenis kelamin": Gender,
            "Absen": absen
        }

        self.save()

        print(Color.Green(
            Center.text(f"{Name} berhasil ditambahkan dengan NISN {NISN}")
        ))
