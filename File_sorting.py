import os
import shutil
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------------- CATEGORY MAP ----------------------
# You can edit this anytime to add/remove extensions
CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".js", ".html", ".css", ".java",".c"],
    "PPT_sildes": [".pptx"],
    "Application": [".exe"],
}

# -----------------------------------------------------------

def organize_folder(path):
    if not os.path.exists(path):
        print(Fore.RED + "❌ Folder does not exist.")
        return

    print(Fore.CYAN + f"\n📁 Organizing: {path}\n")

    # List only files, not folders
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    if not files:
        print(Fore.YELLOW + "⚠ No files found to organize.")
        return

    categories = {}

# ---------------------- GROUPING FILES ----------------------
    for i in files:
        x = os.path.splitext(i)[1].lower()  # get extension
        category_found = False

        # Check which category this extension belongs to
        for category, extensions in CATEGORY_MAP.items():
            if x in extensions:
                categories.setdefault(category, []).append(i)
                category_found = True
                break

        # If no category matched → put in Others
        if not category_found:
            categories.setdefault("Others", []).append(i)

# ---------------------- MOVING FILES ----------------------
    for category, file_list in tqdm(categories.items(), desc="Organizing", colour="green"):
        folder_path = os.path.join(path, category)

        # Make the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for j in file_list:
            src = os.path.join(path, j)
            dest = os.path.join(folder_path, j)

            # If file with same name already exists → rename to avoid overwrite
            if os.path.exists(dest):
                name, extension = os.path.splitext(j)
                dest = os.path.join(folder_path, f"{name}_copy{extension}")

            shutil.move(src, dest)

    print(Fore.GREEN + "\n🎉 Done! Files have been organized.\n")

# -----------------------------------------------------------

if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ").strip().replace('"', '')
    organize_folder(folder_path)
