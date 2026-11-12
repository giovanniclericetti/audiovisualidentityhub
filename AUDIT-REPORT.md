# Audiovisual Identity Hub — revisione del 12 novembre 2026

Intervento sulla copia locale del repository. Nessun deploy o push eseguito. Il rapporto del 28 ottobre, conservato più sotto, documenta interventi precedenti: i suoi risultati non vanno confusi con i test di questa revisione.

## A. Problemi individuati

| Problema verificato | Gravità | File |
| --- | --- | --- |
| Card delle fasce animate parzialmente fuori schermo quando ricevono il focus da tastiera | Alta | `js/site.js`, `css/interactions.css` |
| Refusi, concordanze e sintassi ancora da correggere | Media | Capitoli 1.2–1.6 e 3.4 |
| Didascalia e testo alternativo «Descrizione Video» privi di significato | Media | `documentazione/1.8.html` |
| Parola Netflix divisa da uno span ridondante, con colore inline | Bassa | `case-studies/10-personalizzazione-delle-thumbnail-netflix.html` |
| Due link Flopicco non più disponibili | Media | `documentazione/biblio.html`, `case-studies/3-lol.html` |
| Immagini grandi senza scelta di risoluzione per schermi piccoli | Media | Capitolo 1.1 e Disney+ |
| Il test responsive registrava overflow dei singoli elementi senza far fallire il controllo; risposte HTTP errate non controllate | Media | `scripts/check_browser.py` |
| Lo script screenshot modificava l’asset social del sito durante l’audit | Media | `scripts/capture_screenshots.py` |
| Contrasto dei colori originali insufficiente in più componenti | Alta, aperta | CSS condivisi |

## B. Modifiche effettuate

### Contenuti

Corretti errori certi, fra cui «accompagne», «le si riprende», «con gli insegnanti si rivolgevano», «formazione li», «tutt’ora», «alla esigenze», «rappresentative», «acquisto Italia 1», «altre emittente», «Il Individual Brand», «Striscia la Notiza», «elemento principali». Sistemate la parentesi di La5 e la concordanza del passaggio sulle reti locali. Nessuna riscrittura di capitoli o modifica delle date storiche.

Nel capitolo 1.8, dopo aver osservato l’immagine, il placeholder è stato sostituito con «Composizione grafica dei bumper di Rai Storia», sia nella didascalia sia nell’alt. Nella scheda Netflix è stato eliminato lo span che spezzava la parola: non si trattava di uno spazio effettivamente visibile, ma di frammentazione del testo nel markup.

Verificate le correzioni già presenti: email ufficiale e mailto, Pajè 2024 nel passaggio richiesto, Disney+ 2024, Casi Studio, TV e Video Identity nei testi editoriali, IDENTITÀ, copyright 2025. Le varianti presenti nei titoli bibliografici e nelle citazioni letterali sono preservate. I crediti di Rai Yoyo restano completi.

Recuperati e verificati con risposta GET 200:

