# ZBIRKA VPRAŠANJ ZA IZPIT - UMETNA INTELIGENCA V INFORMATIKI

## 1. OSNOVNI KONCEPTI

### [1 točka] Kaj je strojno učenje? Opišite s svojimi besedami.
**Vprašanje:**
Kaj je strojno učenje? Opišite s svojimi besedami in navedite en konkreten primer uporabe.

**Rešitev:**
Strojno učenje je področje umetne inteligence, kjer računalniški sistem namesto eksplicitnega programiranja za vsako nalogo, **sam prepoznava vzorce v podatkih** in se iz njih uči. Na podlagi učnih primerov zgradi model, ki ga nato uporabi za napovedovanje ali odločanje na novih podatkih.

*Primer:* Sistem za prepoznavanje neželene pošte (spam filter) se nauči prepoznavati spam na podlagi tisočih označenih e-poštnih sporočil.

---

### [1 točka] Kaj je sistem na osnovi pravil (rule-based system) in kako se razlikuje od strojnega učenja?

**Vprašanje:**  
Opišite sistem na osnovi pravil. V čem se razlikuje od pristopov strojnega učenja? Kdaj je bolje uporabiti pravilno zasnovan sistem namesto strojnega učenja? Kakšne so prednosti?

**Rešitev:**  
Sistem na osnovi pravil deluje na podlagi vnaprej ročno napisanih pogojev (if-else). Ne uči se iz podatkov, ampak sledi eksplicitni logiki. Razlikuje se od strojnega učenja, kjer model sam odkriva vzorce iz podatkov. Sistemi na osnovi pravil so uporabni, ko:
- imamo opravka z dobro razumljenim in stabilnim problemom,
- želimo popoln nadzor in predvidljivost,
- nimamo veliko podatkov ali so ti predragi za označevanje.

**Konkreten primer: Zaščitni sistem jedrske elektrarne**
Predstavljajte si sistem za zaustavitev jedrskega reaktorja v primeru previsoke temperature. V tem primeru morda ni zdravo ugibati.

Inženirji napišejo pravila po načelu **če-potem**:
- **ČE** temperatura v sredici reaktorja **preseže** 650 °C **IN** tlak v primarnem krogu **pade pod** 120 barov,
- **POTEM** takoj **spusti** kontrolne palice v reaktor (Scram).

To pravilo temelji na fizikalnih zakonitostih in več desetletjih raziskav jedrske fizike. Sistem ne išče vzorcev v podatkih - če bi se odločali na podlagi strojnega učenja, bi potrebovali ogromno podatkov o jedrskih nesrečah (ki jih na srečo nimamo), poleg tega pa model ne bi bil pojasnljiv (explainable). Regulatorji zahtevajo, da je vsak varnostni ukaz mogoče **natančno utemeljiti** in revidirati - kar sistemi na osnovi pravil omogočajo, "črne skrinjice" strojnega učenja pa ne.

---

### [2 točki] Kaj je Minimax algoritem in kako ga uporabimo pri igrah, kot so križci in krožci?
**Vprašanje:**  
Razložite Minimax algoritem za igre z ničelno vsoto (npr. križci in krožci). Kako deluje rekurzivno? Kaj pomenijo vrednosti +1, -1, 0? Ali to uvrščamo med strojno učenje? Utemeljite.

**Rešitev:**  
Minimax je rekurzivni algoritem za iskanje optimalne poteze v igrah, kjer si igralca izmenjujeta poteze. Deluje tako, da simulira vse možne nadaljnje poteze do končnih stanj (zmaga, poraz, neodločeno) in jim pripiše vrednosti:
- +1 za zmago AI,
- -1 za poraz AI,
- 0 za neodločeno.
AI na svoji potezi izbere potezo z **najvišjo** vrednostjo (maksimizira), nasprotnik pa mu nasprotuje z izbiro poteze z **najnižjo** vrednostjo (minimizira). To ni strojno učenje, ker ne vključuje učenja iz podatkov - gre za klasično iskanje po drevesu.

---

### [1 točka] Kaj je alfa-beta rezanje (alpha-beta pruning) in zakaj ga uporabljamo pri Minimaxu?
**Vprašanje:**  
Kaj je alfa-beta rezanje in kako izboljša učinkovitost algoritma Minimax? Zakaj je pomembno pri kompleksnejših igrah?

**Rešitev:**  
Alfa-beta rezanje je tehnika za optimizacijo Minimaxa, ki odreže (ne obišče) veje drevesa, za katere je gotovo, da ne bodo vplivale na končno odločitev. S tem prihranimo računski čas, ne da bi spremenili končni rezultat. Bistveno je pri igrah z večjim prostorom stanj (npr. šah), kjer bi bilo preiskovanje celotnega drevesa prepočasno.

---

### [1 točka] Kaj je word2vec? Opišite.
**Vprašanje:**
Kaj je word2vec? Opišite njegov namen in osnovno idejo.

**Rešitev:**
Word2vec je tehnika za **predstavitev besed kot vektorjev** (številskih vrednosti) v večdimenzionalnem prostoru. Namenjena je zajemanju pomenskih in skladenjskih odnosov med besedami. Osnovna ideja je, da se besede, ki se pojavljajo v podobnih kontekstih, nahajajo blizu skupaj v vektorskem prostoru. To omogoča matematične operacije, kot npr. "kralj" - "moški" + "ženska" = "kraljica".

---

### [2 točki] Kakšna je razlika med arhitekturama CBOW in Skip-gram pri word2vec?
**Vprašanje:**  
Razložite razliko med modeloma **CBOW (Continuous Bag of Words)** in **Skip-gram** pri tehniki word2vec. Kdaj je katera primernejša?

**Rešitev:**  
- **CBOW** napoveduje ciljno besedo na podlagi besed v njeni okolici (konteksta). Deluje hitreje in je primernejši za pogostejše besede.
- **Skip-gram** napoveduje okoliške besede glede na ciljno besedo. Počasnejši je, vendar deluje bolje za redke besede in manjše količine podatkov. Oba pristopa uporabljata plitvo nevronsko mrežo, katere uteži postanejo vektorji besed (embeddingi).

---

### [2 točki] Razložite razliko med parametričnimi in neparametričnimi modeli.
**Vprašanje:**
Razložite razliko med parametričnimi in neparametričnimi modeli v strojnem učenju. Za vsakega navedite en primer algoritma.

**Rešitev:**
- **Parametrični modeli:** Imajo vnaprej določeno strukturo in fiksno število parametrov, ne glede na količino podatkov. So hitrejši za učenje, a manj prilagodljivi. *Primer:* Linearna regresija, logistična regresija.
- **Neparametrični modeli:** Neparametrični modeli nimajo vnaprej določenega fiksnega števila parametrov; njihova kompleksnost lahko raste s količino podatkov. So bolj prilagodljivi, a počasnejši in zahtevnejši za učenje. *Primer:* k-najbližjih sosedov (k-NN), odločitvena drevesa.

---

### [2 točki] Kaj je klasifikacija? Napišite primer.
**Vprašanje:**  
Kaj je klasifikacija v strojnem učenju? Razložite pojem in navedite konkreten primer problema, ki ga rešujemo s klasifikacijo.

**Rešitev:**  
Klasifikacija je vrsta nadzorovanega učenja, kjer model napoveduje **kategorično oznako (razred)** za dane vhodne podatke. Cilj je, da novim primerom dodelimo enega od vnaprej določenih razredov.

*Primer:* V jedrski elektrarni želimo na podlagi senzorskih podatkov (temperatura sredice, tlak v primarnem krogu, pretok hladila) **klasificirati stanje reaktorja** v eno od kategorij:  
- "normalno obratovanje",  
- "prehodno stanje" (npr. zagon ali zaustavitev),  
- "izredni dogodek" (npr. povišana radioaktivnost).  

Model se nauči iz zgodovinskih simulacij in podatkov o preteklih dogodkih, nato pa v realnem času pomaga operaterjem pri hitrem in pravilnem odločanju.

---

### [2 točki] Kaj je regresija? Napišite primer.
**Vprašanje:**  
Kaj je regresija v strojnem učenju? Razložite pojem in navedite konkreten primer problema, ki ga rešujemo z regresijo.

