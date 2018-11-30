# pig_latin
""" Description
A group of Vatican City police officers are planning a trip to the United States. Since they only speak Pig Latin, they will need to translate a lot of English phrases. Write a simple program to perform basic English to Pig Latin translation.

Translation rules
If a word has no letters, don't translate it.
All punctuation should be preserved.
If the word begins with a capital letter, then the translated word should too.
Separate each word into two parts. The first part is called the prefix and extends from the beginning of the word up to, but not including, the first vowel. (The letter y will be considered a vowel.) The Rest of the word is called the stem.
The Pig Latin text is formed by reversing the order of the prefix and stem and adding the letters ay to the end. For example, sandwich is composed of s + andwich + ay + . and would translate to andwichsay.
If the word contains no consonents, let the prefix be empty and the word be the stem. The word ending should be yay instead of merely ay. For example, I would be Iyay.
Phase 1
Your first task is to produce a function that takes one argument, a word, and returns the portion of the word up to, but not including the first vowel. For example, if you sent 'banana' to your function, it should return 'b'. Sending 'Sibley' should return 'S', 'stream' should return 'str', and 'break' should return 'br'. Print out your working function and a sample run.

Phase 2
Using what you learned from Phase 1, write a function (or functions) that takes a single word as an argument and returns the word with the prefix and stem reversed.

Phase 3
Modify the function from Phase 2 to properly handle the ay word ending, capital letters, and punctuation.

Final Phase
Input
Your program should perform translation one line at a time. The program will continue to accept input until it is terminated by a Ctrl-D character.

Output
Program output should follow each input line. The translation rules will determine how each word is translated.

Sample session
--> Stop
Opstay
--> No littering
Onay itteringlay
--> No shirts, no shoes, no service
Onay irtsshay, onay oesshay, onay ervicesay
--> No persons under 14 admitted
Onay ersonspay underay 14 admitteday
--> Hey buddy, get away from my car!
Eyhay uddybah, etgay awayyay omfray ymay arcay!
--> ^D""""
