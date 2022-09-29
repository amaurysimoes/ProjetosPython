import os
import re
import shutil

# função para encontrar os arquivos
# function to find the files

def find_files(pattern, path):
    for path, dirs, files in os.walk(path):
        for filename in files:
            full_file_name = os.path.join(path, filename)
            match = re.match(pattern, full_file_name)
            if match:
                yield full_file_name

# função para copiar os arquivos encontrados
# function to copy match files
def copy_files(pattern, src_path, dest_path):
    for full_file_name in find_files(pattern, src_path):
        #print(full_file_name)
        try:
            shutil.copy(full_file_name, dest_path)
        except IOError:
            pass

if __name__ == '__main__':
    copy_files('.', 'C:/Temp', 'D:/')

    def files_path01(*args):
        for item in args:
            for p, _, files in os.walk(os.path.abspath(item)):
                for file in files:
                    print(os.path.join(p, file))
    files_path01('D:/')
