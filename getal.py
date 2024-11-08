# naam = "Fu-An"
# klas = "V1R"
# studentnummer = 1888783

import random
import time

def play_game():
    # genereert een random getal tussen 1 en 13
    invoer_getal= random.randrange(1, 13)

    # maximaal aantal kansen en hoeveel kansen er zijn geweest
    max_kansen = 3
    kansen = 0

    # vraagt voor een getal aan de gebruiker
    time.sleep(1)
    guess = int(input("U heeft 3 kansen om het juiste nummer te raden. Kies een nummer tussen 1 en 13: "))

    # herhaalt tot dat de gebruiker het nummer heeft geraden of
    # tot dat de gebruiker het maximaal aantal kansen heeft bereikt
    while invoer_getal != guess and kansen < max_kansen - 1:
        kansen += 1  # Bij gebruik +1 bij kansen
        if guess < invoer_getal: # als het geraden getal lager is dan het getal, dan wordt dit aan de gebruiker vermeld.
            time.sleep(1)
            print("Te laag")
            time.sleep(1)
            guess = int(input("Kies opnieuw een nummer: "))
            time.sleep(1)
        elif guess > invoer_getal: # dit gebeurd ook als het getal te hoog is.
            time.sleep(1)
            print("Te hoog")
            time.sleep(1)
            guess = int(input("Kies opnieuw een nummer: "))
            time.sleep(1)
        else:
            break

    # kijkt of de gebruiker het getal heeft geraden. Of kijkt of het aantal maximaal kansen is bereikt.
    if invoer_getal == guess:
        print("Gefeliciteerd, u heeft het juiste nummer geraden!")
    else:
        print(f"Sorry, u heeft het nummer niet kunnen raden. Het nummer was {invoer_getal}.")
    time.sleep(1)
    print("Bedankt voor het spelen")