# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    reversedWord = ''.join(reversed(word)).lower()
    lowercaseAnagram = anagram.lower()
    if (reversedWord == lowercaseAnagram):
        return True
    else:
        return False


print(find_anagram("hello","olleh"))
print(find_anagram("below", "elbow"))

