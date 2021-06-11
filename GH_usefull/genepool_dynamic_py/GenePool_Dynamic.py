"""Provides a scripting component.
    Inputs:
        G: moved GenePool
        min: set GenePool min
        max: set GenePool max
        dec: set GenePool Decimals
        df: set GenePool defalt
        cnt: set GenePool count
        df_update: update defalt
        Recom: Recompute
        """

Par = ghenv.Component.Params
gp = Par.Input[0].Sources[0]
print(gp.Minimum)#.VolatileData
print(gp.Maximum)

gp.Minimum = float(min)
gp.Maximum = float(max)
gp.Decimals = dec
gp.Count = cnt
if df_update:
    for i in range(int(gp.Count)):
        gp.Value[i] = df
if Recom:
    gp.ExpireSolution(True)
