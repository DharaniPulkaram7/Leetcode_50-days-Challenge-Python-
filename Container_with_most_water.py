class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max=0
        left=0
        right=len(height)-1
        while(left<right):
            Height=min(height[left],height[right])
            width=abs(left-right)
            Area=Height*width
            Max=max(Max,Area)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return Max