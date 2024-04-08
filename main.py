# Remove None values from a list in Python

my_list = [1, None, 3, None, 8, None]

new_list = [i for i in my_list if i is not None]

print(new_list)  # 👉️ [1, 3, 8]