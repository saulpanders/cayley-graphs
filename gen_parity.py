# Paul Sanders
# 9/15/18
# generates a .csv file displaying a graph on n verticies as an adj matrix
# input: n
# output: .csv file
# to be used with undir_graph.py


filename = ".\\g.csv"
f = open(filename, "w+")

print("generic graphz")
print("what size matrix? (int)")
n = input()
print(n)
tmp = []
for i in range(0, int(n)):
    for j in range(0, int(n)):
        if i == j:
            tmp.append("0")
        elif (i + j) % 2 == 0:
            tmp.append("1")
        else:
            tmp.append("0")
    ln = ','.join(tmp)
    f.write(ln + '\n')
    tmp.clear()

f.close()
