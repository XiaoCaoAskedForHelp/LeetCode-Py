from typing import List


class Solution:
    # 双指针
    def trap(self, height: List[int]) -> int:
        leftheight, rightheight = [0] * len(height), [0] * len(height)

        leftheight[0] = height[0]
        for i in range(1, len(height)):
            leftheight[i] = max(leftheight[i - 1], height[i])
        rightheight[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            rightheight[i] = max(rightheight[i + 1], height[i])

        result = 0
        for i in range(0, len(height)):
            sum = min(leftheight[i], rightheight[i]) - height[i]
            result += sum
        return result

    # 单调栈
    '''
    单调栈是按照 行 的方向来计算雨水
    从栈顶到栈底的顺序：从小到大
    通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
    雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
    雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）
    '''

    # stack储存index，用于计算对应的柱子高度
    def trap1(self, height: List[int]) -> int:
        stack = [0]
        result = 0
        for i in range(1, len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    result += h * w
            if stack and height[i] == height[stack[-1]]:
                stack.pop()
            stack.append(i)
        return result


Solution().trap1([4, 2, 0, 3, 2, 5])