**Rešitev:**  
Regresija je vrsta nadzorovanega učenja, kjer model napoveduje **številsko (kontinuirano) vrednost** na podlagi vhodnih podatkov. Cilj je čim natančneje oceniti neznano količino.

*Primer:* Astronomi želijo napovedati **oddaljenost zvezde** od Zemlje na podlagi njenega navideznega sija in barve (spektralnega razreda). Z regresijskim modelom, naučenim na znanih zvezdah (kjer je oddaljenost izmerjena s paralakso ali drugimi metodami), lahko nato za nove zvezde ocenijo oddaljenost v svetlobnih letih.

---

## 2. VRSTE UČENJA IN ALGORITMI

### [2 točki] Kaj je linearna regresija? Napišite primer.
**Vprašanje:**
Kaj je linearna regresija? Na kratko opišite princip delovanja in navedite konkreten primer uporabe.

**Rešitev:**
Linearna regresija je nadzorovana metoda strojnega učenja za **napovedovanje številskih (kontinuiranih) vrednosti**. Deluje tako, da skozi podatkovne točke "povleče" premico (ali hiperravnino - ko imamo več vhodnih spremenljivk), ki najbolje opisuje odnos med vhodnimi spremenljivkami (značilkami) in izhodno vrednostjo. Cilj je minimizirati razdalje med dejanskimi in napovedanimi vrednostmi.

*Primer:* Napovedovanje cene rabljenega avtomobila glede na starost, prevožene kilometre in moč motorja.

---

### [1 točka] Kaj nam pove MSE pri linearni regresiji? Ali je boljši model z visoko ali nizko vrednostjo MSE?
**Vprašanje:**
Kaj nam pove MSE pri linearni regresiji? Ali je boljši model z visoko ali nizko vrednostjo MSE? Utemeljite.

**Rešitev:**
MSE je okrajšava za Mean Squared Error (povprečna kvadratna napaka).

MSE meri **povprečje kvadratov razlik** med dejanskimi in napovedanimi vrednostmi. Pove nam, kako dobro se model prilega podatkom - nižji kot je MSE, manjše so napake modela. **Boljši je model z nižjo vrednostjo MSE**, saj njegove napovedi odstopajo manj od dejanskih vrednosti.

---

### [2 točki] Kaj je logistična regresija in kako se razlikuje od linearne?
**Vprašanje:**
Kaj je logistična regresija? V čem se bistveno razlikuje od linearne regresije in za kakšne probleme jo uporabljamo?

**Rešitev:**
Logistična regresija je kljub imenu **klasifikacijska metoda** (ne regresijska). Uporablja se za napovedovanje verjetnosti pripadnosti določeni kategoriji (npr. da/ne). Bistvena razlika od linearne regresije je v tem, da uporablja **sigmoidno (logistično) funkcijo**, ki linearni rezultat "stisne" v območje med 0 in 1, kar interpretiramo kot verjetnost. Uporabljamo jo za **binarno klasifikacijo** (npr. ali bo stranka kupila izdelek: da/ne).

---

### [1 točka] Kaj je koeficient determinacije (R^2) in kaj nam pove?
**Vprašanje:**  
Kaj je koeficient determinacije, označen kot R^2? Kako ga interpretiramo pri regresijskih modelih? Kakšne vrednosti lahko zavzame in kaj pomeni R^2 = 0, kaj pa R^2 = 1?

**Rešitev:**  
Koeficient determinacije R^2 je metrika za ocenjevanje kakovosti regresijskih modelov. Pove, kolikšen delež variance ciljne spremenljivke je pojasnjen z modelom (z vhodnimi značilkami).

- R^2 = 1 pomeni, da model popolnoma pojasni varianco podatkov - vse točke ležijo na regresijski premici (ali hiperravnini).
- R^2 = 0 pomeni, da model ne pojasni nič več variance, kot bi jo pojasnili s preprosto uporabo povprečja ciljne spremenljivke.
- R^2 je lahko tudi **negativen**, kar pomeni, da je model slabši od napovedi s konstantnim povprečjem - to se zgodi, če model ni pravilno prilagojen podatkom (npr. napačna izbira modela, premajhna količina podatkov ali premočna regularizacija).

R^2 se pogosto uporablja skupaj z **MSE** (povprečno kvadratno napako). MSE meri absolutno velikost napak, R^2 pa meri **relativno izboljšanje** glede na osnovni model (napoved s povprečjem).

---

### [2 točki] Kaj so odločitvena drevesa? Opišite zgradbo in primer.
**Vprašanje:**
Kaj so odločitvena drevesa? Opišite njihovo zgradbo (kaj so vozlišča, veje, listi) in navedite en primer uporabe.

**Rešitev:**
Odločitvena drevesa so nadzorovana metoda strojnega učenja, ki deluje tako, da podatke **večkrat razdeli** na manjše podmnožice na podlagi vrednosti značilk.
- **Korensko vozlišče:** predstavlja celotno množico podatkov.
- **Notranja vozlišča:** predstavljajo pogoje (vprašanja) o značilkah.
- **Veje:** predstavljajo možne odgovore na pogoje.
- **Listi:** predstavljajo končne napovedi (razrede ali vrednosti).

*Primer:* Ocenjevanje tveganja pri odobritvi posojila - drevo sprašuje po dohodku, zaposlitvi, zgodovini odplačevanja in na koncu razvrsti stranko v "varno" ali "tvegano".

---

### [2 točki] Kaj so nevronske mreže? Opišite osnovne gradnike.
**Vprašanje:**
Kaj so umetne nevronske mreže? Opišite njihove osnovne gradnike (vhodni sloj, skriti sloji, izhodni sloj, nevroni, uteži, aktivacijske funkcije).

**Rešitev:**
Umetne nevronske mreže so računski modeli, navdihnjeni z delovanjem človeških možganov. Sestavljene so iz **plasti nevronov**:
- **Vhodni sloj:** sprejema vhodne podatke (značilke).
- **Skriti sloji:** obdelujejo podatke, vsak nevron izračuna uteženo vsoto vhodov in jo pošlje skozi **aktivacijsko funkcijo** (npr. ReLU, sigmoid), ki doda nelinearnost.
- **Izhodni sloj:** vrne končno napoved.
- **Uteži** so parametri na povezavah med nevroni, ki se tekom učenja prilagajajo, da model čim bolje napove rezultat.

---

### [3 točke] Kaj pomeni, da zelo velike nevronske mreže (npr. LLM) pogosto delujejo dobro kljub ogromnemu številu parametrov? Kaj je pruning?
**Vprašanje:**  
Pri zelo velikih nevronskih mrežah (npr. LLM) kljub nevarnosti prekomernega prilagajanja te mreže pogosto delujejo dobro na testnih podatkih. Razložite ta pojav. Prav tako opišite, kaj je **pruning** (čiščenje) nevronskih mrež.

**Rešitev:**  
Pri zelo velikih mrežah se pojavi t. i. **"double descent"** - ko presežemo določeno velikost, se napaka na testnih podatkih spet začne zmanjševati. Razlog je v tem, da mreža z veliko parametri lažje najde dober optimum in postane bolj robustna, čeprav ima teoretično dovolj kapacitete za popolno prilagajanje učnim podatkom.  
**Pruning** je tehnika, pri kateri po učenju odstranimo nevrone ali povezave z majhnimi utežmi, ki ne prispevajo bistveno k napovedim. S tem zmanjšamo velikost modela, pospešimo sklepanje in včasih celo izboljšamo posploševanje, ne da bi bistveno poslabšali natančnost.

---

### [2 točki] Kakšni so izzivi pri delu z velikimi nevronskimi mrežami?
**Vprašanje:**
Kakšni so glavni izzivi pri delu z velikimi nevronskimi mrežami (globoko učenje)? Naštejte vsaj tri in jih na kratko opišite.

**Rešitev:**
1. **Potrebna je ogromna količina podatkov:** Globoke mreže imajo milijone parametrov, zato potrebujejo ogromno učnih primerov, da se ne prekomerno prilagodijo.
2. **Visoki računski stroški:** Učenje zahteva zmogljivo strojno opremo (GPE/TPU), kar je drago in porabi veliko energije.
3. **Prekomerno prilagajanje (overfitting):** Zaradi velike kapacitete se model lahko "nauči" šuma v podatkih namesto pravih vzorcev.
4. **Težave z interpretacijo (black box problem):** Težko je razložiti, zakaj je model sprejel določeno odločitev.
5. **Občutljivost na hiperparametre:** Zahtevajo skrbno nastavljanje arhitekture in parametrov učenja.

