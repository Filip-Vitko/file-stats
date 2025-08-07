# 📁 File Stats Reporter

A simple Python CLI tool to analyze and summarize statistics about files in a specified folder.  
Outputs include file type breakdown, size statistics, and last modified timestamps. A backup report is generated for each run.

> ⚙️ **Project Goal:**  
> This project was built as part of a personal exercise to get more familiar with Python's most-used built-in modules such as `os`, `datetime`, `collections`, and `sys`.  
> It helped reinforce concepts like file handling, CLI interaction, and simple formatting logic.

## 🧰 Features

- Counts total files and categorizes by extension
- Displays:
  - Largest and smallest file (by size)
  - Mean file size (formatted in B, KB, MB...)
  - Oldest and most recently modified file
  - Time since last modification (delta)
- Generates a clean text report
- Automatically saves a backup `.txt` report in a `log/` folder

## 💻 Example Output
```
📁 Folder: /path/to/folder
Total files: 23
File types:
.py: 18
.txt: 1
.jpg: 0
.zip: 0
others: 4

Biggest file: imports.csv (2.5 MB)
Smallest file: contact_list.py (0 B)
Mean file size: 232.4 KB
Oldest modified file: 2025-02-26 11:03:32
Last modified: 2025-08-05 09:34:53 -> 2 days, 7:16:22 ago

✅ Backup created: ./log/2025-08-07T16:51:16.txt
```
## 🚀 Usage

Run the script and enter a valid folder path:
```python file_stats.py```

## 🗃️ Requirements
Python 3.10+  
No external dependencies

## 📂 Structure
```
file_stats.py
log/
  └── [timestamp].txt     # Generated reports
```

## ⚖️ License
This project is licensed under the MIT License.
