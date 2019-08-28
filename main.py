#!/usr/bin/env python3

import utils

utils.check_version((3,7))
utils.clear()

print(('Hello, my name is Shantanu Bhattacharya, I am a freshman this year and I am from India.'))
name = input('What is your name? ')
print('')
print('Hi '+ name + ' ,nice to meet you.')
print('')
print(('''My favourite game is the new God of War that sony released,
I just love the fact that the entire game was shot and created with just one camera angle!
I also find the combat in the game to be very satisfing and I love it.'''))
print('')
game = input('Is God of War ' + str(2018) + ' your favourite game too? Please answer with either a Yes or a No. ')
if game.lower().strip() == 'yes':
    print('')
    print('Great! We love the same game!')
elif game.lower().strip() == 'no':
    print('')
    print('Aww.... well you definetly must have not played it.')
print('')   
print('Okay this is some other Information about me: ')
print('')
print('''My concern about this class is how much will I be able to push my creativity?
Will I really be able to create games? Even the thought of it makes me really exited.

I am very exited about creating fun action games myself and maybe someday 
also creating a masterpiece like God of War myself.

My stackoverflow.com user name is: 11980900

The URL to my github.com profile is: https://github.com/seoLegna
''')

