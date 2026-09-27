# Wie kann ich bei Problemen Hilfe bekommen?

Kurze Antwort: ein **Issue** in diesem Repository eröffnen. Issues sind öffentlich, werden
gelesen und helfen auch anderen Nutzern mit demselben Problem.

## Bei einem Fehler in der App

→ [*Bug melden* mit Vorlage](.github/ISSUE_TEMPLATE/bug_report.yml)

Bitte angeben: **App-Version**, **Android-Version**, **Gerätemodell** und die **Schritte**, mit
denen sich das Problem nachstellen lässt. Ohne diese Angaben kommt man meist nicht weiter.

## Bei einem Wunsch oder einer Idee

→ [*Feature-Wunsch mit Vorlage*](.github/ISSUE_TEMPLATE/feature_request.yml)

## Bei einer Sicherheitslücke

Bitte **kein öffentliches Issue** – so wird es vermieden, dass Details vor der Behebung
verbreitet werden:

→ [*Security Advisory (privat)*](https://github.com/barezi5527/OnlineSoccer-Download/security/advisories/new)
· mehr unter [SECURITY.md](SECURITY.md#meldung-einer-sicherheitslücke)

## Häufige Fragen

**Die Installation wird blockiert.**
Android muss für die manuelle Installation von APKs einmalig die Quelle freigeben. Beim
ersten Öffnen der Datei fragt Android das automatisch und verweist auf die Einstellung
„Unbekannte Apps installieren". Das ist normales Verhalten und kein Fehler der App.

**„App nicht installiert" / Installationsfehler.**
Häufigste Ursache: eine ältere Version derselben App ist installiert und
`versionCode` ist höher. Lösung: App deinstallieren, danach die neue APK installieren und
erneut anmelden. Prüfe außerdem den freien Speicherplatz und die Mindestversion Android 8.0.

**Die APK gilt meinem Virenscanner als unsicher.**
Der Scanner kennt die App nicht und meldet jede unbekannte App. Der Nachweis, dass die Datei
unverändert ist, steht in [SECURITY.md](SECURITY.md#signatur--integritätsprüfung):
SHA-256-Prüfsumme und Zertifikats-Fingerprint sind dort dokumentiert.

**Ich kann mich nicht anmelden / „Server nicht erreichbar".**
Zuerst prüfen, ob [os.ongapo.com](https://os.ongapo.com) im Browser erreichbar ist. Ist die
Website erreichbar, die App schließen und erneut öffnen. Besteht das Problem, bitte ein
Issue mit den Angaben aus der Bug-Vorlage.

**Ich habe ein Update verpasst.**
Neue Versionen stehen immer unter [*Releases*](https://github.com/barezi5527/OnlineSoccer-Download/releases);
das vollständige Änderungsprotokoll in der [CHANGELOG.md](CHANGELOG.md). Es gibt keine
automatische Aktualisierung – die App wird bewusst nicht im Play Store veröffentlicht.

**Wie melde ich mich ab, sodass niemand meine Daten sieht?**
„Abmelden" in der App genügt normalerweise. Für ein vollständiges Löschen: App
deinstallieren. Details unter [PRIVACY.md](PRIVACY.md#daten-auf-deinem-gerät).
