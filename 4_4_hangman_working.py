Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> book_name = 'Programming Raspberry Pi'
>>> book_name
'Programming Raspberry Pi'
>>> print (book_name)
Programming Raspberry Pi
>>> len (book_name)
24
>>> book_name(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    book_name(1)
TypeError: 'str' object is not callable
>>> book_name[1]
'r'
>>> book_name[0]
'P'
>>> book_name[5000]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    book_name[5000]
IndexError: string index out of range
>>> book_name[0:11]
'Programming'
>>> book_name[12:22]
'Raspberry '
>>> book_name[12:21]
'Raspberry'
>>> book_name[12:]
'Raspberry Pi'
>>> numbers = [123, 34, 55, 321, 9]
>>> len(numbers)
5
>>> numbers[0]
123
>>> numbers[1:3]
[34, 55]
>>> numbers[0] = 1
>>> numbers
[1, 34, 55, 321, 9]
>>> numbers
[1, 34, 55, 321, 9]
>>> more_numbers = [5, 66, 44]
>>> numbers + more_numbers
[1, 34, 55, 321, 9, 5, 66, 44]
>>> numbers.sort()
>>> numbers
[1, 9, 34, 55, 321]
>>> numbers.pop()
321
>>> numbers
[1, 9, 34, 55]
>>> numbers.pop (1)
9
>>> numbers
[1, 34, 55]
>>> numbers.insert(1, 66)
>>> numbers
[1, 66, 34, 55]
>>> big_list = [123, 'hello', ['inner list', 2, True]]
>>> big_list
[123, 'hello', ['inner list', 2, True]]
>>> 
 RESTART: C:\Users\Admin\Documents\Programming\Python\python_monk\4_1_list_and_for.py 
1
one
2
True
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_2_polite_function.py 
Pass the salt please
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_3_hello_n.py 
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_3_hello_n.py", line 6, in <module>
    say_hello(5)
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_3_hello_n.py", line 3, in say_hello
    for x in range (o, n):
NameError: name 'o' is not defined
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_3_hello_n.py 
Hello
Hello
Hello
Hello
Hello
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py", line 9, in <module>
    print (pick_a_word())
NameError: name 'pick_a_word' is not defined
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
frog
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
frog
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
cat
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
chicken
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
dog
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
cat
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_words.py 
cat
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play.py 
You are Hung!
The word was: chicken
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play.py 
You are Hung!
The word was: frog
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py", line 33, in <module>
    play()
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py", line 9, in play
    guess = get_guess(word)
  File "C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py", line 19, in get_guess
    print_word_with_blanks(word)
NameError: name 'print_word_with_blanks' is not defined
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
print_word_with_blanks: not done yet
Lives Remaining: 14
 Guess a letter or a whole word?asd
print_word_with_blanks: not done yet
Lives Remaining: 13
 Guess a letter or a whole word?x
print_word_with_blanks: not done yet
Lives Remaining: 12
 Guess a letter or a whole word?a
print_word_with_blanks: not done yet
Lives Remaining: 11
 Guess a letter or a whole word?s
print_word_with_blanks: not done yet
Lives Remaining: 10
 Guess a letter or a whole word?f
print_word_with_blanks: not done yet
Lives Remaining: 9
 Guess a letter or a whole word?s
print_word_with_blanks: not done yet
Lives Remaining: 8
 Guess a letter or a whole word?a
print_word_with_blanks: not done yet
Lives Remaining: 7
 Guess a letter or a whole word?s
print_word_with_blanks: not done yet
Lives Remaining: 6
 Guess a letter or a whole word?c
print_word_with_blanks: not done yet
Lives Remaining: 5
 Guess a letter or a whole word?a
print_word_with_blanks: not done yet
Lives Remaining: 4
 Guess a letter or a whole word?ds
print_word_with_blanks: not done yet
Lives Remaining: 3
 Guess a letter or a whole word?g
print_word_with_blanks: not done yet
Lives Remaining: 2
 Guess a letter or a whole word?ss
print_word_with_blanks: not done yet
Lives Remaining: 1
 Guess a letter or a whole word?d
You are Hung!
The word was: cat
>>> d
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/04_06_hangman_get_guess.py 
print_word_with_blanks: not done yet
Lives Remaining: 14
 Guess a letter or whole word?a
print_word_with_blanks: not done yet
Lives Remaining: 13
 Guess a letter or whole word?c
print_word_with_blanks: not done yet
Lives Remaining: 12
 Guess a letter or whole word?t
print_word_with_blanks: not done yet
Lives Remaining: 11
 Guess a letter or whole word?a
print_word_with_blanks: not done yet
Lives Remaining: 10
 Guess a letter or whole word?s
print_word_with_blanks: not done yet
Lives Remaining: 9
 Guess a letter or whole word?d
print_word_with_blanks: not done yet
Lives Remaining: 8
 Guess a letter or whole word?e
print_word_with_blanks: not done yet
Lives Remaining: 7
 Guess a letter or whole word?i
print_word_with_blanks: not done yet
Lives Remaining: 6
 Guess a letter or whole word?o
print_word_with_blanks: not done yet
Lives Remaining: 5
 Guess a letter or whole word?u
print_word_with_blanks: not done yet
Lives Remaining: 4
 Guess a letter or whole word?
print_word_with_blanks: not done yet
Lives Remaining: 3
 Guess a letter or whole word?
print_word_with_blanks: not done yet
Lives Remaining: 2
 Guess a letter or whole word?
print_word_with_blanks: not done yet
Lives Remaining: 1
 Guess a letter or whole word?
You are Hung!
The word was: frog
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
---
Lives Remaining: 14
 Guess a letter or a whole word?a
-a-
Lives Remaining: 13
 Guess a letter or a whole word?s
-a-
Lives Remaining: 12
 Guess a letter or a whole word?c
ca-
Lives Remaining: 11
 Guess a letter or a whole word?
ca-
Lives Remaining: 10
 Guess a letter or a whole word?r
ca-
Lives Remaining: 9
 Guess a letter or a whole word?e
ca-
Lives Remaining: 8
 Guess a letter or a whole word?w
ca-
Lives Remaining: 7
 Guess a letter or a whole word?q
ca-
Lives Remaining: 6
 Guess a letter or a whole word?y
ca-
Lives Remaining: 5
 Guess a letter or a whole word?t
cat
Lives Remaining: 4
 Guess a letter or a whole word?d
cat
Lives Remaining: 3
 Guess a letter or a whole word?s
cat
Lives Remaining: 2
 Guess a letter or a whole word?s
cat
Lives Remaining: 1
 Guess a letter or a whole word?s
You are Hung!
The word was: cat
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
---
Lives Remaining: 14
 Guess a letter or a whole word?a
-a-
Lives Remaining: 14
 Guess a letter or a whole word?t
-at
Lives Remaining: 14
 Guess a letter or a whole word?c
You win! Well Done!
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/04_06_hangman_get_guess.py 
print_word_with_blanks: not done yet
Lives Remaining: 14
 Guess a letter or whole word?
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
---
Lives Remaining: 14
 Guess a letter or a whole word?a
---
Lives Remaining: 13
 Guess a letter or a whole word?e
---
Lives Remaining: 12
 Guess a letter or a whole word?i
---
Lives Remaining: 11
 Guess a letter or a whole word?o
-o-
Lives Remaining: 11
 Guess a letter or a whole word?u
-o-
Lives Remaining: 10
 Guess a letter or a whole word?b
-o-
Lives Remaining: 9
 Guess a letter or a whole word?l
-o-
Lives Remaining: 8
 Guess a letter or a whole word?t
-o-
Lives Remaining: 7
 Guess a letter or a whole word?c
-o-
Lives Remaining: 6
 Guess a letter or a whole word?g
-og
Lives Remaining: 6
 Guess a letter or a whole word?d
You win! Well Done!
>>> 
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
---
Lives Remaining: 14
 Guess a letter or a whole word?cat
---
Lives Remaining: 13
 Guess a letter or a whole word?dog
You win! Well Done!
>>> 
>>> 
 RESTART: C:/Users/Admin/Documents/Programming/Python/python_monk/4_4_hangman_play_with get_guess.py 
---
Lives Remaining: 14
 Guess a letter or a whole word?cat
You win! Well Done!
>>> 
