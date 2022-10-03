__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


def clean_cache():
    path = os.path.abspath("files/cache")
    if os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.abspath("files/cache") + "/" + file)
        print("Cache is empty")
    else:
        os.mkdir(path)
        print("New folder made in files")

    return clean_cache


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path, "r") as zip:
        zip.extractall(cache_dir_path)
        print("Zipfile extracted in cache")
    return


def cached_files():
    path = os.path.abspath("files\cache")
    list_cached_files = []
    for file in os.listdir(path):
        file_path = str(os.path.abspath(path)+"\\" + file)
        list_cached_files.append(file_path)
    return list_cached_files


def find_password(list_of_file_paths: list) -> str:
    for file_path in list_of_file_paths:
        with open(file_path, "r")as file:
            for line in file.readlines():
                if "password" in line:
                    password = line.split(" ")
    return password[1][0:-1]
