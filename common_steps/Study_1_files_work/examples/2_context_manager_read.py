# from files import TXT_FILE_PATH

TXT_FILE_PATH = "common_steps/study_1_files_work/files/example.txt"

with open(TXT_FILE_PATH, "r") as file:
    print(file.read())
    # No need to call close method

print("\n", 20 * "=", "\n")

with open(TXT_FILE_PATH, "r") as file:
    for line in file.readlines():
        print(line, end='')

print("\n", 20 * "=", "\n")

with open(TXT_FILE_PATH, "r") as file1, open(TXT_FILE_PATH, "r") as file2 :
    for line in file1.readlines():
        print(line, end='!')
    for line in file2.readlines():
        print(line, end='?')