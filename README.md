# Audiovisual Identity Hub

Sito statico indipendente in HTML, CSS e JavaScript. Font, loghi e immagini sono salvati nella cartella `assets/`; non occorrono build, framework o servizi di hosting specifici.

## Preview locale

Dalla cartella del progetto:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Aprire http://localhost:8000. Dopo aver salvato una modifica, aggiornare la pagina.

## Struttura

- `index.html`: homepage con fasce animate, introduzione, ricerca, elaborato e casi studio.
- `about.html`: progetto e contributi.
- `documentazione/`: capitoli della ricerca e bibliografia.
- `case-studies/`: archivio e schede dei casi studio.
- `css/site.css`: font, navigazione, homepage e componenti comuni.
- `css/pages.css`: layout delle pagine interne.
- `css/mobile.css`: adattamento fino a 767 px, caricato per ultimo per mantenere coerenti centrature, superfici e spaziature con il desktop.
- `js/site.js`: menu mobile, fasce a ciclo continuo, immagini della ricerca e colonne responsive dell’archivio.
- `assets/`: risorse originali locali.

I video incorporati nelle schede utilizzano i player YouTube originali e richiedono una connessione. I collegamenti email aprono il programma di posta. La ricostruzione conserva contenuti e risorse del riferimento; la corrispondenza visiva su ogni viewport va verificata prima della pubblicazione.

Le fasce dei marchi e dei casi studio scorrono in modo continuo anche al passaggio del mouse. Si fermano per la navigazione da tastiera e rispettano la preferenza di sistema per il movimento ridotto. Il footer condiviso include logo e tre pulsanti; About include le immagini e i collegamenti delle due sezioni finali.

## Pubblicazione

Sito statico predisposto per Vercel, senza comando di build. Il repository GitHub conserva i sorgenti; la cartella `verification/` contiene verifiche locali e non viene pubblicata.

Sito pubblico: https://audiovisualidentityhub.vercel.app
Repository pubblico: https://github.com/giovanniclericetti/audiovisualidentityhub

La prima pubblicazione è stata eseguita direttamente dalla cartella locale. Il collegamento automatico tra GitHub e Vercel non è attivo: la prima pubblicazione è avvenuta tramite CLI. Per aggiornare la produzione dalla cartella del progetto:

```sh
vercel deploy --prod --scope team_L01cREHuCUQ967VesGEAGq7G
```

## Contenuti condivisi e verifiche

Menu, indirizzo email, anno del copyright e capitoli sono definiti in `data/navigation.json`; il footer è in `templates/footer.html`. Dopo aver modificato questi file, eseguire:

```sh
python3 scripts/sync_shared.py
python3 scripts/sync_shared.py --check
```

Il comando aggiorna gli HTML statici e `sitemap.xml`. Il sito resta utilizzabile senza JavaScript e non richiede una build. Il copyright rimane fissato al 2025.

Per ripetere gli audit locali, con il server della preview attivo sulla porta 8000:

```sh
python3 -m venv /tmp/aih-audit-env
/tmp/aih-audit-env/bin/pip install -r scripts/requirements-audit.txt
/tmp/aih-audit-env/bin/python scripts/check_static.py
/tmp/aih-audit-env/bin/python scripts/check_browser.py
/tmp/aih-audit-env/bin/python scripts/check_interactions.py
/tmp/aih-audit-env/bin/python scripts/capture_screenshots.py after
```

I test browser utilizzano Google Chrome tramite Playwright; `AIH_BROWSER_CHANNEL` permette di scegliere un altro canale installato. I player esterni vengono esclusi dai test di layout. Per axe-core, impostare `AIH_AXE_SCRIPT` sul percorso locale di `axe.min.js` ed eseguire `scripts/check_accessibility.py`.

Gli esiti e gli screenshot sono salvati in `verification/audit/`, esclusa da Git e dalla pubblicazione. Le immagini originali sono conservate in `assets/media/`; `assets/optimized/` contiene le copie WebP senza perdita e le varianti responsive. Non cancellare gli originali: restano le sorgenti dell’archivio visivo.

`AUDIT-REPORT.md` descrive le correzioni, le misurazioni e i punti editoriali o di accessibilità ancora aperti. Le etichette Company/Design/Branding descrivono la tassonomia: non sono controlli di filtro.
