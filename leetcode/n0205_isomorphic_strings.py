
class Solution:

    def isIsomorphic(self, s: str, t: str):
        mapping = {}
        mapped = set()

        for character_1, character_2 in zip(s, t):
            if (
                character_1 not in mapping
            ):
                mapping[character_1] = character_2
                mapped.add(character_2)
            elif (
                mapping[character_1] not in mapped and
                mapping[character_1] == character_2
            ):
                continue
            elif(
                mapping[character_1] != character_2
            ):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.isIsomorphic(
            s="egg",
            t="add",
        )
    )
    print(
        solution.isIsomorphic(
            s="foo",
            t="bar",
        )
    )
    print(
        solution.isIsomorphic(
            s="paper",
            t="title",
        )
    )
    print(
        solution.isIsomorphic(
            s="badc",
            t="baba",
        )
    )
