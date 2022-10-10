# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`

with open('C:\\Users\\User\\Desktop\\HomeWork\\file1.txt', 'r') as data:
    text1 = data.read()

def coding_text(text):
    i = 0
    encoding = ""
    while i < len(text):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        
# добавляет к результату текущий символ и его количество
        encoding += str(count) + text[i]
        i = i + 1
 
    return encoding

print(coding_text(text1))

with open('C:\\Users\\User\\Desktop\\HomeWork\\file2.txt', 'w') as data:
    text2 = data.write(coding_text(text1))

with open('C:\\Users\\User\\Desktop\\HomeWork\\file2.txt', 'r') as data:
    text2 = data.read()

def decoding_text(text2):
    count = ''
    str_decode = ''
    for char in text2:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_text(text2)
print(str_decode)








exit()
def encode(s):
 
    encoding = "" # сохраняет выходную строку
 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'ABBCCCD'
    print(encode(s))
 