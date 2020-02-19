class DirectedGraph(object):
    def __init__(self, d):
        if isinstance(d, dict):
            self.__graph = d
        else:
            self.__graph = dict()
            print('Sth error')

    def __generatePath(self, graph, path, end, results):
        current = path[-1]
        if current == end:
            results.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.__generatePath(graph, path + [n], end, results)

    def searchPath(self, start, end):
        self.__results = []
        self.__generatePath(self.__graph, [start], end, self.__results)
        self.__results.sort(key = lambda x:len(x))    #按照所有路徑的長度排序
        print('The path from ',self.__results[0][0], ' to ', self.__results[0][-1], ' is:')
        for path in self.__results:
            print(path)

d = {'A':['B', 'C', 'D'],
     'B':['E'],
     'C':['D', 'F'],
     'D':['B', 'E', 'G'],
     'E':['D'],
     'F':['D', 'G'],
     'G':['E']}
g = DirectedGraph(d)
g.searchPath('A', 'D')
g.searchPath('A', 'E')
