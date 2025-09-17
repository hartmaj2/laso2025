# Fast Fourier Transform

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

Převedeme problém vyhodnocení polynomu $P$ v bodech $1,\omega, \ldots \omega^{2^n-1}$ na vyhodnocení dvou pomocných polynomů v bodech $1,\omega^2, \omega^4, \ldots \omega^{2^n-2}$.

Ukáže se, že z výsledných hodnot dokážeme z každé získat dvě původní, které jsou od sebe přesně na opačné straně jednotkové kružnice.

Jakým trikem se nám to povede? Máme-li polynom $P(x) = a_0 x^0 + a_1 x^1 + \cdots a_{2^n-1}x^{2^n-1}$. Tak ho rozdělíme na dva polynomy:

Sudé mocniny: $S'(x) = a_0 x^0 + a_2 x^2 + \cdot + a_{2^n-2} x^{2^n-2}$.

Liché mocniny: $L'(x) = a_1 x^1 + a_3 x^3 + \cdot + a_{2^n-1} x^{2^n-1}$.

Dále můžeme z $L'$ vytknout $x$ a získat tak:

 $L''(x) = a_1 x^0 + a_3 x^2 + \cdot + a_{2^n-1} x^{2^n-2}$.

Všimněme si, že polynomy výše jsou jen vyhodnocením následujících polynomů v bodě $x^2$:


 $S(x) = a_0 x^0 + a_2 x^1 + \cdot + a_{2^{n-1}-1} x^{2^{n-1}-1}$.

 $L(x) = a_1 x^0 + a_3 x^1 + \cdot + a_{2^{n-1}-1} x^{2^{n-1}-1}$.

 Tedy můžeme přepsat $P$ jako $P(x) = S(x^2) + x \cdot L(x^2)$.

 Pokud tedy dostaneme například vyhodnocení $S$ a $L$ v bodech $1,\omega^4,\omega^8,\omega^{12}$, tak z nich dokážeme vytřískat vyhodnocení původního $P$ v bodech:

 $1 \rightarrow \omega, \omega^8$

 $\omega^4 \rightarrow \omega^2, \omega^{10}$

 $\omega^8 \rightarrow \omega^4, \omega^{12}$

 $\omega^{12} \rightarrow \omega^6, \omega^{14}$