import xml.etree.ElementTree as ET

tree = ET.fromstring(input())
ans = {"red": 0, "green": 0, "blue": 0}


def dfs(cube, res, depth):
    res[cube.attrib["color"]] += depth
    print(cube.attrib, depth)
    for i in cube.findall("cube"):
        dfs(i, res, depth + 1)


dfs(tree, ans, 1)
print(ans["red"], ans["green"], ans["blue"])
