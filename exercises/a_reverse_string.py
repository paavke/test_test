
def reverse_string(s):
    # Write your code here
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str
 
