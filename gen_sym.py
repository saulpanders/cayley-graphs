# Paul Sanders
# 9/15/18
# generates a .csv file displaying the complete graph on n verticies as an adj matrix
# input: n
# output: .csv file
# to be used with undir_graph.py
filename = ".\\kn.csv"
f = open(filename, "w+")

print("what size matrix? (int)")
n = input()
print(n)
tmp = []
for i in range(0, int(n)):
    for j in range(0, int(n)):
        if i == j:
            tmp.append("0")
        else:
            tmp.append("1")
    ln = ','.join(tmp)
    f.write(ln + '\n')
    tmp.clear()

f.close()
