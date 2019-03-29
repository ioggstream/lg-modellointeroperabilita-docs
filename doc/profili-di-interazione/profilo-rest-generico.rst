
# Modalità di interazione, profili, casi d`uso e tecnologie

Il terzo documento del Modello di Interoperabilità 2018, così come introdotto
nella Visione generale, fornisce indicazioni concrete, a livello tecnico, su differenti
modalità operative per realizzare l'interoperabilità, tenendo conto delle possibili tecnologie ed
approcci disponibili.

Questa versione si focalizza prevalentemente sulle modalità sincrone ed asincrone
 (basate su scambio di messaggi) e sulle tecnologie basate su SOAP e REST.





## 2 MEP - Message Exchange Patterns

Una possibile classificazione delle interfacce di servizio è basata sullo
stile di interazione

richiesto dalle diverse operazioni disponibili: sincrono o asincrono. Nelle
operazioni

sincrone, un client esprime la sua richiesta nella forma di una chiamata ed
attende una

risposta prima di continuare l'esecuzione. Nelle operazioni asincrone, invece,
il client invia

un documento/messaggio ma non si aspetta nessuna risposta (se non il fatto che
la

richiesta è stata presa in carico). La risposta da parte dell'interfaccia di
servizio, nei casi in

cui ci sia, può apparire ore o anche giorni più tardi.

Si noti come i MEP vengano definiti a prescindere dalla specifica tecnologia
utilizzata per

la realizzazione.

## 2.1 Sincrono

Nell'interazione sincrona, la richiesta del cliente viene immediatamente
soddisfatta ed il

risultato dell'elaborazione fornito come risposta. Il caso più comune di
interazione

sincrona è la cosiddetta Remote Procedure Call - RPC (chiamata remota a
procedura) in

cui il client richiede l'esecuzione di una qualche operazione, la cui
complessità può variare.

A scopo esemplificativo, il calcolo del codice fiscale può essere effettuato
da una

interfaccia di servizio nella forma di una RPC.



Un altro classico esempio di interazione sincrona è quello in cui si ha un
accesso di tipo

CRUD (Create, Read, Update, Delete) su determinati oggetti di interesse. Si
tratta in

questo caso di operazioni di accesso ad oggetti informativi, dove la logica
applicativa è

solitamente molto semplice. A scopo esemplificativo, si può considerare il
caso in cui un

fruitore debba accedere alle informazioni anagrafiche di un persona fisica o
giuridica.



La differenza tra RPC ed accesso CRUD è essenzialmente quindi nello scopo
della

chiamata. Sebbene, in qualche misura, si possa considerare l'accesso CRUD un
caso

particolare di RPC, negli accessi CRUD il focus è sulla manipolazione di uno
specifico dato,

mentre nel caso più generico di RPC, l'interfaccia di servizio può richiedere
l'applicazione di

logiche applicative più complesse. Il caso di invio di documenti può essere
esemplificativo

di questa differenza. Un documento può essere inviato per la sua semplice

memorizzazione o aggiornamento, oppure può essere uno degli input per
l'espletamento

di una procedura più sofisticata.

3

leggere da interfacce di servizio apposite. Una variante di questa modalità
richiede il

mantenimento di una connessione attiva (es. websocket).





# 3 Profili

Il termine ​profilo​, in questo documento, viene utilizzato per fissare alcune
caratteristiche,

indipendentemente dal MEP, al fine di semplificare l'interoperabilità,
imponendo

determinate linee guida che ne vincolano l'applicazione. Questa sezione va a
dettagliare,

per ognuna delle tecnologie preminenti nell'ambito dell'interoperabilità, i
profili da

utilizzare.



Le interfacce di servizio permettono di accedere - interagendo via software -
ad

informazioni e servizi offerti dalle PA, e a diverse PA di interagire. Il
presente capitolo è

organizzato in schede relative alle differenti tecnologie. In particolare, per
quanto riguarda

le sezioni relative a REST e SOAP, alcuni concetti comuni vengono replicati al
fine di

massimizzare l'auto-contenimento delle sezioni.

## 3.1 REST

In questa sezione si raccolgono le linee guida per il ModI valide come best-
practice ai fini

dell'interoperabilità.

### 3.1.1. Formato dei dati

Tranne ove previsto da standard e specifiche settoriali, in REST la
comunicazione deve

