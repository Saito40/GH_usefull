
px = ghenv.Component.Params.Input[0]

def func(dmy):
    for s in px.Sources:
        px.RemoveSource(px.Sources[0])
        a = '働きたくないでござる'

doc = ghenv.Component.OnPingDocument()
ghenv.LocalScope.doc.ScheduleSolution(1, func)
