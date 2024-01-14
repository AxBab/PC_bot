from os import system, chdir
from settings import programm_dir

def create_folder(text):
    folder_name = text.split()[2].capitalize()
    
    chdir("C:/Users/Алексей/Desktop")
    system(f"md {folder_name}")
    chdir(programm_dir)


def remove_folder(text):
    folder_name = text.split()[2].capitalize()

    chdir("C:/Users/Алексей/Desktop")
    system(f"rmdir {folder_name}")
    chdir(programm_dir)