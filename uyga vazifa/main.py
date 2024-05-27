

https://github.com/botirjonabduqaxxorov/vazifa

# 1
# def count_words_in_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         words = content.split()

#         return len(words)
    
#     except FileNotFoundError:
#         return "Fayl topilmadi."

# file_path = 'path_to_your_file.txt'

# word_count = count_words_in_file(file_path)

# print(f"Fayldagi so'zlar soni: {word_count}")



# 2
# def find_longest_word_in_file(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         words = content.split()

#         longest_word = max(words, key=len) if words else ""
        
#         return longest_word
    
#     except FileNotFoundError:
#         return "Fayl topilmadi."

# file_path = 'path_to_your_file.txt'

# longest_word = find_longest_word_in_file(file_path)

# print(f"Fayldagi eng uzun so'z: {longest_word}")





# 3
# def find_disrupting_element(numbers):
#     if len(numbers) <= 1:
#         return None
    
#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i - 1]:
#             return numbers[i]
    
#     return None

# numbers = [1, 2, 3, 7, 5, 6, 8]

# disrupting_element = find_disrupting_element(numbers)

# print(f"Buzuvchi element: {disrupting_element}")


# 4
# def find_gmail_addresses(data_list):
#     return [item for item in data_list if isinstance(item, str) and item.endswith("@gmail.com")]

# data = input("Ma'lumotlar listini kiriting (bo'laklarni probel bilan ajrating): ").split()

# gmail_addresses = find_gmail_addresses(data)

# if gmail_addresses:
#     print("Gmail manzillari:")
#     for address in gmail_addresses:
#         print(address)
# else:
#     print("Listda Gmail manzillari topilmadi.")
