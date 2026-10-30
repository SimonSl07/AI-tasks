# Romanian version
Alex, plictisit în timpul său liber, a decis să își formeze o bază de date cu știri din diferite categorii și categoria căreia îi aparține fiecare, ordonate astfel încât texte din aceeași categorie să fie unele lângă celelalte. Mândru de reușita sa, își cheamă prietenii (Mihai, Samuel și Vincențiu) să se uite la ce a făcut. În timp ce le arăta, Alex a trebuit să plece repede până la baie, iar când s-a întors, a rămas îngrozit. "Prietenii" săi plecaseră, iar baza lui de date era un dezastru: Mihai i-a amestecat ordinea datelor salvate, Samuel a șters coloana cu categoriile, iar Vincențiu a adăugat zgomot (multe texte în plus, care nu sunt știri, dar **toate fac parte dintr-o singură categorie**).

 Atunci, Alex s-a gândit **"Cu așa prieteni, nu mai ai nevoie de dușmani..."**.

Astfel, rămas doar cu o bază de date cu multe știri necategorizate, printre care mai este ascuns și zgomot, vă roagă pe voi să îl ajutați să categorizeze textele.

**Puteți utiliza modelul "BAAI/bge-small-en-v1.5"**

### Descrierea setului de date

Testare: Fișierul ```test_data.csv``` conține textele din baza de date după giumbușlucurile "prietenilor" lui Alex.

### Subtask-uri

#### Subtask 1 - A fi sau a nu fi zgomot (40 puncte)

Salvați-l pe Alex de zgomotul adăugat de Vincențiu!

**Obiectiv**: Pentru fiecare text din setul de date, preziceți dacă textul este sau nu zgomot.
**Output**:  Etichetele de clasificare: **1 = zgomot, 0 = știre**.

#### Subtask 2 - Categorizarea știrilor (60 puncte)

Categorizați textele! **Țineți cont de faptul că nu se cunosc categoriile și nici numărul acestora**.

**Obiectiv**: Pentru toate textele din setul de date, categorizați-le în funcție de ce tip de știri sunt.
 **Output**: Etichetele de clasificare: **categoria -1 pentru zgomot**, iar restul de categorii  pentru știri **valori începând cu 1** (presupunând că sunt n categorii: 1 pentru prima categorie, 2 pentru a doua categorie, ..., n pentru a n-a categorie).

### Formatul output-ului

Soluția trimisă trebuie să fie în format .csv și să conțină răspuns pentru ambele subtask-uri, având următoarele trei coloane:

subtaskID | datapointID | answer
-|-|-
id-ul subtaskului (1 sau 2)| id-ul datelor cum apare în datele de test | răspunsul pentru fiecare id

Exemplu de fișier de trimitere (``` sample_output.csv ```)

```csv
subtaskID, datapointID, answer
1, 0, 0
1, 1, 0
1, 2, 1
1, 3, 0
...
2, 0, 2
2, 1, 1
2, 2, -1
2, 3, 1
...

```
**Valorile de mai sus sunt exemple aleatorii!**


### Punctare

#### Subtask 1 (40 puncte)

Punctarea este bazată pe scorul MCC (Matthews Correlation Coefficient), în funcție de valoarea aceasta acordându-se un punctaj, în valoare de maxim 40 de puncte

| Metric | Score |
| --- | --- | 
|$\text{MCC} \geq 0.87$| 40 de puncte|
|$0 \leq \text{MCC} < 0.87$ | Normalizare liniară între 4 și 40 de puncte| 
|$\text{MCC} < 0$ | 4 puncte|


#### Subtask 2 (60 puncte)

Punctarea este bazată pe scorul AMI (Adjusted Mutual Information), în funcție de valoarea aceasta acordându-se un punctaj, în valoare de maxim 60 de puncte

| Metric | Score |
| --- | --- | 
|$\text{AMI} \geq 0.53$| 60 de puncte|
|$0 \leq \text{AMI} < 0.53$ | Normalizare liniară între 6 și 60 puncte| 
|$\text{AMI} < 0$ | 6 puncte|

# HU version
Alex, unalmában, úgy döntött, hogy létrehoz egy adatbázist különböző kategóriájú hírekből, amely tartalmazza azt is, hogy melyik szöveg melyik kategóriába tartozik, úgy rendezve a híreket, hogy az azonos kategóriájú szövegek egymás mellett legyenek. Büszkén az eredményére, meghívja barátait (Mihai, Samuel és Vincențiu), hogy nézzék meg, mit alkotott. Miközben mutatta nekik, Alexnek hirtelen ki kellett mennie a mosdóba, és amikor visszatért, rémülten látta, mi történt. A „barátai” eltűntek, az adatbázisa pedig romokban hevert: Mihai összekeverte az adatok sorrendjét, Samuel törölte a kategória oszlopot, Vincențiu pedig zajt adott hozzá (sok olyan extra szöveget, amelyek nem hírek, de **egyetlen kategóriába tartoznak**).

Ekkor Alex csak ennyit gondolt: **„Ilyen barátok mellett nincs szükség ellenségekre…”**.

Így, egy olyan adatbázissal maradt, amely csomó kategorizálatlan hírszöveget tartalmaz, amelyek között zaj is rejtőzik és most segítséget kér tőletek a szövegek rendszerezéséhez.

**Használhatjátok a „BAAI/bge-small-en-v1.5 modellt.”**

### Az adatkészlet leírása

Tesztelés: A ```test_data.csv``` fájl tartalmazza az adatbázis szövegeit Alex „barátainak” tréfái után.

