class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position,speed))
        
        fleets = len(position)

        lastCar = pairs.pop()
        maxTime = (target - lastCar[0]) / lastCar[1]
        print(maxTime)

        while pairs:
            lastCar = pairs.pop()
            currTime = (target - lastCar[0]) / lastCar[1]
            if currTime <= maxTime:
                fleets -= 1
            else:
                maxTime = currTime

        return fleets