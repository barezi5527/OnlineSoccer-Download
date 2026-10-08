<div align="center">

# Online Soccer (inoffizielle) App

**Die Android-App für das Online-Fußballspiel – [_os.ongapo.com_](https://os.ongapo.com)**

[![Release](https://img.shields.io/badge/Release-v1.2.1-2ea44f)](https://github.com/barezi5527/OnlineSoccer-Download/releases/tag/v1.2.1)
[![Android](https://img.shields.io/badge/Android-8.0%2B-3DDC84)](https://developer.android.com/about/versions/oreo)
[![Lizenz](https://img.shields.io/badge/Lizenz-GPL--3.0-blue)](LICENSE)
[![Signiert](https://img.shields.io/badge/Signatur-valid%20%2B%20Release--3DDC84)](#signatur--und-integrit%C3%A4tspr%C3%BCfung)
[![Sicherheit](https://img.shields.io/badge/Berechtigungen-2-orange)](#berechtigungen-der-app)

[⬇️ APK herunterladen (v1.2.1)](https://github.com/barezi5527/OnlineSoccer-Download/releases/latest/download/OnlineSoccer-1.2.1-release.apk)
&nbsp;&nbsp;·&nbsp;&nbsp;
[📊 Downloadzähler](https://barezi5527.github.io/OnlineSoccer-Download/)
&nbsp;&nbsp;·&nbsp;&nbsp;
[📋 Änderungsprotokoll](CHANGELOG.md)
&nbsp;&nbsp;·&nbsp;&nbsp;
[🛡️ Sicherheit & Berechtigungen](SECURITY.md)
&nbsp;&nbsp;·&nbsp;&nbsp;
[🔒 Datenschutz](PRIVACY.md)

</div>

---

## Was ist das?

**Online Soccer** ist ein Managerspiel im Browser: Du übernimmst einen Verein, gibst die
Taktik vor, beobachtest die Spieltage (ZAT) und treibst deinen Verein in der Liga nach oben.

Diese App ist der **native Android-Client** für dieses Spiel. Die App bildet mittlerweile 
schon ziemlich viele Bereiche von Online Soccer ab – von Dashboard, ZAT und Taktik über Kader, 
Transfers und Statistiken bis hin zu Spielberichten, Bewerben, Stadion und weiteren Funktionen.

> **Hinweis:** Diese App ist **kein** offizielles Produkt von *ongapo* und steht in keiner
> Verbindung zu den Betreibern des Spiels. Sie ist ein inoffizieller, von der Community
> entwickelter Client. Alle Spielinhalte, Spieler- und Vereinsdaten stammen von
> `os.ongapo.com` und unterliegen den dortigen Nutzungsbedingungen. Du brauchst ein
> bestehendes Online-Soccer-Konto, um dich anzumelden.

Alternativdomains: https://www.online-soccer.eu & https://www.os-zeitungen.com

## ⬇️ Download

| | |
|---|---|
| **Version** | 1.2.1 (versionCode 4) |
| **Datei** | [`OnlineSoccer-1.2.1-release.apk`](https://github.com/barezi5527/OnlineSoccer-Download/releases/latest/download/OnlineSoccer-1.2.1-release.apk) |
| **Größe** | 16,0 MB |
| **SHA-256** | `fe26db8f0d2a8093500c336fd739488d1d40a554e015941569af8a363fa5d157` |
| **Mindestversion** | Android 8.0 (Oreo, API 26) |
| **Zielversion** | Android 15 (API 35) |
| **Paketname** | `com.onlinesoccer.app` |
| **Preis** | kostenlos, keine Werbung, keine In-App-Käufe |

Alle Versionen mit vollständigem Änderungsprotokoll findest du unter
[**Releases**](https://github.com/barezi5527/OnlineSoccer-Download/releases).

### Installation

1. APK-Datei aus dem [Release](https://github.com/barezi5527/OnlineSoccer-Download/releases/latest) herunterladen.
2. Prüfsumme kontrollieren (siehe [Integritätsprüfung](#signatur--und-integrit%C3%A4tspr%C3%BCfung)).
3. Die Datei auf dem Gerät öffnen.
4. Beim ersten Mal fragt Android nach der Erlaubnis für **„Unbekannte Apps installieren"** –
   das ist die normale Freigabe für jede manuell installierte APK. Danach startet die App.


**Hinweise**

- Ein Upgrade der App funktioniert ohne Datenverlust – `versionCode` steigt monoton.
- Ein Downgrade ist mit Android blockiert. Bei Problemen: App deinstallieren, APK neu
  installieren, mit dem eigenen Konto erneut anmelden.
- Die App ist **nicht** im Google Play Store. Das ist Absicht: Die APK hier ist
  signiert und mit einer SHA-256-Prüfsumme versehen, und der Quellcode ist unter
  [GPL-3.0](https://github.com/barezi5527/OnlineSoccer/blob/main/LICENSE) offen.
  Damit kannst du prüfen, was auf deinem Gerät landet, und die App selbst bauen.

### 📊 Downloadzähler

Wie oft wurde welche APK-Version heruntergeladen? Die Zählung steht auf einer eigenen
Seite: **<https://barezi5527.github.io/OnlineSoccer-Download/>**

| | |
|---|---|
| **Seite** | <https://barezi5527.github.io/OnlineSoccer-Download/> |
| **Aktualisierung** | stündlich geprüft, geschrieben wird nur bei einer Zahlenänderung; zusätzlich direkt nach jedem Release |
| **Datenquelle** | die Downloadzähler der Release-Assets von GitHub |

Die Werte liest ein Workflow ([.github/workflows/download-count.yml](.github/workflows/download-count.yml))
stündlich über die GitHub-API und schreibt sie nach
[`docs/downloads.json`](docs/downloads.json). Die Seite ruft selbst keine API ab, weil
die unauthentifizierte GitHub-API nur 60 Anfragen pro Stunde und IP erlaubt.
Stehen die Zahlen unverändert, erzeugt der Workflow keinen Commit.

**Einschränkung, offen benannt:** GitHub zählt jeden Abruf der Release-Datei. Das
schließt automatisierte Abrufe, Vorschau-Links und Spiegelungen mit ein. Die Zahl ist
also die Zahl der Dateiabrufe, nicht die Zahl der verschiedenen Installationen.
Auf der Seite werden keine Besucherdaten, IP-Adressen oder Cookies erhoben.

---

## ✨ Funktionen

| Bereich | Was drin ist |
|---|---|
| **Dashboard** | Kaderüberblick, nächster Spieltag, Vertrags- und Jugendspieler-Hinweise, Schnellzugriff auf alle Hubs |
| **Spieltag (ZAT)** | Aufstellung, Einwechslungen mit Sonderplätzen, ZAT-Editor, Zuzu-/Zugabgabe, Vereinigungsübersicht |
| **Taktik** | Formation, Positionszuweisung, Spielsystem-Editor |
| **Spielbericht** | Einheitlicher Spielverlauf, Spielerstatistik mit **Elf-Noten (K1–K5)**, KI-Pressekonferenz mit Heim-/Gasttrainer-Kommentaren, Live-Zwischenstände nach Toren |
| **Elf des Spieltags** | Für alle Ligen, Land-/Liga-Auswahl, Zwischenspeicherung je Saison und Spieltag |
| **Statistiken** | Top-Teams, Topscorer, Topspieler, Fairplay, Spielersuche, Spielervergleich, Spiel- und Tabellenstatistiken – mit fixierbaren Tabellen und Filtern |
| **Transfers** | Transfermarkt, Versteigerungsmarkt, „Auf den VM setzen", eigene Gebote, Leihe, Transferstatus, letzte Aktionen |
| **Team** | Teaminformationen (auch fremde Vereine), Spielerkarte, Verletzungen im Kader, Trainer einstellen und feuern, Freundschaften |
| **Jugendteam** | Vier überarbeitete Bereiche, dynamische Positions-/Namens-/Vertragsauswahl bei A-Team-Berufungen |
| **Bewerbe** | Spieltag-Auswahl mit Saisonfilter, Landespokal, OSC-/OSE-Qualifikationen mit Hin- und Rückspielanzeige, Siegerhinweis auf Wunsch, Club-Ranking mit Vereinssuche |
| **Server-Bereiche** | Freie Teams, Zweitteams, Managerliste, Manager-Suche |
| **Private Nachrichten** | Posteingang, Gesendet, Trainer-PN direkt aus Verein- und Spielerkarte, Ungelesen-Badge |
| **Stadion & Ausstattung** | Stadionausbau mit Kapazitätsanzeige, Tribünenverteilung, Rasenmuster, Premium-Ausstattung, Saisonwechsel |
| **Spielerscout** | Sechs Kategorien live aus der Spielersuche-Engine |
| **Oberfläche** | Native Bottom-Navigation, Dark Mode, Offline-Zwischenspeicher mit TTL, Rotation ohne Datenverlust |

---

## 🔐 Sicherheit auf einen Blick

| | |
|---|---|
| **Berechtigungen** | nur 2 – `INTERNET` und `ACCESS_NETWORK_STATE` |
| **Kamera, Mikrofon, Standort, Kontakte, Speicher** | ❌ werden nicht angefordert |
| **Datenverkehr** | ausschließlich HTTPS; Klartext ist global deaktiviert (`usesCleartextTraffic="false"`) |
| **Session-Token** | verschlüsselt (AES-256-GCM) über Android Keystore abgelegt, `allowBackup="false"` |
| **Passwort** | wird nie gespeichert, nie protokolliert, nur während des Logins im Arbeitsspeicher gehalten |
| **Tracking / Analytics** | keiner – keine Drittanbieter-SDKs, keine Werbe-IDs |
| **Signatur** | offiziell mit einem eigenen RSA-2048-Release-Zertifikat signiert |

Ausführliche Angaben, inklusive Sicherheitsaudit und bekannter Einschränkungen:
**[SECURITY.md](SECURITY.md)**

---

## Signatur- und Integritätsprüfung

Damit du sicher sein kannst, dass die APK unverändert und vom Projekt stammt:

**1. SHA-256 der Datei vergleichen**

```bash
sha256sum OnlineSoccer-1.2.1-release.apk
# erwartet: fe26db8f0d2a8093500c336fd739488d1d40a554e015941569af8a363fa5d157
```

**2. Signaturzertifikat prüfen**

```bash
apksigner verify --print-certs OnlineSoccer-1.2.1-release.apk
```

| Feld | Wert |
|---|---|
| Inhaber | `CN=Online Soccer, OU=App, O=Online Soccer, C=DE` |
| Algorithmus | RSA 2048 |
| Gültig ab | 25.09.2026 |
| SHA-256-Fingerprint | `C9:67:D5:43:C9:68:E2:83:C9:D9:D9:82:9D:D9:B4:33:AB:A1:BC:46:B3:10:52:9A:D3:29:2F:FC:58:C0:DD:69` |

**3. Prüfen, ob der Erstinstaller-Zertifikats-Fingerprint in der App-Info-Ansicht
„App installieren" steht** – dieser bleibt über alle Updates hinweg gleich.

---

## 🐛 Fehler melden & mitmachen

Issues und Diskussionen laufen öffentlich in diesem Repository – das ist der schnellste Weg
zu einer Korrektur:

- **Bug melden** → [*Bug reporten*](.github/ISSUE_TEMPLATE/bug_report.yml)
- **Wunsch äußern** → [*Feature request*](.github/ISSUE_TEMPLATE/feature_request.yml)
- **Sicherheitslücke** → **nicht** als Issue, sondern wie in
  [SECURITY.md](SECURITY.md#meldung-einer-sicherheitslücke) beschrieben melden.

Bitte gib bei Bugreports immer an: App-Version (`1.2.1`), Android-Version, Gerätemodell und
was genau passiert bzw. was du erwartet hast.

---

## 🧑‍💻 Quellcode & Mitwirken

**Der Quellcode der App ist seit dem 02.10.2026 öffentlich** – unter der
[GPL-3.0-Lizenz](https://github.com/barezi5527/OnlineSoccer/blob/main/LICENSE).

| | |
|---|---|
| **Repository** | [barezi5527/OnlineSoccer](https://github.com/barezi5527/OnlineSoccer) |
| **Lizenz** | GPL-3.0 |
| **Sprache / Stack** | Kotlin, Jetpack Compose, Hilt, OkHttp, Jsoup |
| **Mindestversion** | Android 8.0 (API 26), Build gegen API 35 |

### Wann welcher Weg?

- **Du willst die App benutzen?** Nimm die APK hier oben. Das ist der
  empfohlene Weg – vorkompiliert, signiert, mit Prüfsumme.
- **Du willst mitentwickeln?** Nimm den Quellcode. Du brauchst JDK 17 und das
  Android SDK API 35, dann genügt `./gradlew :app:assembleDebug`.

### Selbst bauen

```bash
git clone https://github.com/barezi5527/OnlineSoccer.git
cd OnlineSoccer
export ANDROID_HOME=$HOME/Android/Sdk
  ./gradlew :app:testDebugUnitTest   # 37 Testklassen
./gradlew :app:assembleDebug
```

Eine Schritt-für-Schritt-Anleitung steht in der
[README des Quellcode-Repos](https://github.com/barezi5527/OnlineSoccer#mitwirken).

### Was beitragen?

Beiträge sind ausdrücklich willkommen. Der Einstieg lohnt sich besonders in
diesen Bereichen:

| Bereich | Warum |
|---|---|
| **Barrierefreiheit** | TalkBack, Bedienbarkeit mit großer Schrift |
| **Übersetzungen** | Texte liegen derzeit fest auf Deutsch vor |
| **Parser-Robustheit** | os.ongapo.com ändert sein Layout gelegentlich |
| **Tests** | 37 Testklassen bei 150 Produktions-Kotlin-Dateien – Luft nach oben |
| **Dokumentation** | Teils veraltete Analyse-Dokumente im Repo |

Bitte lies vor dem ersten Pull Request die
[CONTRIBUTING.md](https://github.com/barezi5527/OnlineSoccer/blob/main/CONTRIBUTING.md).
Sicherheitslücken bitte **nicht** als Issue melden, sondern wie in
[SECURITY.md](SECURITY.md#meldung-einer-sicherheitslücke) beschrieben.

### Was GPL-3.0 für dich bedeutet

Du darfst den Code lesen, ändern, bauen und weitergeben. Wenn du eine veränderte
Fassung an Dritte weitergibst, musst du **auch diese** unter GPL-3.0
veröffentlichen. Das ist der einzige Vorbehalt – und der Grund, warum die App
nicht in einer geschlossenen Kopie weiterverkauft werden kann.

---

## 📄 Weitere Dokumente

| Datei | Inhalt |
|---|---|
| [CHANGELOG.md](CHANGELOG.md) | Vollständiges Änderungsprotokoll aller Versionen |
| [SECURITY.md](SECURITY.md) | Berechtigungen im Detail, Sicherheitsaudit, Signatur, Meldeweg für Lücken |
| [PRIVACY.md](PRIVACY.md) | Welche Daten verarbeitet werden, was **nicht** erhoben wird |
| [LICENSE](LICENSE) | Lizenzbedingungen |

---

<div align="center">

**Online Soccer 1.2.1 (inoffiziell)** – entwickelt für die Community.
<sub>Der Quellcode steht unter GPL-3.0 offen zur Verfügung:
<a href="https://github.com/barezi5527/OnlineSoccer">barezi5527/OnlineSoccer</a>.
Dieses Repository enthält die Release-Artefakte, die veröffentlichte App-Version
und deren Dokumentation.</sub>

</div>
