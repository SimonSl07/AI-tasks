# Romanian version
Gigel, un băiat simplu pasionat de fotografie, și-a cumpărat o nouă cameră foto după ce aparatul vechi i s-a stricat. Acum, dorind să își testeze camera, merge la faimoasa expoziție a muzeului intergalactic de artă contemporană: **"A matter of perspective"**. Acesta privește mai multe opere de artă din diferite perspective, mișcându-se pe orizontală în jurul obiectului, făcându-i poze din mai multe unghiuri. Atunci, Gigel, din ce în ce mai interesat de domeniul inteligenței artificiale, își pune următoarea întrebare: Oare ar putea fi creat un model de inteligență artificială care:

1) fiind date câte trei poze, conținând două poze cu același obiect din perspective diferite și o poză cu un obiect diferit, să prezică **imaginea cu obiectul diferit**
2) fiind dată o poză cu un obiect, să estimeze **unghiul** din care este privit

Desigur, acesta vă pune la dispoziție și o colecție de poze făcute de el în muzeu și unghiurile din care sunt făcute.

### Descrierea setului de date

Folderul  "train_data" conține:
- un folder cu imagini
- **train_data.csv**, ce conține pentru fiecare imagine unghiul din care este privit obiectul

Folderul "test_data" conține:
- un folder cu imagini
- **test_data.csv**, ce conține datele pe care va fi testat obiectul, cu următoarele coloane:

subtaskID | datapointID | img1 | img2 | img3
-|-|-|-|-
id-ul subtask-ului (1 sau 2)| id-ul datelor | id-ul primei imagini | id-ul imaginii doi pentru subtaskul 1, respectiv nimic("") pentru subtaskul 2 | id-ul imaginii trei pentru subtaskul 1, respectiv nimic("") pentru subtaskul 2 

### Subtask-uri

#### Subtask 1 - Găsirea intrusului (40 puncte)

**Obiectiv**: Fiind date perechi de câte trei imagini, două conținând același obiect din perspective diferite, să se prezică care imagine conține alt obiect.
**Output**: Numărul imaginii ce conține alt obiect (1, 2 sau 3).

#### Subtask 2 - Aflarea perspectivei (60 puncte)

**Obiectiv**: Fiind date mai multe imagini, aflați pentru fiecare unghiul din care este privit obiectul.
**Output**: Unghiul din care este privit obiectul (valoare între 0 și 359).

### Formatul output-ului

Soluția trimisă trebuie să fie în format **.csv** și să conțină răspuns pentru ambele subtask-uri

subtaskID | datapointID | answer
-|-|-
id-ul subtask-ului (1 sau 2)| id-ul datelor de test| răspunsul pentru fiecare id

Exemplu de fișier de trimitere (``` sample_output.csv ```)

```csv
subtaskID, datapointID, answer
1, 1, 2
1, 2, 1
1, 3, 3
1, 4, 3
...
2, 1, 25
2, 2, 43
2, 3, 271
2, 4, 0
...

```
**Valorile de mai sus sunt exemple aleatorii!**


### Punctare

#### Subtask 1 (40 puncte)

Pentru subtaskul 1 soluția voastră va fi comparată cu setul de răspunsuri corecte, iar în funcție de **acuratețe** veți primi un punctaj până la un maxim de 40 de puncte.

#### Subtask 2 (60 puncte)

Pentru subtaskul 2 soluția voastră va fi comparată cu setul de răspunsuri corecte, iar punctarea urmărește acest model:

- dacă pe o imagine unghiul prezis este de x grade, iar unghiul adevărat este de y grade, aflăm unghiul dintre ele $z = min(abs(x - y), 360 - abs(x - y))$, iar participantul va primi un procentaj din punctaj egal cu coeficientul $max(0, 1 - z / 90)$ 

- de exemplu, dacă pe o imagine, unghiul prezis este de 20 grade, iar unghiul adevărat este de 350 de grade, aflăm unghiul dintre ele (z = 30 de grade) și oferim $max(0, 1 - 30 / 90)= 0.67 = 67$% din scor


# HU version

Gigel, egy egyszerű fiú, aki szenvedélyesen érdeklődik a fotózás iránt, új fényképezőgépet vásárolt magának, miután a régi elromlott. Mivel ki akarta próbálni az új gépét, ellátogatott a híres intergalaktikus kortárs művészeti múzeum kiállítására: **„A matter of perspective”**. Ott különböző műalkotásokat figyelt meg különböző nézőpontból, vízszintesen körbejárva az objektumokat, és több szögből készítve róluk képeket. Ezután Gigel, aki egyre jobban érdeklődik a mesterséges intelligencia iránt, feltette magának a következő kérdést: Lehetséges lenne-e egy olyan mesterséges intelligencia modellt készíteni, amely:

1) ha adva van három kép – ahol kettő ugyanazt az objektumot ábrázolja más-más nézőpontból, a harmadik pedig egy másik objektumot ábrázol – képes előrejelezni a **különböző objektumot ábrázoló képet** 
2) ha adva van egy kép, amely egy objektumot ábrázol, képes meghatározni, hogy **milyen szögből** készült a felvétel 

Természetesen Gigel egy fényképgyűjteményt is rendelkezésetekre bocsát, amelyeket a múzeumban készített, valamint azokat a szögeket is, amelyekből a fényképeket készítette.

### Az adatkészlet leírása

A „train_data” mappa tartalmaz:
- egy képeket tartalmazó mappát 
- a **train_data.csv** fájlt, amely minden képhez megadja a nézőpont szögét 

A „test_data” mappa tartalmaz:
- egy képeket tartalmazó mappát 
- a **test_data.csv** fájlt, amely a teszteléshez szükséges adatokat tartalmazza, az alábbi oszlopokkal: 