---

## 3. VREDNOTENJE MODELOV

### [2 točki] Zakaj ločimo podatke na učno in testno množico? Opišite proces.
**Vprašanje:**
Zakaj v strojnem učenju podatke ločimo na učno in testno množico? Opišite celoten proces (kaj naredimo s katero množico) in pojasnite, zakaj ne uporabimo istih podatkov za učenje in testiranje.

**Rešitev:**
Podatke ločimo, da **objektivno ocenimo uspešnost modela** na novih, nevidnih podatkih.
- **Učna množica (npr. 80% podatkov):** Uporabimo jo za **učenje modela** - model na njej prilagaja svoje parametre.
- **Testna množica (npr. 20% podatkov):** Uporabimo jo za **končno evalvacijo** - po končanem učenju preverimo, kako dobro model napoveduje na podatkih, ki jih še ni videl.

Če bi model testirali na istih podatkih, kot smo ga učili, bi dobili preveč optimistično oceno (model bi si podatke zapomnil, ne pa se naučil vzorcev - overfitting). To je enako, kot če bi se "napiflali" vseh odgovorov na vprašanja, ne bi pa znali odgovoriti na drugače postavljeno vprašanje ali na nalogo, ki bi zahtevala logično sklepanje. To bi pomenilo, da v praksi (na novih podatkih) model ne bi deloval dobro. 


---

### [2 točki] Kaj je validacijska množica in zakaj jo uporabljamo?
**Vprašanje:**
Poleg učne in testne množice včasih uporabljamo tudi validacijsko množico. Kakšen je njen namen in kdaj jo potrebujemo?

**Rešitev:**
Validacijsko množico uporabljamo za **nastavljanje hiperparametrov** modela (npr. stopnja učenja, število dreves, moč regularizacije) in za **primerjavo različnih modelov** med razvojem. Učimo na učni množici, preverjamo na validacijski, ko smo zadovoljni, pa končno oceno dobimo na testni množici. S tem preprečimo, da bi se model posredno "naučil" tudi testnih podatkov preko prilagajanja hiperparametrov.

---

### [2 točki] Kaj je matrika zmede (confusion matrix)? Opišite njene elemente.
**Vprašanje:**
Kaj je matrika zmede (confusion matrix) pri klasifikaciji? Opišite štiri osnovne elemente (TP, TN, FP, FN) in pojasnite, kaj pomenijo.

**Rešitev:**
Matrika zmede je orodje za vizualizacijo uspešnosti klasifikacijskega modela. Primerja dejanske razrede (tisto, kar v resnici je) z napovedanimi razredi (tisto, kar je model napovedal). Običajno je predstavljena kot tabela, kjer vrstice predstavljajo dejanske vrednosti, stolpci pa napovedane vrednosti.

Za binarno klasifikacijo (npr. "pozitivno" in "negativno") poznamo:
- **TP (True Positive):** Pravilno napovedani pozitivni primeri.
- **TN (True Negative):** Pravilno napovedani negativni primeri.
- **FP (False Positive):** Lažno pozitivni - model je napovedal pozitivno, dejansko je negativno.
- **FN (False Negative):** Lažno negativni - model je napovedal negativno, dejansko je pozitivno.

Matrika zmede je osnova za izračun drugih metrik, kot so natančnost, priklic in mera F1.

---

### [2 točki] Kakšna je razlika med natančnostjo (precision) in priklicem (recall)?
**Vprašanje:**
Razložite razliko med **natančnostjo (precision)** in **priklicem (recall)**. Kdaj je pomembnejša natančnost in kdaj priklic? Navedite primere.

**Rešitev:**
- **Natančnost (precision):** Od vseh primerov, ki jih je model označil kot pozitivne, koliko jih je res pozitivnih? Formula: TP / (TP + FP). **Visoka natančnost** pomeni malo lažnih alarmov.
- **Priklic (recall):** Od vseh res pozitivnih primerov, koliko jih je model uspešno našel? Formula: TP / (TP + FN). **Visok priklic** pomeni, da smo odkrili večino pozitivnih primerov.

*Kdaj kaj?*
- **Natančnost je pomembnejša**, ko so lažno pozitivni rezultati dragi (npr. označevanje e-pošte kot spam - nočemo, da se izgubi pomembno sporočilo).
- **Priklic je pomembnejši**, ko so lažno negativni rezultati dragi (npr. odkrivanje raka - nočemo spregledati bolnika).

---

### [1 točka] Kaj je mera F1 in zakaj jo uporabljamo namesto natančnosti ali priklica?
**Vprašanje:**
Kaj je mera F1 in zakaj jo uporabljamo namesto natančnosti ali priklica posamič? Pri odgovoru razložite tudi, kaj pomeni, da je F1 mera **harmonično povprečje**.

**Rešitev:**
Mera F1 je **harmonično povprečje natančnosti (precision) in priklica (recall)**. Uporabljamo jo, ko želimo **uravnoteženo oceno** modela, še posebej pri neuravnoteženih razredih (ko je enega razreda veliko več kot drugega). Daje enoten pogled na obe meritvi hkrati.

**Kaj je harmonično povprečje?**
Harmonično povprečje se od bolj znanega aritmetičnega povprečja (navadnega seštevanja in deljenja) razlikuje v tem, da **kaznuje velika odstopanja** med vrednostmi. Bolj kot aritmetično povprečje upošteva **manjše vrednosti** - če je ena od vrednosti zelo nizka, bo tudi harmonično povprečje nizko.

Formula za mero F1:  
`F1 = 2 * (natančnost * priklic) / (natančnost + priklic)`

**Primer:**
Recimo, da imamo dva modela za odkrivanje goljufij:

- **Model A:** natančnost = 0,9 (90 %), priklic = 0,1 (10 %)
- **Model B:** natančnost = 0,5 (50 %), priklic = 0,5 (50 %)

Če bi uporabili **aritmetično povprečje**:
- Model A: (0,9 + 0,1) / 2 = 0,5
- Model B: (0,5 + 0,5) / 2 = 0,5

Po aritmetičnem povprečju sta modela enako dobra, kar je zavajajoče - model A je v resnici slab, saj odkrije le 10 % goljufij!

Če uporabimo **harmonično povprečje (F1)**:
- Model A: 2 × (0,9 × 0,1) / (0,9 + 0,1) = 2 × 0,09 / 1 = 0,18
- Model B: 2 × (0,5 × 0,5) / (0,5 + 0,5) = 2 × 0,25 / 1 = 0,5

F1 mera pravilno pokaže, da je model B bistveno boljši, ker uravnoteži obe meritvi. Model A ima kljub visoki natančnosti nizek priklic, zato je F1 nizka.

**Zakaj je to pomembno?**
F1 mero uporabljamo, ko želimo model, ki je hkrati **natančen** (ko nekaj napove, ima prav) in **občutljiv** (odkrije čim več pozitivnih primerov). Posebej je uporabna pri neuravnoteženih razredih, kjer bi nas sama natančnost (accuracy) lahko zavedla.

---

## 4. TEŽAVE PRI MODELIRANJU

### [2 točki] Konkretno opišite vsaj 2 problema velikih jezikovnih modelov.
**Vprašanje:**
Veliki jezikovni modeli (LLM) imajo več pomanjkljivosti. Konkretno opišite **vsaj dva problema**, ki se pojavljata pri njihovi uporabi. Pri vsakem problemu navedite tudi možen vzrok in en konkreten ukrep za omilitev.

**Rešitev:**
1. **Haluciniranje (izmišljanje dejstev):**
   - *Opis:* Model samozavestno generira neresnične ali izmišljene informacije, ki zvenijo verodostojno.
   - *Vzrok:* Model nima pravega razumevanja resničnosti, temveč le statistično napoveduje naslednjo besedo (oz. token). Prav tako nima dostopa do zunanjih virov znanja (razen, če jih dodamo).
   - *Ukrep:* Uporaba tehnike RAG (Retrieval-Augmented Generation), kjer model pred odgovarjanjem poišče relevantne informacije v zunanji bazi znanja.

