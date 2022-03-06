def compressString(s, n) :
    result = ""
    # 'char' will be used to store the previous item of the string.
    char = ""

    # The dictionary is provided "" value to help proceed with ' str_dict.pop(char)' in below for loop
    str_dict = {"":""}

    for i in range(n):
        #If current and preceeding element in string 's' are same then we increment the value by 1. 
        if s[i] == char: 
            str_dict[s[i]] = (str_dict[s[i]] + 1)

        # If current element in string 's' is not equal to the previous one, then add new key(current element)
        # with value of 1.
        # And remove the key and value for preceeding element from dictionary after updating the 'result'.
        else:
            str_dict[s[i]] = 1
            result = result + "".join((char,str(str_dict[char])))
            str_dict.pop(char)
        
        # Updating 'char' variable with current element.
        char = s[i]
    
    # Adding last element in the result post loop exit.
    print(result+"".join((char,str(str_dict[char]))))
            
# Driver code
if __name__ == "__main__" :
 
    s = "aaaabbbccccccccdddaabbcsda"
    n = len(s)
 
    compressString(s, n)

# TESTCASE:
# -----------
# I/P : aaaabbbccccccccdddaa
# O/P : a4b3c8d3a2