class Solution:
    def is_valid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        print(d[')'])
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    solution = Solution()
    print(solution.is_valid(s))
