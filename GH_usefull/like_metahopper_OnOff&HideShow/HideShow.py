from Grasshopper.Kernel import Special

y = not y

def f(dmy):
    for d in D:
        try:
            d.Hidden = y
            d.ExpireSolution(False)
        except: print(d)

D = []
doc = ghenv.Component.OnPingDocument()
a = doc.ActiveObjects()

for _a in a:
    for _x in x:
        if _x == str(_a.InstanceGuid):
            D.append(_a)
            break

doc.ScheduleSolution(1, f)
