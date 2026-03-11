class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums
    
# prueba = Solution()
# print(prueba.getConcatenation([1,2,3]))


    # def shuffle(self, nums: list[int], n: int) -> list[int]:
    #     xv=nums[:n]
    #     yv=nums[n:]
    #     answer = []
    #     for x in range(len(xv)):
    #         answer.append(xv[x])
    #         answer.append(yv[x])
    #     return answer

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        j=0
        num=[0]*(2*n)
        for i in range(n):
            num[j]=nums[i]
            num[j+1]=nums[i+n]
            j+=2
        return num

# prueba = Solution()
# print(prueba.shuffle([2,5,1,3,4,7],3))

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_consecutive = 0
        actual_consecutive = 0

        for _ in nums:
            if _ == 1:
                actual_consecutive += 1
                if actual_consecutive > max_consecutive:
                    max_consecutive = actual_consecutive
            else:
                actual_consecutive = 0

        return max_consecutive

# prueba = Solution()
# print(prueba.findMaxConsecutiveOnes([1,1,0,1,1,1]))
    
    def findErrorNums(self, nums: list[int]) -> list[int]:
        last_number = None
        for _ in nums:
            if last_number == None:
                last_number = _

            else:
                if last_number == _:
                    return last_number-1, last_number
                

prueba = Solution()
print(prueba.findMaxConsecutiveOnes([1,2,4,4,5,6]))   
        
        