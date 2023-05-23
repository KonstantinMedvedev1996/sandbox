# from files import TXT_FILE_PATH

TXT_FILE_PATH = 'common_steps/study_1_files_work/examples/example.txt'

# TXT_FILE_PATH = "example.txt"

some_file = open(TXT_FILE_PATH, "r")

# some_file = open("example.txt", "r")

# Read the exact bites amount
# print(some_file.read(7))
# print(some_file.readline())


# Read a single line
# print(some_file.readline())
# print(some_file.readline())
# print(some_file.readline())
# print(some_file.readline())

# some_file.seek(0)


# print(some_file.readline())
# print(some_file.readline())


# Get all lines as list
# print(some_file.readlines(), "\n")

# Read from current cursor position till the end
# print(some_file.read())

a = some_file.read()
print(a)

# Position cursor within the file
# some_file.seek(0)

# To open it as writable use r+
# some_file.write("test")

some_file.close()
