from Datamanager.DataEditor import BaseManager

class StudentScoreEditor(BaseManager):

    def __init__(self, filepath):
        super().__init__(filepath)

        if "StudentScore" not in self.db:
            self.db["StudentScore"] = {}

    @staticmethod
    def Report(NH, PTS, PAS):
        return round(NH * 0.40 + PTS * 0.30 + PAS * 0.30, 2)

    @staticmethod
    def SelectSubject(daftar):
        for i, p in enumerate(daftar, 1):
            print(f"{i}. {p}")
        return daftar[int(input("Pilih: ")) - 1]

    @staticmethod
    def InputScores():
        return (
            float(input("NH: ")),
            float(input("PTS: ")),
            float(input("PAS: "))
        )

    def AddSubjectScore(self, NISN, subject, NH, PTS, PAS, Final):
        NISN = str(NISN)

        if NISN not in self.db["StudentScore"]:
            print("NISN tidak terdaftar, tambahkan siswa terlebih dahulu")
            return

        if Final >= 90:
            Final = f"{Final} - (A)"
        elif Final >= 80:
            Final = f"{Final} - (B+)"
        elif Final >= 75:
            Final = f"{Final} - (B-)"
        elif Final >= 70:
            Final = f"{Final} - (C+)"
        elif Final >= 60:
            Final = f"{Final} - (C-)"
        else:
            Final = f"{Final} - (D)"

        if NH >= 90:
            NH = f"{NH} - (A)"
        elif Final >= 80:
            NH = f"{NH} - (B+)"
        elif Final >= 75:
            NH = f"{NH} - (B-)"
        elif NH >= 70:
            NH = f"{NH} - (C+)"
        elif NH >= 60:
            NH = f"{NH} - (C-)"
        else:
            NH = f"{NH} - (D)"

        if PTS >= 90:
            PTS = f"{PTS} - (A)"
        elif PTS >= 80:
            PTS = f"{PTS} - (B+)"
        elif PTS >= 75:
            PTS = f"{PTS} - (B-)"
        elif PTS >= 70:
            PTS = f"{PTS} - (C+)"
        elif PTS >= 60:
            PTS = f"{PTS} - (C-)"
        else:
            PTS = f"{PTS} - (D)"

        if PAS >= 90:
            PAS = f"{PAS} - (A)"
        elif PAS >= 80:
            PAS = f"{PAS} - (B+)"
        elif PAS >= 75:
            PAS = f"{PAS} - (B-)"
        elif PAS >= 70:
            PAS = f"{PAS} - (C+)"
        elif PAS >= 60:
            PAS = f"{PAS} - (C-)"
        else:
            PAS = f"{PAS} - (D)"
            

        self.db["StudentScore"][NISN][subject] = {
            "Nilai harian": NH,
            "Penilaian tengah semester(PTS)": PTS,
            "Penilian akhir semester(PAS)": PAS,
            "Rata-rata nilai akhir": Final
        }

        self.save()
