from random import randint

class CernParts:

    def particle(self):
        nummer = randint(0, 15)
        particle_list = ['Antihydrogon', 'Baryon', 'Diquark', 'Electron-neutrino', 'Gluon', 'Graviton', 'Lepton',
                         'Meson',
                         'Muon-neutrino', 'Pentaquark', 'Photon', 'Preons', 'Quarkonium', 'Tau-neutrino', 'W-Boson',
                         'Z-Boson']
        return particle_list[nummer]

    def particleN(self):
        return  randint(2, 989)

    def s_energy(self):
        return randint(8324747, 8806630838) / 1000

    def e_energy(self):
        return randint(8324747, 8809495866) / 1000

    def col(self):
        list_col = ["Yes", "No"]
        nummer = randint(0, 1)
        return list_col[nummer]

    def create_colpoint(self):
        lst_colpoint = ['CL1', 'CL2', 'CL3', 'CL5', 'CP1', 'CS1', 'CS2',]
        nummer = randint(0, 6)
        return lst_colpoint[nummer]

    def CyclusID(self):
        list_Cyclus = ['LHC', 'PS', 'SPS']
        nummer = randint(0, 2)
        return list_Cyclus[nummer]

    def Cyclus_EnterSpeed(self):
        return randint(56, 199988) / 1000
    def Cyclus_ExitSpeed(self):
        return  randint(80047, 320648) / 1000

    def create_measurepoint(self):
        lst_measurepoint = ['CL1', 'CL2', 'CP1', 'CS1', 'CS2',]
        nummer = randint(0, 4)
        return  lst_measurepoint[nummer]