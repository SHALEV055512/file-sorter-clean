# 📁 File Sorter with CSV Report

An automation script written in Python that organizes files in a specified folder by their type (Excel, PDF, Word, and images), generates a CSV summary, and copies the files into sorted subfolders — all with a single run.

---

## 🧠 Overview

This tool is designed to:

* Automatically identify and categorize files based on extension (`.xlsx`, `.pdf`, `.png`, `.docx`\*)
* Generate a CSV report listing each file and its category
* Create a new `Sorted` folder containing subfolders per category, and copy the matching files into them

Great for office use, backups, or cleaning up your download folders!

> \*Note: The current script uses `.dock` instead of `.docx` — typo can be corrected if needed.

---

## ⚙️ Technologies Used

* **Python 3**
* `os` – Directory and path management
* `shutil` – File copying
* `re` – Regular expressions for extension matching
* `csv` – For report generation

---

## 🗂️ Folder Structure

```
file_sorter_with_csv_report/
├── manage_files.py         # The main script file
├── report.csv              # Auto-generated report after script runs
└── Sorted/                 # Auto-created folder with sorted subfolders
    ├── Excel/
    ├── PDF/
    ├── Word/
    └── Picture/
```

---

## 🚀 How to Run

1. Clone or download the repository.
2. Make sure you have Python 3 installed.
3. Run the script in a terminal:

```bash
python manage_files.py
```

4. When prompted, enter the full path to the folder you want to organize.

---

## ✅ Features

* Handles basic error-checking (folder exists, file type matches)
* Supports Hebrew and Unicode file names
* CSV report created in the working directory
* Keeps original files intact – uses `copy2` to retain metadata

---

## 🔬 Coming Soon

* `unittest` testing suite
* Logging with timestamps
* GUI (Tkinter-based) version

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Fork the project, make your improvements, and open a PR.

---

## 🛡️ Security Note

This script does not access the internet or handle sensitive data. Safe to run in isolated folders.

---

## 📬 Contact

Built with 💡 by **Shalev Harari**
If you like it, feel free to ⭐️ the project or reach out via GitHub!
