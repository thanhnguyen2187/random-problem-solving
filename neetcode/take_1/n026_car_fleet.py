from typing import List


def calculate_time(target, pair):
    position = pair[0]
    speed = pair[1]
    return (target - position) / speed


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        pairs = [
            (p, s)
            for p, s in zip(positions, speeds)
        ]
        pairs.sort(key=lambda pair: (pair[0], -pair[1]), reverse=True)

        times = [
            calculate_time(target=target, pair=pairs[0])
        ]

        for pair in pairs[1:]:
            time_current = calculate_time(target=target, pair=pair)
            time_last = times[-1]
            if time_current > time_last:
                times.append(time_current)

        return len(times)


if __name__ == "__main__":
    solution = Solution()
    positions = [7, 6, 4, 4, 1, 0]
    speeds = [1, 3, 3, 2, 2, 1]
    result = solution.carFleet(positions=positions, speeds=speeds, target=10)
    print(result)
