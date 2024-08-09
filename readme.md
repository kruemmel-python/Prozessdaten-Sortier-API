
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

### Projekt klonen

Klonen Sie dieses Repository auf Ihren lokalen Computer:

```bash
git clone https://github.com/kruemmel-python/Prozessdaten-Sortier-API.git
cd Prozessdaten-Sortier-API
```

## Nutzung

Starten Sie den Flask-Server mit dem folgenden Befehl:

```bash
python sort_api.py
```

Öffnen Sie einen Webbrowser und navigieren Sie zu `http://127.0.0.1:5000`, um die Anwendung zu nutzen.

### API-Endpunkte

- **`/sort`**: Dieser Endpunkt akzeptiert POST-Anfragen, um die Prozessdaten zu sortieren. Die Daten werden anhand der in der Anfrage angegebenen Kriterien sortiert und als HTML-Seite angezeigt.

#### Beispiel für eine POST-Anfrage:

```python
import requests

url = 'http://127.0.0.1:5000/sort'
data = {
    "key": "StartUhrZeit",
    "data": [...]  # Hier kommen die zu sortierenden Daten im JSON-Format
}

response = requests.post(url, json=data)
print(response.text)
```

## Sortieralgorithmus

Der hybride Sortieralgorithmus in diesem Projekt ist eine Kombination aus direkter Sortierung und QuickSort. Der Algorithmus analysiert die Anzahl der Inversionen in den Daten, um zu entscheiden, welche Methode effizienter ist. Bei einer geringen Anzahl von Inversionen wird eine direkte Sortierung verwendet, ansonsten QuickSort.

### Optimierung des Algorithmus

In zukünftigen Versionen könnte der Algorithmus durch adaptive Inversionsanalyse, zusätzliche Sortiermethoden und Parallelisierung weiter optimiert werden.

## HTML-Ausgabe

Die sortierten Daten werden auf einer HTML-Seite angezeigt, die durch Flask generiert wird. Es gibt zwei Hauptdateien:

- **index.html**: Ermöglicht dem Benutzer die Auswahl der Sortierkriterien und das Filtern der Daten.
- **results.html**: Zeigt die sortierten Daten basierend auf den ausgewählten Kriterien an.

## Beispieldaten

In der Datei `zufaellige_prozessdaten.csv` finden Sie Beispielprozessdaten, die zum Testen der API verwendet werden können.

## Verbesserungsmöglichkeiten

### 1. Optimierung des Sortieralgorithmus

- **Adaptive Inversionsanalyse**: Dynamische Anpassung der Schwelle für den Wechsel der Sortiermethode.
- **Erweiterung der Sortiermethoden**: Hinzufügen von MergeSort oder HeapSort.
- **Parallelisierung**: Beschleunigung des Sortierprozesses durch Parallelisierung.

### 2. Erweiterung der API

- **Filtern der Daten**: Hinzufügen von Funktionen zum Filtern und Aggregieren der Daten.
- **Datenvalidierung**: Sicherstellung der Datenintegrität vor der Sortierung.

### 3. Benutzeroberfläche

- **Erweiterung der Weboberfläche**: Hinzufügen von Dropdown-Menüs für die Sortierkriterien, Upload-Funktionen für CSV-Dateien und eine erweiterte Ergebnisanzeige.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Details finden Sie in der `LICENSE.md`-Datei.
