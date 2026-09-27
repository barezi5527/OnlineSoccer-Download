<div align="center">

# Inoffiziell Online Soccer

**Die Android-App für das Online-Fußballspiel – [_os.ongapo.com_](https://os.ongapo.com)**

[![Release](https://img.shields.io/badge/Release-v1.0.0-2ea44f)](https://github.com/barezi5527/OnlineSoccer-Download/releases/tag/v1.0.0)
[![Android](https://img.shields.io/badge/Android-8.0%2B-3DDC84)](https://developer.android.com/about/versions/oreo)
[![Lizenz](https://img.shields.io/badge/Lizenz-MIT-blue)](LICENSE)
[![Signiert](https://img.shields.io/badge/Signatur-valid%20%2B%20Release--3DDC84)](#signatur--und-integrit%C3%A4tspr%C3%BCfung)
[![Sicherheit](https://img.shields.io/badge/Berechtigungen-2-orange)](#berechtigungen-der-app)

[⬇️ APK herunterladen (v1.0.0)](https://github.com/barezi5527/OnlineSoccer-Download/releases/latest/download/OnlineSoccer-1.0.0-release.apk)
&nbsp;&nbsp;·&nbsp;&nbsp;
[📋 Änderungsprotokoll](CHANGELOG.md)
&nbsp;&nbsp;·&nbsp;&nbsp;
[🛡️ Sicherheit & Berechtigungen](SECURITY.md)
&nbsp;&nbsp;·&nbsp;&nbsp;
[🔒 Datenschutz](PRIVACY.md)

</div>

---

## Was ist das?

**Online Soccer** ist einManagerspiel im Browser: Du übernimmst einen Verein, gibst die
Taktik vor, beobachtest die Spieltage (ZAT) und treibst deinen Verein in der Liga nach oben.

Diese App ist der **native Android-Client** für dieses Spiel. Sie bringt das komplette
Spiel in eine App, die sich wie eine native Anwendung anfühlt – mit eigener Navigation,
Bottom-Bar, Dark Mode und Zwischenspeichern statt WebView.

> **Hinweis:** Diese App ist **kein** offizielles Produkt von *ongapo* und steht in keiner
> Verbindung zu den Betreibern des Spiels. Sie ist ein inoffizieller, von der Community
> entwickelter Client. Alle Spielinhalte, Spieler- und Vereinsdaten stammen von
> `os.ongapo.com` und unterliegen den dortigen Nutzungsbedingungen. Du brauchst ein
> bestehendes Online-Soccer-Konto, um dich anzumelden.

---

## ⬇️ Download

| | |
|---|---|
| **Version** | 1.0.0 (versionCode 1) |
| **Datei** | [`OnlineSoccer-1.0.0-release.apk`](https://github.com/barezi5527/OnlineSoccer-Download/releases/latest/download/OnlineSoccer-1.0.0-release.apk) |
| **Größe** | 15,9 MB |
| **SHA-256** | `f243b676c94b282e6a500326e119f428b5b4a33acc1e962f4623036a5cceea68` |
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

Alternativ ohne Dateimanager:

```bash
# adb aus den Android-Backtüren, erreichbar mit Platform-Tools
adb install OnlineSoccer-1.0.0-release.apk
```

**Hinweise**

- Ein Upgrade der App funktioniert ohne Datenverlust – `versionCode` steigt monoton.
- Ein Downgrade ist mit Android blockiert. Bei Problemen: App deinstallieren, APK neu
  installieren, mit dem eigenen Konto erneut anmelden.
- Die App ist **nicht** im Google Play Store. Das ist Absicht: der Quellcode-Build ist bewusst
  nicht über Dritte verteilt und lässt sich so jederzeit unabhängig prüfen.

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
| **Team** | Teaminformationen (auch fremde Vereine), Spielerkarte, Vereins- und Mannschaftsseiten, Freundschaften |
| **Bewerbe** | Spieltag-Auswahl mit Saisonfilter, Landespokal, Internationale Spiele |
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
sha256sum OnlineSoccer-1.0.0-release.apk
# erwartet: f243b676c94b282e6a500326e119f428b5b4a33acc1e962f4623036a5cceea68
```

**2. Signaturzertifikat prüfen**

```bash
apksigner verify --print-certs OnlineSoccer-1.0.0-release.apk
```

| Feld | Wert |
|---|---|
| Inhaber | `CN=Online Soccer, OU=App, O=Online Soccer, C=DE` |
| Algorithmus | RSA 2048 |
| Gültig ab | 25.09.2026 |
| SHA-256-Fingerprint | `C9:67:D5:43:C9:68:E2:83:C9:9D:98:29:DD:9B:43:3A:B4:A3:3A:C1:1E:96:2F:F4:62:30:36:32:60:DD:69` |

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

Bitte gib bei Bugreports immer an: App-Version (`1.0.0`), Android-Version, Gerätemodell und
was genau passiert bzw. was du erwartet hast.

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

**Online Soccer 1.0.0** – entwickelt für die Community, nicht verifiziert.
<sub>Der Quellcode-Build ist privat. Dieses Repository enthält ausschließlich
Release-Artefakte, die veröffentlichte App-Version und deren Dokumentation.</sub>

</div>
