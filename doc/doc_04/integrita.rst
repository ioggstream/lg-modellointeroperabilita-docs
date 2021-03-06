Integrità
=========

[M2MS03] Integrità della payload del messaggio SOAP
---------------------------------------------------

.. _scenario-6:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  Integrità della payload del messaggio.

Nel caso in cui il certificato per garantire l’integrità è valido anche
per identificare il soggetto fruitore, il presente profilo estende
**M2MS01** o **M2MS02**, e quindi viene assicurato:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

.. _descrizione-6:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e la
firma della payload del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida l'integrità della payload del messaggio firmato. Se la verifica e
la validazione sono superate, l’erogatore consuma la richiesta e produce
la relativa risposta.

.. _dettaglio-6:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Integrità della payload del messaggio
   :alt: Integrità della payload del messaggio

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-6:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

Al messaggio è aggiunta la firma della payload stesso.

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509 e valida la firma.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-6:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore calcola la firma della payload del messaggio usando
   l’XML Signature. Il digest è firmato usando la chiave privata
   associata al certificato X.509 del fruitore. L’elemento
   ``<Signature>`` è posizionato nell’header ``<Security>`` del messaggio.

3. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   d. ``<wsse:BinarySecurityToken>``

   e. ``<wsse:KeyIdentifier>``

   f. ``<wsse:SecurityTokenReference>``

4. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

5. L’erogatore recupera il certificato X.509 referenziato nell’header
   ``<Security>``.

6. L’erogatore verifica il certificato secondo i criteri del trust.

7. L’erogatore valida la firma verificando l’elemento <Signature>
   nell’header ``<Security>``.

8. Se il certificato è valido anche per identificare il soggetto
   fruitore, l’erogatore autentica lo stesso

9. Se le azioni da 5 a 8 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   <Signature> rispettivamente ``<DigestMethod>``,``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` si fa riferimento agli algoritmi indicati
   alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della payload del del messaggio risposta dell’erogatore al
   fruitore.

.. _tracciato-4:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

  soap="http://schemas.xmlsoap.org/soap/envelope/"
  wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
  ds="http://www.w3.org/2000/09/xmldsig#"
  ec="http://www.w3.org/2001/10/xml-exc-c14n#"
  "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

   <soap:Envelope>
     <soap:Header>
       <wsse:Security soap:mustUnderstand="1">
         <wsse:BinarySecurityToken EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"    wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIBAgIECxY+9TAhkiG9w...
         </wsse:BinarySecurityToken>
         <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">
           <ds:SignedInfo>
             <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
               <ec:InclusiveNamespaces PrefixList="soap" />
             </ds:CanonicalizationMethod>
             <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
               <ds:Reference URI="#bd-567d101-aed1-789e-81cb-5ae1c5dbef1a"> <ds:Transforms>
                 <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                   <ec:InclusiveNamespaces PrefixList="soap" />
                 </ds:Transform>
               </ds:Transforms>
               <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
               <ds:DigestValue>0cJNCJ1W8Agu66fGTXlPRyy0EUNUQ9OViFlm8qf8Ysw=</ds:DigestValue>
             </ds:Reference>
           </ds:SignedInfo>
           <ds:SignatureValue>AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...</ds:SignatureValue>
           <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8">
             <wsse:SecurityTokenReference wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3">
              <wsse:Reference URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7" ValueType="http://docs.oasis-open.org/   wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>          </wsse:SecurityTokenReference>
           </ds:KeyInfo>
         </ds:Signature>
       </wsse:Security>
        </soap:Header>
     <soap:Body xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"    wsu:id="bd-567d101-aed1-789e-81cb-5ae1c5dbef1a">
       <ns2:sayHi xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">
         <arg0>Hello World!</arg0>
       </ns2:sayHi>
     </soap:Body>
   </soap:Envelope>

Il codice rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``)

-  algoritmo per il digest (``DigestMethod``)

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato al sezione "\  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__\ ", nonché la modalità di inclusione o
referenziazione del certificato x509.

[M2MR03] Integrità della payload del messaggio REST
---------------------------------------------------

.. _scenario-7:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  Integrità della payload del messaggio

Nel caso in cui il certificato per garantire l’integrità è valido anche
per identificare il soggetto fruitore, il presente profilo estende
M2MR01 o M2MR02, e quindi viene assicurato:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

.. _descrizione-7:

Descrizione
^^^^^^^^^^^

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’ :RFC:`7519` `[1] <#bibliografia>`__

-  JSON Web Signature (JWS) definita dall’ :RFC:`7515` `[2] <#bibliografia>`__

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo il certificato X.509 e la firma della payload
del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida l’integrità della payload del messaggio firmato. Se la verifica e
la validazione sono superate, l’erogatore consuma la richiesta e produce
la relativa risposta.

