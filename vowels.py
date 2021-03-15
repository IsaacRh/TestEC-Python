# set array vowels
vowels_lowercase = ['a', 'e', 'i', 'o', 'u']
vowels_uppercase = ['A', 'E', 'I', 'O', 'U']
accented_vowels_lowercase = ['á', 'é', 'í', 'ó', 'ú']
accented_vowels_uppercase = ['Á', 'É', 'Í', 'Ó', 'Ú']


def get_next_vowel(check_vowel, vowels_array):
    index = 0
    for vowel in vowels_array:
        index += 1
        if vowel == check_vowel:
            if index > len(vowels_array)-1:
                return vowels_array[0]
            return vowels_array[index]


def set_text(text):
    new_text = ''
    vowel_counter = 0
    for character in text:
        if (character in vowels_lowercase) or (character in vowels_uppercase) or (character in accented_vowels_lowercase) or (character in accented_vowels_uppercase):
            vowels_array = []
            if character in vowels_lowercase: 
                vowels_array = vowels_lowercase
            elif character in vowels_uppercase:
                vowels_array = vowels_uppercase
            elif character in accented_vowels_lowercase:
                vowels_array = accented_vowels_lowercase
            elif character in accented_vowels_uppercase:
                vowels_array = accented_vowels_uppercase
            next_vowel = get_next_vowel(character, vowels_array)
            new_text += next_vowel
            vowel_counter += 1

        else:
            new_text += character

    return (new_text, vowel_counter)


if __name__ == '__main__':
    # get data from input
    print("Type a string")
    text = input()
    result = set_text(text)

    print('Vowels number => {}'.format(result[1]))
    print('New Text => {}'.format(result[0]))
