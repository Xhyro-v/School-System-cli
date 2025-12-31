import os
from Utility.Utility import Color, Input, Center
from Datamanager.DataEditor import StudentDataEditor
from Datamanager.Graders import StudentScoreEditor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Datacenter")

DATA_PATH = os.path.join(DATA_DIR, "Students.json")
DATA_PATH1 = os.path.join(DATA_DIR, "StudentsScore.json")

os.makedirs(DATA_DIR, exist_ok=True)

daftar = [
      "Matematika",
      "Bahasa Indonesia",
      "IPA (Ilmu Pengetahuan Alam)",
      "IPS (Ilmu Pengetahuan Sosial)",
      "Bahasa Inggris",
      "Pendidikan Agama",
      "Pendidikan Jasmani dan Olahraga (PJO)",
      "Seni Budaya",
      "PKN (Pendidikan Kewarganegaraan)",
      "Prakarya",
      "Teknologi Informasi dan Komunikasi (TIK)",
      "Bahasa Daerah"
]

print(Center.box(""))

while True:
    TM = input("Test add: ")

    if TM == "1":
        SDE = StudentDataEditor(DATA_PATH)

        name = Input.letter("nama: ").capitalize()
        age = Input.number("umur: ").strip()
        gender = input("jenis kelamin: ").capitalize()
        nisn = Input.number("NISN murid: ").strip()
        grade = Input.number("kelas: ").strip()
        subgrade = Input.letter(f"{grade} ruang: \n")

        SDE.add(grade, subgrade, name, age, gender, nisn)

        SSE = StudentScoreEditor(DATA_PATH1)
        SSE.db["StudentScore"].setdefault(nisn, {})
        SSE.save()

        print(Center.text("Done"))

    elif TM == "2":
        SS = StudentScoreEditor.SelectSubject
        IS = StudentScoreEditor.InputScores
        R  = StudentScoreEditor.Report

        nisn = Input.number("Masukkan NISN siswa: ").strip()
        subject = SS(daftar)
        NH, PTS, PAS = IS()
        Final = R(NH, PTS, PAS)

        SSE = StudentScoreEditor(DATA_PATH1)
        SSE.AddSubjectScore(nisn, subject, NH, PTS, PAS, Final)

        print(Color.Green(Center.text(
            f"Nilai {subject} berhasil disimpan"
        )))

    elif TM == "0":
        print(Color.Blue(Center.text("Program dimatikan")))
        break
