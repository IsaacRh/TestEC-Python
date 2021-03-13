
def get_next_vowel(check_vowel, vowels_array):
    index = 0
    for vowel in vowels_array:
        index += 1
        if vowel == check_vowel:
            if index > len(vowels_array)-1: return vowels_array[0]
            return vowels_array[index]
# set array vowels
vowels_lowercase = ['a', 'e', 'i', 'o', 'u']
vowels_uppercase = ['A', 'E', 'I', 'O', 'U']
vowel_counter = 0
new_text = ''

# get data from input
print("Type a string")
text = input()
for character in text:
    if character in vowels_lowercase:
        next_vowel = get_next_vowel(character, vowels_lowercase)
        new_text += next_vowel
        vowel_counter += 1
    elif character in vowels_uppercase:
        next_vowel = get_next_vowel(character, vowels_uppercase)
        new_text += next_vowel
        vowel_counter += 1
    else:
        new_text += character

print('Vowels number => {}'.format(vowel_counter))
print('New Text => {}'.format(new_text))