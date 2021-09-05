import os

def string_quantity(file):
    quantity = len(file.readlines())
    return quantity

def get_file_list(path):
    files_list = []
    for roots, dirs, files in os.walk(path):
        for file in files:
            files_list.append(file)
    return files_list

def sort_files(file_list):
    unsorted_list = {}
    for files in file_list:
        with open('list/' + files, 'r', encoding='utf-8') as file:
            unsorted_list[files] = string_quantity(file)
    sorted_list = sorted(unsorted_list, key=unsorted_list.get)
    return sorted_list

def write_sorted_files(sorted_files):
    with open('result/result.txt', 'a', encoding='utf-8') as result_file:
        for files in sorted_files:
            result_file.write(f'{files}\n')
            with open('list/' + files, 'r', encoding='utf-8') as file:
                result_file.write(f'{(string_quantity(file))}\n')
            with open('list/' + files, 'r', encoding='utf-8') as file:
                data = file.read()
                result_file.write(f'{data}\n')

file_list = get_file_list('list/')
sorted_files = sort_files(file_list)
write_sorted_files(sorted_files)
