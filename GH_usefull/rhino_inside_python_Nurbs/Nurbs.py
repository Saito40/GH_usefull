import rhinoinside, csv
# import rhino3dm

import matplotlib.pyplot as plt
rhinoinside.load('C:\Program Files\Rhino 7\System')
import System
from System.Collections.Generic import List

from Rhino.Geometry import NurbsCurve
from Rhino.Geometry import ControlPoint
from Rhino.Geometry import Circle
from Rhino.Geometry.Intersect import Intersection
from Rhino.Geometry import Plane
from Rhino.Geometry import Point3d

Cdir = 'GH_usefull/rhino_inside_python_Nurbs'

def NurbCrv(P, W, K):
    n = 3
    P_ = List[Point3d]()
    for p in P: P_.Add(Point3d(p[0], p[1], p[1]))
    nc = NurbsCurve.Create(False, n, P_)
    for i in range(len(P)):
        # cp = ControlPoint()
        # cp.X = P[i][0]
        # cp.Y = P[i][1]
        # cp.Z = P[i][2]
        # cp.W = W[i]
        w = System.Double(W[i])
        cp = ControlPoint(P[i][0], P[i][1], P[i][2], w)
        nc.Points[i] = cp
    for i in range(nc.Knots.Count):
        nc.Knots[i] = K[i]
    C = nc
    return C

def DivDist2D(crv, dist):
    ## 以下を改造しました
    ## Hiroaki Saito : GH C#_Divide Distance With List
    ## https://openddl.com/post/166/
    ## 閲覧：2021/6/2
    pln = Plane.WorldXY
    points = []
    paramList = []

    if crv:
        tmpParam = 0.
        pt = crv.PointAtStart
        dummy_out = System.Double(0)
        tmpParam = crv.ClosestPoint(pt, dummy_out)[1]
        
        points.append(pt)
        paramList.append(tmpParam)
        
        for i in range(len(dist)):
            d = System.Double(dist[i])
            circle = Circle(pln, points[i], d)
            tmpCrv = circle.ToNurbsCurve()
            ci = Intersection.CurveCurve(crv, tmpCrv, 0, 0)
            
            addCheck = False
            tmpList = sorted(ci, key=lambda x:x.ParameterA)
            
            for item in tmpList:
                tmpParam = item.ParameterA
                if tmpParam > paramList[i]:
                    points.append(item.PointA)
                    paramList.append(tmpParam)
                    addCheck = True
                    break
            if not addCheck: break
        pt = crv.PointAtEnd
        points.append(pt)
    return points

P = []
W = []
K = []
reader=csv.reader(open(Cdir + '/PWK.csv', 'r'))
for row in reader:
    try: P.append([float(row[0]), float(row[1]), float(row[2])])
    except: break
for row in reader:
    try: W.append(float(row[0]))
    except: break
for row in reader:
    try: K.append(float(row[0]))
    except: break

# print(P)
# print(W)
# print(K)

C = NurbCrv(P, W, K)
D = [1 for i in range(3810)]
R = DivDist2D(C, D)

# print(R)
x, y = [], []
for r in R:
    # print(r.X, r.Y, r.Z)
    x.append(float(r.X))
    y.append(float(r.Y))

# plt.plot(x, y)
# plt.show()
# plt.savefig(Cdir + "/nurbs.png")
# plt.close()

writer=csv.writer(open(Cdir + '/xy.csv', 'w', newline = ""))
for i in range(len(x)):
    writer.writerow([str(x[i]), str(y[i])])
