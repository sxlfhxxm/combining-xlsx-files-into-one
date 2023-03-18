import pandas as pd

# Завантажити файли Excel
file1 = pd.read_excel('file1.xlsx')
file2 = pd.read_excel('file2.xlsx')
file3 = pd.read_excel('file3.xlsx')

# Об'єднати файли в один DataFrame
merged_data = pd.concat([file1, file2, file3], ignore_index=True)

# Виконати очищення даних
cleaned_data = merged_data.dropna()  # Видалити рядки з пропущеними значеннями

# Зберегти результат
cleaned_data.to_excel('cleaned_data.xlsx', index=False)
