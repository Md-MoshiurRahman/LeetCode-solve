class Solution(object):
    def maxArea(self, height):
        maxarea = 0
        front = 0
        end = len(height)-1
        distance = len(height)-1

        while True:
            if height[front] < height[end]:
                minheight = height[front]
                flag = 0
            else:
                minheight = height[end]
                flag = 1

            area = minheight * distance
            if maxarea < area:
                maxarea = area

            distance -= 1
            if flag == 0:
                front += 1
            else:
                end -= 1

            if front == end:
                break

        return maxarea


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))