.. _dettaglio-7:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Integrità della payload del messaggio
   :alt: Integrità della payload del messaggio
   
   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-7:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT:

-  include o referenzia il certificato X.509 riconosciuto
   dall’erogatore.

-  include almeno le claim per referenziare:

   -  il digest della payload del messaggio;

   -  l’algoritmo per il calcolo del digest della payload del messaggio.

**B: Risultato**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma del token JWT e verifica il digest
della payload del messaggio.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-7:

Regole di processamento
^^^^^^^^^^^^^^^^^^^^^^^

**A: Richiesta**

1. Il fruitore predispone il body del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il token JWT popolando:

   a. l’header JSON Object Signing and Encryption (JOSE) con almeno:

      i.   il parameter ``alg`` al fine di definire l’algoritmo utilizzato per
           la signature

      ii.  il parameter ``typ`` pari a JWT

      iii. referenziare il certificato X.509, uno dei seguenti parameters:

           - ``x5u`` (X.509 URL)

           - ``x5c`` (X.509 Certificate Chain)

           - ``x5t#S256`` (X.509 Certificate SHA-256 Thumbprint)

   b. si consideri di utilizzare le seguenti claim nel payload, secondo le finalità del servizio:

      - ``iss``: identificativo del mittente
      - ``aud``: identificativo del destinatario
      - ``iat``: timestamp UNIX emissione del JWT
      - ``exp``: timestamp UNIX di scadenza del JWT
      - ``jti``: identificativo del JWT, per evitare replay attack
      - ``sub``: soggetto del jwt e/o identificativo dello scambio

.. rpolli TODO vediamo un attimo i nomi. Io userei un sistema simile al `Digest` header.

      - ``pda`` [1]_: contenente l’algoritmo di hashing utilizzato per il
          calcolo del digest della payload del messaggio

      - ``mpd`` [2]_: contenente il digest della payload del messaggio

3. il fruitore firma il token JWT secondo la specifica JWS adottando
   la JWS Compact Serialization

4. il fruitore posiziona il token JWT firmato nell’header HTTP
   Authorization

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risultato**

6.  L’erogatore decodifica il token JWT presente nell’header HTTP
    Authorization

7.  L’erogatore recupera il certificato X.509 referenziato nell’header
    JOSE.

8.  L’erogatore verifica il certificato secondo i criteri del trust.

9.  L’erogatore valida la firma verificando l’elemento Signature del
    token JWT

10. Se il certificato è valido anche per identificare il soggetto
    fruitore, l’erogatore autentica lo stesso

11. L’erogatore calcola il digest della payload del messaggio
    utilizzando l’algoritmo indicato nel claim pda.

12. L’erogatore verifica la corrispondenza tra il digest presente nel
    claim mpd contenuto nel payload del token JWT rispetto a quanto
    calcolato al passo precedente.

13. Se le azioni da 6 a 12 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nelle claim ``alg`` e ``pda``
   si fa riferimento agli algoritmi indicati sezione "\  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__\ ".

-  Un meccanismo simile può essere utilizzato per garantire l’integrità
   della risposta da parte dell’erogatore al fruitore.

.. _tracciato-5:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

.. code-block:: http

   POST http://localhost:8080/ws-test/service/hello/echo/
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...
   .
   .
   .

Esempio porzione token JWT

.. code-block:: http

   header
   {
     "alg": "RS256",
     "typ": "JWT",
     "x5c": [
       "MIICyzCCAbOgAwIBAgIEC..."
     ]
   }
   payload
   {
     "pda":"S256",
     "mpd":"B89AB4CA23D27F197AAE30F50843F0136900A1A154DCA00CDD8A5B8B4D071500"
   }

Esempio del body del messaggio

.. code-block:: http

   {
   "testo":"Hello world!"
   }

Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

-  riferimento al certificato X.509 (``x5c``)

-  algoritmi di firma e digest (``alg``).

-  algoritmo di hashing per calcolare il digest del body (``pda``)

Gli enti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto presente nella sezione "\  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__\ ", nonché la modalità di inclusione o referenziazione del certificato x509.

.. [1]
   Il presente documento ha individuato il claim con sigla "pda" al fine
   di indicare in maniera univoca per la pubblica amministrazione
   italiana il valore dell’algoritmo di hashing utilizzato per il
   calcolo del digest della payload del messaggio.

.. [2]
   Il presente documento ha individuato il claim con sigla "mpd" al fine
   di gestire in maniera univoca per la pubblica amministrazione
   italiana il valore del digest relativo della payload del messaggio.

.. discourse::
   :topic_identifier: 8908
