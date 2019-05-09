# Palindromes

Lists all the palindromes in a given string and prints them along with their starting index and length. 

Palindromes are mirrors around a central character. The algorithm is to go through each character in the string and see if the surrounding characters are equal. If they are, then they are considered a palindrome and added to the list. This needs to be done for both odd length and even length palindromes. The odd length palindromes like 'ama' have one central character, so the left and right characters around it are checked for equality.The even length palindromes like 'bb' have two central characters, so each character in the string along with the one beside it are checked for equality.

## Requirements ##

This code is written in Python 2.7. 

## Quick Start #

To run the program:

    python main.py
    
 It will then prompt you:
 
    Please enter a string :
   
 Enter the string (for example abba) :
 
    Please enter a string: abba
  
 Expected Output:
 
    abba,0,4
    bb,1,2
