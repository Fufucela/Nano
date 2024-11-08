# naam = "Fu-An"
# klas = "V1R"
# studentnummer = 1888783


import getal
import dagboek
import time

print("Welkom bij de keuzemenu") # Er wordt gevraagd of de gebruiker optie 1 of 2 wilt kiezen. En de daarbij behorende functie en bestand wordt geopened.
time.sleep(1)
print("1: Raad het nummer")
time.sleep(1)
print("2: Dagboek")
time.sleep(1)
keuze = input("Kies een optie:")
if keuze == "1":
    getal.play_game()
if keuze == "2":
    dagboek.open_dagboek()

