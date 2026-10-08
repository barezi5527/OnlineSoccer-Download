# Sicherheit & Berechtigungen

Wie die App mit deinen Daten und deinem Gerät umgeht – und wie du selbst prüfen kannst,
dass die APK unverändert ist.

> **Kurzfassung:** Die App fordert **zwei** Berechtigungen an, beide für den Netzwerkzugriff
> und nicht entfernbar. Keine Kamera, kein Mikrofon, kein Standort, keine Kontakte, kein
> Speicherzugriff, kein Tracking.
>
> **Online Soccer ist eine inoffizielle App.** Sie steht in keiner Verbindung zu den
> Betreibern des Spiels `os.ongapo.com` und wird nicht von ihnen unterstützt oder
> verifiziert.

---

## Inhalt

- [Unterstützte Versionen](#unterstützte-versionen)
- [Berechtigungen der App](#berechtigungen-der-app)
- [Wie die App deine Daten behandelt](#wie-die-app-deine-daten-behandelt)
- [Was die App *nicht* tut](#was-die-app-nicht-tut)
- [Signatur & Integritätsprüfung](#signatur--integritätsprüfung)
- [Bekannte Einschränkungen](#bekannte-einschränkungen)
- [Sicherheitsaudit](#sicherheitsaudit)
- [Meldung einer Sicherheitslücke](#meldung-einer-sicherheitslücke)
- [Sicherheitsrelevante Änderungen](#sicherheitsrelevante-änderungen)

---

## Unterstützte Versionen

Sicherheitsfixes werden ausschließlich für die aktuelle stabile Version bereitgestellt.

| Version | Unterstützt | Bemerkung |
|---|---|---|
| 1.2.1 | ✅ | aktuelle stabile Version |
| 1.2.0 | ❌ | veraltet – bitte aktualisieren |
| 1.1.0 | ❌ | veraltet – bitte aktualisieren |
| 1.0.0 | ❌ | veraltet – bitte aktualisieren |

---

## Berechtigungen der App

Die vollständige Berechtigungsliste der App – **nichts anderes** wird angefordert:

| Berechtigung | Zweck | Erforderlich? | Risiko |
|---|---|---|---|
| `android.permission.INTERNET` | Anmeldung, Datenabruf, Nachrichten, Transfers | ja – Kernfunktion | keines |
| `android.permission.ACCESS_NETWORK_STATE` | Erkennt, ob eine Netzwerkverbindung steht, um verständliche Fehlermeldungen statt Hängern zu zeigen | ja – Kernfunktion | keines |

Ausdrücklich **nicht** angefordert:

| Nicht angefordert | |
|---|---|
| `CAMERA` | keine Foto- oder Videoaufnahme |
| `RECORD_AUDIO` | kein Mikrofonzugriff |
| `ACCESS_FINE_LOCATION` / `ACCESS_COARSE_LOCATION` | keine Standortdaten |
| `READ_CONTACTS` / `WRITE_CONTACTS` | kein Zugriff auf Kontakte |
| `READ_EXTERNAL_STORAGE` / `WRITE_EXTERNAL_STORAGE` / `READ_MEDIA_*` | kein Zugriff auf Bilder, Videos oder Dateien |
| `POST_NOTIFICATIONS` | keine Benachrichtigungen im Hintergrund |
| `REQUEST_INSTALL_PACKAGES` | fordert keine weitere Installation an |
| `SYSTEM_ALERT_WINDOW` | kein Overlay |

Du kannst die Liste jederzeit selbst prüfen:

- **Ohne Datei:** Einstellungen → Apps → Online Soccer → Berechtigungen
- **Mit Datei:**
  ```bash
  aapt dump permissions OnlineSoccer-1.2.1-release.apk
  ```

---

## Wie die App deine Daten behandelt

| Aspekt | Umsetzung |
|---|---|
| **Zugangsdaten** | Login als HTTPS-POST direkt an `os.ongapo.com`. Kein Umweg über Dritte. |
| **Passwort** | wird **nie** gespeichert und **nie** protokolliert. Es lebt nur während des Anmeldevorgangs im Arbeitsspeicher und ist nach dem Login verworfen. |
| **Session-Token** | verschlüsselt abgelegt – Android Keystore (AES-256-GCM), Schlüsselnamen AES-256-SIV. Die Daten liegen also im hardwaregestützten Schlüsselspeicher, nicht als Klartext in den App-Einstellungen. |
| **Cloud-Backup** | `allowBackup="false"` – die App-Daten werden **nicht** in Google-Backup oder andere Backups kopiert. |
| **Netzwerk** | ausschließlich HTTPS. Klartext-Verkehr ist global abgeschaltet (`usesCleartextTraffic="false"`), auch für dieBilddaten der Vereinswappen. |
| **Zwischenspeicher** | Antworten des Spielservers werden lokal zwischengespeichert (Cache mit Zeitstempel), damit das Umschalten zwischen Ansichten schnell bleibt. |
| **Protokollierung** | Im Produktivcode gibt es kein Logging von Zugangsdaten, Tokens oder personenbezogenen Daten. |

---

## Was die App *nicht* tut

- **Kein Tracking.** Keine Analytics-SDK, keine Werbe-ID, keine Fingerprinting-Bibliothek.
- **Keine Drittanbieter-SDKs.** Keine Werbung, keine In-App-Käufe, keine Absturz- oder
  Analyse-Dienste, die Daten nach außen geben.
- **Keine WebView.** Es gibt kein eingebettetes Browser-Fenster, das beliebiges JavaScript
  aus Spielinhalten ausführt – damit entfällt eine typische Angriffsfläche.
- **Kein Hintergrunddienst**, der selbstständig Daten sendet. Netzwerkzugriff findet nur
  statt, während du eine Ansicht in der App öffnest.
- **Keine Werbung, kein Tracking, keine Datenabflüsse an Dritte** – die einzige Verbindung
  geht zum Spielserver.

---

## Signatur & Integritätsprüfung

Die veröffentlichte APK ist mit einem eigenen Release-Zertifikat signiert (nicht mit der
Debug-Signatur). Damit kannst du jederzeit prüfen, ob die Datei echt und unverändert ist.

| | |
|---|---|
| **Zertifikatsinhaber** | `CN=Online Soccer, OU=App, O=Online Soccer, C=DE` |
| **Algorithmus** | RSA, Schlüssellänge 2048 Bit |
| **Signaturschema** | APK Signature Scheme v2 |
| **Gültig ab** | 25.09.2026 |
| **SHA-256-Fingerprint** | `C9:67:D5:43:C9:68:E2:83:C9:D9:D9:82:9D:D9:B4:33:AB:A1:BC:46:B3:10:52:9A:D3:29:2F:FC:58:C0:DD:69` |

**Prüfschritte**

```bash
# 1. Datei-Hash
sha256sum OnlineSoccer-1.2.1-release.apk
# 1.2.1: fe26db8f0d2a8093500c336fd739488d1d40a554e015941569af8a363fa5d157

# 2. Signatur und Zertifikat
apksigner verify --print-certs --verbose OnlineSoccer-1.2.1-release.apk
```

Beide Werte für jede Version stehen in den [Release-Notizen](https://github.com/barezi5527/OnlineSoccer-Download/releases).

Der **Erstinstaller-Fingerprint** bleibt über alle Updates hinweg unverändert. Zeigt die
App in den Einstellungen unter „App installieren" einen anderen Fingerprint, ist die APK
nicht von diesem Projekt.

---

## Bekannte Einschränkungen

Offen und bewusst kommuniziert – damit du die Bewertung selbst treffen kannst:

| Thema | Bewertung |
|---|---|
| **Kein Zertifikat-Pinning** | Die App prüft Zertifikate über den System-Trust-Store, nicht gegen einen fest verdrahteten Pin. Auf einem Gerät mit manipulierter Trust-Liste (z. B. erzwungener Unternehmensproxy) wäre ein MITM-Angriff theoretisch möglich. Für den Normalbetrieb ist das der übliche Standard. |
| **Keine Code-Verschleierung** | Die APK ist nicht per R8/ProGuard minimiert und dadurch leichter analysierbar. Sie beeinträchtigt die Funktionalität nicht. |
| **HTTP-Cache im Klartext** | Zwischengespeicherte Seiteninhalte liegen unverschlüsselt im App-Cache. Auf einem gerooteten Gerät wären sie lesbar. Durch `allowBackup="false"` ist die Ausweitung auf Backups begrenzt. |
| **Abmelden invalidiert die Serversitzung nicht vollständig** | Der dauerhafte Login-Token bleibt serverseitig gültig, bis er abläuft. Auf gemeinsam genutzten Geräten solltest du die App beim Wechsel abmelden. |
| **Server-URLs werden nicht per Host-Allowlist geprüft** | Pfade aus Spielinhalten werden übernommen, bevor der Cookie-Speicher die Domaingrenze greift. Praktisch relevant nur bei kompromittiertem Server. |
| **Nicht im Play Store veröffentlicht** | Die App wird nicht automatisch aktualisiert. Neue Versionen musst du manuell herunterladen. |

---

## Sicherheitsaudit

Die App wurde einem statischen Sicherheitsaudit nach **OWASP MASVS / MASTG** unterzogen
(Quellcode, Build-Konfiguration, Manifest, Ressourcen, Git-Historie, Signaturkonfiguration,
zusätzlich empirische Prüfung der gebauten APK).

**Ergebnis: keine kritischen oder verteilungsverhindernden Befunde.**

Geprüft und bestätigt:

- keine eingebetteten Zugangsdaten, API-Keys oder privaten Schlüssel im Projekt
- Keystore und `keystore.properties` sind per `.gitignore` ausgeschlossen und **nie**
  committet worden
- Login nur über HTTPS, Passwort weder gespeichert noch protokolliert
- Token-Ablage verschlüsselt
- keine WebView, keine `addJavascript`-Brücke, keine dynamisch geladenen Skripte
- minimaler Berechtigungssatz (siehe oben)
- kein Logging sensibler Daten im Produktivcode
- keine personenbezogenen Daten realer Personen im Projekt – die Testdaten bestehen
  ausschließlich aus virtuellen Spieldaten und werden nicht in die APK gepackt

Nicht geprüft wurde die **Sicherheit des Spiel-Servers** (`os.ongapo.com`): TLS-Konfiguration,
Sitzungsverwaltung und Server-seitige Schutzmechanismen liegen außerhalb dieser App und
außerhalb der Verantwortung dieses Projekts.

---

## Meldung einer Sicherheitslücke

Wenn du eine Schwachstelle findest, melde sie bitte **nicht** als öffentliches Issue.

1. Öffne ein **privates** Issue über
   [*Security Advisories*](https://github.com/barezi5527/OnlineSoccer-Download/security/advisories/new)
   – oder nutze das Kontaktformular, falls dir das lieber ist.
2. Beschreibe: betroffene Version, Android-Version, betroffenes Gerät, Schritt-für-Schritt-
   Anleitung zur Reproduktion und die beobachtete Auswirkung.
3. Bitte **keine** Daten Dritter, keine fremden Zugangsdaten und keine aktiven Exploits
   beifügen.
4. Du erhältst eine Bestätigung des Eingangs. Nach Behebung und Veröffentlichung einer
   neuen Version wird die Meldung in den Release-Notizen und im Änderungsprotokoll
   gewürdigt – auf Wunsch namentlich.

**Was nicht als Schwachstelle gilt:** Fehler in der Darstellung von Spielinhalten, die vom
Spielserver geliefert werden, sowie Probleme des Spiel-Servers selbst.

---

## Sicherheitsrelevante Änderungen

Vollständige Liste aller Versionen: [CHANGELOG.md](CHANGELOG.md).

### 1.2.1 – 2026-10-08

- Keine neuen Android-Berechtigungen; die Berechtigungsliste bleibt unverändert.
- Das Release-Zertifikat und der Erstinstaller-Fingerprint bleiben gegenüber 1.2.0 unverändert.

### 1.2.0 – 2026-10-06

- Keine neuen Android-Berechtigungen; die Berechtigungsliste bleibt unverändert.
- A-Team-Berufungen laden Position, Name und Vertrag dynamisch vom Server; erst der
  separat bestätigte finale Schritt sendet die Beförderung.
- Release-Zertifikat und Erstinstaller-Fingerprint bleiben gegenüber 1.1.0 unverändert.

### 1.1.0 – 2026-10-02

**Keine sicherheitsrelevanten Änderungen.** Der Quellcode ist ab dieser Version
öffentlich (GPL-3.0); der Funktionsumfang und der Berechtigungssatz bleiben
unverändert. Signatur und Erstinstaller-Fingerprint sind identisch zu 1.0.0.

### 1.0.0 – 2026-09-27

**Hinzugefügt**
- Signaturprüfung: Fingerprint des Erstinstallers in [README](README.md#signatur--und-integritätsprüfung) dokumentiert
- SHA-256-Prüfsumme je Release als eigenes Artefakt
- Sicherheitsrichtlinie und Berechtigungsübersicht als eigene Dokumente

**Geändert**
- Release-Signierung von der Debug-Signatur auf einen eigenen RSA-2048-Release-Keystore
  umgestellt
- Verschlüsselte Token-Ablage über Android Keystore (AES-256-GCM), `allowBackup="false"`
- Klartext-Verkehr global deaktiviert
- `.gitignore` erweitert, damit Keystore, `keystore.properties` und Credentials-Dateien
  niemals ins Repository gelangen
- Debug-Hilfsansicht auf `exported="false"` gesetzt und ausschließlich in Debug-Builds
  belassen (in der Release-APK nicht enthalten)
