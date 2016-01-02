#3_2_double_dice
import random
for x in range (1, 11):
    throw_1 = random.randint(1,6)
    throw_2 = random.randint(1,6)
    total = throw_1 + throw_2
    print(total)
    if total == 7:
        print ('Seven thrown')
    if total == 11:
        print ('Eleven thrown')
    if throw_1 == throw_2:
        print ('Double thrown')
    if not (total <5 or total >9):
        print ('not bad')
    if total > 10:
        print('Good Throw!')
    if total < 4:
        print('Unlucky!')
        
