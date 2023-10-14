sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    input_term = input('Enter a word in English or EXIT: ')
    if input_term == 'EXIT':
        break
    if input_term in sample_dict:
        print ('Translation:', sample_dict[input_term])
    else:
        print('No match!')
print('Bye!')
