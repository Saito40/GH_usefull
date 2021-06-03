
px = ghenv.Component.Params.Input[0]
for s in px.Sources:
    px.RemoveSource(px.Sources[0])
    px.ExpireSolution(True)
    a = '働きたくないでござる'
