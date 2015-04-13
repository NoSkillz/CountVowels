__author__ = 'VerDe'

'''
 Count Vowels – Enter a string and the program counts the number of vowels in the text.
 For added complexity have it report a sum of each vowel found.
'''

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

string_input = input("Throw me a string: ")
total_vowels = 0

for i in string_input:
    if i in vowels:
        vowels[i] += 1
        total_vowels += 1

# print("Your string has the following number of vowels: {0}".format(int(vowels['e'])))
print("Number of 'a' characters: {0}.\nNumber of 'e' characters: {1}.\nNumber of 'i' characters: {2}.\n"
      "Number of 'o' characters: {3}.\nNumber of 'u' characters: {4}.\nTotal vowels: {5}.".format(vowels['a'],
                                                                                                  vowels['e'],
                                                                                                  vowels['i'],
                                                                                                  vowels['o'],
                                                                                                  vowels['u'],
                                                                                                  total_vowels))