subtaskID | datapointID | img1 | img2 | img3 
-|-|-|-|-
részfeladat azonosító (1 vagy 2) | adat azonosítója | az első kép azonosítója | a második kép azonosítója (1. részfeladatnál), illetve üres (2.-nál) | a harmadik kép azonosítója (1. részfeladatnál), illetve üres (2.-nál) 

### Részfeladatok

### 1. Részfeladat – A betolakodó megtalálása (40 pont)

**Cél:** Három képből álló fényképcsoport esetén – ahol kettő ugyanazt az objektumot ábrázolja különböző nézőpontokból – határozzátok meg, hogy melyik kép tartalmaz egy másik objektumot. 
**Kimenet:** Annak a képnek a sorszáma, amely egy másik objektumot ábrázol (1, 2 vagy 3). 

### 2. Részfeladat – A nézőpont meghatározása (60 pont)

**Cél:** Több kép esetén adjátok meg minden egyes képre a szöget, amelyből az objektum látható. 
**Kimenet:** A nézőpont szöge (0 és 359 közötti érték). 

### A kimenet formátuma

A beadott megoldásnak **.csv** formátumúnak kell lennie, és tartalmaznia kell a választ mindkét részfeladatra.

subtaskID | datapointID | answer 
-|-|-
részfeladat azonosító (1 vagy 2) | a tesztadat azonosítója | az adott id-hez tartozó válasz 

Példa beadandó fájlra (sample_output.csv)

```csv
subtaskID, datapointID, answer
1, 1, 2
1, 2, 1
1, 3, 3
1, 4, 3
...
2, 1, 25
2, 2, 43
2, 3, 271
2, 4, 0
...
```
**A fenti értékek csak példák!**

### Pontozás

#### 1. Részfeladat (40 pont)

Az 1. részfeladatnál a megoldásotokat a helyes válaszokkal hasonlítják össze, és legtöbb 40 pontot kaphattok az **accuracy (pontosság)** alapján.

#### 2. Részfeladat (60 pont)

A 2. részfeladatnál a megoldásotokat a helyes válaszokkal hasonlítják össze, és a pontozás az alábbi módon történik:

- ha egy képnél az előrejelzett szög $x°$ fok, a valódi szög pedig $y°$ fok, akkor a köztük lévő szöget így számítjuk ki: $z = min(abs(x - y), 360 - abs(x - y))°$ és a pontszámotok a $max(0, 1 - z / 90)$ együttható százaléka lesz

- például: ha egy képen a becsült szög 20°, a valódi pedig 350°, akkor a köztük levő szög $z = 30°$, így a kapott pontszám $max(0, 1 - 30/90) = 0.67 = 67%$-a lesz a lehetséges maximális pontszámnak.

# English version
Gigel, a simple boy with a passion for photography, bought a new camera after his old one broke. Now, wanting to test his brand new camera, he goes to the famous exhibition of the intergalactic museum of contemporary art: **"A matter of perspective"**.  There he looks at several artworks from different perspectives, moving horizontally around the object, taking pictures of it from multiple angles. Then, Gigel, increasingly interested in the field of artificial intelligence, asks himself the following question: Could an artificial intelligence model be created that predicts:

1) given sets of three pictures, containing two pictures with the same object from different perspectives and one picture with a different object, to predict the **image with the different object**
2) given a picture of an object, to find the **angle** from which it is viewed

Of course, he also provides you with a collection of pictures taken by him in the museum, and the angle from which it was taken.

### Dataset description

The "train_data" folder contains:
- an images folder
- **train_data.csv**, which contains for each image the angle from which the object is viewed

The "test_data" folder contains:
- an images folder
- **test_data.csv**, which contains the data on which the model will be tested, with the following columns:

subtaskID | datapointID | img1 | img2 | img3
-|-|-|-|-
subtask id (1 or 2)| id of the data| id of the first image| id of the second image for subtask 1, respectively nothing for subtask 2 | id of the third image for subtask 1, respectively nothing for subtask 2 

### Subtasks

#### Subtask 1 - Finding the intruder (40 points)

**Objective**: Given sets of three images, two of which contain the same object from different perspectives, predict which image contains a different object.
**Output**: The number of the image which contains another object (1, 2 or 3).


#### Subtask 2 - Finding the perspective (60 points)

**Objective**: Given multiple images, predict for each one the angle from which the object is viewed.
**Output**: The angle from which the object is viewed(value between 0 and 359).

### Output format

The submitted solution must be in **.csv** format and contain answers for both subtasks.

subtaskID | datapointID | answer
-|-|-
subtask id (1 or 2)| test data id| the answer for each id

Example of a submission file (``` sample_output.csv ```)

```csv
subtaskID, datapointID, answer
1, 1, 2
1, 2, 1
1, 3, 3
1, 4, 3
...
2, 1, 25
2, 2, 43
2, 3, 271
2, 4, 0
...

```

**The values above are random examples!**


### Scoring

#### Subtask 1 (40 points)

For subtask 1, your solution will be compared against the set of correct answers, and depending on **accuracy**, you will receive a score up to a maximum of 40 points.

#### Subtask 2 (60 points)

For subtask 2, your solution will be compared against the set of correct answers, and you will receive a score that follows this model:

- if for an image the predicted angle is x degrees, and the true angle is y degrees, we find the angle between them $z = min(abs(x - y), 360 - abs(x - y))$ and the participant will receive a percentage of the score with the coefficient $max(0, 1 - z / 90)$ %

- for example, if for an image, the predicted angle is 20 degrees, and the true angle is 350 degrees, we find the angle between them (z = 30 degrees) and it receives $max(0, 1 - 30 / 90) = 0.67 = 67$ % of the score