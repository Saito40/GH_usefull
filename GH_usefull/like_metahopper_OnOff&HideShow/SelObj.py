doc = ghenv.Component.OnPingDocument()
a_ = doc.SelectedObjects()

a = []
for _a in a_:
    print(   _a.InstanceGuid)
    a.append(str(_a.InstanceGuid))
