#args
def meyveler(*meyve):
    print("Meyve: ", meyve[1])

meyveler("Elma", "Armut", "Muz", "Karpuz")

print("**************************")

#kwargs
def meyveler(**meyve):
    print("meyve: ", meyve["meyve1"])

meyveler(meyve1= "kiraz", meyve2= "kavun")
