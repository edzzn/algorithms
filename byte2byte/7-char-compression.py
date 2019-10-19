#!/bin/python3


# def compress(text):
#     compressed_text = ''

#     max_char_counter = 1
#     current_char = text[0]
#     for i in range(1, len(text)):
#         if current_char == text[i]:
#             max_char_counter += 1
#         else:
#             compressed_text += f'{current_char}{max_char_counter}'
#             current_char = text[i]
#             max_char_counter = 1

#      compressed_text += f'{current_char}{max_char_counter}'

#     return compressed_text

def compress(text):
    compressed_text = ''

    max_char_counter = 1

    for i in range(len(text)-1):
        current_char = text[i]
        if current_char == text[i+1]:
            max_char_counter += 1
        else:
            print('else')
            compressed_text += f'{current_char}{max_char_counter}'
            max_char_counter = 1

    compressed_text += f'{current_char}{max_char_counter}'
    return compressed_text


if __name__ == '__main__':
    text = 'aaacbb'
    result = compress(text)
    print(f'result {result}')  # a3b2
