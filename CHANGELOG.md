# Änderungsprotokoll

Alle nennenswerten Änderungen an **Online Soccer** für Android werden in diesem Dokument
festgehalten.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
die Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).

---

## [Unveröffentlicht]

### Geändert

- **Lizenzwechsel MIT → GPL-3.0.** App und Dokumentation stehen ab sofort unter
  der GNU General Public License Version 3. Die bis 27.09.2026 gültige
  MIT-Einordnung ist aufgehoben.
- Der Quellcode der App ist unter
  [barezi5527/OnlineSoccer](https://github.com/barezi5527/OnlineSoccer)
  öffentlich einsehbar und unter GPL-3.0 mitwirkbar.
- Die Startseite hat einen neuen Abschnitt „Quellcode & Mitwirken" mit
  Verweis auf das Quellcode-Repository und die Contributing-Anleitung.

### Geändert (Dokumentation)

- `AGENTS.md`: Die frühere Vorgabe, den Quellcode geheim zu halten, ist
  aufgehoben. Ton-Vorgabe auf Du-Ansprache vereinheitlicht.

Hinweis: Das veröffentlichte Release-Artefakt ist von dieser Änderung nicht
betroffen – die APK wurde nicht neu gebaut, ihre SHA-256-Prüfsumme in diesem
Repository gilt unverändert weiter. Die Umstellung der Lizenz wirkt sich auf
künftige Builds aus.

---

## [1.0.0] – 2026-09-27

Erste öffentliche Version. Die App stellt das vollständige Online-Soccer-Spiel als nativen
Android-Client bereit.

### hinzugefügt

**Grundfunktionen**
- Anmeldung am Online-Soccer-Konto mit verschlüsselter Session-Speicherung
- Dashboard mit Kaderüberblick, nächstem Spieltag und Vertrags-/Jugendspieler-Hinweisen
- Spieltag (ZAT) mit Aufstellung, Einwechslungen inkl. Sonderplätzen, ZAT-Editor sowie
  Zuzu- und Zugabgabe
- Taktikbereich mit Formation, Positionszuweisung und Spielsystem-Editor
- Teambereich mit Teaminformationen, Spielerkarte, Vereins- und Mannschaftsseiten
  sowie Freundschaften
- Private Nachrichten mit Posteingang, Gesendet-Bereich und Trainer-PN direkt aus der
  Vereins- und Spielerkarte
- Server-Bereiche: Freie Teams, Zweitteams, Managerliste und Manager-Suche

**Spieltag-Auswertung**
- Spielbericht mit einheitlichem Spielverlauf und namentlicher Zuordnung aller Ereignisse
- Spielerstatistik mit **Elf-Noten (K1–K5)** aus einem gewichteten Bewertungsmodell
  (Tore, Vorlagen bis 4., Zweikampfquote und -Quantität, gemessene Kantenspiele)
- KI-Pressekonferenz mit getrennten Kommentaren von Heim- und Gasttrainer sowie
  Tor-Zwischenständen; das Endergebnis wird erst am Schluss genannt
- **Elf des Spieltags** für alle Ligen, mit Land-/Liga-Auswahl und Zwischenspeicherung je
  Saison und Spieltag
- **Statistiken**-Bereich mit Top-Teams, Topscorer, Topspieler, Fairplay, Spielersuche,
  Spielervergleich sowie Spiel- und Tabellenstatistiken – inklusive Filtern und fixierbaren
  Tabellen

**Wirtschaft & Transfers**
- Transfermarkt, Versteigerungsmarkt, „Auf den VM setzen", eigene Gebote, Leihe,
  Transferstatus und Übersicht der letzten Aktionen
- Spielerscout mit sechs Kategorien live aus der Spielersuche-Engine

**Stadion**
- Stadionausbau mit Kapazitätsanzeige, Schätz-Hinweis und plausiblerer Tribünenverteilung
- Stadionplan mit VIP-Streifen auf der Haupttribüne und vergrößertem Barrierefrei-Bereich
- Rasenmuster, Premium-Ausstattung und Saisonwechsel

**Oberfläche**
- Native Bottom-Navigation mit kontextabhängigen Unterbereichen
- Dark Mode inklusive eigener Farbpalette
- Drehschnellbomben-resistente Ansichten (`configChanges` für Orientation, Bildschirmgröße
  und Tastatur)
- Zwischenspeicher für das Dashboard mit 30-Sekunden-TTL und Anfrage-Zusammenführung, damit
  ein Ansichtswechsel nur einen einzigen Request auslöst

### geändert
- Spielersuche, Top-Spieler- und Fairplay-Tabellen auf eine gemeinsame Statistik-Oberfläche
  umgestellt
- Statistik-Tabellen: robuste fixierte Kopf- und Spaltenausrichtung auch bei mehr als zehn
  Zeilen, kompaktere Spaltenbreiten, einklappbare Filter
- Ligatabellen-Erkennung auf mehrere CSS-Klassen erweitert, Tabelle `kader1` wird priorisiert
- Vertragswarnung beim Anmelden, wenn ein Vertrag höchstens zwei ZAT Restlaufzeit hat
- Rückmeldung „Server nicht erreichbar" beim Anmeldeversuch
- Stadionname wird im Spielbericht als eigener Anzeigename geführt
- UTF-8-Dekodierung und Namens-Einfärbung im Spielverlauf vereinheitlicht
- Login-Oberfläche mit markanter Primärfarbe, Autofill für Zugangsdaten
- Bottom-Navigation: Tippen auf den aktiven Tab führt immer zur ersten Übersicht

### behoben
- ZAT-Aufstellung: Klick auf einen Spieler im Mannschaftskader öffnet die Spielerkarte
  an der richtigen Stelle
- Einwechslung: Position bzw. Sonderplatz ist nicht mehr Pflichtfeld, Zeile/Spalte wurden
  durch einen Sonderplatz auf Kartenposition oder als Torwart ersetzt
- ZAT-Report: vorausgewählter Spieltag ist der letzte ZAT, Saison- und ZAT-Filter über
  Dropdowns
- PM: Empfänger-Suche gegen veraltete Antworten abgesichert (Versionsschutz)
- Empfangsbestätigung: Der Briefumschlag-Badge wird zuverlässig aktualisiert
- Dashboard: Popup bei Verlust eines Jugendspielers
- Statistiken: fehlende Synchronisation der fixierten Spalte behoben

### sicherheit
- Umstellung auf einen eigenen Release-Keystore statt Debug-Signatur (RSA 2048)
- Verschlüsselte Token-Ablage über Android Keystore mit AES-256-GCM
- Klartext-Verkehr global deaktiviert (`usesCleartextTraffic="false"`)
- `allowBackup="false"` – keine Sicherung der App-Daten in Cloud-Backups
- Entfernung eines ungenutzten Serialization-Plugins
- `.gitignore` um lokale Arbeits- und Dokumentationsdateien erweitert, damit keine
  Zugangsdaten oder Keystores ins Repository gelangen

---

## Versionsschema

- **MAJOR** – inkompatible Änderung, die eine Neuinstallation oder Datenmigration erfordert
- **MINOR** – neue Funktionen, rückwärtskompatibel
- **PATCH** – Fehlerbehebungen, rückwärtskompatibel

---

## Links zu Releases

Die jeweils veröffentlichten Dateien stehen unter:
[**github.com/barezi5527/OnlineSoccer-Download/releases**](https://github.com/barezi5527/OnlineSoccer-Download/releases)

[Unveröffentlicht]: https://github.com/barezi5527/OnlineSoccer-Download/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/barezi5527/OnlineSoccer-Download/releases/tag/v1.0.0
