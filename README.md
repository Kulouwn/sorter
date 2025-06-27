# File Sorter
Python-скрипт для сортировки файлов в папке по типам (изображения, документы, видео).

## Функции
- Сортирует файлы по расширениям (.jpg, .pdf, .mp4 и т.д.).
- Создает папки: Images, Documents, Videos, Others.
- Обрабатывает ошибки при перемещении.

## Установка
1. Установите Python 3.x.
2. Скопируйте код из `sorter.py`.
3. Укажите путь к папке в переменной `source_folder`.
4. Запустите: `python sorter.py`.

## Пример
До:
- TestFolder/photo.jpg
- TestFolder/doc.pdf
После:
- TestFolder/Images/photo.jpg
- TestFolder/Documents/doc.pdf