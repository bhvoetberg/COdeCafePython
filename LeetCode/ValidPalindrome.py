def is_palindrome(word_to_check: str) -> bool:
    cleaned_word_to_array: list = []
    for c in word_to_check:
        ascii_value = ord(c)
        if ascii_value in range(48,58) or ascii_value in range(65,91) or ascii_value in range(97,123):
            cleaned_word_to_array.append(c.lower())
    if cleaned_word_to_array is cleaned_word_to_array.reverse():
        return True
    else:
        return False


def main():
    word_to_check: str = "A man, a plan, a canal: Panama"
    print(is_palindrome(word_to_check))


if __name__ == '__main__':
    main()
