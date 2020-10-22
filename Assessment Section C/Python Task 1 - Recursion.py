def find_and_replace(string, substring, rep_string, current_index=0):
    '''
    Finds the {substring} in the {string} and replaces it with {rep_string} if found.
    If {substring} is not found in {string} this is indicated.
    If {substring} is found in {string}, the string with the replacement is returned.
    '''

    # Check if the end of {string} has been reached, if yes, {substring} is not in {string}
    if current_index == len(string):
         return "Substring not found in string"

    # If the current position in {string} matches {substring} return the replaced string
    if string[current_index:current_index + len(substring)] == substring:
        return string[0:current_index] + rep_string + string[current_index + len(substring):]
 
    # If not the end of {string} and {substring} not found at current index, recur the function
    else:
        return find_and_replace(string, substring, rep_string, current_index + 1)

        

def main():

    string = input("Please enter a string: ")
    substring = input("Please enter the substring you wish to find: ")
    replace_string = input("Please enter a string to replace the given substring: ")
    result = find_and_replace(string, substring, replace_string)
    print(result)
    

if __name__ == "__main__":
    main()
