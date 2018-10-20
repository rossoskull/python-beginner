import collections


class Graph:
    def __init__(self, graph=None):
        self.graph_dict = graph if graph else {}

    def bfs(self, start_node):
        seen, queue = {start_node}, collections.deque([start_node])
        while queue:
            vertex = queue.popleft()
            self.marked(vertex)
            for node in self.graph_dict[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

    @staticmethod
    def marked(n):
        print(n)


if __name__ == "__main__":
    # The graph dictionary
    graph_dict = {"a": {"b", "c"},
                  "b": {"a", "d"},
                  "c": {"a", "d"},
                  "d": {"e"},
                  "e": {"a"}
                  }
    g = Graph(graph_dict)
    g.bfs("a")
