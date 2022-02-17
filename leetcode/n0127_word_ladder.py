from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    combinations,
    chain,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def difference(
        self,
        word_1: str,
        word_2: str,
    ) -> int:
        return sum(
            1
            if character_1 != character_2
            else 0
            for character_1, character_2 in zip(word_1, word_2)
        )

    def find_min_depth(
        self,
        current_word: str,
        current_depth: int,
        words_dict: DefaultDict[str, Set[str]],
        traversed_words: Set[str],
        end_word: str,
    ) -> Union[int, float]:

        if current_word == end_word:
            return current_depth
        elif (
            current_word in traversed_words or
            not words_dict[current_word]
        ):
            return float("inf")

        traversed_words.add(current_word)
        min_depth = min(
            self.find_min_depth(
                current_word=next_word,
                current_depth=current_depth + 1,
                words_dict=words_dict,
                traversed_words=traversed_words,
                end_word=end_word,
            )
            for next_word in words_dict[current_word]
        )
        traversed_words.remove(current_word)
        return min_depth

    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str],
    ) -> int:

        # create graph
        words_dict: DefaultDict[str, Set[str]] = defaultdict(set)
        for index_1, index_2 in permutations(
            range(len(wordList)), 2
        ):
            word_1 = wordList[index_1]
            word_2 = wordList[index_2]
            if self.difference(
                word_1=word_1,
                word_2=word_2,
            ) == 1:
                words_dict[word_1].add(word_2)
                words_dict[word_2].add(word_1)

        for word in wordList:
            if self.difference(
                word_1=beginWord,
                word_2=word,
            ) == 1:
                words_dict[beginWord].add(word)

        result = self.find_min_depth(
            current_word=beginWord,
            current_depth=0,
            words_dict=words_dict,
            traversed_words=set(),
            end_word=endWord,
        ) + 1

        # return result
        return (
            result
            if result != float("inf")
            else 0
        )


if __name__ == '__main__':
    solution = Solution()
    for (
        begin_word, end_word,
        word_list,
    ) in [
        # (
        #     "hit", "cog",
        #     ["hot", "dot", "dog", "lot", "log", "cog"],
        # ),
        # (
        #     "hit", "cog",
        #     ["hot", "dot", "dog", "lot", "log"],
        # ),
        (
            "qa", "sq",
            [
                "si", "go", "se", "cm", "so",
                "ph", "mt", "db", "mb", "sb",
                "kr", "ln", "tm", "le", "av",
                "sm", "ar", "ci", "ca", "br",
                "ti", "ba", "to", "ra", "fa",
                "yo", "ow", "sn", "ya", "cr",
                "po", "fe", "ho", "ma", "re",
                "or", "rn", "au", "ur", "rh",
                "sr", "tc", "lt", "lo", "as",
                "fr", "nb", "yb", "if", "pb",
                "ge", "th", "pm", "rb", "sh",
                "co", "ga", "li", "ha", "hz",
                "no", "bi", "di", "hi", "qa",
                "pi", "os", "uh", "wm", "an",
                "me", "mo", "na", "la", "st",
                "er", "sc", "ne", "mn", "mi",
                "am", "ex", "pt", "io", "be",
                "fm", "ta", "tb", "ni", "mr",
                "pa", "he", "lr", "sq", "ye",
            ]
        )
    ]:
        print(
            solution.ladderLength(
                beginWord=begin_word,
                endWord=end_word,
                wordList=word_list,
            )
        )
