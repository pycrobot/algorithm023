class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10 = 0, 0
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                count10 += 1
                count5 -= 1
            elif bill == 20 and count10 > 0:
                count10 -= 1
                count5 -= 1
            else:
                count5 -= 3
            if count10 < 0 or count5 < 0:
                return False
        return True
