# x = input('Input something')
# print('Output something' + x)

# lorem_ipsum_text = open('C:/Users/MS/Desktop/text.txt.txt', 'r')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()

# lorem_ipsum_text = open('C:/Users/MS/Desktop/text.txt.txt', 'r')
# for line in lorem_ipsum_text:
#     if 'call' in line.lower():
#         print(line, end='')
# lorem_ipsum_text.close()

# with open('C:/Users/MS/Desktop/text.txt.txt', 'r') as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'call' in line.lower():
#             print(line, end='')

# with open('C:/Users/MS/Desktop/text.txt.txt', 'r') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text.readline()

with open('C:/Users/MS/Desktop/text.txt.txt', 'r') as lorem_ipsum_text:
    lines = lorem_ipsum_text.readlines()
print(lines)
