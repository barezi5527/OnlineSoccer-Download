# Datenschutz

Was die App **Online Soccer** mit deinen Daten macht – kurz und ohne Floskeln.

> **Kurzfassung:** Deine Zugangsdaten gehen ausschließlich an den Spielserver. Es gibt kein
> Tracking, keine Analyse, keine Werbung und keine Drittanbieter-SDK. Der Betreiber dieser App
> erhält keine Kopie deiner Daten.

---

## Wer ist verantwortlich?

| | |
|---|---|
| **Verantwortlich für die App** | das Projekt *Online Soccer (Android)*, veröffentlicht über [`@barezi5527`](https://github.com/barezi5527) |
| **Verantwortlich für die Spielinhalte** | der Betreiber von [os.ongapo.com](https://os.ongapo.com) |

Diese App ist ein **inoffizieller** Client. Sie steht in keiner Verbindung zu den Betreibern
des Spiels. Beim Anmelden akzeptierst du die Nutzungsbedingungen des Spielbetreibers – die
App überträgt sie nicht und ersetzt sie nicht.

---

## Welche Daten die App verarbeitet

| Daten | Zweck | Speicherung |
|---|---|---|
| **E-Mail und Passwort** | einmalig zur Anmeldung am Spielserver | Passwort: **nur im Arbeitsspeicher**, nie gespeichert, nie protokolliert |
| **Session-Token** | hält die Anmeldung aufrecht | verschlüsselt auf dem Gerät (Android Keystore, AES-256-GCM) |
| **Spielinhalte** (Kader, Tabellen, Ergebnisse, Nachrichten, Verträge) | Anzeige in der App | teilweise als Zwischenspeicher im App-Cache, um Ansichten schnell zu laden |
| **Deine Aktionen im Spiel** (Aufstellung, Transfers, ZAT-Eingaben) | werden an den Spielserver übertragen und dort nach den Spielregeln gespeichert | beim Spielserver |

**Wichtig:** Alles, was du in der App tust, ist eine Aktion im Spiel und landet damit beim
Spielserver – genau wie beim Spielen im Browser. Die App ist kein eigenständiges
Datenverarbeitungssystem, sondern ein Client für den bestehenden Spielserver.

---

## Was diese App **nicht** macht

- ❌ **Kein Tracking** – keine Analytics, keine Nutzungsstatistiken, keine Absturzberichte
- ❌ **Keine Werbe-ID**, kein Fingerprinting, kein Geräte-Fingerprint
- ❌ **Keine Drittanbieter-SDKs**, die Daten erhalten könnten
- ❌ **Kein Zugriff** auf Kamera, Mikrofon, Standort, Kontakte, Galerie oder Dateien
- ❌ **Keine Weitergabe** deiner Daten an den App-Betreiber oder an sonstige Dritte
- ❌ **Kein Cloud-Backup** der App-Daten (`allowBackup="false"`)
- ❌ **Kein Klartext-Verkehr** – die Verbindung zum Spielserver ist durchgehend verschlüsselt

---

## Daten auf deinem Gerät

| Ort | Inhalt | Löschbar durch |
|---|---|---|
| App-interne verschlüsselte Ablage | Session-Token | Abmelden oder App deinstallieren |
| App-Cache (Zwischenspeicher) | Spielinhalte, um Ansichten schnell zu laden | Android automatisch, oder: App → Speicher → Cache leeren |
| Login-Auswahl des Systems | gespeicherte E-Mail-Adresse (Autofill) | Android-Einstellungen → Passwörter & Konten |

**App vollständig entfernen:** Einstellungen → Apps → Online Soccer → Deinstallieren.
Damit sind alle lokalen Daten gelöscht. Dein Spielkonto beim Spielserver bleibt davon
unberührt – dort musst du die Daten selbst über die Website löschen lassen.

---

## Auf dem Spielserver

Beim Anmelden gelten die Datenschutzbestimmungen des Spielbetreibers
([os.ongapo.com](https://os.ongapo.com)). Die App überträgt deine Zugangsdaten direkt dorthin –
sie werden von keiner Zwischenstation zwischengespeichert oder umgeleitet. Für Auskunft,
Berichtigung oder Löschung deiner Spielkontodaten ist der Spielbetreiber zuständig.

---

## Ihre Rechte

Sofern die App selbst personenbezogene Daten verarbeitet, gelten die üblichen Rechte
(Auskunft, Berichtigung, Löschung, Widerspruch). In der Praxis speichert die App nur den
Session-Token auf deinem eigenen Gerät; alle übrigen Daten liegen beim Spielbetreiber.

Anfragen zu diesem Repository und zu den Release-Dateien bitte über die
[GitHub-Themen dieses Repositories](https://github.com/barezi5527/OnlineSoccer-Download/issues)
oder per privater Nachricht an [`@barezi5527`](https://github.com/barezi5527).

---

## Änderungen an dieser Erklärung

Jede Anpassung wird im [Änderungsprotokoll](CHANGELOG.md) vermerkt. Wesentliche Änderungen
werden zusätzlich in den Release-Notizen der betroffenen Version genannt.

---

## Siehe auch

- [Sicherheit & Berechtigungen](SECURITY.md) – technische Details zu Berechtigungen, Signatur und Audit
- [Änderungsprotokoll](CHANGELOG.md) – alle Versionen
