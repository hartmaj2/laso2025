# Den 2 poznámky

## Násobení čísel

Jak těžké je násobení čísel? Mějme čísla $a$ a $b$, které mají $m,n$ cifer. Pro každou cifru čísla $b$ ji vynásobíme s každou cifrou čísla $a$, tedy celkem $mn$ operací.

## Násobení polynomů

Máme nějaké číslo $u=a_n \cdot 10^n + \ldots + a_1 \cdot 10^1  + a_0 \cdot 10^0$.

Nemusíme se však nutně omezovat na desítku jako základ a spíše číslo vnímat jako polynom $a_n \cdot x^n + \ldots + a_1 \cdot x^1  + a_0 \cdot x^0$.

Vidíme tedy, že násobení čísel můžeme převést na násobení polynomů se správným dosazením za $x$.

## Reprezentace polynomů

Pozorování: polynom je vlastně jenom funkce.

### Koeficientová

Dostaneme seznam čísel $a_0, \ldots a_n$, které odpovídají koeficientům u jednotlivých členů polynomu.

### Hodnotová

Pokud máme polynom stupně nejvýš $n$, tak nám stačí $n+1$ dvojic typu $(k_0,P(k_0)), \ldots (k_n,P(k_n))$ kde $P$ je funkce představující náš polynom.

Pozor, že nutně musí pro $i \neq j$ být $k_i \neq k_j$.

## Jak si spočítat hodnoty pomocí koeficientů

Máme dvě možnosti:

(a) použijeme Hornerovo schéma

(b) vytvoříme si Vandermondovu matici a vynásobíme s ní koeficienty

## Násobení polynomů pomocí jejich hodnotových reprezentací

Mějme polynomy:

$P(x) = 2x^2+3x+1$

$Q(x) = 6x^2+5x+8$

Pozorování, hodnoty jednoznačně označují i výsledný polynom $P \cdot Q$ když jich bude dostatek. $P \cdot Q$ má stupeň nejvýše $mn$, takže potřebujeme $mn+1$ hodnot na jeho určení.

Původních hodnot máme $m+1$ a $n+1$ takže vynásobením jich můžeme získat až $mn + m + n + 1$.

Mějme polynom a jeho hodnotu $P(x)$, jak vypadá hodnota $P(-x)$?

## Hlavní myšlenky FFT

Postupujeme metodou rozděl a panuj.

Převedeme problém vyhodnocení polynomu $P$ v bodech $1,\omega, \ldots \omega^{2^n}$ na vyhodnocení dvou pomocných polynomů v bodech $1,\omega^2, \omega^4, \ldots \omega^{2^n-1}$.

Ukáže se, že z výsledných hodnot dokážeme z každé získat dvě původní, které jsou od sebe přesně na opačné straně jednotkové kružnice.
