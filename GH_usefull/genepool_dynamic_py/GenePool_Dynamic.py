
Par = ghenv.Component.Params
gp = Par.Input[0].Sources[0]
print(gp.Minimum)
print(gp.Maximum)

gp.Minimum = float(min)
gp.Maximum = float(max)
gp.Decimals = dec
gp.Count = cnt
for i in range(int(gp.Count)):
    gp.Value[i] = df
Par.OnParametersChanged()
        
