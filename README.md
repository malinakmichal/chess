### Chess

## 1. Úvod
Práce se zabývá implementací umělé
inteligence do hry šachy. Je to poměrně složitý problém,
jelikož existuje velké množství tahů. Není
možné tedy projít všechna možná řešení a vybrat to
nejlepší, protože již po 4 tazích existuje asi 168421
možných kombinací a toto číslo roste exponenciálně.
Zatím nebyla nalezena perfektní strategie pro tuto
hru.


## 2. Metody a algoritmy
Použil jsem algoritmus minimax společně s alphabeta
ořezáváním. Skóre algoritmu minimax jsem
vypočítal pomocí heuristické funkce.

# 2.1 Minimax
Algoritmus projde všchny tahy pomocí rekurze do
hloubky 4 a zvolí ten, který je pro hráče nejvýhodnější.
Na jednotlivých hladinách rekurze se střídá
výběr tahu z maxima a minima daného ohodnocení,
podle toho kdo je na tahu.
# 2.2 Heuristická funkce
Funkce ohodnocuje aktuální postavení figurek na
hrací desce a určuje, který hráč je ve výhodě. Hodnota
je vypočtena jako suma hodnot figurek jedné
barvy mínus suma hodnot figurek druhé barvy, kde
každá figurka má vlastní hodnotu podle její schopností.
Zavedeny jsou další vyhodnocovací kritéria
jako např. vzdálenost pešce od startovního pole
nebo pozice figurek okolo středu hrací desky.
# 2.3 Alpha-beta ořezávání
Algoritmus si pamatuje hodnoty alpha a beta a pokud
narazí na větev, která nepřinese zlepšení ohodnocení
tahu větev zahodí. Takové zahození značně
redukuje počet pozic, které je nutno projít a tím
zlepšuje časovou složitost. To nám umožní používat
vetšího zanoření rekurze a tudíž přesnější tahy.

## 3 Výsledky
Námi vytvořená umělá inteligence má lepší výkonost
než průmerný hráč. Další vylepšení by spočívalo ve
zlepšení heuristické funkce a zavedením známých
zahajovacích sekvencí. K dalšímu vylepšení by bylo
potřeba použít jiný přístup (neuronové sítě).
