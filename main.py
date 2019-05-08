def expand(start, end, input_string, results):
    """Check if the left and right characters are equal and expand outwards
    until the start and end indexes are not equal"""
    while start >= 0 and end < len(input_string) and input_string[start] == input_string[end]:
        pali = (input_string[start:end+1], start, end+1-start)
        results.append(pali)
        start -= 1
        end +=1
    return results

def get_all_palindromes(input_string):
    """Go through each character in the string and expand for palindromes of odd length and even length"""
    results_odd = []
    results_even = []
    for index, char in enumerate(input_string):

        results_odd = expand(index-1, index+1, input_string, results_odd)
        results_even = expand(index, index+1, input_string, results_even)

    results = results_odd + results_even
    #sort results according to length in descending order
    sorted_results = sorted(results, reverse=True, key=lambda x: x[2])
    return sorted_results

def print_all_palindromes(results):
    for r in results:
        mystring = ','.join(map(str, r))
        print mystring


if __name__ == '__main__':
    input_string = raw_input("Please enter a string: ")
    #check if input string is empty or only contains whitespaces
    if not input_string.strip():
        print "Please enter a valid string"
        exit()
    # if there are mixed upper and lower case in the input string, convert them to lower
    mixed = any(l.islower() for l in input_string) and any(l.isupper for l in input_string)
    if mixed:
        input_string = input_string.lower()
    palindrome_list = get_all_palindromes(input_string)
    if not palindrome_list:
       print "There are no palindromes for this string."
    else:
        print_all_palindromes(palindrome_list)


