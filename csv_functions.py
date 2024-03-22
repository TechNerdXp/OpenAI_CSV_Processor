import csv

def load_titles(file_path, already_done):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        titles = list(reader)
    return [title[0] for title in titles if title[0] not in already_done]

def load_already_done(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return [vals[0] for vals in rows]

def save_message(file_path, row):
    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
