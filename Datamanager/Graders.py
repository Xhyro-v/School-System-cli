from Utility.Utility import Input, Color, Center, Backcol, Font
from Datamanager.DataEditor import BaseManager
import json, os

class StudentScoreEditor(BaseManager):

    def __init__(self, filepath):
        super().__init__(filepath)

        if "StudentScore" not in self.db:
            self.db["StudentScore"] = {}
            self.save()

    @staticmethod
    def Report(NH, PTS, PAS):
        final_grade = (
            NH * 0.40 +
            PTS * 0.30 +
            PAS * 0.30 
        )
        return round(final_grade, 2)

    @staticmethod
    def SelectSubject(daftar):
        print("Pilih pelajaran: ")
        for i, p in enumerate(daftar, start=1):
            print(f"{i}. {p}")
        pilihan = int(input("Masukkan nomor: "))
        return daftar[pilihan - 1]

    @staticmethod
    def InputScores():
        NH = float(input("Masukan rata-rata nilai harian: "))
        PTS = float(input("Masukan nilai PTS: "))
        PAS = float(input("Masukan nilai PAS: "))
        return NH, PTS, PAS
#Still have a issues here
    def AddSubjectScore(self, nisn, subject, nh, pts, pas, final):
        nisn = str(nisn)
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.db = json.load(f)
    
        if "StudentScore" not in self.db:
            self.db["StudentScore"] = {}
    
        self.db["StudentScore"].setdefault(nisn, {})
        self.db["StudentScore"][nisn][subject] = {
            "NH": nh,
            "PTS": pts,
            "PAS": pas,
            "Final": final
        }
    
        self.save()
      #there is a slight problem with entering data from here to the json score students file