avvenire tramite oggetti JSON ​[RFC 7159​](http://www.rfc-
editor.org/rfc/rfc7159.txt) con il relativo ​[media-
type​](https://www.iana.org/assignments/media-types/media-types.xhtml)
`application/json`.

Specifiche settoriali (es. INSPIRE, HL7) devono essere rispettate anche
laddove queste

siano parzialmente in conflitto con il profilo qui specificato, eg:

 - per​ HL7 si veda FHIR ​[https://www.hl7.org/fhir/](https://www.hl7.org/fhir/)

 - per​ xBLR si veda XBLR-json ​[https://www.xbrl.org/xbrl-json-making-xbrl-
easier/](https://www.xbrl.org/xbrl-json-making-xbrl-easier/)



Codificare dati strutturati con oggetti JSON

I dati strutturati devono essere trasferiti tramite ​oggetti JSON​
​[RFC-7159​](https://tools.ietf.org/html/rfc7159), in modo da

permettere l'estensione retrocompatibile della response con ulteriori
attributi (Eg.

paginazione). Cioè:

  - il payload di una response contenente una entry ritorna un oggetto

{ "given_name": "Paolo", "last_name": "Rossi", "id": 313 }

  - il payload di una response contenente più entry ​ritorna un oggetto
contenente

una lista​ e non direttamente una lista.

```
{ "items": [

{ "given_name": "Carlo", "family_name": "Bianchi", "id": 314 },

{ "given_name": "Giuseppe", "family_name": "Verdi", "id": 315 }

]

}

```

Evitare Content-Type personalizzati

Evitare l'uso di media-type personalizzati come da ​[RFC
6838](https://tools.ietf.org/html/rfc6838#section-3.4) (eg.

application/x.custom.name+json) ed utilizzare nomi standard come
​[application/json​](https://www.iana.org/assignments/media-
types/application/json),

[application/problem+json​](https://www.iana.org/assignments/media-
types/application/problem+json),
​[application/jose+json​](https://www.iana.org/assignments/media-
types/application/jose+json),
​[application/fhir+json​](https://www.iana.org/assignments/media-
types/application/fhir+json).

Utilizzare Content-Type specifici per dati binari, immagini o documenti

Utilizzare le properties secondo nomenclature standard

Le properties devono utilizzare ove possibile la nomenclatura indicata nelle
Linee Guida

per la valorizzazione del Patrimonio informativo nazionale e le relative
ontologie.

Utilizzare formati standard per Data ed Ora

Le date devono essere conformi ad
​[RFC3339​](https://www.ietf.org/rfc/rfc3339.txt), ad esempio 2015-05-28 per
la data e

2015-05-28T14:07:17Z



Le date negli header HTTP devono essere conformi allo standard ​[HTTP date
format ](http://tools.ietf.org/html/rfc7231#section-7.1.1.1)

[defined in RFC 7231​](http://tools.ietf.org/html/rfc7231#section-7.1.1.1).



RFC3339 permette di indicare una timezone prefissando la data con la distanza
da UTC:

  - 2015-05-28T14:07:17+01:00

  - 2015-05-28T14:07:17-05:00

Quando la data è specificata in UTC occorre utilizzare sempre il suffisso Z
(Zulu time

zone)

  - 2015-05-28T14:07:17Z

Tempi di durata e intervalli devono utilizzare ISO 8601.

Di seguito alcuni esempi di durata in formato ​[ISO 8601 per i tempi di
durata​](https://en.wikipedia.org/wiki/ISO_8601#Durations).

Le durate sono prefissate da "P", giorni e Ore sono separati da "T".

Esempi:

P1Y2M3D - 1 anno, 2 mesi e 3 giorni

PT1H4M5S - 1 ora, 4 minuti e 5 secondi

P1M - 1 mese

PT1M - 1 minuto

P1Y2M10DT2H30M - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

Un'analoga sintassi ISO8601 per lo stesso intervallo è la seguente:

P0001-02-10T2:30:00

Utilizzare le convenzioni di rappresentazione

  - I nomi degli array devono essere al plurale.

  - I booleani non devono essere null.

  - Gli array vuoti non devono essere null, ma liste vuote, ad es. "[]".

  - Le enumeration devono essere rappresentate da Stringhe non nulle

---

Usare standard per Lingue, Nazioni e Monete

Utilizzare per le codifiche web gli standard indicati in Linee Guida per la
Valorizzazione

del Patrimonio Informativo Nazionale, inclusi:

  - [ISO 3166-1-alpha2 country (due lettere) ](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

  - [ISO 639-1 language code ](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

  - [BCP-47​](https://tools.ietf.org/html/bcp47) (basato su ISO 639-1) per le
varianti dei linguaggi. Dove non

strettamente necessario il subta​g​b​, basta la prima parte (ad es. it vs it-
IT)

  - [ISO 4217 currency codes​](http://en.wikipedia.org/wiki/ISO_4217) alpha-3
usato in
​[FatturePA](http://www.fatturapa.gov.it/export/fatturazione/sdi/Specifiche_tecniche_del_formato_FatturaPA_v1.0.pdf)

Per le valute, è possibile basarsi sullo schema Money - ripreso dal lavoro di

standardizzazione del ​[Berlin Group sotto l'egida dell'European
Standards​](https://www.berlin-group.org/) ed indicato in:

  - [https://github.com/teamdigitale/openapi/tree/master/docs/schemas](https://github.com/teamdigitale/openapi/tree/master/docs/schemas)

e contenente i campi:

  - amount​ (string)

  - currency (iso-4217)



Esempio 1:


```

{ "tax_id": "imu-e472", "value": { "amount": "100.23", "currency": "EUR"}}

```

Definire `format` quando si usano i tipi Number ed Integer

I numeri e gli interi devono indicare la dimensione secondo la seguente
tabella. Le

implementazioni devono utilizzare il tipo più adatto.



| type | format | valori ammessi

---|---|---

integer | int32 | interi tra -2^31 e 2^31-1
integer | int64 | interi tra -2^63 e 2^63-1
integer | bigint | intero con segno di grandezza arbitraria
number | float | IEEE 754-2008/ISO 60559:2011 decimale a 64 bit
number | double | IEEE 754-2008/ISO 60559:2011 decimale a 128 bit
number | decimal | decimale a precisione ​fissa​ e arbitraria

---|---|---

Le proprietà degli oggetti JSON devono avere un naming consistente (scegliere
uno

dei due) e devono essere codificate in ASCII:

  - snake_case

  - camelCase

Non usare contemporaneamente snake_case e camelCase nella stessa API.

Analogamente non usare contemporaneamente i due stili nella naming convention,
ad

esempio

  - sì​: { "givenName": "Mario", "familyName": "Rossi"}

  - sì: { "given_name": "Mario", "family_name": "Rossi"}

  - no: { "givenName": "Mario", "family_name": "Rossi"}

Preferire l'uso di ASCII snake_case al camelCase: ^[a-z_][a-z_0-9]*$. Sebbene
sia

possibile scegliere coerentemente, ove possibile si deve preferire l'utilizzo
dello

snake_case.

3.1.2. Progettazione e Naming delle Interfacce di Servizio

In assenza di specifiche regole (es. HL7, INSPIRE, ..) per l'API Naming,
valgono le seguenti.



Uso corretto dei metodi HTTP

I metodi HTTP devono essere utilizzati rispettando la semantica indicata in

[rfc7231#section-4.3](https://tools.ietf.org/html/rfc7231#section-4.3)

---

Uso corretto degli header HTTP

In generale gli header:

  - devono essere utilizzati solo per passare informazioni di contesto

  - la semantica e gli intenti delle operazioni deve essere definita tramite URI,

Status e Method e non dagli Header, che dovrebbero supportare funzionalità di

protocollo come flow control, content negotiation, ed authentication, come

indicato ​[RFC-7231​](https://tools.ietf.org/html/rfc7231).

Prima di usare un header:

  - si deve verificare se è già adottato da IANA

[https://www.iana.org/assignments/message-headers/message-
headers.xhtml](https://www.iana.org/assignments/message-headers/message-
headers.xhtml)

Usare l'appropriato REST Maturity Level

9

Le API devono seguire le indicazioni in ​[REST Maturity Level
2​](http://martinfowler.com/articles/richardsonMaturityModel.html#level2) in
modo da essere

resource-oriented e fare affidamento su HTTP verbs e status. Questo include:

  - Evitare le azioni e ragionare intorno alle risorse

  - Evitare i verbi negli URL

  - Usare correttamente gli HTTP method

  - Usare gli status HTTP appropriati



Per API destinate ad interfacciarsi con un front-end o con le persone, può
aver senso

adottare un approccio di tipo HATEOAS o ​[REST Maturity Level 3​](http://martinfowler.com/articles/richardsonMaturityModel.html#level3).

In un contesto machine-to-machine dove le interazioni sono spesso predefinite,
la

complessità di HATEOAS non porta necessariamente dei benefici.

Quando le risorse contengono link e riferimenti a risorse esterne, si
dovrebbero usare le

specifiche indicate in ​[IANA registered link relations​](http://www.iana.org/assignments/link-relations/link-
relations.xml). Se le specifiche IANA contengono

dei dash "-", questi vanno convertiti in underscore "_", e​g. terms-of-service
-&gt;

terms_of_service.



Esempio: una ricerca paginata con link relations.


```
GET /dipendenti?nome=Mario%20Rossi&amp;limit=2

{

"limit": 2

"items": [

{

"id": "RSSMRA75L01H501A",

"nome": "Mario Rossi",

"coniuge": {

"href": "https://...",

"id": "BNCFNC75A41H501G",

"nome": "Francesca Bianchi"

}

},

{

"id": "RSSMRA77L01H501A",

"nome": "Mario Rossi",

"coniuge": {

"href": "https://...",

"id": "VRDBNC81A41H501S",

"nome": "Bianca Verdi"

}

}

],

"first": "https://...",

"next": "https://...",

"prev": "https://...",

"last": "https://..."

}

```



Usare parole separate da trattino "-" per i Path

Questo si applica solo al Path, e non ai parametri del path (eg.
{tax_code_id}).

Esempio:

```
/​tax-code​/{tax_code_id}
```

Inoltre, il Path dovrebbe essere semplice, intuitivo e coerente.

---

Usare un case consistente snake_case o camelCase per i Query Parameters

Una volta scelto un case, siate consistenti: non mescolare snake_case e
camelCase

nella stessa API.

I nomi utilizzati devono usare abbreviazioni e acronimi universalmente
riconosciuti

Preferire Hyphenated-Pascal-Case per gli header HTTP

Esempi:

```
Accept-Encoding

Apply-To-Redirect-Ref

Disposition-Notification-Options

Original-Message-ID
```

Le collezioni di risorse devono usare nomi al plurale

Differenziare il nome delle collezioni e delle risorse permette di separare a
livello di URI

endpoint che sono in larga parte funzionalmente differenti.



Esempio 1: ricerca documenti per data in una collezione

```
GET /​documenti​?data=2018-05-01

{

"items": [ …]

"limit": 10

"next_cursor": 21314123

}

Esempio 2: recupera un singolo documento

GET /​documento​/21314123

{

"id": 21314123

"title: "Atto di nascita ...",

..

}
```
Utilizzare Query Strings standardizzate

Esempio 1: La paginazione dev'essere implementata tramite i parametri cursor,
limit,

offset, sort

Esempio 2: La ricerca, il filtering e l'embedding dei parametri dev'essere
implementata

tramite i parametri q, fields. embed



E' possibile trovare un elenco di parametri standardizzati nel repository:

11

-[https://github.com/teamdigitale/openapi/tree/master/docs](https://github.com/teamdigitale/openapi/tree/master/docs)

---

Non usare Link Headers RFC5988 se la response è in JSON

Usare URI assoluti nei risultati

Restituendo URI assoluti si indica chiaramente al client l'indirizzo delle
risorse di

destinazione e non si obbligano i client a fare "inferenza" dal contesto.

Usare lo schema Problem JSON per le risposte di errore

In caso di errori si deve ritornare:

  - un payload di tipo Problem definito in ​[RFC
7807](http://tools.ietf.org/html/rfc7807)

  - il media type dev'essere application/problem+json

  - lo status code dev'essere esplicativo

  - l'oggetto può essere esteso

Quando si restituisce un errore è importante non esporre dati interni delle
applicazioni e

seguire le indicazioni in

[https://www.agid.gov.it/sites/default/files/repository_files/documentazione/linee_gu](https://www.agid.gov.it/sites/default/files/repository_files/documentazione/linee_guida_per_lo_sviluppo_sicuro_di_codice_v1.0.pdf)

[ida_per_lo_sviluppo_sicuro_di_codice_v1.0.pdf​](https://www.agid.gov.it/sites/default/files/repository_files/documentazione/linee_guida_per_lo_sviluppo_sicuro_di_codice_v1.0.pdf)
§6.4

3.1.3. Performance e Robustezza

Utilizzare lo status code http 429 con gli header per il rate limiting

Gli erogatori devono definire ed esporre ai fruitori politiche di throttling
segnalando

eventuali limiti raggiunti con ​HTTP 429 (too many requests)​.



Le API devono restituire in ogni response i valori globali di throttling
tramite i seguenti

header:

  - X-RateLimit-Limit​: limite massimo di richieste per un endpoint

  - X-RateLimit-Remaining​: numero di richieste rimanenti fino al prossimo reset

  - X-RateLimit-Reset​: il numero di secondi che mancano al prossimo reset



In caso di superamento delle quote le API devono restituire anche l'header:

  - Retry-After​: il numero minimo di secondi dopo cui il client è invitato a
riprovare



Attenzione:

  - l'RFC 7231 prevede che Retry-After header possa essere utilizzato sia in
forma

di data che di secondi;

  - alcune API pubbliche utilizzano l'header ​X-RateLimit-Reset anche nel formato

Unix​ Timestamp



---

12

I fruitori devono:

  - rispettare gli header di throttling

  - rispettare l'header ​X-RateLimit-Reset sia quando restituisce il numero di

secondi che mancano al prossimo reset, sia quando ritorna il timestamp unix

  - rispettare l'header ​[Retry-After​](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Headers/Retry-Afte) sia nella variante che espone il numero
di secondi

dopo cui riprovare, sia nella variante che espone la data in cui riprovare

---

Utilizzare lo status code 503 con l'header Retry-After per segnalare il
sovraccarico

del sistema o l'indisponibilità del servizio

Gli erogatori devono definire ed esporre un piano di continuità operativa
segnalando il

sovraccarico del sistema o l'indisponibilità del servizio con lo status code
http​ 503

(service unavailable)​.



In caso di sovraccarico o indisponibilità, l'erogatore deve ritornare anche
l'header:

  - Retry-After​: il numero minimo di secondi dopo cui il client è invitato a
riprovare



I fruitori devono:

  - rispettare l'header ​[Retry-After​](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Headers/Retry-Afte) sia nella variante che espone il numero
di secondi

dopo cui riprovare, sia nella variante che espone la data in cui riprovare

Ottimizzare l'uso della banda e migliorare la responsività

Utilizzare quando possibile:

  - gzip compression;

  - paginazione;

  - un filtro sugli attributi necessari;

  - le specifiche di optimistic locking (etag, if-(none-)match)



E' possibile ridurre l'uso della banda e velocizzare le richieste filtrando i
campi delle

risorse restituite. Si vedano qui ulteriori informazioni su come supportare il
filtraggio dei

campi delle risorse ritornate:

[https://cloud.google.com/compute/docs/api/how-
tos/performance#partial](https://cloud.google.com/compute/docs/api/how-
tos/performance#partial)



Esempio 1: Non filtrato
```
GET http://api.example.org/resources/123 HTTP/1.1

HTTP/1.1 200 OK

Content-Type: application/json

{

"id": "cddd5e44-dae0-11e5-8c01-63ed66ab2da5",

"name": "Mario Rossi",

"address": "via del Corso, Roma, Lazio, Italia",

"birthday": "1984-09-13",

"partner": {

"id": "1fb43648-dae1-11e5-aa01-1fbc3abb1cd0",

13

"name": "Maria Rossi",

"address": "via del Corso, Roma, Lazio, Italia",

"birthday": "1988-04-07"

}

}
```
Esempio 2: Filtrato[ ](http://zalando.github.io/restful-api-
guidelines/index.html#filtered)

```
GET http://api.example.org/resources/123?fields=(name,partner(name))

HTTP/1.1



HTTP/1.1 200 OK

Content-Type: application/json



{

"name": "Mario Rossi",

"partner": {

"name": "Maria Rossi"

}

}


```

Effettuare la Resource Expansion permette di ridurre il numero di richieste,
quando

bisogna ritornare risorse correlate tra loro.

In tal caso va usato:

  - il​ parametro "embed" utilizzando lo stesso formato dei campi per il
filtering

  - l'attributo _embedded contenente le entry espanse.


```
GET /tax_code/MRORSS12T05E472W?embed=(person) HTTP/1.1



{

"tax_code": "MRORSS12T05E472W",

"_embedded": {

"person": {

"given_name": "Mario",

"family_name": "Rossi",

"id": "1234-ABCD-7890",

} } }

```

Di default il caching deve essere disabilitato tramite:

  - Cache-Control​: no-cache header.

in modo da evitare che delle richieste vengano inopportunamente messe in
cache.



Le API che supportano il caching devono documentare le varie limitazioni e
modalità di

utilizzo tramite gli header definiti in
​[RFC-7234​](https://tools.ietf.org/html/rfc7234):

  - Cache-Control

  - Vary

---

14



Eventuali conflitti nella creazione di risorse vanno gestiti tramite gli
header:

  - [ETag](https://tools.ietf.org/html/rfc7232#section-2.3)

  - [If-Match](https://tools.ietf.org/html/rfc7232#section-3.1)

  - [If-None-Match​](https://tools.ietf.org/html/rfc7232#section-3.2).

contenenti un hash del response body, un hash dell'ultimo campo modificato
della entry

o un numero di versione.

Se l'etag della entry su cui si opera non corrisponde al valore della
richiesta, la response

ritorna lo status code 412 - precondition failed.



Le API devono supportare la paginazione delle collezioni tramite:

  - paginazione classica tramite i query parameter offset e limit

  - paginazione con cursore; la paginazione a cursore permette l'implementazione

di pagine con infinite scrolling.

La paginazione dovrebbe essere implementata in modo da limitare l'uso
improprio delle

API (eg. download in parallelo di interi dataset, …)



Per il ripristino del download di un documento si faccia riferimento a Range
Requests

[RFC 7233​](https://tools.ietf.org/html/rfc7233).

---

Supportare le informazioni di inoltro tramite l'header Forwarded

Le informazioni di inoltro HTTP (eg. indirizzo ip di provenienza, destinazione
…) erogatori

devono essere:

  - preservate​ dall'infrastruttura

  - scambiate tramite l'header Forwarded definito in
​[rfc7239​](https://tools.ietf.org/html/rfc7239) e pronto per IPv6.



eg. Forwarded: for=192.0.2.60; for="[2001:db8:cafe::17]"

; proto=https; by=203.0.113.43



Gli header X-Forwarded-For X-Forwarded-Host e X-Forwarded-Proto - che non
hanno

un comportamento codificato e dipendono dalle varie implementazioni, devono

comunque essere supportati e preservati.

3.1.4. Riferimenti

Specifiche

  - [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/)[
](https://tools.ietf.org/html/bcp47)

Articoli

  - [Roy Thomas Fielding - Architectural Styles and the Design of Network-Based
](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)

[Software
Architectures​](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm).
Definizione teorica dell'approccio REST

15

Libri​[PIs: From Start to Finish ](http://www.infoq.com/minibooks/emag-web-
api)

  - [Blogs](http://www.amazon.de/REST-Practice-Hypermedia-Systems-
Architecture/dp/0596805829)

  - [Service Design Patterns](http://www.servicedesignpatterns.com/)

  - [REST in Practice: Hypermedia and Systems Architecture
](http://www.amazon.de/REST-Practice-Hypermedia-Systems-
Architecture/dp/0596805829)

  - [Build APIs You Won`t Hate ](https://leanpub.com/build-apis-you-wont-hate)

  - [InfoQ eBook - Web A​PIs: From Start to
Finish​](http://www.infoq.com/minibooks/emag-web-
api)[¶](http://www.infoq.com/minibooks/emag-web-api)

  - ​Blogs

  - [Lessons-learned blog: Thoughts on RESTful API Design](http://restful-api-
design.readthedocs.org/en/latest/)

3.2 SOAP

l'utilizzo del protocollo SOAP ai fini di interoperabilità è l'oggetto del
WS-I Basic Profile

(BP) la cui versione 2.01 (ultima versione rilasciata) è quella a cui fa
riferimento il ModI. In

particolare il BP2.0 impiega SOAP 1.22 e WS-Addressing3. I framework
implementativi più

diffusi sono conformi a questa specifica sulla quale quindi il presente
documento non si

soffermerà. Indichiamo di seguito invece le best practice relative alla
specifica dei servizi e

del formato dei dati.

3.2.1. Formato dei dati

Codificare dati strutturati con oggetti XML

I dati strutturati devono essere trasferiti tramite ​oggetti XML​ che
utilizzano elementi

contenitivi per le liste:

  - il payload di una response contenente una entry ritorna un oggetto

&lt;persona givenName="Paolo" familyName="Rossi" id="313" /&gt;

  - il payload di una response contenente più entry ​ritorna un oggetto
contenente

una lista​ e non direttamente una lista.

&lt;persone&gt;

&lt;persona givenName="Carlo" familyName="Bianchi" id="314" /&gt;

&lt;persona givenName="Giuseppe" familyName="Verdi" id="315" /&gt;

&lt;/persone&gt;



Vanno utilizzati namespace e definiti specifici XSD.



---

Evitare Content-Type personalizzati

1 Cf.
​[http://ws-i.org/profiles/BasicProfile-2.0-2010-11-09.html](http://ws-i.org/profiles/BasicProfile-2.0-2010-11-09.html)

2 Cf. ​[https://www.w3.org/TR/soap12/](https://www.w3.org/TR/soap12/)

3 Cf. ​[https://www.w3.org/Submission/ws-
addressing/](https://www.w3.org/Submission/ws-addressing/)

16

Evitare l'uso di media-type personalizzati come da ​[RFC
6838](https://tools.ietf.org/html/rfc6838#section-3.4) (eg.

application/x.custom.name+xml) ed utilizzare nomi standard come
​[application/xml](https://www.iana.org/assignments/media-
types/application/xml)



Utilizzare embedding o referencing per trasferire i dati binari. l'inserimento
di dati binari

all'interno del payload può avvenire o tramite embedding (ed in questo caso la
codifica

base64 è da preferirsi a quella esadecimale) oppure tramite referencing.

---

Attributi ed elementi devono utilizzare ove possibile la nomenclatura indicata
nelle

Linee Guida per la valorizzazione del Patrimonio informativo nazionale e le
relative

ontologie

Utilizzare formati standard per Data ed Ora

Le date devono essere conformi ad
​[RFC3339​](https://www.ietf.org/rfc/rfc3339.txt), ad esempio 2015-05-28 per
la data e

2015-05-28T14:07:17Z



Le date negli header HTTP devono essere conformi allo standard ​[HTTP date
format ](http://tools.ietf.org/html/rfc7231#section-7.1.1.1)

[defined in RFC 7231​](http://tools.ietf.org/html/rfc7231#section-7.1.1.1).



RFC3339 permette di indicare una timezone prefissando la data con la distanza
da UTC:

  - 2015-05-28T14:07:17+01:00

  - 2015-05-28T14:07:17-05:00

Quando la data è specificata in UTC occorre utilizzare sempre il suffisso Z
(Zulu time

zone)

  - 2015-05-28T14:07:17Z

Tempi di durata e intervalli devono utilizzare ISO 8601.

Di seguito alcuni esempi di durata in formato ​[ISO 8601 per i tempi di
durata​](https://en.wikipedia.org/wiki/ISO_8601#Durations).

Le durate sono prefissate da "P", giorni e Ore sono separati da "T".

Esempi:

P1Y2M3D - 1 anno, 2 mesi e 3 giorni

PT1H4M5S - 1 ora, 4 minuti e 5 secondi

P1M - 1 mese

PT1M - 1 minuto

P1Y2M10DT2H30M - 1 anno, 2 mesi, 10 giorni 2 ore e 30 minuti

Un'analoga sintassi ISO8601 per lo stesso intervallo è la seguente:

P0001-02-10T2:30:00

Utilizzare le convenzioni di rappresentazione

Si consiglia l'utilizzo di elementi come figli di un elemento quando:

  - Può esistere come elemento a se stante

  - Occorre definire una lista (gli attributi non possono essere multivalore)

I nomi delle liste devono essere al plurale.

I booleani non devono essere mai null.

17

Le properties devono avere un naming consistente

l'utilizzo più frequente è quello di camelCase sia per gli elementi che per
gli attributi. In

alcuni casi è possibile utilizzare PascalCase per gli elementi e camelCase per
gli attributi

(come nel
​[NIME](https://en.wikipedia.org/wiki/National_Information_Exchange_Model)4)

---

Usare standard per Lingue, Nazioni e Monete

Utilizzare per le codifiche web gli standard indicati in Linee Guida per la
Valorizzazione

del Patrimonio Informativo Nazionale, inclusi:

  - [ISO 3166-1-alpha2 country (due lettere)
](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

  - [ISO 639-1 language code
](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

  - [BCP-47​](https://tools.ietf.org/html/bcp47) (basato su ISO 639-1) per le
varianti dei linguaggi

  - [ISO 4217 currency codes​](http://en.wikipedia.org/wiki/ISO_4217) alpha-3
usato in
​[FatturePA](http://www.fatturapa.gov.it/export/fatturazione/sdi/Specifiche_tecniche_del_formato_FatturaPA_v1.0.pdf)



Nel caso di importi, l'elemento dovrà contenere sia un elemento o attributo di
tipo

standard xs:currency che una indicazione del codice della valuta. Ad esempio:

&lt;prezzo valuta="EUR" totale="100.00" /&gt;

3.2.2. Progetto e Naming delle Interfacce di Servizio

Ai fini del progetto delle interfacce di servizio, esistono diverse
metodologie. In particolare

nel ModI si suggerisce l'utilizzo della metodologia di identificazione delle
interfacce

contenuta nel libro ​[UML Components](https://www.pearson.com/us/higher-
education/program/Cheesman-UML-Components-A-Simple-Process-for-Specifying-
Component-Based-Software/PGM319361.html) che permette di identificare servizi
ed operazioni per

i singoli componenti applicativi.



Descrittività dei nomi utilizzati



I nomi utilizzati per servizi ed operazioni nelle interfacce di servizio
devono essere

auto-descrittivi e fornire quanta più informazione possibile riguardo al
comportamento

implementato. Occorre inoltre eliminare il rischio di collisioni tra nomi in
differenti

domini nel caso in cui un termine possa avere dei significati multipli (es.
protocollo). Si

deve inoltre evitare l'utilizzo di acronimi quando questi non siano
universalmente

riconosciuti anche al di fuori del dominio applicativo.

---

Utilizzo di camelCase e PascalCase



I nomi dei servizi devono essere specificati in PascalCase mentre per le
operazioni

implementate e gli argomenti si utilizza il camelCase.

Utilizzo di nomi agnostici rispetto all'implementazione



I nomi utilizzati per i servizi e le operazioni non dovrebbero rivelare
dettagli

implementativi.

4 Cf.
​[https://en.wikipedia.org/wiki/National_Information_Exchange_Model](https://en.wikipedia.org/wiki/National_Information_Exchange_Model)

18

Non includere il numero di versione all'interno del nome del servizio

---

Non includere la parola Service nel nome del servizio

Unicità dei namespace e utilizzo di pattern fissi



Ogni servizio all'interno del WSDL deve avere un suo namespace unico. I
namespace

utilizzati per i servizi devono seguire un pattern specifico. In particolare,
per i servizi:

http://&lt;dominioOrganizzativo&gt;/ws/&lt;DominioApplicativo&gt;/&lt;NomeServizio&gt;/V&lt;major&gt;



dove &lt;dominioOrganizzativo&gt; indica l'organizzazione che espone il
servizio,

&lt;DominioApplicativo&gt; indica il settore all'interno dell'organizzazione,
&lt;NomeServizio&gt;

segue le specifiche di cui ai punti precedenti, e &lt;major&gt; indica il
numero di versione

(difatti non inserito nel nome del servizio).



Per quanto riguarda gli XSD all'interno del WSDL si segue il pattern seguente:

http://&lt;dominioOrganizzativo&gt;/xmlns/&lt;DominioApplicativo&gt;



3.2.3. Performance e Robustezza

Ottimizzare l'uso della banda e migliorare la responsività

Utilizzare quando possibile, in special modo per le operazioni che ritornano
liste e

risultati di ricerche:

  - gzip compression;

  - paginazione;

  - un filtro sugli attributi necessari.



Le API devono supportare la paginazione delle collezioni tramite:

  - paginazione classica tramite parametri offset e limit

  - paginazione a cursore permette l'implementazione di pagine con infinite

scrolling,

La paginazione deve essere implementata in modo da limitare l'uso improprio
delle API

(eg. download in parallelo di interi dataset, …)



Di default il caching deve essere disabilitato tramite l'header:

  - Cache-Control: no-cache header.

in modo da evitare che delle richieste vengano inopportunamente messe in
cache.



Le API che supportano il caching devono documentare le varie limitazioni e
modalità di

utilizzo tramite gli header definiti in
​[RFC-7234​](https://tools.ietf.org/html/rfc7234):

  - Cache-Control

  - Vary



---

19

In generale le richieste SOAP utilizzando il metodo HTTP POST (non
idempotente), ma

nei casi in cui l'operazione effettuata è idempotente è possibile implementare

meccanismi di caching simili a quelli visti nel caso REST.

---

Gestione del rate limit

l'eventuale superamento dei rate limit deve essere segnalato per mezzo di una
SOAP

fault inserendo all'interno del campo detail della fault tutte le informazioni
necessarie al

fruitore al fine di identificare il reset dei limiti imposti. Il meccanismo di
SOAP fault può

essere utilizzato anche per inviare informazioni in tempo reale ai fruitori
relativi al

numero di chiamate mancanti al raggiungimento del limite così come nel caso
REST.

Utilizzo degli status code HTTP

La versione 1.2 di SOAP definisce in dettaglio (si veda la parte 2 della
specifica) l'utilizzo

di codici di stato HTTP come confermato dal basic profile 2.0. Si richiede
quindi l'utilizzo

di questi codici.

3.2.4. Riferimenti

Specifiche



SOAP 1.2 ​[Parte 1​](https://www.w3.org/TR/soap12/) e ​[Parte
2](https://www.w3.org/TR/soap12-part2/)

[WS-I Basic Profile
2.0](http://ws-i.org/profiles/BasicProfile-2.0-2010-11-09.html)

[WS-Addressing](https://www.w3.org/Submission/ws-addressing/)

[Standard eHealth
Ontario](https://www.ehealthontario.on.ca/architecture/education/courses/service-
oriented-architecture/downloads/SOA-ServiceNamingConventions.pdf)



Libri



[UML Components](https://www.pearson.com/us/higher-education/program/Cheesman-
UML-Components-A-Simple-Process-for-Specifying-Component-Based-
Software/PGM319361.html)

