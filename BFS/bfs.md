## 适合 BFS 的信号

- 最短路径

- 最少步数

- 一层一层扩散

- 层序遍历

- 从多个起点同时扩散

### 比如：

Number of Islands：DFS/BFS 都行

Binary Tree Level Order Traversal：BFS 最自然

Word Ladder：BFS 更合适，因为是最少步数

Permutations：DFS/backtracking

## BFS 为什么用 queue

BFS 是 Breadth-First Search，广度优先搜索。

它的核心思想是：

先把当前这一层都访问完，再去下一层。

这个“谁先被发现，谁先扩展”，本质上就是 先进先出 FIFO。

也就是说：

先发现的节点

应该先处理

后发现的节点，排在后面

这就天然对应 queue。