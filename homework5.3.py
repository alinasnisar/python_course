import string

user_string = input("Введіть рядок: ")

sanitized_string = user_string.translate(str.maketrans('', '', string.punctuation + ''))
words = sanitized_string.split()

capitalized_words = [word.title() for word in words]

hashtag = '#' + ''.join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(f"Хештег: {hashtag}")

# user_text = input('Enter text: ').title()
#
# new_hashtag = '#'
#
# for symbol in user_text:
#     if symbol.isalnum():
#         new_hashtag += symbol
#
#
# print(new_hashtag[:140])
