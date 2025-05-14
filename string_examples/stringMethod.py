# count no of characters
s = "I love India"
count_dict = {}
for char in s:
    if char != " ":
        count_dict[char] = count_dict.get(char, 0) + 1 
print(count_dict)


