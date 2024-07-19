def is_palindrome(text):
    import string
    lowered_text = text.lower().replace(' ', '')
    punctuation_in_text = set(string.punctuation)
    lowered_text = ''.join(vl for vl in lowered_text if vl not in punctuation_in_text)

    return lowered_text == lowered_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
