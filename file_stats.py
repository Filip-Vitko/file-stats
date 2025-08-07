from datetime import date, datetime
import collections
import math
import os
import sys

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def format_file_size(size: int) -> int:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"

def get_all_files(folder_path: str) -> list[str]:
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]

def get_file_size(file_list, total_files) -> str:
    file_sizes: list = [os.stat(file).st_size for file in file_list]
    sizes_names: list = list(zip(file_sizes, [os.path.split(file)[1] for file in file_list]))
    #sizes_names_2: list = list(zip([os.stat(file).st_size for file in file_list], [os.path.split(file)[1] for file in file_list]))

    if not sizes_names:
        return "No file found", "No file found"

    biggest = max(sizes_names)
    smallest = min(sizes_names)
    mean = format_file_size(round(sum(file_sizes) / total_files))

    biggest_file: str = f"{biggest[1]} ({format_file_size(biggest[0])})" if biggest is not None else "No file found"
    smallest_file: str = f"{smallest[1]} ({format_file_size(smallest[0])})" if smallest is not None else "No file found"

    return biggest_file, smallest_file, mean

def get_file_types(file_list) -> list[int]:
    file_extensions: list = [os.path.splitext(file)[1] for file in file_list]
    counter = collections.Counter(file_extensions)
    
    total_files = sum(counter.values())
    py_files = counter.get(".py", 0)
    txt_files = counter.get(".txt", 0)
    jpg_files = counter.get(".jpg", 0)
    zip_files = counter.get(".zip", 0)
    other_files = total_files - py_files - txt_files - jpg_files - zip_files

    return {"py" : py_files,
            "txt" : txt_files,
            "jpg" : jpg_files,
            "zip" : zip_files,
            "other" : other_files,
            "total" : total_files}

def get_file_date(file_list) -> list[str]:
    file_modified_times = [
    (os.stat(file).st_mtime, os.path.split(file)[1])
    for file in file_list
    ]

    oldest = min(file_modified_times, key=lambda x: x[0])
    newest = max(file_modified_times, key=lambda x: x[0])
    formatted_oldest = datetime.fromtimestamp(oldest[0]).strftime("%Y-%m-%d %H:%M:%S")
    last_modified_delta = str(datetime.now() - datetime.fromtimestamp(newest[0])).split('.')[0]
    formatted_modified_file: list = [datetime.fromtimestamp(newest[0]).strftime("%Y-%m-%d %H:%M:%S"), last_modified_delta]

    return formatted_oldest, formatted_modified_file

def create_backup_path() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(script_dir, "log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    now = datetime.now().isoformat()
    filename = os.path.join(log_dir, f"{now}.txt")
    return filename

def report_string(folder_path: str, file_list: list, types: list, biggest_file: int, smallest_file: int, mean_file: int, oldest_file: datetime, last_modified_file: datetime, backup_path: str):
    dash: str = '-' * 50
    return  f"""📁 Folder: {folder_path}
{dash}
Total files: {types['total']}
File types: \n    .py:     {types['py']}\n    .txt:    {types['txt']}\n    .jpg:    {types['jpg']}\n    .zip:    {types['zip']}\n    others:  {types['other']} \n
Biggest file:              {biggest_file}
Smallest file:             {smallest_file}
Mean file size:            {mean_file}
Oldest modified file:      {oldest_file}
Last modified:             {last_modified_file[0]} -> {last_modified_file[1]} ago\n
✅ Backup created:         {backup_path}"""

def cli(folder_path) -> None:
    clear()
    file_list: list = get_all_files(folder_path)
    assert file_list != []
    types = get_file_types(file_list)
    biggest_file, smallest_file, mean_file = get_file_size(file_list, types['total'])
    oldest_file, last_modified_file = get_file_date(file_list)

    backup_path = create_backup_path()
    report = report_string(folder_path, file_list, types, biggest_file, smallest_file, mean_file, oldest_file, last_modified_file, backup_path)

    with open(backup_path, 'w') as file:
        file.write(report)

    print(report)

def start():
    folder_path: str = input("Please provide an path to folder: ")
    if folder_path.lower() in ['e', 'exit', 'n', 'quit']:
        clear()
        sys.exit(0)
    if os.path.isdir(folder_path) == True:
        cli(folder_path)
    else:
        print("Incorrect path please start again")
        start()
        
clear()
start()