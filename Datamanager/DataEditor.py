import json, os
from Utility.Utility import Color, Backcol, Font, Input, Center


# ================= PATH =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Datacenter")

DATA_PATH = os.path.join(DATA_DIR, "Students.json")
DATA_PATH1 = os.path.join(DATA_DIR, "StudentsScore.json")

os.makedirs(DATA_DIR, exist_ok=True)
#==============================================
#There are some issues that prevent the data from being created and not going into the json data file, I am working on it
class BaseManager:
    def __init__(self, filepath):
        self.filepath = filepath

        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                self.db = json.load(f)
        else:
            self.db = {}
            self.save()

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
            self.save()

    def add(self, Grade, Subgrade, Name, Age, Gender, NISN):
        grade = str(Grade)
        subclass = Subgrade.upper()

        self.db["Student"].setdefault(grade, {})
        self.db["Student"][grade].setdefault(subclass, {})

        kelas = self.db["Student"][grade][subclass]

        new_absen = max(
            [value["Absen"] for value in kelas.values()],
            default=0
        ) + 1

        kelas[NISN] = {
            "Nama": Name,
            "Umur": Age,
            "Jenis kelamin": Gender,
            "Absen": new_absen
        }

        self.save()


        if os.path.exists(DATA_PATH1):
            with open(DATA_PATH1, "r") as f:
                nilai = json.load(f)
        else:
            nilai = {"StudentScore": {}}

        nilai.setdefault("StudentScore", {})

        if NISN not in nilai["StudentScore"]:
            nilai["StudentScore"][NISN] = {
                "Matematika": {},
                "Bahasa Indonesia": {},
                "Bahasa Inggris": {},
                "IPS": {},
                "IPA": {},
                "Informatika": {},
                "Pendidikan agama": {},
                "PPKN": {},
                "PJOK": {},
                "Seni budaya": {},
                "Muatan lokal": {}
            }

        with open(DATA_PATH1, "w") as f:
            json.dump(nilai, f, indent=4)


        if Gender == "Laki laki":
            print(Color.Green(
                Center.text(
                    f"Siswa bernama {Name} berhasil dimasukan ke kelas {subclass} dengan NISN {NISN}"
                )
            ))
        elif Gender == "Perempuan":
            print(Color.Green(
                Center.text(
                    f"Siswi bernama {Name} berhasil dimasukan ke kelas {subclass} dengan NISN {NISN}"
                )
            ))
        else:
            print(Color.Red(Center.text("Field error / Something wrong")))