### Részfeladatok

#### 1. Részfeladat – Zaj vagy nem zaj (40 pont)

Mentesítsd Alexet a Vincențiu által hozzáadott zajtól!

**Cél:** Döntsétek el az adatkészlet minden szövegéről, hogy zaj-e vagy sem. 
**Kimenet:** Osztálycímkék: **1 = zaj, 0 = hír** 

#### 2. Részfeladat – A hírek kategorizálása (60 pont)

Kategorizáljátok a szövegeket! **Fontos: nem ismerjük a kategóriákat, sem azok számát.**

**Cél:** Csoportosítsátok az összes szöveget aszerint, hogy milyen típusú hírről van szó. 
**Kimenet:** Osztálycímkék: **-1 = zaj**, a többi kategória pedig a hírek számára **1-től induló számokkal** jelölve (feltételezve, hogy n kategória van: 1 az első, 2 a második, …, n az n-edik kategória). 

### A kimenet formátuma

A beadott megoldásnak .csv formátumúnak kell lennie, és mindkét részfeladat válaszát tartalmaznia kell, az alábbi három oszloppal:

subtaskID | datapointID | answer
-|-|-
részfeladat azonosító (1 vagy 2) | az adat azonosítója a tesztfájlban | az adott azonosítóhoz tartozó válasz

Példa beadandó fájlra (sample_output.csv)

``` csv
subtaskID, datapointID, answer
1, 0, 0
1, 1, 0
1, 2, 1
1, 3, 0
...
2, 0, 2
2, 1, 1
2, 2, -1
2, 3, 1
...
```

**A fenti értékek csak véletlenszerű példák!**

### Pontozás

#### 1. Részfeladat (40 pont)

A pontozás az MCC (Matthews Correlation Coefficient) értéken alapul és ezen érték alapján legtöbb 40 pontot kaphattok.

| Mutató | Pontszám |
| --- | --- | 
|$\text{MCC} \geq 0.87$| 40 pont |
|$0 \leq \text{MCC} < 0.87$ | Lineáris skálázás 4 és 40 pont között | 
|$\text{MCC} < 0$ | 4 pont |

#### 2. Részfeladat (60 pont)

A pontozás az AMI (Adjusted Mutual Information) értéken alapul és ezen érték alapján legtöbb 60 pontot kaphattok.
| Mutató | Pontszám |
| --- | --- | 
|$\text{AMI} \geq 0.53$| 60 pont |
|$0 \leq \text{AMI} < 0.53$ | Lineáris skálázás 6 és 60 pont között | 
|$\text{AMI} < 0$ | 6 pont |

# English version
Alex, bored in his free time, decided to create a database of news from different categories which also contains the category each one belongs to, ordered so that texts from the same category are next to each other. Proud of his success, he calls his friends (Mihai, Samuel, and Vincențiu) to look at what he has done. While showing them, Alex had to leave quickly to go to the bathroom, and when he returned, he was horrified. His "friends" had left, and his database was a disaster: Mihai shuffled the order of the saved data, Samuel deleted the category column, and Vincențiu added noise (many extra texts that are not news, but **they are part of a single category**).

 Then, Alex thought **"With friends like these, who needs enemies..."**.

Thus, left with only a database of many uncategorized news texts, among which noise is also hidden, he asks you to help him categorize the texts.

**You can use the model "BAAI/bge-small-en-v1.5"**

### Dataset description

Testing: The file ```test_data.csv``` contains the texts from the database after the pranks of Alex's "friends".

### Subtasks

#### Subtask 1 - To be or not to be noise (40 points)

Save Alex from the noise added by Vincențiu!

**Objective**: For each text in the dataset, predict whether the text is noise or not.
**Output**: Classification labels: **1 = noise, 0 = news**.

#### Subtask 2 - Categorizing the news (60 points)

Categorize the texts! **Keep in mind that we do not know the categories nor how many there are**.

**Objective**: For all texts in the dataset, categorize them according to what type of news they are.
 **Output**: Classification labels: **category -1 for noise**, and the rest of the categories for news **values starting with 1** (assuming there are n categories: 1 for the first category, 2 for the second category, ..., n for the n-th category).

### Output format

The submitted solution must be in .csv format and contain the answer for both subtasks, having the following three columns:

subtaskID | datapointID | answer
-|-|-
subtask id (1 or 2)| data id as it appears in the test data | the answer for each id

Example of a submission file (``` sample_output.csv ```)

```csv
subtaskID, datapointID, answer
1, 0, 0
1, 1, 0
1, 2, 1
1, 3, 0
...
2, 0, 2
2, 1, 1
2, 2, -1
2, 3, 1
...
```

**The values above are random examples!**

### Scoring

#### Subtask 1 (40 points)
Scoring is based on the MCC (Matthews Correlation Coefficient) score, with points awarded based on this value, up to a maximum of 40 points.

| Metric | Score |
| --- | --- | 
|$\text{MCC} \geq 0.87$| 40 points |
|$0\leq \text{MCC} < 0.87$ | Linear normalization between 4 and 40 points| 
|$\text{MCC} < 0$ | 4 points |

#### Subtask 2 (60 points)
Scoring is based on the AMI (Adjusted Mutual Information) score, with points awarded based on this value, up to a maximum of 60 points.

| Metric | Score |
| --- | --- | 
|$\text{AMI} \geq 0.53$| 60 points |
|$0 \leq \text{AMI} < 0.53$ | Linear normalization between 6 and 60 points| 
|$\text{AMI} < 0$ | 6 points |