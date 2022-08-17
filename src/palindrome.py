from src.string_processor import StringProcessor


class Palindrome(StringProcessor):
    def __init__(self, string) -> None:
        super().__init__(string)

    def find_palindromes(self):
        palindromes = []
        for word in self.string.split():
            if word == word[::-1]:
                palindromes.append(word)
        return palindromes