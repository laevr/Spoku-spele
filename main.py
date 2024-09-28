#1. uzdevums
"""
from random import randint  #importē randint, kas izvēlēsies neveiksmīgās jeb spoka durvis
rezultats = 0  #rezultāts pie kā tiks pieskaitīti punkti

print("Spoku spēle")  #nosaukums
print("Tev priekšā ir trīs durvis... ")  #spēles sākums, izskaidro situāciju
print("Aiz vienām ir SPOKS!")  #situācijas sarežģījums
jutos_drosmigs = True  #noteiks kad beigsies spēle, ja nebūs drosme spēle begsies

while jutos_drosmigs == True:  #kamēr drosme ir
  spoka_durvis = randint(
    1, 3)  #neveiksmīgās durvis ar spoku tiek izvēlētas nejauši
  print("Kuras durvis Tu atvērsi?"
        )  #Jautājums kuras durvis atvērsi veiksmīgās vai neveiksmīgās
  durvis = int(input("1, 2 vai 3?"))  #durvju opcijas
  durvju_num = int(durvis)  #durvis tiek pārdēvētas ar integer
  if durvju_num == spoka_durvis:  #ja izvēlētās durvis ir vienādas ar spoku durvīm
    print("Bēdz prom!")
    print("SPOKS!")
    jutos_drosmigs = False  #vairs nav drosmes spēle beidzas
  else:  #ja izvēlētās durvis nav vienādas ar spoku durvīm
    print("Spoka nav!")
    print("Tu vari ienākt nākamajā istabā.")  #spēle turpinās
    rezultats = rezultats + 1  #pieskaita punktus klāt

print("Spēle beigusies. Tu ieguvi", rezultats,
      "punktus.")  #rezultāta paziņošana kad beidzas spēle
"""
#2. uzvdevums

from random import randint  #importē randint, kas izvēlēsies neveiksmīgās jeb spoka durvis

rezultats = 0  #rezultāts pie kā tiks pieskaitīti punkti
dzivibas = 3  #dzīvības, kuras tiks zaudētas katru reizi ieraugot spoku
dimanti = 0
jutos_drosmigs = True  #noteiks kad beigsies spēle, ja nebūs drosme spēle begsies

print("\33[104m" + "SPOKU SPĒLE👻" + "\33[0m")  #nosaukums
print("Tev ir dotas " + "\33[31m" + "♥ ♥ ♥" + "\33[0m" + " dzīvības")
print("Tev priekšā ir trīs durvis... ")  #spēles sākums, izskaidro situāciju
print("╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ \n╙ ╜ ╙ ╜ ╙ ╜")
print("Aiz vienām durvīm ir SPOKS!")  #situācijas sarežģījums

