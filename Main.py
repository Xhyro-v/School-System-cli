import os
from Utility.Utility import Color, Input, Center, Font, UI
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
          
          UI.opening("MINI SCHOOL SYSTEM")
          print(Font.Italic(Center.text("Simple • Fast • Reliable")))
          print(Font.Italic(Center.text("By:Naufal Azhar")))
          print("")
          print(UI.H1("\nMENU UTAMA"))
          while True:
              print(Font.Bold("\n1.Tambah siswa"))
              print(Font.Bold("2.Masukan nilai siswa"))
              print(Font.Bold("3.Keluar\n"))
              TM = input("Pilih menu: ").strip().capitalize()
          
              if TM in ["1","Tambah siswa"]:
                  print(UI.H1("\nTAMBAH SISWA"))
         
                  SDE = StudentDataEditor(DATA_PATH)
          
                  name = Input.letter(f"{Color.Yellow('[1/6]')} Nama: ").capitalize()
                  age = Input.number(f"{Color.Yellow('[2/6]')} Umur: ").strip()
                  gender = Input.letter(f"{Color.Yellow('[3/6]')} Jenis kelamin: ").capitalize()
                  if gender not in ["laki laki","perempuan","Laki laki","Perempuan"]:
                       while True:
                           gender = Input.letter(f"{Color.Yellow('[3/6]')} Jenis kelamin: ").capitalize()
                  nisn = Input.number(f"{Color.Yellow('[4/6]')} NISN murid: ").strip()
                  grade = Input.number(f"{Color.Yellow('[5/6]')} Kelas: ").strip()
                  print("""RUANG Kelas
                  A     E
                  B     F
                  C     G
                  D     H
                          """)
                  subgrade = Input.letter(f"{Color.Yellow('[6/6]')} {grade} Ruang: ")
          
                  SDE.add(grade, subgrade, name, age, gender, nisn)
          
                  SSE = StudentScoreEditor(DATA_PATH1)
                  SSE.db["StudentScore"].setdefault(nisn, {})
                  SSE.save()
                  
          
              elif TM in ["2","Masukan nilai siswa"]:
                  print(UI.H1("NILAI SISWA"))
                  SS = StudentScoreEditor.SelectSubject
                  IS = StudentScoreEditor.InputScores
                  R  = StudentScoreEditor.Report
          
                  nisn = Input.number(f"{Color.Yellow('[1/4]')}Masukkan NISN siswa: ").strip()
                  print("")
                  subject = SS(daftar)
                  NH, PTS, PAS = IS()
                  Final = R(NH, PTS, PAS)
          
                  SSE = StudentScoreEditor(DATA_PATH1)
                  SSE.AddSubjectScore(nisn, subject, NH, PTS, PAS, Final)
          
                  print("")
                  print(Color.Green(Center.text(
                      f"Nilai {subject} {nisn} berhasil disimpan"
                  )))
          
              elif TM in ["3","Keluar"] :
                  print(Color.Blue(Center.text("Program dimatikan")))
                  break

              else:
                    print(Color.Red(Center.text("Tidak valid")))

Menu.MenuUtama()
            
