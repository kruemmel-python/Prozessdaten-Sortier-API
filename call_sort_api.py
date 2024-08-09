import csv
import requests
import webbrowser

# CSV-Datei einlesen
data = []
with open('zufaellige_prozessdaten.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            "id": row['id'],
            "StartUhrZeit": row['StartUhrZeit'],
            "EndUhrzeit": row['EndUhrzeit'],
            "Prozess": row['Prozess'],
            "Betreff": row['Betreff']
        })

def call_sorting_api(sort_key, data, prozess_filter=None, start_date_filter=None, end_date_filter=None):
    url = 'http://127.0.0.1:5000/sort'
    payload = {
        'key': sort_key,
        'data': data,
        'prozess': prozess_filter,
        'start_date': start_date_filter,
        'end_date': end_date_filter
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        # Öffne die resultierende HTML-Seite im Standardbrowser
        webbrowser.open('http://127.0.0.1:5000/show_sorted_data')
    else:
        print(f"Fehler: {response.status_code}")
        print(response.json())

# Beispiel-Daten aus der CSV sortieren
call_sorting_api(
    sort_key="StartUhrZeit",
    data=data,
    prozess_filter="Prozess_A",  # Optional: Filter nach Prozess
    start_date_filter="2024-08-01 00:00:00",  # Optional: Startdatum-Filter
    end_date_filter="2024-08-02 00:00:00"  # Optional: Enddatum-Filter
)
