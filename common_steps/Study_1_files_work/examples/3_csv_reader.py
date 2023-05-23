import csv
from csv import DictReader

# from files import CSV_FILE_PATH

CSV_FILE_PATH = 'common_steps/study_1_files_work/files/users.csv'

with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(dict(zip(header, row)))

print(100 * "+")

# with open(CSV_FILE_PATH, newline='') as f:
#     reader = csv.reader(f)

#     # Извлекаем заголовок
#     header = next(reader)

#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)

# with open('../files/users.csv', newline='') as f:
#     reader = DictReader(f)

#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)

with open(CSV_FILE_PATH, newline='') as f:
    reader = DictReader(f)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
