import os
from Utility.Utility import Color, Input, Center, Font
from Datamanager.DataEditor import StudentDataEditor
from Datamanager.Graders import StudentScoreEditor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Datacenter")

DATA_PATH = os.path.join(DATA_DIR, "Students.json")
DATA_PATH1 = os.path.join(DATA_DIR, "StudentsScore.json")

os.makedirs(DATA_DIR, exist_ok=True)

class Menu():
      def MenuUtama():
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
          
          print(Center.box("Mini School System"))
          print(Font.Italic(Center.text("By:Naufal\n")))
          print("======Menu utama======")
          print("1.Tambah siswa")
          print("2.Masukan nilai siswa\n")
          while True:
              TM = input("Pilih menu: ").strip().capitalize()
          
              if TM in ["1","Tambah siswa"]:
                  SDE = StudentDataEditor(DATA_PATH)
          
                  name = Input.letter("nama: ").capitalize()
                  age = Input.number("umur: ").strip()
                  gender = Input.letter("jenis kelamin: ").capitalize()
                  while True:
                     if gender not in ["Laki laki","Perempuan"]:
                          gender = Input.letter("Jenis kelamin: ").capitalize()
                     else:
                          nisn = Input.number("NISN murid: ").strip()
                          grade = Input.number("kelas: ").strip()
                          subgrade = Input.letter(f"{grade} ruang: \n")
                  
                          SDE.add(grade, subgrade, name, age, gender, nisn)
                  
                          SSE = StudentScoreEditor(DATA_PATH1)
                          SSE.db["StudentScore"].setdefault(nisn, {})
                          SSE.save()
                  
                          print(Center.text("Done"))
          
              elif TM in ["2","Masukan nilai siswa"]:
                  SS = StudentScoreEditor.SelectSubject
                  IS = StudentScoreEditor.InputScores
                  R  = StudentScoreEditor.Report
          
                  print(Font.Bold(Center.text("Memasukan nilai siswa")))
                  nisn = Input.number("Masukkan NISN siswa: ").strip()
                  subject = SS(daftar)
                  NH, PTS, PAS = IS()
                  Final = R(NH, PTS, PAS)
          
                  SSE = StudentScoreEditor(DATA_PATH1)
                  SSE.AddSubjectScore(nisn, subject, NH, PTS, PAS, Final)
          
                  print(Color.Green(Center.text(
                      f"Nilai {subject} {nisn} berhasil disimpan"
                  )))
          
              elif TM in ["3","Keluar"] :
                  print(Color.Blue(Center.text("Program dimatikan")))
                  break

Menu.MenuUtama()
