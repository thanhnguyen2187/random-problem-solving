class Solution:
    def customSortString(self, order: str, str_: str) -> str:
        order_dict = {
            character: index
            for index, character in enumerate(order)
        }
        return "".join(
            sorted(
                str_,
                key=lambda character: order_dict.get(character, 201)
            )
        )


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.customSortString(
            order="cba",
            str_="abcd",
        )
    )
