<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Authors](#authors)
* [Description of the Problem](#description)
* [Run guide](#run-guide)

## Authors
Piotr Frątczak 300207

Bartosz Świtalski 300279

## Description
W optymalizacji za pomocą algorytmów ewolucyjnych ze względów czasowych ogranicza się liczbę iteracji. Często zdarza się jednak, że liczba ta nie jest sensownie wykorzystywana, ponieważ algorytm utyka w optimum lokalnym i stara się je jak najdokładniej zlokalizować. Rozwiązaniem może być wykrycie bezsensowności dalszej pracy i restart algorytmu. Zaproponować, zaimplementować i przebadać strategię wykrywania bezcelowości dalszej pracy. Przed rozpoczęciem realizacji projektu proszę zapoznać się z zawartością [strony](http://staff.elka.pw.edu.pl/~rbiedrzy/PSZT/index.html).

## Run guide
```
git clone https://github.com/bartoszswitalski/when-to-surrender.git
```
### Pojedyncze uruchomienie ###
```
/when-to-surrender$ ./xsetup.sh
/when-to-surrender$ python3 when−to−surrender/main.py <funkcja> <kryterium> <p1> <p2> <p3> <p4> <plik_wykres>
/when-to-surrender$ ./xclean.sh
```
### Skrypt ###
```
/when-to-surrender$ ./xsetup.sh
/when-to-surrender$ ./xscript.sh
/when-to-surrender$ ./xclean.sh
```
### Oznaczenia argumentów ###
* funkcja - optymalizowana funkcja (dozwolone wartości: 'F4', 'F5', 'F6')
* kryterium - kryterium przerwania (dozwolone wartości: 'k-iter', 'sd', 'best-worst', 'variance')
* pi - kolejne wartości parametru do wcześniej sprecyzowanego kryterium
* plik_wykres - nazwa pliku do którego zostanie zapisany wykres wynikowy
