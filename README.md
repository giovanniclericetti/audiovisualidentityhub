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
