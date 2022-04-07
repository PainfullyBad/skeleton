from datetime import datetime
from time import sleep
from cernitems import CernParts
import csv

f = open("cern.csv", "w")
#Datum
nu = datetime.now()
print(nu)
start_datum = nu.strftime('%Y;%m;%d;%I%p;%M;%S;')
eind_datum = nu.strftime('%Y;%m;%d;%I%p;%M;%S;')

genpart = CernParts()
for bin_teller in range(1000, 1100):
    bin_nummer = bin(bin_teller)
    bin_nummer = bin_nummer.replace('0b', '')
    for runs in range(0,4):
        print(f"|RunID{bin_nummer}|StartDatum-{start_datum}|EindDatum-{eind_datum}|sEnergy-{genpart.s_energy()}|eEnergy-{genpart.e_energy()}"
              f"|Collision-{genpart.col()}|ColPoint-{genpart.create_colpoint()}|CyclusID-{genpart.CyclusID()}|CyclusEnterSpeed-{genpart.Cyclus_EnterSpeed()}|CyclusExitSpeed-{genpart.Cyclus_ExitSpeed()}"
              f"|MeasurePoint-{genpart.create_measurepoint()}|Particle-{genpart.particle()}|ParticleN-{genpart.particleN()}|")
        f.write(f"{bin_nummer};{start_datum};{eind_datum};{genpart.s_energy()};{genpart.e_energy()};{genpart.col()};{genpart.create_colpoint()};{genpart.CyclusID()};{genpart.Cyclus_EnterSpeed()};{genpart.Cyclus_ExitSpeed()};{genpart.create_measurepoint()};{genpart.particle()};{genpart.particleN()}\n")

f.close()
sleep(4)