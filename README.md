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
   
 Enter the string:
 
    Please enter a string: ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD
  
 Expected Output:
 
    ILOVEUEVOLI,26,11
    LOVEUEVOL,27,9
    RACECAR,13,7
    OVEUEVO,28,7
    ABCBA,0,5
    ACECA,14,5
    VEUEV,29,5
    IAMAI,37,5
    BCB,1,3
    OHO,9,3
    CEC,15,3
    ARA,18,3
    RAR,19,3
    EUE,30,3
    AMA,38,3
    LL,7,2
    II,36,2
    GG,46,2
    OO,48,2
    
