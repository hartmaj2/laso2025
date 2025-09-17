# Textové algoritmy

## KMP algoritmus

### Hlavní myšlenka

Kdybychom to dělali hloupě, tak zkusíme každou pozici sena a vyzkoušíme, zda tam začíná naše jehla.

Pokud tam naše jehla nezačíná, tak se v seně posuneme o jedna a v jehle začínáme zase na první pozici.

Lepší by ale bylo, kdybychom mohli využít toho, že i přesto, že máme mismatch, tak je monžé, že nemusíme zahodit celou jehlu, ale nějakou její část využít.

Místo toho, abychom šli tedy na začátek tak se koukneme, k jaké části naší jehly bychom mohli zkusit nenamatchované písmenko připojit.

### Trik

Použijeme tzv. longest prefix-suffix pole, které nám pro každou pozici jehly řekne, od jaké menší části jehly můžeme zkusit zkoušet znovu.

### Z praxe

Spellcheckery používají tzv. *Bloomův filtr*.