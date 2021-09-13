# Задание №3
import pickle, os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
    if file.endswith('.dat'):
        file_to_print = open(file, 'rb')
        result = pickle.load(file_to_print)
        print(result)
