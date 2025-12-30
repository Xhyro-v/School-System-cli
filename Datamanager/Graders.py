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


        self.db["StudentScore"][NISN][subject] = {
            "Nilai harian": NH,
            "Penilaian tengah semester(PTS)": PTS,
            "Penilian akhir semester(PAS)": PAS,
            "Rata-rata nilai akhir": Final
        }

        self.save()
