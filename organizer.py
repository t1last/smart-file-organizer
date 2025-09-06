import os
import shutil
from pathlib import Path

downloads_path = Path.home() / "Downloads"

folders = ["Images", "Documents", "Archives", "Other"]
for folder in folders:
    (downloads_path / folder).mkdir(exist_ok=True)

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

def main():
    print("🐍 Начинаю сортировку файлов в Загрузках...")
    moved_files = 0
    for file_path in downloads_path.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()
            moved = False

            for folder, extensions in file_types.items():
                if extension in extensions:
                    target_dir = downloads_path / folder
                    shutil.move(str(file_path), str(target_dir / file_path.name))
                    print(f"✅ Перемещен: {file_path.name} -> {folder}/")
                    moved = True
                    moved_files += 1
                    break

            if not moved:
                target_dir = downloads_path / "Other"
                shutil.move(str(file_path), str(target_dir / file_path.name))
                print(f"➡️  Перемещен в Other: {file_path.name}")
                moved_files += 1

    print(f"🎉 Готово! Обработано файлов: {moved_files}")

if __name__ == "__main__":
    main()
