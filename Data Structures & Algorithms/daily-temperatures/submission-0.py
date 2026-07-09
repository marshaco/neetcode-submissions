class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        days = []

        for i in range(len(temperatures)):
        
            while days and temperatures[i] > temperatures[days[-1]]:
                lowerDay = days.pop()
                result[lowerDay] = i - lowerDay

            days.append(i)

        return result