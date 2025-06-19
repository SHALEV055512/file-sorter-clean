import csv
import os
import re
import shutil

def Find_folder(folder_path):
    if os.path.exists(folder_path):
        if os.path.isdir(folder_path):
            print("you have a folder")
            Folder_object(folder_path)
            return None
    return None

def Folder_object(folder_path):
    file_dict = {
        "Excel": [],
        "Picture": [],
        "Word": [],
        "PDF": []
    }
    for filename in os.listdir(folder_path):
        if re.search(r"(\w+)\.xlsx", filename):
            file_dict["Excel"].append(filename)
        elif re.search(r"(\w+)\.png", filename):
            file_dict["Picture"].append(filename)
        elif re.search(r"(\w+)\.dock", filename):
            file_dict["Word"].append(filename)
        elif re.search(r"(\w+)\.pdf", filename):
            file_dict["PDF"].append(filename)
    Make_csv_file(file_dict)
    Make_Folders(file_dict, folder_path)

def Make_csv_file(file_dict):
    output_file = "report.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Category"])

        for category, files in file_dict.items():
            for filename in files:
                writer.writerow([filename, category])
    print(f"CSV file created at: {os.path.abspath(output_file)}")

def Make_Folders(file_dict, folder_path):
    sorted_path = os.path.join(folder_path, "Sorted")
    os.makedirs(sorted_path, exist_ok=True)
    for category, files in file_dict.items():
        category_folder = os.path.join(sorted_path, category)
        os.makedirs(category_folder, exist_ok=True)

        for filename in files:
            src_path = os.path.join(folder_path, filename)
            dst_path = os.path.join(category_folder, filename)

            if os.path.exists(src_path):
                shutil.copy2(src_path, dst_path)

if __name__ == '__main__':
    user_input = input("📂 Enter the full path to the folder you'd like to organize:\n")
    Find_folder(user_input)
