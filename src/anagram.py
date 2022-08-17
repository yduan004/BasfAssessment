from src.string_processor import StringProcessor
import itertools


class Anagram(StringProcessor):
    def __init__(self, string) -> None:
        super().__init__(string)

    def find_anagrams(self):
        anagrams = ["".join(perm) for perm in itertools.permutations(self.string)]
        return anagrams