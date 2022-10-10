# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)

# text = del_some_words(text)
# print(text)



my_text = list(' Напишите программу, удаляющую из текста все слова, содержащие ""абв"" '.split())
for i in my_text:
    if 'абв' not in i:
        print(i, end=' ')

# print(list(filter(lambda i: 'абв' not in i, my_text)))