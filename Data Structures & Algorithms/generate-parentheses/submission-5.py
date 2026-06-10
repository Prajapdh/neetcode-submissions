class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr: str, open_count: int, close_count: int):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if open_count < n:
                dfs(curr + "(", open_count + 1, close_count)

            if close_count < open_count:
                dfs(curr + ")", open_count, close_count + 1)

        dfs("", 0, 0)
        return res