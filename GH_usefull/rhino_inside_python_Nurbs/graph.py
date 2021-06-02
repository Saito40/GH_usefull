import csv
import matplotlib.pyplot as plt

Cdir = 'GH_usefull/rhino_inside_python_Nurbs'

x = []
y = []
reader=csv.reader(open(Cdir + '/xy.csv', 'r'))
for row in reader:
    try: 
        x.append(float(row[0]))
        y.append(float(row[1]))
    except: break


plt.plot(x, y)
plt.show()
plt.savefig(Cdir + "/nurbs.png")
plt.close()
