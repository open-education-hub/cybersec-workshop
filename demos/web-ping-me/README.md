# Ping Me

Accesați `http://141.85.224.104:10002/index.php` pentru a interacționa cu aplicația.
Observați că aplicația execută comanda `ping` către o adresă IP dată de utilizator.

Putem presupune că aplicația execută într-o linie de comandă pe server următoarea comandă:

```
$ ping <input>
```

Unde `<input>` este orice introduce utilizatorul în câmpul din pagină.
În consecință, un utilizator al aplicatiei **injecteaza comenzi** direct într-o linie de comandă aflată pe un server la distanță.

Cunoscând faptul că operatorul `;` delimitează comenzi și permite rularea mai multor comenzi într-o singură linie, putem folosi `8.8.8.8; whoami` ca și input.
În acest fel, comenzile care s-ar executa pe server conform presupunerilor noastre sunt:

```
$ ping 8.8.8.8; whoami
```

Validați presupunerile anterioare contra aplicației expuse pe `141.85.224.104:10002`.

Scopul este să accesați fișierul `/secret` de pe server.
Pentru a accesa acest fișier, folosiți utilitarul `cat` și faptul că aveți informația că fișierul căutat se află sub calea `/secret`.

Odată ce aveți un input care funcționează corespunzător, încercați același input și la adresa `141.85.224.104:10002`.
