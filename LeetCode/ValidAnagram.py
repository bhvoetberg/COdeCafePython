def is_anagram_generic(s: str, t: str) -> bool:
    count_frequency = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if ord(s[i]) in count_frequency:
            count_frequency[ord(s[i])] += 1
        else:
            count_frequency[ord(s[i])] = 1
        if ord(t[i]) in count_frequency:
            count_frequency[ord(t[i])] -= 1
        else:
            count_frequency[ord(t[i])] = -1
    for i in count_frequency.keys():
        if count_frequency[i] != 0:
            return False
    return True


def is_anagram(s, t):
    count_frequency = [0] * 26
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        count_frequency[ord(s[i]) - ord('a')] += 1
        count_frequency[ord(t[i]) - ord('a')] -= 1

    for i in range(len(count_frequency)):
        if count_frequency[i] != 0:
            return False
    return True


def main():
    print(is_anagram("teen","neet"))
    print(is_anagram("somee","some"))
    print("---")


    print(is_anagram_generic("teen", "neet"))
    print(is_anagram_generic("true", "thru"))
    print(is_anagram_generic("some", "somet"))


if __name__ == '__main__':
    main()
