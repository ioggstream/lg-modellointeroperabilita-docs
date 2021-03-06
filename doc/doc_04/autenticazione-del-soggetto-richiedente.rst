Autenticazione del soggetto fruitore
====================================

[M2MS01] Direct Trust con certificato X.509 su SOAP
---------------------------------------------------

.. _scenario-2:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitrice, o entrambe le parti;

.. _descrizione-2:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità
di scambio dei certificati X.509) non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-2:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-2:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia la richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

Al messaggio è aggiunta la firma di una porzione significativa dello
stesso.

**B: Risposta**

L’erogatore, ricevuto il messaggio, verifica il
certificato X.509 e valida la firma.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-2:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore calcola la firma per gli elementi significativi del
   messaggio usando l’XML Signature. Il digest è firmato usando la
   chiave privata associata al certificato X.509 del fruitore.
   L’elemento ``<Signature>`` è posizionato nell’header ``<Security>`` del
   messaggio.

3. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   a. ``<wsse:BinarySecurityToken>``

   b. ``<wsse:KeyIdentifier>``

   c. ``<wsse:SecurityTokenReference>``

4. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

5. L’erogatore recupera il certificato X.509 referenziato nell’header
   ``<Security>``.

6. L’erogatore verifica il certificato secondo i criteri del trust.

7. L’erogatore valida la firma verificando l’elemento ``<Signature>``
   nell’header ``<Security>``.

8. L’erogatore autentica il fruitore.

9. Se le azioni da 5 a 8 hanno avuto esito positivo, il messaggio viene
   elaborato e viene restituito il risultato del servizio richiamato.

Note:

