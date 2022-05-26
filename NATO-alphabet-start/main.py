student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_words = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(phonetic_words)


def generate_phonetic():
    user_input = input("Enter the word: ").upper()
    try:
        result = [phonetic_words[letter] for letter in user_input]
    except KeyError:
        print("Sorry, enter only alphabets")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()