# Flask-basierte API zur Sortierung von Prozessdaten

## Projektübersicht

Dieses Projekt implementiert eine RESTful API, die es ermöglicht, Prozessdaten in einer CSV-Datei nach verschiedenen Kriterien zu sortieren. Die sortierten Daten werden dann auf einer HTML-Seite angezeigt. Die API ist in Flask implementiert und nutzt einen hybriden Sortieralgorithmus, der basierend auf der Anzahl der Inversionen in den Daten zwischen einer direkten Sortierung und QuickSort wechselt.

## Inhalt

- [Projektübersicht](#projektübersicht)
- [Installation](#installation)
- [Nutzung](#nutzung)
- [API-Endpunkte](#api-endpunkte)
- [Sortieralgorithmus](#sortieralgorithmus)
- [HTML-Ausgabe](#html-ausgabe)
- [Beispieldaten](#beispieldaten)
- [Verbesserungsmöglichkeiten](#verbesserungsmöglichkeiten)

## Installation

### Voraussetzungen

Stellen Sie sicher, dass Python 3.x installiert ist. Die folgenden Python-Pakete müssen installiert werden:

- Flask
- Requests

Sie können die Pakete mit `pip` installieren:

```bash
pip install Flask requests
```

### Projektstruktur

Das Projekt sollte die folgende Struktur haben:

```bash
project_root/
│
├── zufaellige_prozessdaten.csv  # CSV-Datei mit den Prozessdaten
├── sort_api.py                  # Hauptskript, das die Flask-API startet
├── call_sort_api.py             # Skript, das die API aufruft und die sortierten Daten anzeigt
├── templates/                   # Ordner für HTML-Vorlagen
│   └── results.html             # HTML-Vorlage für die Ausgabe der sortierten Daten
└── README.md                    # Dieses README-Dokument
```

## Nutzung

### Starten der Flask-API

Um den Flask-Server zu starten, führen Sie das `sort_api.py`-Skript aus:

```bash
python sort_api.py
```

Der Server wird unter `http://127.0.0.1:5000` ausgeführt.

### Aufrufen der API

Verwenden Sie das `call_sort_api.py`-Skript, um eine `POST`-Anfrage an die API zu senden, die die Daten sortiert und die HTML-Seite mit den Ergebnissen im Browser öffnet:

```bash
python call_sort_api.py
```

## API-Endpunkte

### POST `/sort`

- **Beschreibung**: Sortiert die übergebenen Prozessdaten nach dem angegebenen Kriterium.
- **Anfragemethode**: `POST`
- **Parameter**:
  - `key`: Der Sortierschlüssel (z.B. `id`, `StartUhrZeit`, `EndUhrzeit`, `Prozess`).
  - `data`: Die zu sortierenden Daten (JSON-Array).
- **Antwort**:
  - Erfolgreich: Eine JSON-Antwort mit einem Redirect-Link zu der Seite mit den sortierten Daten.
  - Fehlerhaft: Eine JSON-Antwort mit einer Fehlermeldung.

### GET `/show_sorted_data`

- **Beschreibung**: Zeigt die zuletzt sortierten Daten in einer HTML-Tabelle an.
- **Anfragemethode**: `GET`
- **Antwort**: Eine HTML-Seite mit den sortierten Daten.

## Sortieralgorithmus

Der in diesem Projekt verwendete hybride Sortieralgorithmus analysiert zunächst die Anzahl der Inversionen in den Daten. Wenn die Anzahl der Inversionen relativ gering ist, wird die eingebaute Python-Sortiermethode verwendet. Andernfalls wird ein QuickSort-Algorithmus angewendet. Dieser Ansatz bietet eine gute Balance zwischen Stabilität und Geschwindigkeit, abhängig von der Reihenfolge der Daten.

### Pseudocode:

```python
def hybrid_sort(arr, key=lambda x: x):
    def analyze_data(arr):
        inversions = sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if key(arr[i]) > key(arr[j]))
        return inversions

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr) // 2])
        left = [x for x in arr if key(x) < pivot]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if key(x) > pivot]
        return quicksort(left) + middle + quicksort(right)

    if len(arr) <= 1:
        return arr

    inversions = analyze_data(arr)
    if inversions < len(arr) // 2:
        return sorted(arr, key=key)
    else:
        return quicksort(arr)
```

## HTML-Ausgabe

Die sortierten Daten werden auf einer HTML-Seite angezeigt. Die Seite ist einfach gehalten, mit einer Tabelle, die die Felder `id`, `StartUhrZeit`, `EndUhrzeit`, `Prozess`, und `Betreff` enthält. Die HTML-Seite wird durch das Flask-Framework generiert und verwendet die `results.html`-Vorlage im `templates`-Ordner.

**Beispielhafte Tabelle:**

```html
<table border="1">
    <tr>
        <th>ID</th>
        <th>StartUhrZeit</th>
        <th>EndUhrzeit</th>
        <th>Prozess</th>
        <th>Betreff</th>
    </tr>
    <!-- Hier werden die sortierten Daten eingetragen -->
</table>
```

## Beispieldaten

Die Beispieldaten (`zufaellige_prozessdaten.csv`) enthalten 1000 Datensätze mit den folgenden Spalten:

- `id`: Eindeutige ID des Prozesses
- `StartUhrZeit`: Startzeit des Prozesses
- `EndUhrzeit`: Endzeit des Prozesses
- `Prozess`: Name des Prozesses
- `Betreff`: Betreff des Prozesses

## Verbesserungsmöglichkeiten

- **Optimierung des Sortieralgorithmus**: Der hybride Sortieralgorithmus könnte weiter optimiert werden, um spezifischere Kriterien für den Wechsel zwischen direkter Sortierung und QuickSort zu verwenden.
- **Erweiterung der API**: Die API könnte erweitert werden, um weitere Operationen auf den Prozessdaten zu unterstützen, wie z.B. das Filtern oder Aggregieren.
- **Benutzeroberfläche**: Eine benutzerfreundlichere Oberfläche könnte hinzugefügt werden, um den Benutzern die Auswahl der Sortierkriterien und das Hochladen von CSV-Dateien zu ermöglichen.

## Kontakt

Falls Sie Fragen oder Probleme mit dem Projekt haben, können Sie sich gerne an den Entwickler wenden.