-  Gli algoritmi da utilizzare nell’elemento
   ``<Signature>`` rispettivamente ``<DigestMethod>``, ``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` sono indicati alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

-  Un meccanismo simile può essere utilizzato per autenticare
   l' erogatore.

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

   <soap:Envelope>
     <soap:Header>
       <wsse:Security soap:mustUnderstand="1">
         <wsse:BinarySecurityToken
           EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
           ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
           wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIBAgIECxY+9TAhkiG9w...
         </wsse:BinarySecurityToken>
         <wsu:Timestamp wsu:Id="TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
           <wsu:Created>2018-10-04T10:17:28.061Z</wsu:Created>
           <wsu:Expires>2018-10-04T10:22:28.061Z</wsu:Expires>
         </wsu:Timestamp>
         <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">
           <ds:SignedInfo>
             <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
               <ec:InclusiveNamespaces PrefixList="soap" />
             </ds:CanonicalizationMethod>
             <ds:SignatureMethod
                 Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
             <ds:Reference URI="#TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
               <ds:Transforms>
                 <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                   <ec:InclusiveNamespaces PrefixList="soap wsse" />
                 </ds:Transform>
               </ds:Transforms>
               <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
               <ds:DigestValue>NWPKndUk42jwIJOpDGXACq7QbyBUg1UfJFSEylsCxQw=</ds:DigestValue>
             </ds:Reference>
           </ds:SignedInfo>
           <ds:SignatureValue>AIrDa7ukDfFJD867goC+c7K3UampxpX/Nj/...</ds:SignatureValue>
           <ds:KeyInfo Id="KI-cad9ee47-dec8-4340-8fa1-74805f7e26f8">
             <wsse:SecurityTokenReference wsu:Id="STR-e193f25f-9727-4197-b7aa-25b01c9f2ba3">
              <wsse:Reference
                URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"  ValueType="http://docs.oasis-open.org/   wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>
                </wsse:SecurityTokenReference>
           </ds:KeyInfo>
         </ds:Signature>
       </wsse:Security>
        </soap:Header>
     <soap:Body>
       <ns2:sayHi xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">
         <arg0>Hello World!</arg0>
       </ns2:sayHi>
     </soap:Body>
   </soap:Envelope>

Il tracciato rispecchia alcune scelte implementative esemplificative:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``)

-  algoritmo per il digest (``DigestMethod``)

-  l’inclusione dell’elemento ``Timestamp`` quale porzione significativa del
   messaggio e la relativa firma.

Le parti, in base alle proprie esigenze, utilizzano gli algoritmi indicati
nella sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__, nonché la modalità di inclusione
o referenziazione del certificato x509.


[M2MS02] Direct Trust con certificato X.509 su SOAP con threat mitigation
-------------------------------------------------------------------------

.. _scenario-3:

Scenario
^^^^^^^^

Il seguente profilo estende il profilo M2MS01.

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti;

-  difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing;

.. _descrizione-3:

Descrizione
^^^^^^^^^^^

Il presente profilo specializza lo standard OASIS Web Services Security
X.509 Certificate Token Profile Versione 1.1.1 `[4] <bibliografia.html>`__.

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità
di scambio dei certificati X.509, non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509,
valida la firma dei claim ed autentica il fruitore. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-3:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-3:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

Al messaggio è aggiunta la firma di una porzione significativa dello
stesso con almeno le seguenti claim:

-  il riferimento dell’erogatore

-  un riferimento temporale univoco per messaggio

**B: Risposta**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma e le claim ricevute.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-3:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore costruisce un messaggio SOAP per il servizio.

2. Il fruitore aggiunge al messaggio l’header ``WS-Addressing`` e
   l’elemento ``<wsu:Timestamp>`` composto dagli elementi ``<wsu:Created>`` e
   ``<wsu:Expires>``

3. Il fruitore calcola la firma per gli elementi significativi del
   messaggio, in particolare ``<wsu:Timestamp>`` e ``<wsa:To>`` del blocco
   ``WS-Addressing``. Il digest è firmato usando la chiave privata associata
   al certificato X.509 del fruitore. L’elemento ``<Signature>`` è
   posizionato nell’header ``<Security>`` del messaggio.

4. Il fruitore referenzia il certificato X.509 usando in maniera
   alternativa, nell’header ``<Security>``, i seguenti elementi previsti
   nella specifica ws-security:

   a. ``<wsse:BinarySecurityToken>``

   b. ``<wsse:KeyIdentifier>``

   c. ``<wsse:SecurityTokenReference>``

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6.  L’erogatore recupera il certificato X.509 referenziato nell’header
    ``<Security>``.

7.  L’erogatore verifica il certificato secondo i criteri del trust.

8.  L’erogatore valida l’elemento <Signature> nell’header ``<Security>``.

    i.  L’erogatore verifica il contenuto dell’elemento ``<wsu:Timestamp>``
        nell’header del messaggio al fine di verificare la validità
        temporale del messaggio anche per mitigare il rischio di replay
        attack.

    ii. L’erogatore verifica la corrispondenza tra se stesso e quanto
        definito nell’elemento ``<wsa:To>`` del blocco WS-Addressing.

9.  L’erogatore autentica il fruitore.

10. Se le azioni da 6 a 11 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nell’elemento
   ``<Signature>`` rispettivamente ``<DigestMethod>``, ``<SignatureMethod>`` e
   ``<CanonicalizationMethod>`` si fa riferimento agli algoritmi indicati
   alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__,

-  Un meccanismo simile può essere utilizzato per autenticare
   l’erogatore.

.. _tracciato-3:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore relativo ad un
servizio di ``echo``.

I namespace utilizzati nel tracciato sono riportati di seguito:

.. code-block:: python

   soap="http://schemas.xmlsoap.org/soap/envelope/"
   wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
   wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
   ds="http://www.w3.org/2000/09/xmldsig#"
   ec="http://www.w3.org/2001/10/xml-exc-c14n#"
   "http://www.w3.org/2005/08/addressing"

.. code-block:: XML

   <soap:Envelope>
     <soap:Header>
       <wsse:Security soap:mustUnderstand="1">
         <wsse:BinarySecurityToken
               EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
               ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
               wsu:Id="X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7">MIICyzCCAbOgAwIBAgIECxY+9TAhkiG9w...
         </wsse:BinarySecurityToken>
         <wsu:Timestamp wsu:Id="TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
           <wsu:Created>2018-10-04T10:17:28.061Z</wsu:Created>
           <wsu:Expires>2018-10-04T10:22:28.061Z</wsu:Expires>
         </wsu:Timestamp>
         <ds:Signature Id="SIG-f58c789e-e3d3-4ec3-9ca7-d1e9a4a90f90">
           <ds:SignedInfo>
             <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
               <ec:InclusiveNamespaces PrefixList="soap" />
             </ds:CanonicalizationMethod>
             <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
             <ds:Reference URI="#TS-cd361ace-ba99-424a-aa3c-8c38c3263ced">
               <ds:Transforms>
                 <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                   <ec:InclusiveNamespaces PrefixList="soap wsse" />
                 </ds:Transform>
               </ds:Transforms>
               <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
               <ds:DigestValue>NWPKndUk42jwIJOpDGXACq7QbyBUg1UfJFSEylsCxQw=</ds:DigestValue>
             </ds:Reference>
             <ds:Reference URI="#id-4398e270-dae1-497e-97db-5fd1c5dbef1a">
               <ds:Transforms>
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
              <wsse:Reference URI="#X509-44680ddc-e35a-4374-bcbf-2b6dcba722d7"
                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"/>
              </wsse:SecurityTokenReference>
           </ds:KeyInfo>
         </ds:Signature>
       </wsse:Security>
       <Action xmlns="http://www.w3.org/2005/08/addressing">
             http://profile.security.modi.agid.org/HelloWorld/sayHi </Action>
       <MessageID xmlns="http://www.w3.org/2005/08/addressing">
              urn:uuid:3edf013f-0e2e-4fec-8487-95ade733a288
       </MessageID>
       <To xmlns="http://www.w3.org/2005/08/addressing"
           wsu:Id="id-4398e270-dae1-497e-97db-5fd1c5dbef1a">
           http://example.profile.security.modi.agid.gov.it/security-profile/echo </To>
     </soap:Header>
     <soap:Body>
       <ns2:sayHi xmlns:ns2="http://example.profile.security.modi.agid.gov.it/">
         <arg0>Hello World!</arg0>
       </ns2:sayHi>
     </soap:Body>
   </soap:Envelope>


Il tracciato rispecchia le seguenti scelte implementative
esemplificative:

-  riferimento al security token (``BinarySecurityToken``)

-  algoritmi di canonizzazione (``CanonicalizationMethod``)

-  algoritmi di firma (``SignatureMethod``).

-  algoritmo per il digest (``DigestMethod``)

Le parti, in base alle proprie esigenze, usano
gli algoritmi indicati in   `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__
, nonché la modalità di inclusione o referenziazione del certificato X.509.

