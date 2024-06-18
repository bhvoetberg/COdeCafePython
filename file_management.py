import os

file_path = '/home/rober/Downloads'

print(file_path)

files = os.listdir(file_path)
print(files)
print(len(files))

for file in files:
    if 'Bonnetje' in file:
        if os.path.isfile(file_path + '/' + file):
            os.remove(file_path + '/' + file)

files = os.listdir(file_path)
print(len(files))

# if os.path.isfile(file_path):
#     print("Okidoki")
# else:
#     print("Nokidoki")
