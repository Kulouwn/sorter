import os
import shutil

source_folder = r"C:\Users\Kulouwn\Downloads" # вашь путь к папке в которой нужна сортировка

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Others": []
}

for folder in file_types.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        destination_folder = "Others"
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = folder
                break
        
        destination_path = os.path.join(source_folder, destination_folder, filename)
        try:
            shutil.move(file_path, destination_path)
            print(f"Переместил {filename} в {destination_folder}")
        except Exception as e:
            print(f"Ошибка при перемещении {filename}: {e}")

print("Сортировка завершена!")