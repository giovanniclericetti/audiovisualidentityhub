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