2. **Pristranskost (bias):**
   - *Opis:* Model reproducira ali celo krepi stereotipe in predsodke, prisotne v učnih podatkih (npr. spolni, rasni stereotipi).
   - *Vzrok:* Učni podatki (spletne strani, knjige) vsebujejo človeške predsodke, ki se jih model nauči.
   - *Ukrep:* Skrbno čiščenje in uravnoteženje učnih podatkov ter uporaba tehnik za zmanjševanje pristranskosti med učenjem (debiasing).

3. **Stroškovna in okoljska zahtevnost:**
   - *Opis:* Učenje in delovanje velikih modelov zahteva ogromno energije in zmogljive strojne opreme.
   - *Vzrok:* Modeli z milijardami parametrov potrebujejo tisoče ur računanja na specializiranih čipih.
   - *Ukrep:* Uporaba manjših, domeni prilagojenih modelov namesto največjih; optimizacija modelov (kvantizacija, obrezovanje - pruning).

---

### [2 točki] Kakšni so okoljski vplivi treniranja velikih jezikovnih modelov?
**Vprašanje:**  
Naštejte vsaj tri okoljske probleme, povezane s treniranjem in delovanjem velikih jezikovnih modelov (LLM). Zakaj so ti vplivi zaskrbljujoči?

**Rešitev:**  
1. **Poraba elektrike:** Podatkovni centri zahtevajo ogromno energije.  
2. **Poraba vode:** Za hlajenje strežnikov se uporablja velike količine vode (iz vodovoda ali rek), ki izhlapeva in se ne vrača neposredno v okolje.  
3. **Hrup:** Hlajenje in delovanje strežnikov povzroča hrup (tudi infrazvok), kar lahko moti okolico.  
4. **Stroški in dostopnost:** Visoki začetni stroški onemogočajo manjšim akterjem vstop na trg, kar vodi v monopol velikih podjetij.

---

### [2 točki] Kaj je RAG? Kje in zakaj se uporablja?
**Vprašanje:**
Kaj pomeni kratica RAG? Kje in zakaj se uporablja? Opišite osnovni princip delovanja.

**Rešitev:**
RAG (Retrieval-Augmented Generation) je tehnika, ki **združuje iskanje po podatkovni bazi z generiranjem odgovorov** z velikim jezikovnim modelom.
- **Princip:** Ko uporabnik postavi vprašanje, sistem najprej poišče relevantne dokumente ali informacije v zunanjem viru (npr. baza znanja podjetja, internet). Te informacije nato doda v "kontekst" (prompt) jezikovnemu modelu, ki na njihovi podlagi generira odgovor.
- **Uporaba:** Uporablja se povsod, kjer potrebujemo **točne in aktualne informacije**, ki jih model sam po sebi nima (npr. klepetalni roboti za podporo strankam, ki črpajo iz interne dokumentacije, odgovarjanje na vprašanja o svežih novicah). RAG zmanjša haluciniranje in omogoča, da model odgovarja na podlagi preverljivih virov.

---

### [1 točka] Kaj je fine-tuning (uglaševanje) jezikovnih modelov in kakšna past se pri tem pogosto pojavi?
**Vprašanje:**  
Kaj pomeni **fine-tuning** velikih jezikovnih modelov? Zakaj lahko pride do tega, da se model po uglaševanju preveč strinja z uporabnikom (sycophancy)?

**Rešitev:**  
Fine-tuning je nadaljnje učenje že osnovnega modela na specifičnih podatkih, da se prilagodi določeni domeni ali nalogi. Pri tem se model lahko nauči, da je nagrajen za odgovore, ki se ujemajo z uporabnikovimi pogledi, tudi če so ti napačni. Posledično model postane preveč popustljiv in ponavlja uporabnikove napake ali pristranskosti, namesto da bi podal objektivne informacije.

---

### [2 točki] Kaj je prompt inženiring in kateri so ključni nasveti za učinkovito komunikacijo z LLM?
**Vprašanje:**  
Opišite koncept **prompt inženiringa**. Katere elemente naj vsebuje dober prompt, da dobimo čim bolj uporaben odgovor od velikega jezikovnega modela? Navedite vsaj tri nasvete.

