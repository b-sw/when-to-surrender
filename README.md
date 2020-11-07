W optymalizacji za pomocą algorytmów ewolucyjnych ze względów czasowych ogranicza się liczbę iteracji. Często zdarza się jednak, że liczba ta nie jest sensownie wykorzystywana, ponieważ algorytm utyka w optimum lokalnym i stara się je jak najdokładniej zlokalizować. Rozwiązaniem może być wykrycie bezsensowności dalszej pracy i restart algorytmu. Zaproponować, zaimplementować i przebadać strategię wykrywania bezcelowości dalszej pracy. Przed rozpoczęciem realizacji projektu proszę zapoznać się z zawartością [strony](http://staff.elka.pw.edu.pl/~rbiedrzy/PSZT/index.html).

Wartościowy artykuł: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.384.4126&rep=rep1&type=pdf

  We note that for EAs it is not necessary to restart the
  algorithm completely. Partial restarts in the sense of re-initializing parts of the
  population are possible

  The first class is a static setting where a certain number of steps is fixed in advance. Then one can discuss whether it is better to spend a lot of time in one long run or in multiple short runs.

  The second class comprises dynamic restart strategies. Here, the point of time for restarts is determined by some fixed schedule that depends on the number of steps counted over all runs or, equivalently, on the number of steps in the current run and the sum of number of steps in all previous runs.
  A practical example proving the usefulness of dynamic, yet non-adaptive, strategies
  are cooling schedules used for simulated annealing.

  The third class - adaptive restart strategies. Here, the restart strategy may depend on the complete history of the current and all previous runs.

Dużo różnych kryteriów: https://www.scitepress.org/papers/2017/65779/65779.pdf
Tutaj są bardzo fajnie opisane strategie z przykładami: https://www.researchgate.net/publication/220974459_On_Stopping_Criteria_for_Genetic_Algorithms
