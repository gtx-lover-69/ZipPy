import time
from zipfile import ZipFile
import os

from colorama.ansi import clear_screen
from tqdm import tqdm

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create(directory):
    def get_all_file_paths(directory):
        global total
        total = 0
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
                total += 1
        return file_paths
    file_path = get_all_file_paths(directory)
    print(file_path)
    with ZipFile(directory +'.zip', 'w') as zip:
        os.chdir(directory)
        with tqdm(range(total), desc="Zipping", colour="blue", ascii="―━") as pbar:
            for file in file_path:
                zip.write(file)
                pbar.update(1)

        print('Zipped successfully!')

def extract(file):
    try:
        with ZipFile(file, 'r') as zip:
            k = file.split('\\')
            t = k[-1]
            print('Extracting...')
            zip.extractall()
            print(t,'extracted')
    except Exception as e:
        print(e)

def main():
    print("Welcome to Zippy!")
    choice = input("""    1. Extract archive (.zip or .rar)
    2. Create archive
    """)
    if choice == '1':
        while True:
            directory = input("Enter the directory of the archive you want to extract: ").strip('"')

            if os.path.isfile(directory):
                break

            print('Directory does not exist!')
            time.sleep(1)
            clear_screen()

        extract(directory)



if __name__ == '__main__':
    main()