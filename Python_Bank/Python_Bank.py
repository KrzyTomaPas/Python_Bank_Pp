# BANK
print("WYBIERZ OPCJ�:")
print("1 => LISTA WSZYSTKICH KLIENT�W BANKU")
print("2 => LOGOWANIE")
print("3 => ZAKO�CZ PROGRAM")
people = [
  '1| JAN NOWAK| 001| 1457.23 z�', '2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
  '3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
  '4| Zofia Pluci�ska| 004| 7344.00 z�', '5| Grzegorz Braun| 005| 455.38 z�'
]

number = int(input("WYBIERZ 1,2 LUB 3: "))
if number == 1:
  for i in people:
    print(i)
  print("WYBIERZ OPCJ�:")
  print("1 => LISTA WSZYSTKICH KLIENT�W BANKU")
  print("2 => LOGOWANIE")
  print("3 => ZAKO�CZ PROGRAM")
  second = int(input("WYBIERZ 1,2 LUB 3: "))
  if second == 2:
    id_user = (str(input("ZAlOGUJ SI� WYBIERAJ�C ID KLIENTA: ")))
    if id_user == "001":
      print("ZALOGOWANY KLIENT \n ID: 1 \n IMI� I NAZWISKO: Jan Nowak \n NR KONTA: 001 \n SALDO: 1457,23 z�\n")
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "001":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|', suma, 'z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, ' z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif id_user == "002":
    print("ZALOGOWANY KLIENT \n ID: 2 \n IMI� I NAZWISKO: Agnieszka Kowalska \n NR KONTA: 002 \n SALDO: 3600.18 z�\n")
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "002":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|', roznica, 'z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 7344.00 + kwota
        white = '\033[0;0m'
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif id_user == "003":
    print("ZALOGOWANY KLIENT \n ID: 3 \n IMI� I NAZWISKO: Robert Lewandowski \n NR KONTA: 003 \n SALDO: 2745.03 z�\n")
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "003":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| ', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 7344.00 + kwota
        white = '\033[0;0m'
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif id_user == "004":
    print("ZALOGOWANY KLIENT \n ID: 4 \n IMI� I NAZWISKO: Zofia Pluci�ska \n NR KONTA: 004 \n SALDO: 7344.00 z�\n")
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "004":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif id_user == "005":
    print("ZALOGOWANY KLIENT \n ID: 5 \n IMI� I NAZWISKO: Grzegorz Braun \n NR KONTA: 005 \n SALDO: 455.38 z�\n")
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "005":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|7344.00 z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
    id_user = print("ZALOGUJ SI� WYBIERAJ�C ID KLIENTA:")
  if second == 3:
    print(" ")
elif number == 2:
  user = str(input("ZALOGUJ SI� WYBIERAJ�C ID KLIENTA: "))
  if user == "001":
    print(
      "ZALOGOWANY KLIENT \n ID: 1 \n IMI� I NAZWISKO: Jan Nowak \n NR KONTA: 001 \n SALDO: 1457,23 z�\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "001":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|', suma, 'z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, ' z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 1457.23:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 1457.23 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', roznica, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif user == "002":
    print(
      "ZALOGOWANY KLIENT \n ID: 2 \n IMI� I NAZWISKO: Agnieszka Kowalska \n NR KONTA: 002 \n SALDO: 3600.18 z�\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "002":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|', roznica, 'z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 3600.18:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 3600.18 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              roznica, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif user == "003":
    print(
      "ZALOGOWANY KLIENT \n ID: 3 \n IMI� I NAZWISKO: Robert Lewandowski \n NR KONTA: 003 \n SALDO: 2745.03 z�\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "003":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| ', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 2745.03:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 2745.03 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', roznica, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif user == "004":
    print(
      "ZALOGOWANY KLIENT \n ID: 4 \n IMI� I NAZWISKO: Zofia Pluci�ska \n NR KONTA: 004 \n SALDO: 7344.00 z�\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "004":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002|3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005| 455.38 z�')
    if konto == "005":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 7344.00:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 7344.00 - kwota
        suma = 455.38 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', roznica, 'z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
  elif user == "005":
    print(
      "ZALOGOWANY KLIENT \n ID: 5 \n IMI� I NAZWISKO: Grzegorz Braun \n NR KONTA: 005 \n SALDO: 455.38 z�\n"
    )
    konto = str(input("WPISZ NUMER KONTA NA KT�RY CHCESZ WYKONA� PRZELEW: "))
    if konto == "005":
      RED = '\033[31m'
      print(RED + "NIE MO�ESZ ZROBI� PRZELEWU NA W�ASNE KONTO")
    if konto == "001":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 1457.23 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001|', suma, 'z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
    if konto == "003":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 2745.03 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003|', suma, 'z�',
              '\n4| Zofia Pluci�ska| 004| 7344.00 z�',
              '\n5| Grzegorz Braun| 005|', suma, 'z�')
    if konto == "004":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 7344.00 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�',
              '\n2| AGNIESZKA KOWALSKA| 002| 3600.18 z�',
              '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|', suma, 'z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
    if konto == "002":
      kwota = float(input("PODAJ KWOT� PRZELEWU: "))
      if kwota > 455.38:
        print("NIE MA WYSTARCZAJ�CYCH �RODK�W NA KONCIE")
      else:
        roznica = 455.38 - kwota
        suma = 3600.18 + kwota
        green = '\033[0;32m'
        white = '\033[0;0m'
        print(green + "PRZELEW ZOSTA� WYKONANY")
        print(white + '1| JAN NOWAK| 001| 1457.23 z�', '\n2| AGNIESZKA KOWALSKA| 002|',
              suma, 'z�', '\n3| ROBERT LEWANDOWSKI| 003| 2745.03 z�',
              '\n4| Zofia Pluci�ska| 004|7344.00 z�',
              '\n5| Grzegorz Braun| 005|', roznica, 'z�')
elif number == 3:
  print(" ")