**Rešitev:**  
Prompt inženiring je veščina oblikovanja vnosov (navodil) za jezikovne modele, da ti vrnejo želen in kakovosten odgovor. Ključni nasveti:
- **Določitev vloge:** modelu povemo, naj nastopa kot strokovnjak za določeno področje (npr. »Si programer C#«).
- **Jasna naloga in cilj:** natančno opišemo, kaj želimo (npr. »Napiši funkcijo, ki sešteje dve števili«).
- **Kontekst in omejitve:** dodamo morebitne omejitve (npr. dolžina odgovora, slog, format).
- **Kritično vrednotenje:** ne zaupamo slepo, ampak preverimo dejstva, saj model lahko halucinira.

---

### [3 točke] Kaj je prekomerno prilagajanje (overfitting)?
**Vprašanje:**
Kaj je prekomerno prilagajanje (overfitting) v strojnem učenju? Opišite, kako prepoznamo, da se je zgodilo. Dodajte en primer.

**Rešitev:**
Prekomerno prilagajanje (overfitting) se zgodi, ko se model **preveč natančno prilagodi učnim podatkom**, vključno s šumom in nepomembnimi podrobnostmi. Posledica je odlična napoved na učnih podatkih, a slaba na novih, nevidnih podatkih.
- **Prepoznavanje:** Ko je napaka na učni množici bistveno manjša kot na testni/validacijski množici.
- **Preprečevanje:**
    1. **Regularizacija** (npr. L1, L2) - kaznovanje prevelikih uteži.
    2. **Zgodnje zaustavljanje (early stopping)** - ustavimo učenje, ko se napaka na validacijski množici začne povečevati.
    4. **Zmanjšanje kompleksnosti modela** (npr. manj plasti v nevronski mreži, manj globoko drevo).
    5. **Metoda prečnega preverjanja (cross-validation)** - podatke večkrat razdelimo na učni in validacijski del ter model ocenimo na vseh delitvah. S tem dobimo bolj robustno oceno in preprečimo, da bi bil model preveč prilagojen eni sami delitvi.

Primer:
Predstavljajte si, da model za napovedovanje vremena dobro napove pretekle podatke, ker si je zapomnil vsak deževen dan, a na novo napoved je popolnoma zgrešil. To je overfitting.

---

### [2 točki] Kaj je podprileganje (underfitting) in zakaj se pojavi?
**Vprašanje:**
Kaj je podprileganje (underfitting)? Zakaj pride do njega in kako ga odpravimo?

**Rešitev:**
Podprileganje (underfitting) se zgodi, ko je model **preveč preprost**, da bi zajel osnovne vzorce v podatkih. Posledica je slaba napoved tako na učni kot na testni množici.
- **Vzroki:** Model je premalo kompleksen (npr. linearna regresija za nelinearne podatke), premalo učnih podatkov ali premočna regularizacija.
- **Odprava:** Uporabimo kompleksnejši model, dodamo več značilk (feature engineering), podaljšamo učenje ali zmanjšamo regularizacijo.

Konkreten primer:
Predstavljajmo si, da želimo napovedati ceno stanovanja glede na njegovo velikost. V resnici cena z velikostjo narašča, vendar ne linearno - manjša stanovanja imajo višjo ceno na kvadratni meter, večja pa nižjo. Če za napoved uporabimo preprosto linearno regresijo (premico), bo model "spregledal" ta upogib. Rezultat bo, da bo model enako slabo napovedoval tako za učna stanovanja (ki jih je "videl") kot za nova - povsod bo zgrešil za kakšnih 50.000 €. Model se preprosto ni mogel naučiti pravilnega odnosa, ker je bil preveč preprost za to nalogo.

Rešitev v tem primeru: Uporabimo polinomsko regresijo ali drug nelinearni model (npr. odločitvena drevesa), ki lahko zajame upogib v podatkih.

---

## 5. NAPREDNE TEHNIKE IN KONCEPTI

### [2 točki] Kaj so konvolucijske nevronske mreže (CNN) in za kaj se uporabljajo?
**Vprašanje:**
Kaj so konvolucijske nevronske mreže (CNN)? Za kakšno vrsto podatkov so še posebej primerne in zakaj? Opišite osnovni princip delovanja (konvolucija, združevanje).

**Rešitev:**
Konvolucijske nevronske mreže (CNN) so posebna arhitektura nevronskih mrež, **posebej prilagojena za obdelavo podatkov z lokalno prostorsko strukturo**, kot so slike, video posnetki ali spektrogrami. Njihova prednost je, da samodejno zaznavajo prostorske vzorce - od preprostih (robovi, kotički) do zapletenih (oblike, teksture, deli objektov).

**Osnovna principa delovanja:**

1. **Konvolucija:**
   - Filter (imenovan tudi jedro) je majhna matrika števil (npr. 3×3 ali 5×5), ki drsi čez celotno sliko.
   - Na vsaki lokaciji filter izračuna zmnožek svojih vrednosti z vrednostmi pikslov pod seboj in rezultate sešteje.
   - Rezultat tega procesa je **nova slika (imenovana karta značilk)** - vsaka točka v novi sliki pove, kako močno se ujema vzorec iz filtra z delom originalne slike.
   - *Primer:* Filter, občutljiv na navpične robove, bo dal visoke vrednosti povsod, kjer so v sliki navpični prehodi (robovi), nizke pa povsod drugje.

2. **Združevanje (Pooling):**
   - Zmanjšuje velikost slike (dimenzionalnost) in povzema informacije.
   - Najpogostejši je **max pooling**, ki vzame največjo vrednost iz vsakega majhnega okna (npr. 2×2).
   - S tem ohranimo najpomembnejše informacije, hkrati pa zmanjšamo število parametrov in računsko zahtevnost.

**Uporaba:**
- Prepoznavanje objektov na slikah (npr. ali je na sliki mačka)
- Klasifikacija medicinskih slik (npr. odkritje tumorjev)
- Segmentacija slik (označevanje vsakega piksla, npr. za avtonomna vozila)
- Obdelava videa in prepoznavanje obrazov

---

### [2 točki] Kaj so rekurentne nevronske mreže (RNN) in kaj je njihova posebnost?
**Vprašanje:**
Kaj so rekurentne nevronske mreže (RNN)? Kakšna je njihova ključna lastnost, ki jih loči od običajnih nevronskih mrež, in za kakšne podatke so najprimernejše?

**Rešitev:**
Rekurentne nevronske mreže (RNN) imajo **povratne zanke**, kar jim omogoča, da ohranjajo "spomin" prejšnjih vhodov. Med obdelavo zaporedja prenašajo skrito stanje iz enega koraka v naslednjega. iz prejšnjega koraka v naslednjega.
- **Ključna lastnost:** Sposobnost obdelave **zaporednih podatkov** spremenljive dolžine.
- **Uporaba:** Napovedovanje časovnih vrst, obdelava naravnega jezika (besedila), prepoznavanje govora, strojno prevajanje.

---

### [2 točki] Kaj je mehanizem pozornosti (attention) in zakaj je revolucionaren?
**Vprašanje:**
Kaj je mehanizem pozornosti (attention mechanism) v nevronskih mrežah? Zakaj je pomemben in kje se najbolj pogosto uporablja?

**Rešitev:**
Mehanizem pozornosti omogoča modelu, da se pri napovedovanju **osredotoči na najpomembnejše dele vhodnih podatkov**, namesto da bi enakovredno obravnaval vse. Pri obdelavi jezika to pomeni, da model pri generiranju naslednje besede "pogleda" nazaj in oceni, katere prejšnje besede so najbolj relevantne.
- **Pomen:** Rešil je težavo pozabljanja pri dolgih zaporedjih (ki so jo imeli RNN-ji) in omogočil vzporedno obdelavo.
- **Uporaba:** Je osnova za **transformerske arhitekture** (npr. BERT, GPT), ki danes poganjajo večino najsodobnejših modelov za jezik.

---

### [2 točki] Kaj so transformatorski modeli (transformers)?
**Vprašanje:**
Kaj so transformatorski modeli (transformers)? Opišite njihovo glavno inovacijo in zakaj so nadomestili RNN-je za obdelavo jezika.

**Rešitev:**
Transformatorski modeli so arhitektura, ki v celoti temelji na **mehanizmu pozornosti** in ne uporablja ponavljajočih se zank (kot RNN). Njihova glavna inovacija je, da obdelujejo **celotno zaporedje vzporedno**, kar omogoča veliko hitrejše učenje na zmogljivi strojni opremi.
- **Prednost:** Boljše obvladovanje dolgih odvisnosti v besedilu in možnost skaliranja na ogromne modele.
- **Uporaba:** Večina sodobnih LLM (GPT, BERT, Llama) temelji na transformatorjih.

---

### [2 točki] Kaj so GAN-i (generativne sovražne mreže)?
**Vprašanje:**
Kaj so generativne sovražne mreže (GAN)? Opišite osnovno idejo dveh mrež (generator in diskriminator) in za kaj se uporabljajo.

**Rešitev:**
Generativne sovražne mreže (GAN) so sestavljene iz dveh nevronskih mrež, ki tekmujeta med seboj:
- **Generator:** Poskuša ustvariti čim bolj realistične umetne podatke (npr. slike).
- **Diskriminator:** Poskuša ločiti med pravimi podatki in tistimi, ki jih je ustvaril generator.
- **Učenje:** Generator se uči "preslepiti" diskriminatorja, diskriminator pa se uči bolje prepoznavati ponaredke. Sčasoma generator postane zelo dober v ustvarjanju realističnih podatkov. Učenje poteka v obliki minimax igre.
- **Uporaba:** Ustvarjanje realističnih slik (npr. obrazi ljudi, ki ne obstajajo), prenos sloga, povečevanje ločljivosti slik.

---

## 6. PRAKTIČNI PRIMERI IN UPORABA

### [2 točki] Kaj je značilka (feature) in inženiring značilk (feature engineering)?
**Vprašanje:**
Kaj je značilka (feature) v strojnem učenju? Kaj pomeni inženiring značilk (feature engineering) in zakaj je pomemben?

**Rešitev:**
- **Značilka (feature)** je merljiva lastnost ali atribut podatkov, ki ga uporabimo kot vhod v model (npr. starost osebe, število sob v hiši, barva piksla na sliki).
- **Inženiring značilk (feature engineering)** je postopek ustvarjanja novih, bolj informativnih značilk iz obstoječih podatkov, da bi izboljšali delovanje modela. Vključuje lahko transformacije (npr. logaritem), kombinacije (npr. razmerje dveh spremenljivk) ali diskretizacijo (npr. ločitev starosti po kategorijah: < 18, 18-25, 25-30, ...).
- **Pomembnost:** Dobre značilke so pogosto pomembnejše od izbire algoritma.

---

### [2 točki] Kaj je normalizacija podatkov in zakaj jo izvajamo?
**Vprašanje:**
Kaj je normalizacija (oz. standardizacija) podatkov? Zakaj je pomembna za nekatere algoritme strojnega učenja (npr. nevronske mreže, k-NN, SVM)?

**Rešitev:**
Normalizacija je postopek **spreminjanja merila vrednosti značilk**, tako da so v primerljivem območju (npr. med 0 in 1 ali s povprečjem 0 in standardnim odklonom 1).
- **Zakaj je pomembna:** Algoritmi, ki temeljijo na razdaljah (k-NN, SVM) ali gradientnem spustu (nevronske mreže), so občutljivi na merilo. Če ima ena značilka veliko večje vrednosti (npr. dohodek v evrih) od druge (npr. starost v letih), bo dominirala pri izračunu razdalje ali posodabljanju uteži. Normalizacija zagotovi, da vse značilke enakovredno prispevajo k učenju.

---

### [2 točki] Kaj je reinforcement learning?
**Vprašanje:**
Kaj je učenje z ojačitvijo (reinforcement learning)? Opišite osnovne koncepte: agent, okolje, akcija, nagrada. Navedite primer uporabe.

**Rešitev:**
Učenje s posredovanjem je vrsta strojnega učenja, kjer se **agent uči s poskušanjem** v interakciji z okoljem. Prejema **nagrade** (ali kazni) za svoja dejanja in poskuša povečati skupno nagrado skozi čas.
- **Agent:** tisti, ki se uči in sprejema odločitve.
- **Okolje:** svet, v katerem agent deluje.
- **Akcija:** poteza, ki jo agent naredi.
- **Nagrada:** povratna informacija iz okolja (kako dobra je bila akcija).
- **Primer:** Učenje igranja šaha - agent (računalnik) igra poteze (akcije) na šahovnici (okolje) in prejme nagrado ob zmagi (ali kazen ob porazu).

---

### [2 točki] Kaj so vdelave (embeddings)?
**Vprašanje:**
Kaj so vdelave (embeddings) v kontekstu strojnega učenja? Opišite njihov namen in navedite primer (npr. za besede).

**Rešitev:**
Vdelave (embeddings) so **vektorji realnih števil**, ki predstavljajo objekte (npr. besede, uporabnike, izdelke) v večdimenzionalnem prostoru. Namen je, da objekti s podobnim pomenom ali lastnostmi ležijo blizu skupaj v tem prostoru.
- **Primer (word embeddings):** Besedi "kralj" in "kraljica" sta si v vektorskem prostoru blizu, prav tako obstajajo regularnosti (npr. "Pariz" - "Francija" = cca. "Berlin" - "Nemčija").
- **Uporaba:** V sistemih za priporočanje (uporabniški vektorji in vektorji filmov), obdelavi naravnega jezika, iskanju podobnih elementov.

---

### [1 točka] Kaj je grozdenje (clustering)? Navedite primer.
**Vprašanje:**
Kaj je grozdenje (clustering) v nenadzorovanem učenju? Navedite en konkreten primer uporabe.

**Rešitev:**
Grozdenje (clustering) je tehnika združevanja podatkovnih točk v skupine (grozde) tako, da so si točke znotraj istega grozda čim bolj podobne, točke iz različnih grozdov pa čim bolj različne. Podatki niso vnaprej označeni.
- *Primer:* Trgovska veriga razdeli svoje stranke v skupine glede na nakupovalne navade (npr. "družine z otroki", "študenti", "upokojenci"), da za vsako skupino pripravi marketinške akcije.

---

### [1 točka] Kaj je metoda najbližjih sosedov (k-NN)?
**Vprašanje:**
Na kratko opišite metodo k-najbližjih sosedov (k-NN). Ali potrebuje fazo učenja (kot npr. linearna regresija)? Kako poteka napovedovanje?

**Rešitev:**
Metoda k-najbližjih sosedov (k-NN) je eden najpreprostejših algoritmov strojnega učenja. Uporablja se predvsem za klasifikacijo (razvrščanje), lahko pa tudi za regresijo (napovedovanje številskih vrednosti).

**Osnovna ideja:**
"Povej mi, s kom se družiš, in povem ti, kdo si." - nov primer uvrstimo v razred, ki prevladuje med njegovimi najbližjimi sosedi v učni množici.

**Kako deluje v praksi:**
1. **Shranjevanje podatkov:** Model si preprosto zapomni vse učne primere (njihove značilnice in razrede).
2. **Napovedovanje za nov primer:**
   - Izračuna razdaljo (npr. evklidsko) med novim primerom in vsemi shranjenimi primeri.
   - Izbere **k najbližjih** (tistih z najmanjšo razdaljo).
   - Pri klasifikaciji nov primer dodeli v razred, ki se najpogosteje pojavi med izbranimi sosedi. Pri regresiji izračuna povprečje vrednosti sosedov.

**Ali potrebuje fazo učenja?**
k-NN spada med **lene učence (lazy learners)** - nima prave faze učenja, saj ne zgradi modela vnaprej. Vse delo opravi šele v fazi napovedovanja. To pomeni:
- **Prednost:** Je zelo preprost in prilagodljiv.
- **Slabost:** Napovedovanje je lahko počasno, ker mora za vsak nov primer izračunati razdaljo do **vseh** učnih podatkov. Zato je manj primeren za velike količine podatkov.

**Primer:** Recimo, da imamo podatke o živalih (teža, višina) in njihove vrste (pes, mačka). Če dobimo novo žival s težo 15 kg in višino 40 cm, k-NN pogleda, katerih 5 (če je k=5) obstoječih živali je najbolj podobnih po teh lastnostih. Če so 4 od njih psi in 1 mačka, novo žival označimo kot psa.

---

### [2 točki] Kaj je točnost (accuracy) in zakaj ni vedno dobra metrika?
**Vprašanje:**
Kaj je točnost (accuracy) kot metrika za klasifikacijske modele? Zakaj kljub svoji preprostosti ni vedno primerna metrika za ocenjevanje modela? Navedite primer.

**Rešitev:**
Točnost (accuracy) je metrika, ki meri **delež pravilnih napovedi** med vsemi napovedmi. Izračunamo jo kot (število pravilnih napovedi) / (skupno število napovedi).

Ni vedno dobra metrika, ker je **zavajajoča pri neuravnoteženih razredih** (ko je enega razreda bistveno več kot drugega).

*Primer:* Imamo model za odkrivanje redke bolezni, ki prizadene le 1% populacije. Če model za vse paciente napove "zdrav", bo njegova natančnost 99%, a je popolnoma neuporaben, saj ne odkrije nobenega bolnika (priklic je 0). V takih primerih so boljše metrike natančnost (precision), priklic (recall) ali mera F1.

---

### [2 točki] Kaj je gradientni spust (gradient descent)? Opišite osnovno idejo.
**Vprašanje:**
Kaj je gradientni spust (gradient descent)? Opišite njegovo osnovno idejo in analogijo, s katero si lahko pomagamo pri razumevanju. Zakaj je pomemben pri učenju nevronskih mrež?

**Rešitev:**
Gradientni spust je **optimizacijski algoritem** za iskanje minimuma funkcije. V strojnem učenju ga uporabljamo za minimizacijo napake (izgube) modela s prilagajanjem njegovih parametrov (uteži).

**Osnovna ideja:**
1. **Izračun gradienta:** Najprej izračunamo gradient (odvod) funkcije izgube. Gradient nam pove smer največjega naraščanja funkcije izgube.
2. **Korak v nasprotno smer:** Ker želimo napako zmanjšati, se premaknemo v **nasprotno smer gradienta**.
3. **Ponavljanje:** Ta postopek ponavljamo, dokler ne pridemo do (lokalnega) minimuma, kjer je gradient blizu nič.

**Analogija:** Predstavljajte si, da stojite na hribu (visoka napaka) v megli in želite priti v dolino (minimum). Tipate teren z nogo (izračun gradienta) in naredite korak v smeri, kjer teren najbolj pada. To ponavljate, dokler ne pridete v dolino.

Je temeljni algoritem za učenje nevronskih mrež in večine drugih modelov - omogoča prilagajanje parametrov na podlagi podatkov.

---

### [2 točki] Kaj je stohastični gradientni spust (SGD) in kako se razlikuje od klasičnega gradientnega spusta?
**Vprašanje:**  
Razložite razliko med **gradientnim spustom** in **stohastičnim gradientnim spustom (SGD)**. Kakšne so prednosti in slabosti SGD pri učenju nevronskih mrež?

**Rešitev:**  
- **Gradientni spust (»batch«):** Izračuna gradient na celotni učni množici v enem koraku. Natančen, a počasen in zahteva veliko pomnilnika.
- **Stohastični gradientni spust (SGD):** Posodablja uteži na podlagi **enega samega naključnega primera** (ali majhne skupine - »mini-batch«) naenkrat. Je hitrejši in lahko uide iz lokalnih minimumov zaradi šuma, vendar je manj stabilen. Danes se večinoma uporablja mini-batch SGD.

---

### [2 točki] Kaj je eksplodirajoči gradient (exploding gradient) in kaj je izginjajoči gradient (vanishing gradient)? Kdaj se pojavita?
**Vprašanje:**
Razložite problema **eksplodirajočega gradienta (exploding gradient)** in **izginjajočega gradienta (vanishing gradient)**. Kdaj se ta pojava pojavljata in kakšne so njune posledice za učenje modela? Pri katerih arhitekturah sta še posebej izrazita?

**Rešitev:**
Oba pojava sta povezana z učenjem globokih nevronskih mrež (z veliko plastmi) in se nanašata na obnašanje gradientov med vzvratnim širjenjem napake (backpropagation).

- **Izginjajoči gradient (vanishing gradient):**
    - *Opis:* Gradienti postajajo vse manjši, ko se širijo nazaj skozi plasti. Pri zgodnjih plasteh so tako blizu nič, da se uteži skoraj ne posodabljajo več.
    - *Posledica:* Mreža se ne uči več ali se uči zelo počasi. Sprednje plasti ostanejo naključno inicializirane.
    - *Vzrok:* Uporaba določenih aktivacijskih funkcij (npr. sigmoid), katerih odvodi so manjši od 1. Množenje veliko majhnih števil povzroči eksponentno padanje gradienta.
    - *Pojavi se pri:* Globokih nevronskih mrežah, zlasti pri RNN-jih pri obdelavi dolgih zaporedij.

- **Eksplodirajoči gradient (exploding gradient):**
    - *Opis:* Gradienti postajajo vse večji, ko se širijo nazaj, in lahko dosežejo zelo velike vrednosti.
    - *Posledica:* Uteži se dramatično spremenijo v vsakem koraku, kar vodi do nestabilnega učenja, prekoračitve (overshooting) minimuma ali celo do pojava NaN vrednosti (model "eksplodira").
    - *Vzrok:* Pojavi se, ko so odvodi aktivacijskih funkcij ali uteži večji od 1, njihovo zaporedno množenje pa povzroči eksponentno rast.
    - *Pojavi se pri:* Globokih mrežah, še posebej pri RNN-jih, in pri slabi inicializaciji uteži.

**Rešitve:** Uporaba ustreznih aktivacijskih funkcij (npr. ReLU), skrbna inicializacija uteži, normalizacija podatkov, gradient clipping (omejitev velikosti gradienta za eksplodirajoče gradiente) in uporaba arhitektur, kot je LSTM pri RRN - (Long Short-Term Memory).

---

### [2 točki] Kaj je dropout in zakaj ga uporabljamo?
**Vprašanje:**
Kaj je **dropout** v kontekstu nevronskih mrež? Opišite, kako deluje in zakaj ga uporabljamo (kakšen problem rešuje).

**Rešitev:**
Dropout je tehnika **regularizacije** za preprečevanje prekomernega prilagajanja (overfittinga) pri nevronskih mrežah.
- **Kako deluje:** Med učenjem naključno "izklopimo" (drop out) določen delež nevronov v plasti (njihove izhode nastavimo na 0). V vsaki iteraciji se izklopi drugačen naključen nabor nevronov.
- **Zakaj ga uporabljamo:** S tem preprečimo, da bi se mreža preveč zanašala na posamezne nevrone in postala preveč specializirana za učne podatke. Mreža se mora naučiti bolj robustnih in splošnih značilnic, saj lahko kadarkoli odpove katerikoli del. Deluje kot povprečenje več različnih manjših mrež (ensemble effect). Poleg tega na ta način delamo manj izračunov za posamezen korak učenja (gradientni spust).

---

### [2 točki] Kaj je poštenost (fairness) v strojnem učenju in zakaj je pomembna?
**Vprašanje:**
Kaj pomeni **poštenost (fairness)** v kontekstu strojnega učenja? Zakaj je pomembno, da se s tem ukvarjamo? Navedite konkreten primer, kako lahko model diskriminira določeno skupino.

**Rešitev:**
Poštenost v strojnem učenju se nanaša na **odsotnost pristranskosti (bias)** v modelih, ki bi lahko vodila do nepoštenega ali diskriminatornega obravnavanja posameznikov ali skupin na podlagi zaščitenih atributov, kot so rasa, spol, starost, vera ipd.

**Zakaj je pomembna:**
1. **Preprečevanje diskriminacije:** Modeli lahko nenamerno okrepijo obstoječe družbene neenakosti in prikrajšajo ranljive skupine (npr. pri zaposlovanju, odobritvi posojil, sodnih odločitvah).
2. **Zaupanje in etika:** Nepošteni modeli spodkopavajo zaupanje javnosti v tehnologijo.
3. **Zakonodaja:** Vse več je zakonskih zahtev, ki prepovedujejo diskriminatorno avtomatizirano odločanje.
4. **Kakovost modela:** Model, ki je pristranski, pogosto slabo posplošuje na celotno populacijo.

*Primer diskriminacije:* Algoritem za pomoč pri zaposlovanju, naučen na zgodovinskih podatkih podjetja, kjer so bili pretežno moški na vodilnih položajih, bi lahko samodejno "kaznoval" prijave žensk, ker so v preteklosti redkeje napredovale. Model bi tako ohranjal spolno neenakost.

---

### [2 točki] Kaj je razložljiva umetna inteligenca (XAI)?
**Vprašanje:**
Kaj pomeni kratica XAI (eXplainable Artificial Intelligence) oziroma **razložljiva umetna inteligenca**? Zakaj je to področje v zadnjih letih vse pomembnejše?

**Rešitev:**
Razložljiva umetna inteligenca (XAI) je področje, ki si prizadeva narediti odločitve in delovanje modelov umetne inteligence **razumljive in interpretabilne za ljudi**. Ukvarja se z metodami in tehnikami, ki pojasnjujejo, **zakaj** je model sprejel določeno odločitev.

**Pomembnost:**
1. **Zaupanje:** Uporabniki in strokovnjaki (npr. zdravniki, sodniki) bolj zaupajo sistemu, če razumejo njegovo odločitev.
2. **Odgovornost:** Omogoča preverjanje, ali model deluje pošteno in etično ter ali se morebitne napake lahko pripiše določenim vzrokom.
3. **Izboljševanje modelov:** Razumevanje, zakaj model dela napake, pomaga pri odkrivanju težav (npr. pristranskost, učenje napačnih vzorcev) in izboljšanju modela.
4. **Skladnost s predpisi:** Nekatere zakonodaje (npr. GDPR v EU) zahtevajo pravico do pojasnila o avtomatiziranem odločanju.

---

### [2 točki] Kakšna je razlika med nadzorovanim in nenadzorovanim učenjem?
**Vprašanje:**
Razložite ključno razliko med **nadzorovanim (supervised)** in **nenadzorovanim (unsupervised)** učenjem. Za vsako vrsto navedite po en primer algoritma in en konkreten problem, ki ga z njim rešujemo.

**Rešitev:**
Ključna razlika je v **prisotnosti oznak (labels)** v učnih podatkih.

- **Nadzorovano učenje:**
    - Učni podatki vsebujejo vhode in pripadajoče pravilne izhode (oznake).
    - Cilj je naučiti se preslikave iz vhodov v izhode, da lahko napovemo oznake za nove, nevidne podatke.
    - *Primer algoritmov:* Linearna regresija, odločitvena drevesa, podporni vektorji (SVM).
    - *Konkreten problem:* Napovedovanje cene stanovanja (regresija) ali klasifikacija e-pošte kot spam/ne-spam.

- **Nenadzorovano učenje:**
    - Učni podatki **nimajo oznak**. Model sam odkriva skrite strukture, vzorce ali skupine v podatkih.
    - Cilj je razumeti porazdelitev podatkov ali jih združiti v smiselne skupine.
    - *Primer algoritmov:* Metoda voditeljev (k-means), hierarhično grozdenje, analiza glavnih komponent (PCA).
    - *Konkreten problem:* Razdelitev strank v skupine glede na nakupovalne navade za trženje (grozdenje) ali zmanjšanje dimenzionalnosti podatkov za vizualizacijo.

---

### [2 točki] Kakšna je razlika med parametri in hiperparametri modela?
**Vprašanje:**
Razložite razliko med **parametri** in **hiperparametri** modela v strojnem učenju. Za vsakega navedite, kako se določita (nastavita) in po en konkreten primer.

**Rešitev:**
Razlika je v tem, ali se vrednost **nauči iz podatkov** med učenjem ali jo **nastavi uporabnik** pred začetkom učenja.

- **Parametri:**
    - So notranje spremenljivke modela, ki jih model **sam prilagaja med učenjem** na podlagi podatkov.
    - So ključni za napovedovanje; model brez njih ne more delovati.
    - *Primer:* Uteži (koeficienti) v linearni regresiji ali nevronskih mrežah. Te se med učenjem spreminjajo, da model čim bolje napove ciljno spremenljivko.

- **Hiperparametri:**
    - So nastavitve modela, ki jih **določi uporabnik vnaprej**, pred začetkom učenja.
    - Ne naučijo se iz podatkov, ampak jih moramo ročno nastaviti (npr. s prečnim preverjanjem), da dosežemo čim boljše delovanje.
    - Vplivajo na to, kako se model uči in kakšno strukturo ima.
    - *Primer:* Stopnja učenja (learning rate), število dreves v naključnem gozdu, globina odločitvenega drevesa, število skritih plasti v nevronski mreži, parameter k pri k najbližjih sosedih.

---

### [2 točki] Imamo 95 % accuracy, ampak zelo nizek recall za pozitiven razred. Kaj to pomeni v praksi?
**Vprašanje:**
Model za odkrivanje goljufij pri pisanju izpita (premiki miške, menjave zavihkov, čas reševanja) ima **natančnost (accuracy) 95 %**, vendar je **priklic (recall) za pozitivni razred (goljufije) zelo nizek**, npr. 10 %. Kaj to pomeni v praksi? Ali je model uporaben? Kakšne so posledice takega delovanja?

**Rešitev:**
Visoka natančnost ob zelo nizkem priklicu za pozitivni razred je tipičen znak **neuravnoteženih razredov** - negativni razred (brez goljufanja) močno prevladuje.

V praksi to pomeni, da model **dobro prepoznava negativne primere** (brez goljufanja), vendar **večine goljufij sploh ne odkrije**. Od vseh dejanskih goljufij jih najde le 10 %, 90 % goljufij pa spregleda!

**Ali je model uporaben?**
**Model ni uporaben**, kljub visoki natančnosti. Posledica bi bila, da bi večina goljufij ostala neodkrita.

**Kaj storiti?**
Potrebno je izbrati drugo metriko za optimizacijo (npr. mero F1) ali model prilagoditi, da bi izboljšali priklic, tudi za ceno nekoliko nižje natančnosti.

Lepo, da želite zbirko dopolniti še s konkretnimi vprašanji o velikih jezikovnih modelih (LLM). To so danes zelo aktualne teme. Tukaj so nova vprašanja v enakem formatu, z odgovori, pripravljenimi za vašo zbirko.

---

## 7. VELIKI JEZIKOVNI MODELI (LLM)

### [1 točka] Kaj so tokeni in zakaj so pomembni pri delu z LLM?
**Vprašanje:**
Kaj so **tokeni** v kontekstu velikih jezikovnih modelov (LLM)? Opišite, kako jih model uporablja in zakaj so pomembni za razumevanje stroškov in zmogljivosti modela.

**Rešitev:**
Tokeni so **osnovne enote besedila**, s katerimi delajo veliki jezikovni modeli. Preden model sploh začne obdelovati naše vprašanje, le-tega razdeli (proces imenujemo tokenizacija) na manjše kose - tokene. Ti niso niti črke niti vedno cele besede, ampak nekaj vmes - običajno deli besed (angl. *subwords*).

- **Kako izgledajo:** Kratke in pogoste besede so običajno en token - npr. beseda "voda" je en token. Daljše ali redkejše besede pa model razdeli na več delov. Slovenska beseda **"protidružbenost"** se bo zaradi svoje dolžine in sestavljenosti verjetno razbila na nekaj kosov, npr. ["proti", "druž", "ben", "ost"]. Presledki in ločila so prav tako svoji tokeni.

- **Pomen:** Tokeni so "valuta" sveta LLM.
    1.  **Cena:** Ponudniki storitev LLM zaračunavajo glede na število tokenov, ki jih pošljemo v model (vhod) in jih od njega dobimo nazaj (izhod).
    2.  **Zmogljivost:** Velikost t. i. "kontekstnega okna" modela je določena s številom tokenov, ki jih lahko obdela naenkrat.
    3.  **Jezikovne razlike:** Število tokenov na besedo se razlikuje. Angleščina porabi približno 1,3 do 1,5 tokena na besedo. Slovenščina je zaradi svojih zloženk in sklanjatev lahko nekoliko bolj "potratna" od angleščine (cca. 1,5 do 2.5).

---

### [2 točki] Kaj je velikost konteksta (context size)?
**Vprašanje:**
Kaj pomeni izraz **velikost konteksta (context size)** pri velikih jezikovnih modelih? Zakaj je ta podatek pomemben? Kaj se naredi, če uporabljamo zelo majhen ali zelo velik kontekst?

**Rešitev:**
Velikost konteksta (kontekstno okno) je **maksimalna količina besedila (v tokenih)**, ki jo model lahko upošteva, ko generira odgovor. To je njegov kratkoročni "delovni spomin" - če neka informacija ni znotraj tega okna, je model ne vidi.

- **Zakaj je pomembna:** Večje kontekstno okno pomeni, da lahko model obdeluje daljše dokumente, vodi kompleksnejše pogovore ali upošteva več navodil hkrati. Število tokenov, jih LLM zajame v kontekst, je 4096 do 1 milijon za novejše in zmogljivejše modele.

- **Izzivi velikega konteksta:**
    1.  **Računska zahtevnost:** Obdelava dolgih besedil je računsko zahtevnejša. Ko se kontekst podvoji, se potrebna računska moč poveča za štirikrat.
    2.  **Informacijski šum:** Če je v kontekstu preveč nepomembnih podatkov, ima model težave z iskanjem bistva. Raziskave kažejo, da so modeli najbolj pozorni na začetek in konec konteksta, sredino pa pogosto spregledajo (učinek primarnosti in recentnosti).
- **Strategije upravljanja:**
    - **RAG (Retrieval-Augmented Generation):** Namesto da bi v kontekst strpali celotno knjižico, najprej poiščemo le najbolj relevantne odlomke in jih podamo modelu.
    - **Povzemanje (Summarization):** Pri dolgotrajnih pogovorih lahko starejši del pogovora stnemo v kratek povzetek in ga dodamo v kontekst namesto celotne zgodovine.
    - **Čiščenje (Pruning):** Odstranjevanje manj pomembnih delov pogovora.

---

### [2 točki] Kaj je MCP in za kaj se uporablja?
**Vprašanje:**
Kaj je **MCP**? Opišite osnovno idejo. Navedite konkreten primer uporabe.

**Rešitev:**
MCP (Model Context Protocol) je odprt protokol, ki so ga leta 2024 predstavili v podjetju Anthropic. Njegov cilj je **standardizirati način povezovanja velikih jezikovnih modelov z zunanjimi podatki in orodji** (npr. datotekami, bazami podatkov, spletnimi storitvami).

**Težava pred MCP:** Pred MCP je vsaka povezava med modelom in zunanjim virom zahtevala svojo, unikatno programsko rešitev. Če ste želeli, da model dostopa do Google Drive, do baze podatkov in do platforme GitHub, ste morali za vsakega posebej napisati kodo.

**Rešitev MCP:** MCP uvaja skupen jezik za vse te povezave. Zato mu pravijo tudi **"USB-C za AI aplikacije"** - tako kot USB-C polni vse naprave prek istega vtičnika, MCP omogoča, da se različni AI modeli prek istega protokola povezujejo z različnimi viri podatkov.

**Arhitektura:**
- **Strežnik (Server):** Vsak zunanji vir (npr. GitHub, lokalni disk, baza podatkov) ima svoj strežnik MCP, ki "govori" ta skupni jezik.
- **Odjemalec (Client):** Je AI aplikacija (npr. Visual Studio Code), ki prek protokola MCP komunicira s strežniki in dostopa do njihovih podatkov.

**Konkreten primer uporabe:**
Recimo, da imamo v Visual Studio Code nameščen MCP za GitHub. V klepetalniku (ki je del urejevalnika) lahko modelu preprosto naročimo:
> *"Poglej odprte pull requeste v repozitoriju 'moj-projekt' in napiši povzetek sprememb."*

Model prek protokola MCP pokliče ustrezno orodje (v smislu metode API) na strežniku GitHub, ta pridobi podatke iz GitHub API in jih vrne modelu, ki nato sestavi odgovor. Vse to brez po meri napisane kode za povezavo z GitHub.

**Uporaba:** MCP se uporablja povsod, kjer želimo modelom omogočiti dostop do zunanjih virov - za branje lokalnih datotek, poizvedovanje po bazah podatkov, dostop do orodij za vodenje projektov (npr. Jira), pošiljanje e-pošte, brskanje po spletu ipd.