while jutos_drosmigs == True:  #kamēr drosme ir
  spoka_durvis = randint(
    1, 3)  #neveiksmīgās durvis ar spoku tiek izvēlētas nejauši
  dimanta_durvis = randint(
    1, 8
  )  #lai gan nav 15 durvis izvēlējos šādu skaitli lai dimantiņibūtu pieejami retāk
  slepenas_durvis = randint(1, 30) 
  slepena_spoka_durvis = randint(1, 5)
  slepenas_davanas_durvis = randint(1, 5)
  print("------------------------------")
  print("Kuras durvis Tu atvērsi?"
        )  #Jautājums kuras durvis atvērsi veiksmīgās vai neveiksmīgās
  print("╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ \n╙ ╜ ╙ ╜ ╙ ╜")
  durvis = int(input("1, 2 vai 3? "))  #durvju opcijas
  durvju_num = int(durvis)  #durvis tiek pārdēvētas ar integer

  if durvju_num == spoka_durvis:  #ja izvēlētās durvis ir vienādas ar spoku durvīm
    print("------------------------------")
    if spoka_durvis == 1:
      print("╓ ╖ ╓ ╖ ╓ ╖\n👻  ║ ║ ║ ║\n╙ ╜ ╙ ╜ ╙ ╜")
    elif spoka_durvis == 2:
      print("╓ ╖ ╓ ╖ ╓ ╖\n║ ║ 👻  ║ ║\n╙ ╜ ╙ ╜ ╙ ╜")
    elif spoka_durvis == 3:
      print("╓ ╖ ╓ ╖ ╓ ╖\n║ ║ ║ ║ 👻\n╙ ╜ ╙ ╜ ╙ ╜")
    print("Bēdz prom!")
    print("SPOKS!")
    dzivibas = dzivibas - 1
    if dzivibas == 2:
      print("Tev ir pieejamas " + "\33[31m" + "♥ ♥" + "\33[0m" + " dzīvības")
    elif dzivibas == 1:
      print("Tev ir pieejama " + "\33[31m" + "♥" + "\33[0m" + " dzīvība")
    if dzivibas == 0:
      jutos_drosmigs = False  #vairs nav drosmes spēle beidzas
    else:
      continue
  elif durvju_num > 3:  #lai spēlētājam nebūtu iespēja dabūt punktus izvēloties durvis, kas neeksistē
    print("Šīs durvis neeksistē...")
    continue
  else:  #ja izvēlētās durvis nav vienādas ar spoku durvīm
    print("Spoka nav!")
    rezultats = rezultats + 1  #pieskaita punktus klāt
    if dimanta_durvis <= 3:
      if dimanta_durvis == durvju_num:
        print("Aiz", dimanta_durvis, "durvīm jūs atradāt dimantu!")
        if dimanta_durvis == 1:
          print("╓ ╖ ╓ ╖ ╓ ╖\n💎  ║ ║ ║ ║\n╙ ╜ ╙ ╜ ╙ ╜")
        elif dimanta_durvis == 2:
          print("╓ ╖ ╓ ╖ ╓ ╖\n║ ║ 💎  ║ ║\n╙ ╜ ╙ ╜ ╙ ╜")
        elif dimanta_durvis == 3:
          print("╓ ╖ ╓ ╖ ╓ ╖\n║ ║ ║ ║ 💎\n╙ ╜ ╙ ╜ ╙ ╜")
        dimanti += 1
    print("Tu vari ieiet nākamajā istabā.")  #spēle turpinās

    if slepenas_durvis <= 5:
      print("------------------------------")
      print("Tu esi atklājis īpašu istabu ar 5 durvīm!")
      print(
        "Vienā no šīm durvīm atrodas dāvaniņa, kas dos bonusa punktus tavam rezultātam!"
      )
      print(
        "Bet neaizmirsti, ka spoks vēl joprojām slēpjas aiz vienām no šīm durvīm."
      )
      print("Kuras durvis Tu atvērsi?")
      print("╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
      slepenas_durvis = int(input("1, 2, 3, 4 vai 5?"))
      slepeno_durvju_num = int(slepenas_durvis)
      if durvju_num > 5:
        print("Šīs durvis neeksistē...")
        continue
      if slepena_spoka_durvis == slepeno_durvju_num:
        print("------------------------------")
        if slepena_spoka_durvis == 1:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n👻║ ╟ ║ ╟ ║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepena_spoka_durvis == 2:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ 👻║ ╟ ║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepena_spoka_durvis == 3:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ 👻║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepena_spoka_durvis == 4:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ 👻║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepena_spoka_durvis == 5:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ ╟ ║ 👻║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        print("Bēdz prom!")
        print("SPOKS!")
        dzivibas = dzivibas - 1
        if dzivibas == 2:
          print("Tev ir pieejamas " + "\33[31m" + "♥ ♥" + "\33[0m" +
                " dzīvības")
        elif dzivibas == 1:
          print("Tev ir pieejama " + "\33[31m" + "♥" + "\33[0m" + " dzīvība")
        if dzivibas == 0:
          jutos_drosmigs = False  #vairs nav drosmes spēle beidzas
      elif slepenas_davanas_durvis == slepeno_durvju_num: 
        print("------------------------------")
        if slepenas_davanas_durvis == 1:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n🎁║ ╟ ║ ╟ ║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepenas_davanas_durvis == 2:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ 🎁║ ╟ ║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepenas_davanas_durvis == 3:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ 🎁║ ╟ ║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepenas_davanas_durvis == 4:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ 🎁║ ╟ ║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")
        elif slepenas_davanas_durvis == 5:
          print(
            "╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ ╓ ╖ \n╟ ║ ╟ ║ ╟ ║ ╟ ║ 🎁║\n╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜ ╙ ╜")

        dimantu_skaits = randint(3, 10)
        dimanti = dimanti + dimantu_skaits
        print("Tu saņēmi", dimantu_skaits, "dimantus!")
      else:
        print("Neko nelaimēji :( vari doties uz nākamo istabu! ")
        continue

print("\33[41m" + "SPĒLE BEIGUSIES!!!" + "\33[0m")
print("Tu ieguvi", rezultats, "🪙  punktus un", dimanti,
      "💎 dimantus!")  #rezultāta paziņošana kad beidzas

#Papildinājumi:
#dimanti
#vizuālās durvis
#dzīvības
#dāvaniņas kas dod bonusa punktus, kas atrodamas tikai tad, kad ieej telpā ar 5 druvīm
"""
if tavs_gajiens == 1:
    print(" ____________\n|   |   |   |\n| 🍬| 2 | 3 |\n|___|___|___|\n|   |   |   |\n| 4 | 5 | 6 |\n|___|___|___|")
elif tavs_gajiens == 2:
    print(" ____________\n|   |   |   |\n| 1 | 🍬| 3 |\n|___|___|___|\n|   |   |   |\n| 4 | 5 | 6 |\n|___|___|___|")
elif tavs_gajiens == 3:
    print(" ____________\n|   |   |   |\n| 1 | 2 | 🍬|\n|___|___|___|\n|   |   |   |\n| 4 | 5 | 6 |\n|___|___|___|")
elif tavs_gajiens == 4:
    print(" ____________\n|   |   |   |\n| 1 | 2 | 3 |\n|___|___|___|\n|   |   |   |\n| 🍬| 5 | 6 |\n|___|___|___|")
elif tavs_gajiens == 5:
    print(" ____________\n|   |   |   |\n| 1 | 2 | 3 |\n|___|___|___|\n|   |   |   |\n| 4 | 🍬| 6 |\n|___|___|___|")
elif tavs_gajiens == 6:
    print(" ____________\n|   |   |   |\n| 1 | 2 | 3 |\n|___|___|___|\n|   |   |   |\n| 4 | 5 | 🍬|\n|___|___|___|")
    """