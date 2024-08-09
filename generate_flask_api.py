import csv

def generate_code_from_csv(csv_file):
    # Lesen der Spaltenköpfe aus der CSV-Datei
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)

    # Generierung des neuen Python-Codes
    code = f"""
from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime
import csv

app = Flask(__name__)

letzte_sortierte_daten = []

def validate_data(data):
    required_keys = {{"{headers[0]}", "{headers[1]}", "{headers[2]}", "{headers[3]}", "{headers[4]}"}}  # Angepasste Spaltenköpfe
    for entry in data:
        if not required_keys.issubset(entry.keys()):
            return False
    return True

def filter_data(data, prozess=None, start_date=None, end_date=None):
    filtered_data = data
    if prozess:
        filtered_data = [entry for entry in filtered_data if entry['{headers[3]}'] == prozess]
    if start_date:
        filtered_data = [entry for entry in filtered_data if datetime.strptime(entry['{headers[1]}'], "%Y-%m-%d %H:%M:%S") >= start_date]
    if end_date:
        filtered_data = [entry for entry in filtered_data if datetime.strptime(entry['{headers[2]}'], "%Y-%m-%d %H:%M:%S") <= end_date]
    return filtered_data

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

    def mergesort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    inversions = analyze_data(arr)
    if inversions < len(arr) // 2:
        return sorted(arr, key=key)
    else:
        return mergesort(arr)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_data():
    global letzte_sortierte_daten

    sort_key = request.form['sort_key']
    prozess_filter = request.form.get('prozess_filter')
    start_date_filter = request.form.get('start_date_filter')
    end_date_filter = request.form.get('end_date_filter')

    # CSV-Datei einlesen
    data = []
    with open('zufaellige_prozessdaten.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({{
                "{headers[0]}": row['{headers[0]}'],
                "{headers[1]}": row['{headers[1]}'],
                "{headers[2]}": row['{headers[2]}'],
                "{headers[3]}": row['{headers[3]}'],
                "{headers[4]}": row['{headers[4]}']
            }})

    if not validate_data(data):
        return jsonify({{"error": "Ungültige Daten"}}), 400

    data = filter_data(data, prozess_filter, datetime.strptime(start_date_filter, "%Y-%m-%dT%H:%M") if start_date_filter else None, datetime.strptime(end_date_filter, "%Y-%m-%dT%H:%M") if end_date_filter else None)

    if sort_key == "{headers[1]}":
        sorted_data = hybrid_sort(data, key=lambda x: datetime.strptime(x['{headers[1]}'], "%Y-%m-%d %H:%M:%S"))
    elif sort_key == "{headers[2]}":
        sorted_data = hybrid_sort(data, key=lambda x: datetime.strptime(x['{headers[2]}'], "%Y-%m-%d %H:%M:%S"))
    elif sort_key == "{headers[0]}":
        sorted_data = hybrid_sort(data, key=lambda x: int(x['{headers[0]}']))
    elif sort_key == "{headers[3]}":
        sorted_data = hybrid_sort(data, key=lambda x: x['{headers[3]}'])
    else:
        return jsonify({{"error": "Ungültiger Sortierschlüssel"}}), 400

    letzte_sortierte_daten = sorted_data

    return redirect(url_for('show_sorted_data'))

@app.route('/show_sorted_data', methods=['GET'])
def show_sorted_data():
    return render_template('results.html', data=letzte_sortierte_daten)

if __name__ == '__main__':
    app.run(debug=True)
    """

    return code

# Beispielanwendung
csv_file = 'zufaellige_prozessdaten.csv'
generated_code = generate_code_from_csv(csv_file)
print(generated_code)