- Portfolio: [Flopicco — Our Work](https://flopicco.com/our-work/).
- Progetto LOL: [Flopicco — Chi ride è fuori Toolkit](https://flopicco.com/chi-ride-e-fuori/).

La cronologia Disney+ già corretta è confermata dal [comunicato Disney del 27 marzo 2024](https://press.disneyplus.com/hulu-on-disney-plus-launches-today-in-the-us-for-bundle-subscribers), che associa il lancio di Hulu negli Stati Uniti all’aggiornamento del marchio.

### Interazioni e manutenzione

Durante il focus le fasce di card diventano righe stabili e scorribili, il collegamento attivo viene portato in vista e lo scorrimento viene azzerato all’uscita. Il comportamento animato ordinario resta invariato. Aggiunto un focus esplicito al controllo dell’indice. Nessuna modifica a palette, famiglie tipografiche, categorie, classificazioni o composizione ordinaria.

Aggiornati i parametri di versione di `site.js` e `interactions.css` negli HTML, per evitare che una futura pubblicazione usi copie in cache. Menu, footer, indice e paginazione condivisi risultano sincronizzati: non era necessario ricostruirli.

I test ora rilevano come errori anche overflow dei singoli elementi, H1 inattesi e caricamenti locali falliti. Il controllo statico verifica anche srcset, canonical, metadati social, email e titoli duplicati. La cattura degli screenshot scrive soltanto nell’archivio di verifica.

### Media

Aggiunte quattro varianti WebP a 640/960 px per due immagini, mantenendo gli originali nel srcset come risoluzione massima e nel src come fallback. Compressione senza perdita rispetto ai pixel ridimensionati con Lanczos, verificata tramite confronto pixel; il ridimensionamento non è equivalente alla conservazione di ogni dettaglio dell’originale.

| Immagine | Originale | 640 px | 960 px |
| --- | ---: | ---: | ---: |
| Famiglia con televisore, capitolo 1.1 | 538.932 B | 186.386 B | 390.284 B |
| Catalogo Disney+ | 472.212 B | 131.994 B | 271.294 B |

Il `sizes` di Disney+ tiene conto dell’ingrandimento necessario per il ritaglio originale: alle larghezze mobile testate con DPR 1 viene scelta la variante 960, da tablet in su l’originale. Non sono stati modificati crop, immagini originali, video o font.

## C. Test della revisione corrente

- **Responsive:** 38 pagine × 9 larghezze (320, 375, 390, 430, 768, 1024, 1280, 1440, 1920) = **342 scenari superati**. Nessun overflow pagina/elemento, immagine locale rotta, H1 inatteso, errore JavaScript o caricamento locale fallito. Verifica aggiuntiva di Disney+ alle nove larghezze dopo l’adeguamento del srcset.
- **Interazioni:** **14 gruppi superati**, inclusi menu, Escape, click esterno, uscita del focus, cambio breakpoint, touch, precedente/successivo, 15 card archivio, mailto, movimento ridotto, assenza JavaScript e visibilità delle card al focus.
- **Accessibilità automatica:** axe-core su **76 combinazioni** (38 pagine a 390 e 1440 px). Restano violazioni `color-contrast` in tutte le combinazioni. Nessun’altra regola violata rilevata dalla configurazione WCAG A/AA adottata; non è una certificazione completa.
- **HTML:** 40 file passano HTML Validate con la configurazione adottata. Escluse regole stilistiche `void-style`, `no-inline-style`, `attr-quotes`, `doctype-style`, `no-trailing-whitespace`, `long-title`, `prefer-native-element`, `wcag/h32`.
- **Statici:** percorsi, anchor, ID, alt/dimensioni immagini, srcset, email, metadati e titoli passano. `sync_shared.py --check`, `node --check` per entrambi gli script e `git diff --check` passano. Nessun riferimento runtime a Framer trovato negli HTML/CSS/JS.
- **Integrità:** confronto con HEAD su 40 HTML: testi dei blockquote, URL degli iframe e paragrafi contenenti Farnsworth/Giorgio VI invariati.
- **Screenshot:** 114 schermate a pagina intera prima e dopo (38 × 3 viewport), più 18 catture di sezioni per fase. Confronto automatizzato delle 132 coppie; 90 identiche pixel per pixel. Le differenze includono correzioni testuali, immagini responsive e variazioni di rasterizzazione. Le quattro variazioni di altezza riguardano righe dei capitoli 1.2/1.6 e della bibliografia. Revisione visiva di panoramiche e dettagli rappresentativi desktop/tablet/mobile; nessun redesign o sovrapposizione osservato nei campioni.
- **Link esterni:** 106 URL controllati via HEAD: 83 risposte 200, 8 risposte 403, 6 risposte 404, 6 risposte 401, 2 risposte 405, 1 risposta 503. Due dei sei 404 sono stati sostituiti con URL Flopicco verificati anche via GET. I quattro 404 rimasti sono elencati sotto. 401/403/405 non dimostrano indisponibilità per gli utenti.
- **Sito pubblico:** `index.html` risponde HTTP 200 da Vercel. Questo non verifica una pubblicazione delle modifiche locali, che non è stata eseguita.

### Lighthouse mobile locale

Sei esecuzioni sequenziali su Chrome, throttling simulato, server HTTP Python locale, player YouTube/Vimeo esclusi. Disney+ rimisurato dopo il srcset finale. Valori di laboratorio; nessun confronto quantitativo controllato prima/dopo con l’audit di ottobre.

| Pagina | Performance | Accessibilità | Best practices | SEO | LCP | CLS | TBT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Home | 91 | 95 | 100 | 100 | 3.46 s | 0.00000 | 0 ms |
| About | 92 | 96 | 100 | 100 | 3.15 s | 0.00339 | 0 ms |
| Capitolo 1.1 | 79 | 95 | 100 | 100 | 5.25 s | 0.00000 | 0 ms |
| Bibliografia | 92 | 95 | 100 | 100 | 3.01 s | 0.00025 | 0 ms |
| Archivio Casi Studio | 92 | 95 | 100 | 100 | 3.08 s | 0.00000 | 0 ms |
| Disney+ | 79 | 96 | 96 | 100 | 5.56 s | 0.00000 | 0 ms |

**INP non misurato.** TBT non lo sostituisce. Gli esiti grezzi, le immagini e i confronti sono in `verification/audit/`, esclusa dalla pubblicazione.

## D. Problemi ancora aperti

1. **Contrasto.** L’azzurro originale su bianco misura circa 2,97:1; alcune etichette, pulsanti e testi secondari non raggiungono le soglie AA. Il vincolo esplicito sui colori è stato rispettato; non è possibile dichiarare piena conformità.
2. **Movimento.** Restano fasce automatiche senza comando persistente di pausa. Il precedente rapporto documenta la rimozione richiesta dei pulsanti; sono mantenuti movimento ridotto e pausa al focus, che non equivalgono da soli a soddisfare ogni requisito WCAG sulla pausa.
3. **Fonti incomplete e attribuzioni.** Restano le pagine mancanti di Grasso (1996), fonti generiche e discrepanze elencate nell’audit storico. Nuova evidenza: lo stesso passaggio sull’intelligenza artificiale compare attribuito a Tolino nel capitolo 1.8 e a Pajè nel 2.1; serve confronto con le interviste originali. Nel capitolo 1.2 l’attribuzione «Colombo, 1953» va riconciliata con il racconto del 3 gennaio 1954. Citazioni e attribuzioni non sono state alterate.
4. **Quattro link 404 residui:** intervista Motiongraphics/Pajè; Channel 4 Idents 2023 su 4Creative; TG1 16/02/2025 su RaiPlay; articolo Panorama Audiovisual sulla Kings League. Per quest’ultimo le versioni spagnola e inglese sono ancora indicizzate, ma anche quelle restituiscono 404 via GET: conservato il riferimento originale, senza dichiararlo riparato. Amazon/RaiPlay ha restituito 503 e richiede controllo manuale.
5. **Cronologie storiche.** Restano i casi già segnalati nell’audit precedente. Per LOL, la pagina dello studio recuperata conferma il 2021; il passaggio «2001» è segnalato per la revisione accademica, senza modificare autonomamente la cronologia richiesta come protetta da verifica editoriale.
6. **Categorie.** Sono etichette tassonomiche, non controlli di filtro implementati. Non è stata inventata una corrispondenza fra categorie e schede.
7. **Limiti dei test.** Non eseguiti screen reader manuale completo, dispositivi fisici, Safari/Firefox, riproduzione e sottotitoli dei player, dati sul campo di INP/LCP, nuova pubblicazione e verifica di tutti i redirect della produzione. I test browser bloccano le richieste esterne per isolare il sito.

## E. Stato finale

| Area | Stato |
| --- | --- |
| Build/codice | Statico, nessuna build necessaria; sintassi e controlli adottati superati |
| Responsive | 342 scenari Chrome superati; confronto visivo eseguito |
| Navigazione | Menu e paginazione verificati; corretto focus nelle fasce |
| Performance | Media responsive aggiunti; LCP ancora da migliorare, INP non misurato |
| Accessibilità | Problema di focus risolto; contrasto e pausa persistente restano aperti |
| SEO | Metadati/canonical/sitemap verificati; Lighthouse SEO 100 nei sei campioni |
| Pubblicazione | Modifiche locali, produzione non aggiornata |

---

# Archivio: audit del 28 ottobre 2026

# Audiovisual Identity Hub — rapporto di audit

Data: 28 ottobre 2026. Modifiche applicate alla copia locale; nessun aggiornamento della produzione eseguito in questo intervento. Anteprima: http://localhost:8000.

## Aggiornamento successivo richiesto

Rimossi i pulsanti «Pausa scorrimento» da home e About su richiesta. Rimangono il rispetto del movimento ridotto e la pausa al focus. Le box Company, Design e Branding hanno ora fondi rispettivamente `#ffffff`, `#f5fbfe` e `#e8f5fc`; titoli ed etichette usano nuovamente l’azzurro originale `#009fe3`, come richiesto nel successivo aggiornamento. La selezione del testo ha fondo `#009fe3` e testo bianco. Le misure di audit sotto descrivono la versione precedente a questo aggiornamento; il test delle interazioni è stato adeguato.

## A. Problemi individuati

| Problema | Gravità | File interessati |
| --- | --- | --- |
| Navigazione, indice, contenuti About e parti del footer nascosti su mobile; gestione del menu incompleta | Alta | `css/site.css`, `css/pages.css`, `js/site.js`, HTML delle sezioni |
| Indici duplicati e non uniformi, capitolo 3.5 assente dalla bibliografia, collegamento finale incompleto | Media | `documentazione/*.html` |
| Email incoerenti, CTA contributi diretta alla documentazione, refusi e nomenclatura non uniforme | Media | `index.html`, `about.html`, `documentazione/*.html`, `case-studies/*.html` |
| Anno Disney+ incoerente e placeholder bibliografico | Media | `case-studies/12-disney.html`, `documentazione/biblio.html` |
| Immagini pesanti, dimensioni mancanti, caricamenti superflui e spostamento iniziale del menu | Alta | HTML, `css/site.css`, risorse multimediali |
| Semantica delle liste e delle citazioni, link non distinguibili, animazioni senza controllo di pausa | Media | HTML, CSS, `js/site.js` |
| Contrasto insufficiente in alcune combinazioni della palette originale | Alta, aperta | CSS condivisi: azzurro, etichette e alcuni testi secondari |
| Metadati incompleti o generici, sitemap e pagina 404 mancanti | Media | HTML, configurazione di pubblicazione |
| Collegamenti esterni obsoleti e riferimenti accademici incompleti | Media, parzialmente aperta | Bibliografia, documentazione e crediti |

## B. Modifiche effettuate

### Contenuti e fonti

- Uniformati indirizzo visibile e link `mailto:` a **audiovisualidentityhub@gmail.com**. La CTA contributi di About apre ora una mail al progetto.
- Applicate le convenzioni **Casi Studio**, **TV**, **Video Identity**, **IDENTITÀ**, rispettando titoli bibliografici e citazioni letterali. Copyright fissato a **© 2025**.
- Corretta a **2024** l'attribuzione della citazione contemporanea di Mirko Pajè in «Definire la videografica» e la relativa introduzione. Conservati gli altri riferimenti al volume del 2004.
- Corretti refusi, accenti, concordanze, didascalie, spaziature e frasi chiaramente difettose; allineati i titoli dei capitoli all'indice. Eliminata una ripetizione esatta di paragrafo nei capitoli 1.8 e 2.3, mantenendo integralmente una copia del testo.
- Verificata la conservazione delle citazioni e dei paragrafi storici protetti su Giorgio VI e Farnsworth.
- Disney+: anno 2024, didascalia corretta e distinzione fra aggiornamento del marchio e lancio di Hulu su Disney+ negli Stati Uniti. Fonti primarie: [Disney+ Logo 2024](https://press.disneyplus.com/about/disney-plus-logo-2024) e [comunicato del 27 marzo 2024](https://press.disneyplus.com/hulu-on-disney-plus-launches-today-in-the-us-for-bundle-subscribers). Immagini e URL dei player conservati.
- Conservati i crediti di Rai Yoyo, inclusi Roberto Bagatti e Marco Salemi. Corretta la descrizione non pertinente della scheda sulle thumbnail Netflix.
- Rimossi `pp. xx-xx` e irregolarità di formattazione in bibliografia, senza inventare pagine. Sostituiti due collegamenti obsoleti con [Netflix Brand](https://brand.netflix.com/en/) e [Rai Brand System di Flopicco](https://vimeo.com/226272277).

### Navigazione e manutenzione

`data/navigation.json`, `templates/footer.html` e `scripts/sync_shared.py` centralizzano menu, capitoli, email e footer. Il generatore aggiorna gli HTML statici, i collegamenti precedente/successivo e la sitemap; `--check` rileva divergenze. Non occorre JavaScript per leggere la navigazione e non è stato introdotto un framework.

L'indice comprende tutti i capitoli, incluso «Scenari evolutivi e innovazione», e la bibliografia. Menu e stato attivo sono coerenti. Gestiti mouse, touch, tastiera, Escape, click esterno, uscita del focus e cambi di breakpoint.

L'archivio mantiene tutte le 15 schede e le categorie esistenti. Le etichette originali erano elementi di testo, senza logica di filtro né associazioni complete fra categorie e schede: non è stata inventata una classificazione. È stato rimosso l'invito fuorviante a utilizzare filtri inesistenti.

### Layout e accessibilità

- Ripristinati su mobile contenuti, indice, metadati, collegamenti e footer precedentemente nascosti.
- Sistemati wrapping, griglie, titoli lunghi, email, margini e spaziature tramite valori condivisi; migliorati interlinea e didascalie.
- Conservati colori, famiglie tipografiche, immagini, proporzioni e direzione artistica. Nessun redesign.
- Aggiunti controlli pausa/riprendi alle fasce animate e supporto coerente a `prefers-reduced-motion`.
- Corretti liste annidate, figure e didascalie, testi alternativi, titoli dei player, skip link, focus e aree di attivazione del menu/footer.
- Separato il fallback senza JavaScript in `css/no-script.css`: eliminato lo spostamento iniziale causato dalla comparsa temporanea della navigazione.

### Media, font e SEO

22 immagini PNG grandi hanno copie WebP senza perdita, verificate confrontando i pixel decodificati: da 40.905.393 a 32.099.038 byte, circa **8,8 MB risparmiati (21,5%)** sui file a piena risoluzione. Varianti responsive per 21 sorgenti riducono ulteriormente il trasferimento sui piccoli schermi. Gli originali sono conservati e la risoluzione completa rimane disponibile.

Aggiunti caricamento differito, dimensioni esplicite, priorità per le immagini iniziali e una vera immagine responsive per la sezione ricerca mobile. Quattro sottoinsiemi dei font originali riducono complessivamente i file da 208.964 a 161.816 byte; verificata l'identità delle larghezze dei glifi. I font completi restano come fallback.

Ogni pagina di contenuto dispone di titolo e descrizione dedicati, canonical, metadati Open Graph e Twitter. Aggiunti anteprima social, favicon, `robots.txt`, sitemap con 37 URL e `404.html`. La vecchia variante dell'URL Camera Café è esclusa dall'indicizzazione. `vercel.json` contiene i redirect pertinenti; la loro esecuzione effettiva su Vercel richiede una pubblicazione.

Aggiornati README, esclusioni dalla pubblicazione e script opzionali di verifica. Nessuna dipendenza runtime aggiunta. Le risorse originali non sono state eliminate perché costituiscono le sorgenti dell'archivio.

## C. Test eseguiti

Gli esiti locali sono in `verification/audit/`, esclusa da Git e dalla pubblicazione.

| Verifica | Esito e limiti |
| --- | --- |
| Playwright responsive | **342 combinazioni**: 38 pagine × 320, 375, 390, 430, 768, 1024, 1280, 1440 e 1920 px. Nessun overflow orizzontale rilevato, immagine locale rotta o errore JavaScript della pagina. |
| Interazioni | **13 gruppi superati**: menu su sei tipi di pagina, tastiera, touch, focus, navigazione capitoli, CTA email, 15 schede a ogni numero di colonne, pausa/riprendi, movimento ridotto e navigazione senza JavaScript. |
| axe-core | **76 controlli pagina/viewport**, 38 pagine a 390 e 1440 px. Risolte le violazioni strutturali rilevate; rimane la regola `color-contrast`. Non equivale a certificazione WCAG. |
| HTML | 40 file verificati con HTML Validate; nessun errore nella configurazione adottata. Escluse regole stilistiche e preferenze non pertinenti: void-style, no-inline-style, attr-quotes, doctype-style, no-trailing-whitespace, long-title, prefer-native-element e wcag/h32. |
| Controlli statici | Nessun problema rilevato su percorsi interni, anchor, ID duplicati, H1, titoli e attributi delle immagini. |
| Integrità contenuti | Citazioni, URL dei player e paragrafi storici protetti confrontati con la versione iniziale; nessuna alterazione rilevata. |
| Immagini e font | Confronto pixel delle 22 conversioni senza perdita; confronto delle metriche dei glifi per i quattro font ridotti. |
| Screenshot | 24 iniziali; 114 finali a pagina intera (38 × mobile/tablet/desktop), 18 catture intermedie/finali di pagine lunghe e campioni dopo l'ottimizzazione dei font. Revisione visiva tramite panoramiche e catture mirate. |
| Codice e generazione | `node --check` per gli script JS, `git diff --check` e `python3 scripts/sync_shared.py --check` superati. Nessuna build prevista per questo sito statico. |
| Font finali | Campioni visivi e Lighthouse ripetuti dopo il sottoinsieme dei font; la matrice responsive completa precede questo ultimo intervento, per il quale sono state verificate le metriche invariate. |

### Lighthouse mobile finale

Chrome locale, throttling mobile simulato, server Python HTTP locale. Player di terze parti esclusi dalle misure. I risultati sono di laboratorio e possono variare; non rappresentano misure sul sito pubblico.

| Pagina | Performance | Accessibilità | Best practices | SEO | LCP | CLS | TBT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Home | 92 | 95 | 100 | 100 | 3,30 s | 0 | 1 ms |
| About | 93 | 96 | 100 | 100 | 3,08 s | 0,00026 | 0 ms |
| Capitolo 1.1 | 79 | 95 | 100 | 100 | 5,48 s | 0 | 0 ms |
| Bibliografia | 95 | 95 | 100 | 100 | 2,71 s | 0,00011 | 0 ms |
| Archivio Casi Studio | 92 | 95 | 100 | 100 | 3,23 s | 0 | 0 ms |
| Disney+ | 79 | 96 | 96 | 100 | 5,41 s | 0 | 0 ms |

Il CLS della home è passato da circa 0,30 nella prima misura diagnostica a 0. LCP resta migliorabile, soprattutto nelle pagine con immagini grandi. **INP non misurato**: richiede dati reali di interazione; TBT non è un suo sostituto. Compressione, cache e comportamento della CDN non sono verificabili tramite il server locale.

Sono stati controllati 106 URL esterni. Due collegamenti sono stati corretti con destinazioni primarie verificate. Errori 401/403 e restrizioni automatiche dei provider non dimostrano che una pagina sia indisponibile nel browser dell'utente.

Non eseguiti: certificazione manuale completa con screen reader, prove su dispositivi fisici/Safari/Firefox, verifica integrale di riproduzione e sottotitoli dei player esterni, verifica dei redirect e degli header su una nuova pubblicazione. I test Playwright escludono le richieste ai player per isolare il layout del sito.

## D. Problemi ancora aperti

1. **Contrasto e vincolo sui colori.** L'azzurro originale `#009fe3` su bianco misura circa 2,97:1; alcune etichette su fondi chiari circa 2,65:1. Anche alcuni testi secondari non raggiungono la soglia richiesta. Non ho cambiato la palette espressamente protetta. Per dichiarare conformità AA serve una decisione sul colore dei testi/sfondi o sulla loro presentazione; l'audit attuale non è completamente superato.
2. **Bibliografia.** Per Grasso (1996), «Sigle tv», in *Enciclopedia della televisione*, mancano i numeri di pagina: eliminato soltanto il placeholder. Alcuni riferimenti generici (fra cui Fazio/Repubblica e Grasso/RaiPlay) richiedono una risorsa precisa. Il riferimento Farnsworth attribuito all'Università dello Utah rimanda a Britannica. Restano da riconciliare anno e opera nei richiami Davis (2024/2015), Morabito (2018/2023) e nei diversi riferimenti Pajè; alcune interviste e attribuzioni, fra cui Chinese, Tolino e Nielsen, richiedono dati completi. Non sono stati inventati dati bibliografici.
3. **Fonti esterne.** Restano risposte 404 per il vecchio articolo Motiongraphics su Pajè, la pagina 4creative 2023 e il collegamento RaiPlay TG1 di febbraio 2025. Rai Teche ha restituito 500. Diversi provider hanno risposto 401/403. Conservati i riferimenti senza sostituirli con fonti non equivalenti; occorre recuperare gli originali o identificare copie autorevoli.
4. **Informazioni storiche/cronologiche da verificare.** Fra i passaggi rilevati: «Carosello 1957–1877», LOL/Prime Video «2001», Prime Video Italia «2011», Warner TV trattato insieme alle piattaforme streaming e YouTube «2004» rispetto al 2005 citato altrove. Anche alcune date dei Casi Studio sembrano riferirsi all'origine del marchio anziché al progetto analizzato (Netflix, Rai Storia, Camera Café, Che tempo che fa, Kings League). Non modificate perché richiedono verifica editoriale e accademica. I paragrafi su Giorgio VI e Farnsworth rimangono invariati come richiesto.
5. **Filtri.** Non esisteva una funzionalità di filtro da riparare. Implementarne una richiederebbe definire associazioni attendibili tra le categorie conservate e ogni scheda, oltre al comportamento di selezione; nessuna classificazione è stata inventata.
6. **Prestazioni e media esterni.** LCP ancora superiore a 2,5 s nei campioni mobile simulati; mantenuta la qualità dell'archivio. Da misurare sulla distribuzione reale, insieme a INP, riproduzione dei video e disponibilità dei sottotitoli.

## E. Stato finale

- **Build:** sito statico pronto alla preview; controlli di sintassi, HTML e generazione superati. Nessun framework introdotto.
- **Responsive:** matrice richiesta superata in Chrome; contenuti mobile ripristinati e schermate controllate.
- **Navigazione:** link interni e interazioni verificate; indici/footer centralizzati, navigazione senza JavaScript disponibile.
- **Performance:** risorse alleggerite senza perdita sulle conversioni originali, caricamento responsive e CLS corretto; LCP e dati reali restano da migliorare/verificare.
- **Accessibilità:** semantica e comandi migliorati; contrasto ancora non conforme in alcuni elementi. Nessuna dichiarazione di piena conformità WCAG.
- **SEO:** 100/100 nei sei campioni Lighthouse, metadati e sitemap presenti. Indicizzazione e redirect di hosting da verificare dopo pubblicazione.
- **Pubblicazione:** modifiche disponibili localmente su http://localhost:8000; produzione non aggiornata in questo intervento.

## Revisione mobile successiva

Rivisto il layout fino a 767 px con `css/mobile.css`: menu senza simbolo + (Menu/Chiudi), titoli e CTA centrati, ritorni a capo naturali, pannelli e gradienti coerenti con il desktop, padding ripristinato nelle categorie e footer centrato. La home segue ora anche su mobile l’ordine desktop: introduzione, ricerca, Casi Studio, elaborato. I testi lunghi della documentazione e dei casi restano allineati a sinistra.

Acquisite schermate prima/dopo per sei tipi di pagina a 390 px e controllate schermate mirate a 320 px. Ripetuti con esito positivo 342 scenari responsive (320–1920 px), 13 gruppi di interazioni, controlli statici, sintassi JavaScript e sincronizzazione dei contenuti condivisi. Nessun overflow rilevato a livello di pagina o singolo elemento. I dati Lighthouse precedenti non sono stati rimisurati per questa revisione.
