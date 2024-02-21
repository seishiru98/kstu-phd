import glob
import os

# Папка, из которой нужно удалить файлы
folder_path = 'Dissertation'  # Используем прямой слэш или удвоенный обратный слэш

# Шаблон имени файлов для удаления (например, все файлы с расширением .aux)
pattern = '*.aux'

# Файлы, которые нужно удалить вне зависимости от шаблона
files_to_delete = ['thesis-kstu.aux', 'thesis-kstu.bbl', 'thesis-kstu.bcf', 'thesis-kstu.blg',
                   'thesis-kstu.lof', 'thesis-kstu.log', 'thesis-kstu.lot', 'thesis-kstu.nlo',
                   'thesis-kstu.out', 'thesis-kstu.run.xml', 'thesis-kstu.synctex.gz', 'thesis-kstu.toc']

# Получение списка файлов, соответствующих шаблону, в указанной папке
files_to_delete_in_folder = glob.glob(os.path.join(folder_path, pattern))

# Объединение списков
files_to_delete += files_to_delete_in_folder

# Удаление файлов
for file in files_to_delete:
    try:
        os.remove(file)
        print(f'{file} удален успешно')
    except OSError as e:
        print(f'Ошибка при удалении {file}: {e.strerror}')

