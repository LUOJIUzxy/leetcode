
## 适合 DFS 的信号

- 求连通块数量

- 求是否存在路径

- 枚举所有方案

- 回溯

- flood fill / island 类问题

## Backtracking 模板：
这个本质上也是 DFS，只不过多了“做选择 → 递归 → 撤销选择”。

'''
def backtrack(path, choices):
    if 终止条件:
        res.append(path[:])
        return

    for choice in choices:
        if 不合法:
            continue

        path.append(choice)      # 做选择
        backtrack(path, choices) # 递归
        path.pop()               # 撤销选择
'''

经典题：

Permutations

Subsets

Combination Sum

N-Queens

###  DFS 为什么用 stack

DFS 是 Depth-First Search，深度优先搜索。

它的核心思想是：

一条路先走到底，走不动了再回头。

这个“先走最新发现的那条路”，本质上就是 后进先出 LIFO。

也就是说：

你刚发现的节点, 你最想马上继续往下走, 所以它应该先被取出来, 这就天然对应 stack。

举个例子
A -> B, C
B -> D, E


如果从 A 开始 DFS：

访问 A, 发现 B, C, 通常先往 B 深入, 到了 B 又发现 D, E, 继续先深入 D

你会发现这个过程很像：

把当前位置压进去, 不断进入更深层, 走不通再弹出来，回到上一个位置, 这就是栈的感觉。

为什么递归 DFS 也行

因为 递归本身就隐含一个调用栈 call stack。

比如：

def dfs(node):
    for nei in graph[node]:
        dfs(nei)


你虽然没手写 stack = []，但程序底层其实帮你在用栈。

所以：

递归 DFS = 用系统调用栈

迭代 DFS = 你自己手写一个 stack

本质一样。

### DFS 的目标是沿着一条路径尽可能往深处搜索，所以需要优先处理最近刚发现的节点，这对应后进先出的 stack。BFS 的目标是按层遍历，先访问离起点更近的节点，因此需要按照发现顺序处理节点，这对应先进先出的 queue。