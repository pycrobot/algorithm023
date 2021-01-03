class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)
        new_num = str(int(num)+1)
        new_list = [int(j) for j in new_num]
        for x in range(len(digits)-len(new_list)):
            new_list.insert(0,0)
        return new_list