[M2MR01] Direct Trust con certificato X.509 su REST
---------------------------------------------------

.. _scenario-4:

Scenario
^^^^^^^^

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti.

.. _descrizione-4:

Descrizione
^^^^^^^^^^^

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’ :RFC:`7519`

-  JSON Web Signature (JWS) definita dall’ :RFC:`7515`

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità
di scambio dei certificati X.509, non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e una
porzione significativa del messaggio firmata.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509 e
valida la porzione firmata del messaggio. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-4:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-4:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT include o referenzia il certificato X.509 riconosciuto
dall’erogatore.

**B: Risposta**

L’erogatore, ricevuto il messaggio, verifica il
certificato X.509 e valida la firma del token JWT.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-4:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore predispone la payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il token JWT popolando:

   a. l’header JSON Object Signing and Encryption (JOSE) con almeno i ``parameter``:

      i.   ``alg`` per definire l’algoritmo di firma

      ii.  ``typ`` uguale a ``JWT``

      iii. una o più delle seguenti opzioni per referenziare il certificato X.509:

           #. ``x5u`` (X.509 URL)

           #. ``x5c`` (X.509 Certificate Chain)

           #. ``x5t#S256`` (X.509 Certificate SHA-256 Thumbprint)

   b. la payload del JWT con zero o più claim rappresentative degli
      elementi chiave del messaggio.

3. il fruitore firma il token ``JWT`` secondo la specifica ``JWS`` adottando
   la ``JWS Compact Serialization``

