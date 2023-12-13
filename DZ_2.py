with open('1.txt', 'r', encoding='utf-8') as file: #читаем каждый файл, считаем количество строк
    lines_1 = len(file.readlines())

with open('2.txt', 'r', encoding='utf-8') as file:
    lines_2 = len(file.readlines())

with open('3.txt', 'r', encoding='utf-8') as file:
    lines_3 = len(file.readlines())

files_lens = [lines_1, lines_2, lines_3]
files_lens_sort = sorted(files_lens) #сортируем

with open('result.txt', 'a', encoding='utf-8') as file:
    file.write(f'файл: 2.txt\n\nколичество строк: {str(files_lens_sort[0])}\n\n')

with open('2.txt', 'r', encoding='utf-8') as first_file, open('result.txt', 'a', encoding='utf-8') as second_file: #содержимое файла добавляем
    counting = 0
    for line in first_file:
        counting += 1
        second_file.write(f'строка №  {counting}  {line}')
    second_file.write('\n\n')

with open('result.txt', 'a', encoding='utf-8') as file:  
    file.write(f'файл: 1.txt\n\nколичество строк: {str(files_lens_sort[1])}\n\n')

with open('1.txt', 'r', encoding='utf-8') as first_file, open('result.txt', 'a', encoding='utf-8') as second_file: 
    counting = 0
    for line in first_file:
        counting += 1
        second_file.write(f'строка №  {counting}  {line}')
    second_file.write('\n\n')

with open('result.txt', 'a', encoding='utf-8') as file: 
    file.write(f'файл: 3.txt\n\nколичество строк: {str(files_lens_sort[2])}\n\n')

with open('3.txt', 'r', encoding='utf-8') as first_file, open('result.txt', 'a', encoding='utf-8') as second_file: #содержимое файла добавляем
    counting = 0
    for line in first_file:
        counting += 1
        second_file.write(f'строка №  {counting}  {line}')
    second_file.write('\n\n')