# Den 1 poznámky

## Druhy neřešitelných úloh

- příliš velká data
- principiálně neřešitelné

# Příliš velká data

## Steinhaus-Moser notation

Hrajeme si s trojúhelníčky, čtverečky a kolečky.

- $\triangle(n)$ ... $n^n$
- $\square(n)$ ... $\overbrace{\triangle( \cdots (\triangle(}^{n \text{ times }}n) \cdots )$
- $\bigcirc(n)$ ... $\overbrace{\square( \cdots (\square(}^{n \text{ times }}n) \cdots )$

Roste to rychle...

## Boj s hydrou

Hydra je kořenový strom.
Hlavy hydry jsou listy stromu.
Po useknutí hlavy se z dědovi hlavy vytvoří kopie podstromu od dědy směrem k dítěti, které bylo useknuté, ale už bez té useknuté hlavy.
Po useknutí hlavy připojené ke kořeni už nevyrosté nová kopie.

### Otázky

Za jak dlouho hydru zlikvidujeme?
Dokážeme hydru zlikvidovat i pokud si hydra vybere, kolik kopií

### Jak to analyzovat

Obecný případ. Pokud máme dvoupatrovou vidlici o $n$ zubech, tak ji dokážeme zredukovat na keřík o $2^n$ větvičkách.

## Knuth arrow notation

$a \overbrace{\uparrow \ldots \uparrow}^{k \text{ times}} b = \underbrace{a \overbrace{\uparrow \ldots \uparrow}^{k-1 \text{ times}} ( a \overbrace{\uparrow \ldots \uparrow}^{k-1 \text{ times}}( \cdots a \overbrace{\uparrow \ldots \uparrow}^{k-1 \text{ times}}a) \cdots )}_{b \text { times}}$

Also $a \uparrow b = a^b$

## Ackermann function

Do nultého sloupečku zapisuji vždy prvek z $n-1$ řádku v prvním sloupci.

Do sloupečku $n$ zapíši prvek z předchozího řádku na pozici rovné hodnotě prvku v $n-1$ ním sloupečku na stejném řádku.

Formálně zapsáno jako:

$$A(i,j)= 
    \begin{cases}
    j+1 & \text{ if } i = 0, \\
    A(i-1,1) & \text{ if } j = 0, \\
    A(i-1,A(i,j-1)) & \text{ else }
    \end{cases}    
$$



# Principiálně neřešitelné

Víme, že dokážeme enumerovat všechny napsatelné programy. Například je seřadit lexikograficky.

## Postův korespondenční problém

Cílem je vytvořit dva stejné řetězce znaků.

Máme k dispozici kartičky, které mají na horní a spodní straně nějaký řetězec. Od každého typu můžeme použít neomezeně mnoho kartiček.

Řetězce tvoříme tak, že kartičky skládáme za sebe.

Například mějme k dispozici následující kartičky:

$\begin{bmatrix} bc \\ ca \end{bmatrix}$,
$\begin{bmatrix} a \\ ab \end{bmatrix}$,
$\begin{bmatrix} ca \\ a \end{bmatrix}$,
$\begin{bmatrix} abc \\ c \end{bmatrix}$

Korespondující posloupnosti dokážeme vytvořit následovně:

$\begin{bmatrix} a \\ ab \end{bmatrix}$,
$\begin{bmatrix} bc \\ ca \end{bmatrix}$,
$\begin{bmatrix} a \\ ab \end{bmatrix}$,
$\begin{bmatrix} abc \\ c \end{bmatrix}$

Simulace [zde](https://kubokovac.eu/pcp/).

### Problém

Jde z kartiček poskládat stejné řetězce?

### Realita

Post dokázal, že neexistuje program, který by dokázal pro libovolně zadané kartičky říci, zda existuje řešení či ne.

## Zobecněná Collatz sequence

### Původní problém pro k = 2

Počítáme následovníky, dokud nenarazíme na 1.

$c(n) = \begin{cases} 3n + 1 & n \text{ liché} \\ n/2 & n \text{ sudé } \end{cases}$

### Zobecněný problém

Vezměme libovolný modulus $k$. 

Dále vymyslíme $k$ pravidel pro výpočet $c(n)$ podle toho, jaký bude mít $n$ zbytek po vydělení $k$. 

Jediné omezení na pravidla je, že musí vždy vzniknout přirozené číslo.

Příklad pro $k=3$:

$c(n) = 
    \begin{cases} 
    n/3 & \text{ if } n \mod k = 0 \\ 
    2n + 1 & \text{ if } n \mod k = 1 \\
    n + 4 & \text{ if } n \mod k = 2 \\
    \end{cases}
$

Zde už pro $n=6$ máme cyklus.

## Halting problem

## Game of life 

Otázka je, zastaví se daná konfigurace, nebo se bude nekonečně cyklit?

## Maximal indepset and min vertex cover

Problem: Given a graph $G$ find a set s.t. it is a maximal independent set of $G$ and also a minimal vertex cover of $G$ or output impossible if that does not exist.

### Analysis

Odd cycles are bad, even cycles are good.

Suppose we have a set $S$ that satisfies the property we look for i.e. it is a indep. set and also a vertex cover. How does the situation look?

We have two sets of vertices $S$ and $B = V \setminus S$. Since $S$ is an independent set, we know there is no edge $e$ s.t. both endpoints lie in $S$. Also, there is no edge s.t. both endpoints lie in $B$, since $S$ is a vertex cover.

Thus we are looking for a partition of the graph into a bipartite graph.