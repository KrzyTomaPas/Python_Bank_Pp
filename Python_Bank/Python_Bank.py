# BANK
print("WYBIERZ OPCJÊ:")
print("1 => LISTA WSZYSTKICH KLIENTÓW BANKU")
print("2 => LOGOWANIE")
print("3 => ZAKOÑCZ PROGRAM")
people = [
  '1| JAN NOWAK| 001| 1457.23 z³', '2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
  '3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
  '4| Zofia Pluciñska| 004| 7344.00 z³', '5| Grzegorz Braun| 005| 455.38 z³'
]

number = int(input("WYBIERZ 1,2 LUB 3: "))
if number == 1:
  for i in people:
    print(i)
  print("WYBIERZ OPCJÊ:")
  print("1 => LISTA WSZYSTKICH KLIENTÓW BANKU")
  print("2 => LOGOWANIE")
  print("3 => ZAKOÑCZ PROGRAM")
  second = int(input("WYBIERZ 1,2 LUB 3: "))
  if second == 2:
    id_user = (str(input("ZAlOGUJ SIÊ WYBIERAJ¥C ID KLIENTA: ")))
    if id_user == "001":
      print("ZALOGOWANY KLIENT \n ID: 1 \n IMIÊ I NAZWISKO: Jan Nowak \n NR KONTA: 001 \n SALDO: 1457,23 z³\n")
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "001":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|', suma, 'z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, ' z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif id_user == "002":
    print("ZALOGOWANY KLIENT \n ID: 2 \n IMIÊ I NAZWISKO: Agnieszka Kowalska \n NR KONTA: 002 \n SALDO: 3600.18 z³\n")
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "002":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|', roznica, 'z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 7344.00 + kwota
        white = '\033[0;0m'
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif id_user == "003":
    print("ZALOGOWANY KLIENT \n ID: 3 \n IMIÊ I NAZWISKO: Robert Lewandowski \n NR KONTA: 003 \n SALDO: 2745.03 z³\n")
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "003":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| ', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 7344.00 + kwota
        white = '\033[0;0m'
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif id_user == "004":
    print("ZALOGOWANY KLIENT \n ID: 4 \n IMIÊ I NAZWISKO: Zofia Pluciñska \n NR KONTA: 004 \n SALDO: 7344.00 z³\n")
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "004":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif id_user == "005":
    print("ZALOGOWANY KLIENT \n ID: 5 \n IMIÊ I NAZWISKO: Grzegorz Braun \n NR KONTA: 005 \n SALDO: 455.38 z³\n")
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "005":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|7344.00 z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
    id_user = print("ZALOGUJ SIÊ WYBIERAJ¥C ID KLIENTA:")
  if second == 3:
    print(" ")
elif number == 2:
  user = str(input("ZALOGUJ SIÊ WYBIERAJ¥C ID KLIENTA: "))
  if user == "001":
    print(
      "ZALOGOWANY KLIENT \n ID: 1 \n IMIÊ I NAZWISKO: Jan Nowak \n NR KONTA: 001 \n SALDO: 1457,23 z³\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "001":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|', suma, 'z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, ' z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif user == "002":
    print(
      "ZALOGOWANY KLIENT \n ID: 2 \n IMIÊ I NAZWISKO: Agnieszka Kowalska \n NR KONTA: 002 \n SALDO: 3600.18 z³\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "002":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|', roznica, 'z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif user == "003":
    print(
      "ZALOGOWANY KLIENT \n ID: 3 \n IMIÊ I NAZWISKO: Robert Lewandowski \n NR KONTA: 003 \n SALDO: 2745.03 z³\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "003":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| ', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif user == "004":
    print(
      "ZALOGOWANY KLIENT \n ID: 4 \n IMIÊ I NAZWISKO: Zofia Pluciñska \n NR KONTA: 004 \n SALDO: 7344.00 z³\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "004":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002|3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005| 455.38 z³')
    if konto == "005":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', roznica, 'z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
  elif user == "005":
    print(
      "ZALOGOWANY KLIENT \n ID: 5 \n IMIÊ I NAZWISKO: Grzegorz Braun \n NR KONTA: 005 \n SALDO: 455.38 z³\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAÆ PRZELEW: "))
    if konto == "005":
      RED = '\033[31m'
      print(RED + "NIE MO¯ESZ ZROBIÆ PRZELEWU NA W£ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
    if konto == "003":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z³',
              '\n4| Zofia Pluciñska| 004| 7344.00 z³',
              '\n5| Grzegorz Braun| 005|', suma, 'z³')
    if konto == "004":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z³',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|', suma, 'z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
    if konto == "002":
      kwota = float(input("PODAJ KWOTÊ PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ¥CYCH ŒRODKÓW NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA£ WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z³', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z³', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z³',
              '\n4| Zofia Pluciñska| 004|7344.00 z³',
              '\n5| Grzegorz Braun| 005|', roznica, 'z³')
elif number == 3:
  print(" ")




