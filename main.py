from model import SVMBreastPredictor

predictor=SVMBreastPredictor()

print("Inpute Format(mm) --(Leave blank for unknown data")
print("1. Radius Mean\n2. TextureMean\n3. Perimeter Mean\n4. Area Mean")
try:
    rm=float(input("Enter radius mean: "))
    tm=float(input("Enter texture mean: "))
    pm=float(input("Enter perimeter mean: "))
    am=float(input("Enter area mean: "))
except:
    print("Invalid input")
    exit()
try:
    res=predictor.predict(rm=rm, tm=tm, pm=pm, am=am)
    if res==1:
        print("Malignant")
    else:
        print("Benign")
except:
    print("Please Run Again")