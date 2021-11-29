#Program to find the count of each vowel in a string(use dictionary)

string = input("Enter a string :")
lowercase = string.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
print("Count of Vowels :", vowel_counts)