from collections import deque


class Bfs:
    def __init__(self, adj):
        self.adj = adj

    def traverse(self, start):
        visited = {start}
        order = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order


def main():
    adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    bfs = Bfs(adj)
    print(" ".join(str(n) for n in bfs.traverse(0)))


if __name__ == "__main__":
    main()
