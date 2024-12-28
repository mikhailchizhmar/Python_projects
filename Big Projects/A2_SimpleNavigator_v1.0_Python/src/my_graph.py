import numpy as np


class Graph:
    def __init__(self):
        self.size = 0
        self.matrix = np.array(0)

    def get_graph_matrix(self):
        return self.matrix

    def get_graph_size(self):
        return self.size

    def load_graph_from_file(self, filename):
        try:
            self.matrix = np.loadtxt(filename, skiprows=1, dtype=int)
            self.size = len(self.matrix)
            return True
        except Exception as exp:
            print(exp)
            return False

    def export_graph_to_dot(self, filename):
        try:
            except_list = []
            with open(filename, "w") as f:
                f.write("graph graphname {\n")
                for i in range(self.size):
                    for j in range(self.size):
                        if self.matrix[i][j] > 0 and (i, j) not in except_list:
                            except_list.append((j, i))
                            f.write("\t" + str(i + 1) + " -- " + str(j + 1) + ";\n")
                f.write("}")
        except Exception as exp:
            print(exp)
    
    def is_directed_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True
