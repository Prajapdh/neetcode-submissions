class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def dfs(node, canRob):
            if not node:
                return 0

            state = (node, canRob)
            if state in dp:
                return dp[state]

            # Skipping this node always permits robbing its children.
            skip = dfs(node.left, True) + dfs(node.right, True)

            if canRob:
                take = (
                    node.val
                    + dfs(node.left, False)
                    + dfs(node.right, False)
                )
                money = max(take, skip)
            else:
                # Its parent was robbed, so this node must be skipped.
                money = skip

            dp[state] = money
            return money

        return dfs(root, True)