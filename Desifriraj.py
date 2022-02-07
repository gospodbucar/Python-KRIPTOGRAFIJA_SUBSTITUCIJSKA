# Janez Bučar 35160122 izjavljam da je program moje delo 19.12.2021
# Program sem delal v PyCharm community edition, in vse deluje kot mora, ker ob testiranju v visualstudio nedelajo Č
#  in Ž tako, da prosim da uporabljate omenjen program ob testiranju.
# DODA PIP ČE ŠE NI INSTALIRAN 'pip install Counter':
# PROGRAM OMOGOČA POMIK PO ABECEDI V NAPREJ ALI NAZAJ AMPAK GA NISEM UPORABIL PRI NALOGI
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'Counter'])


from collections import Counter

# odpre datoteko
file = open("tajnopis.txt", "r")

# prebere
data = file.read().encode('windows-1250').decode('utf-8')

# dobi frekfenco znakov
Frekfenca_Ponavljanja = Counter(data)

print(len(data))
# prikaz
print("Frekfenca ponavljanja posameznih znakov je:\n "
      + str(Frekfenca_Ponavljanja))

# zamenjava črk funkcija


def zamenjaj(sporocilo):
    p = 'w'
    y = input("Katero črko želite zamenjati?:  ")
    z = input("Za Katero črko jo želite zamenjati?:  ")

    sporocilo = sporocilo.replace(z, p).replace(y, z). replace(p, y)

    return sporocilo

# pomik po abecedi funkcija


def pomik(sporocilo):

    abeceda = 'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'

    novo_sporocilo = ''
    kljuc = int(input("kljuc:  "))
    print(type(kljuc))
    for i in sporocilo:

        if i not in abeceda:
            novo_sporocilo += i
        else:

            pos = abeceda.find(i)
            newpos = (pos + kljuc) % 25
            novo_sporocilo += abeceda[newpos]

    return novo_sporocilo


def main():

    sporocilo = data
    x = 7
    while x != 9:

        print("Zamenjaj crko - 1, prikaži sporočilo - 2, Pomik po abecedi (naprej) - 3, izhod - 4")
        x = input()
        if x == '1':


                sporocilo = zamenjaj(sporocilo)
                print(sporocilo)

                Frekfenca_Ponavljanja = Counter(sporocilo)

                print("Frekfenca ponavljanja posameznih znakov je:\n "
                      + str(Frekfenca_Ponavljanja))

        elif x == '2':

            print(sporocilo)

        elif x == '3':

            lsporocilo = pomik(sporocilo)

            print(lsporocilo)

        else:
            x = 9


main()
