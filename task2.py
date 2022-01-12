print("Swallow Speed Analysis: Version 1.0") 
KPH=[]
MPH=[]
while True:
    s=input("Enter the Next Reading:") #Ask to enter the reading.
    if s=="":
        break
    speed=float(s[1:]) 
    MPH.append(speed) if s[0].lower()=="u" else  KPH.append(speed)
newlst = MPH.copy()
MPH+=[i*0.621371 for i in KPH] #Converting miles into kilometers.
KPH+=[i*1.60934 for i in newlst] #Converting kilometers into miles.
if len(KPH)!=0: 
    print("{} Readings Analysed".format(len(KPH)))
    print("Max Speed:{:.2f}KPH, {:.2f}MPH".format(max(KPH),max(MPH)))
    print("Min Speed:{:.2f}KPH, {:.2f}MPH".format(min(KPH),min(MPH)))
    print("Avg Speed:{:.2f}KPH, {:.2f}MPH".format(sum(KPH)/len(KPH),sum(MPH)/len(MPH)))
else:
    print("No readings entered. Nothing to do.")
