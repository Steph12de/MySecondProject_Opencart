# OpenCart – Automatisiertes Testing einer E-Commerce-Webanwendung mit Python
Dieses Projekt demonstriert ein automatisiertes Testframework zur Qualitätssicherung zentraler Funktionen der Open-Source-E-Commerce-Plattform **OpenCart**, entwickelt mit **Selenium und Python**. 
Ziel ist es, die Funktionalität und Stabilität der Anwendung effizient durch automatisierte Tests sicherzustellen.

# Projektziele
- Entwicklung eines strukturierten Testframeworks zur Qualitätssicherung
- Validierung zentraler Funktionalitäten wie Registrierung, Login, Produktsuche, Warenkorb und Checkout
- Aufbau eines stabilen und wartbaren Testprozesses

# Projektumfang
-  Erstellung eines strukturierten **Testplans** und mehrerer **Testfälle**
-  Durchführung von **funktionalen Tests**
-  Identifikation, Dokumentation und Nachverfolgung von **Fehlern (Bugs)**
-  Integration von **Git** zur Versionskontrolle
-  Einsatz von **Jenkins** zur CI/CD-Automatisierung
-  Verwendung eines **Jira Scrum Boards** zur agilen Aufgabenplanung und Fortschrittsverfolgung


# Eingesetzte Technologien
- **Python 3.12.2**
- **Selenium WebDriver**
- **Pytest** (Test-Framework)
- **Jenkins** (CI/CD)
- **Git & GitHub**
- **Jira** (Scrum Board)

#  Projektstruktur (Beispiel)
opencart-tests/
├── base/ # Basisklassen (z. B. BaseDriver)
├── Configuration/ # Konfigurationsdateien
├── Logs/ # Automatisch generierte Log-Dateien
├── pageObjects/ # Page Object Model-Klassen
├── Reports/ # Testberichte (z. B. HTML Reports)
├── Screenshots/ # Screenshots bei Fehlern oder zur Dokumentation
├── testcases/ # Testskripte (z. B. Login, Checkout, Suche)
├── Testdata/ # Externe Testdaten (CSV, Excel)
├── utilites/ # Hilfsfunktionen (z. B. Logger, Leser für Excel/JSON)
└── README.md # Projektdokumentation

# Notizen
Dieses Projekt dient dem Ausbau meiner Kenntnisse im Bereich Testautomatisierung mit Python.
Es wird kontinuierlich erweitert – unter anderem mit:
- Zusätzlichen Testfällen
- Integrationstests und CI/CD
