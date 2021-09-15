def longest_palindrome(a_string: str):
    longest_length = 0
    longest_substring = ""
    for i in range(len(a_string)-1):
        for j in range(len(a_string), i, -1):
            if a_string[i:j] == a_string[i:j][::-1] and len(a_string[i:j]) > longest_length:
                longest_length = len(a_string[i:j])
                longest_substring = a_string[i:j]

    return longest_substring

print(longest_palindrome("ababc"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("cbbdababc"))
print(longest_palindrome("banana"))