4. il fruitore posiziona il token ``JWT`` firmato nell’header ``HTTP Authorization``

.. rpolli TODO verificare se ha senso mettere Bearer o no.

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6.  L’erogatore decodifica il token ``JWT`` presente nell’header HTTP
    ``Authorization``

7.  L’erogatore recupera il certificato X.509 referenziato nell’header ``JOSE``

8.  L’erogatore verifica il certificato secondo i criteri del trust

9.  L’erogatore valida la firma verificando l’elemento Signature del
    token ``JWT``

10. L’erogatore autentica il fruitore

11. Se le azioni da 6 a 10 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato

Note:

-  Gli algoritmi da utilizzare in ``alg`` sono indicati in  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`_.
   Un meccanismo simile può essere utilizzato per autenticare l’erogatore.

.. _tracciato-2:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

.. code-block:: http

   GET http://localhost:8080/ws-test/service/hello/echo/Ciao  HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

   .
   .
   .


Esempio porzione token JWT

.. code-block:: python

   # header
   {
     "alg": "RS256",
     "typ": "JWT",
     "x5c": [
       "MIICyzCCAbOgAwIBAgIEC..."
     ]
   }
   # payload
   {
    "exp": 1554382879
   }

Il tracciato rispecchia le seguenti scelte implementative
esemplificative:


-  Inserito istante di scadenza dell'asserzione,
   in modo che essa possa essere utilizzata solo fino all'istante ``exp``;

-  riferimento al certificato X.509 (``x5c``)

-  algoritmi di firma e digest (``alg``).

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__, nonché la modalità di inclusione
o referenziazione del certificato X.509.

[M2MR02] Direct Trust con certificato X.509 su REST con threat mitigation
-------------------------------------------------------------------------

.. _scenario-5:

Scenario
^^^^^^^^

Il seguente profilo estende il profilo M2MR01.

Comunicazione tra fruitore ed erogatore che assicuri a livello di
messaggio:

-  autenticazione del soggetto fruitore, quale organizzazione o unità
   organizzativa fruitore, o entrambe le parti

-  la difesa dalle minacce derivanti dagli attacchi: Replay Attack e
   Spoofing

.. _descrizione-5:

Descrizione
^^^^^^^^^^^

Il presente profilo declina l’utilizzo di:

-  JSON Web Token (JWT) definita dall’:RFC:`7519` `[1] <bibliografia.html>`__

-  JSON Web Signature (JWS) definita dall’:RFC:`7515` `[2] <bibliografia.html>`__

Si assume l’esistenza di un trust tra fruitore (client) ed erogatore
(server), che permette il riconoscimento da parte dell’erogatore del
certificato X.509, o la CA emittente.

Il meccanismo con cui è stabilito il trust, inclusa la modalità
di scambio dei certificati X.509) non condiziona il presente
profilo.

Il fruitore inoltra un messaggio all’interfaccia di servizio
dell’erogatore includendo o referenziando il certificato X.509 e
assicurando la firma dei claim del messaggio.

L’erogatore, ricevuto il messaggio, verifica il certificato X.509,
valida la firma dei claim ed autentica il fruitore. Se la verifica e la
validazione sono superate, l’erogatore consuma la richiesta e produce la
relativa risposta.

.. _dettaglio-5:

Dettaglio
^^^^^^^^^

.. mermaid::
   :caption: Autenticazione del Fruitore
   :alt: Autenticazione del Fruitore

   sequenceDiagram
      participant F as Fruitore
      participant E as Erogatore
      activate F
      F->>E: 1. Request()
      activate E
      E-->>F: 2. Reply
      deactivate E
      deactivate F

.. _flusso-delle-interazioni-5:

Flusso delle interazioni
~~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

Il fruitore invia il messaggio di richiesta all’interfaccia di
servizio dell’erogatore.

Il messaggio include il token JWT firmato.

Il token JWT:

-  include o referenzia il certificato X.509 riconosciuto
   dall’erogatore,

-  include almeno i seguenti claim:

   -  il riferimento dell’erogatore

   -  un riferimento temporale univoco per messaggio

**B: Risposta**

L’erogatore, ricevuto il messaggio, provvede alla verifica del
certificato X.509, valida la firma del token JWT e le claim ricevute.

L’erogatore predispone il messaggio di risposta e lo inoltra al
fruitore.

.. _regole-di-processamento-5:

Regole di processamento
~~~~~~~~~~~~~~~~~~~~~~~

**A: Richiesta**

1. Il fruitore predispone la payload del messaggio (ad esempio un
   oggetto JSON)

2. Il fruitore costruisce il token ``JWT`` popolando:

   a. l’header JSON Object Signing and Encryption (JOSE) con almeno:

      i.   la claim alg al fine di definire l’algoritmo utilizzato per
           la signature

      ii.  la claim typ pari a ``JWT``

      iii. in maniera alternativa, per referenziare il certificato
           X.509, una delle seguenti claim:

           #. ``x5u`` (X.509 URL)

           #. ``x5c`` (X.509 Certificate Chain)

           #. ``x5t#S256`` (X.509 Certificate SHA-256 Thumbprint)

   b. la payload del JWT con le claim rappresentative degli elementi
      significativi del messaggio, quali almeno:

      iv. ``iat``: UNIX timestamp di rilascio del JWT

      v. ``aud``: contenente il riferimento del destinatario del JWT

3. il fruitore firma il token JWT secondo la specifica JWS adottando
   la JWS Compact Serialization

4. il fruitore posiziona il token JWT firmato nell’header HTTP
   Authorization

5. Il fruitore spedisce il messaggio all’interfaccia di servizio
   dell’erogatore.

**B: Risposta**

6.  L’erogatore decodifica il token JWT presente nell’header HTTP
    Authorization

7.  L’erogatore recupera il certificato X.509 referenziato nell’header
    JOSE.

8.  L’erogatore verifica il certificato secondo i criteri del trust.

9.  L’erogatore valida la firma verificando l’elemento Signature del
    token JWT

10. L’erogatore verifica il contenuto della claim iat contenuta nella
    payload del JWT al fine di verificare la validità temporale del
    messaggio anche per mitigare il rischio di replay attack.

11. L’erogatore verifica la corrispondenza tra se stesso e quanto
    definito nella claim aud contenuta nella payload del JWT.

12. L’erogatore autentica il fruitore.

13. Se le azioni da 6 a 12 hanno avuto esito positivo, il messaggio
    viene elaborato e viene restituito il risultato del servizio
    richiamato.

Note:

-  Per quanto riguarda gli algoritmi da utilizzare nella claim alg si fa
   riferimento agli algoritmi indicati alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__.

-  Un meccanismo simile può essere utilizzato per autenticare
   l’erogatore.

.. _tracciato-5:

Tracciato
~~~~~~~~~

Di seguito è riportato un tracciato del messaggio inoltrato dal
fruitore all’interfaccia di servizio dell’erogatore.

Esempio porzione pacchetto HTTP

.. code-block:: JSON

   GET http://localhost:8080/ws-test/service/hello/echo/Ciao  HTTP/1.1
   Accept: application/json
   Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5c.vz8...

   .
   .

Esempio porzione token JWT

.. code-block::

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
     "aud": "http://localhost:8080/ws-test/service/hello/echo"
     "iat": "1516239022",
     "exp": "1516239024"
   }


Il tracciato rispecchia alcune scelte implementative esemplificative in
merito:

-  Inserito intervallo temporale di validità dell'asserzione,
   in modo che essa possa essere utilizzata solo nell'intervallo ``iat``, ``exp``;

-  riferimento al certificato X.509 (``x5c``);

-  algoritmi di firma e digest (``alg``).

Le parti, in base alle proprie esigenze, individuano gli specifici
algoritmi secondo quanto indicato alla sezione  `Elenco degli algoritmi <elenco-degli-algoritmi.html>`__, nonché la modalità di inclusione
o referenziazione del certificato x509.

.. discourse::
   :topic_identifier: 8907
