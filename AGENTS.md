# AGENTS.md

Arbeitsanweisungen für dieses Repository. Bei AI-gestützten Beiträgen verbindlich.

## Zweck des Repositories

Dieses Repository ist **ausschließlich** der Download-Bereich der Android-App
**Online Soccer** (Paket `com.onlinesoccer.app`).

Hier gehört hinein:

- die veröffentlichte Release-APK als GitHub-Release-Asset
- das Änderungsprotokoll (`CHANGELOG.md`)
- Sicherheits- und Berechtigungsangaben (`SECURITY.md`)
- Datenschutzangaben (`PRIVACY.md`)
- Support-Dokumentation

Hier gehört **nicht** hinein: der Quellcode-Build. Er bleibt privat. Wer ihn
veröffentlicht, verletzt die Absicht des Projekts.

## Inoffiziell-Kennzeichnung

**Verbindliche Regel: „inoffiziell" gehört in den Titel.**

Die App ist ein inoffizieller Client für `os.ongapo.com`. Es besteht keine Verbindung zu
den Betreibern des Spiels. Diese Kennzeichnung ist für das Projekt rechtlich und
kommunikativ wesentlich und darf nie wegfallen.

Bei **jedem** neuen Release und bei jeder Änderung der Startseite gilt:

| Stelle | Anforderung |
|---|---|
| `README.md`, H1 (erste Zeile) | muss „inoffiziell" enthalten, z. B. `# Online Soccer – inoffizielle App` |
| Release-Titel | muss „inoffiziell" enthalten, z. B. `Online Soccer (inoffiziell) 1.1.0 – <Kurzbeschreibung>` |
| Release-Notizen | müssen den Hinweis auf fehlende Verbindung zu den Betreibern enthalten |
| `SECURITY.md` | Kurzfassung weist auf den inoffiziellen Status hin |
| `PRIVACY.md` | weist auf den inoffiziellen Status hin |
| `LICENSE` | weist auf den inoffiziellen Status hin |
| Release-Asset-Dateiname | **ohne** Zusatz – `OnlineSoccer-<Version>-release.apk` bleibt unverändert |

Grammatik: „inoffiziell" ist ein Adjektiv und muss dekliniert werden. Die Form
`Inoffiziell Online Soccer` ist falsch und darf nicht verwendet werden.

Bewusst **ohne** Kennzeichnung bleiben: der Dateiname der APK sowie das App-Label im
Quellcode (`Online Soccer`). Ein sauberer Dateiname ist gewollt. Das App-Label zu ändern
ist eine Entscheidung des Projekts, keine Dokumentationsauflage – bei entsprechender
Weisung wird `app/src/main/res/values/strings.xml` angepasst.

## Release-Ablauf

1. Im privaten Quellcode-Repo: `./gradlew clean assembleRelease`
2. Signatur prüfen und Werte auslesen:
   ```bash
   ~/Android/Sdk/build-tools/<version>/apksigner verify --print-certs <apk>
   sha256sum <apk>
   ```
3. Asset-Dateiname auf `OnlineSoccer-<versionName>-release.apk` setzen
4. `checksums.txt` mit dem SHA-256 der APK erzeugen und als zweites Asset hochladen
5. Release-Notizen aus dem Änderungsprotokoll ableiten, `versionName`/`versionCode`,
   Größe, SHA-256, Zertifikats-Fingerprint, Mindestversion und Berechtigungen nennen
6. `README.md` und `CHANGELOG.md` auf die neue Version aktualisieren
7. Nach dem Upload gegenprüfen: Download ohne Anmeldung möglich, SHA-256 des heruntergeladenen
   Datei stimmt mit `checksums.txt` und den Notizen überein, Signatur unverändert

## Versionsschema

Semantic Versioning: MAJOR für inkompatible Änderungen, MINOR für neue Funktionen,
PATCH für Fehlerbehebungen. `versionCode` steigt bei jedem Release monoton.

`CHANGELOG.md` folgt [Keep a Changelog](https://keepachangelog.com/de/1.1.0/): Abschnitte
`Hinzugefügt`, `Geändert`, `Entfernt`, `Behoben`, `Sicherheit`.

## Ton der Dokumentation

- Deutsch, Siezen Sie. Sachlich und nüchtern, keine Werbesprache.
- Sicherheitsrelevante Aussagen müssen überprüfbar sein. Keine Behauptung ohne Beleg.
- Bekannte Einschränkungen offen benennen, nicht verschweigen. Wer die App aus einer
  privaten APK-Installation bekommt, soll wissen, worauf er sich einlässt.
- Keine Drittanbieter-Namen als Träger von Sicherheitsversprechen verwenden. Das
  Audit wird nach OWASP MASVS / MASTG geführt, nicht nach Marketing-Claims.

## Inhaltliche Regeln

- Die Berechtigungsliste in `SECURITY.md` muss der `AndroidManifest.xml` entsprechen. Nach
  jeder neuen Berechtigung beide Dateien nachziehen.
- `apksigner`-Fingerprint und SHA-256 gehören in `README.md`, `SECURITY.md`, in die
  Release-Notizen und in `checksums.txt` – bewusst mehrfach, damit jede einzelne Quelle
  nachprüfbar bleibt.
- Adressen und Kontaktwege nicht erfinden. Für Rückfragen dieses Repository und
  `os.ongapo.com` verwenden.
