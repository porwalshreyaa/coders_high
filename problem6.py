# happy -> 0.3  stressed ->0.5, happy->stressed 0.7 , stressed->happy 0.5
happy = 1000
stressed = 0
i=0
while i<100 :
# and isinstance(happy, int) and isinstance(stressed, int) and happy>=0 and stressed>=0:
    x=int(stressed*0.5)
    stressed-=x
    y=int(happy*0.7)
    happy-=y
    happy,stressed= happy+x,stressed+y
    i+=1
    print("Happy: ",happy,", Stressed: ",stressed)