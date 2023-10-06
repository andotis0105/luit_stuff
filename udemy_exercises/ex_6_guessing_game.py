while True:
    year = int(input('When was Python 1.0 released? '))
    if year == 1994:
        print('Correct!')    
        break
    if year >= 1995:
        print('It was earlier than that!')
    if year <= 1993:
        print('It was later than that!')