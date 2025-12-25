import json, os
from Utility.Utility import Color, Backcol, Input, Font, Center
from Datamanager.DataEditor import BaseManager, StudentDataEditor
#from Datamanager.Graders import Base, BaseKit, CountScore, StudentFinalScore
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Datacenter")
DATA_PATH = os.path.join(DATA_DIR, "Students.json")

os.makedirs(DATA_DIR, exist_ok = True)

print(Center.box(""))
TM = input("Menu selection: ")
if TM == "1":
      SDE = StudentDataEditor(DATA_PATH)
      name = Input.letter("nama: ").capitalize()
      age = Input.number("umur: ").strip()
      gender = input("jenis kelamin: ").capitalize()
      nisn = Input.number("NISN murid: ").strip()
      grade = Input.number("kelas: ").strip()
      subgrade = Input.letter(f"{grade} ruang: \n")
      SDE.add(grade, subgrade , name, age, gender, nisn)
