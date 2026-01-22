"""
park: stays=0.5, go to apartment=0.3, go to restaurant=0.2
apartment: stays=0.1, go to park=0.5, go to restaurant=0.4
restaurant: stays=0.1, go to park=0.1, go to apartment=0.8
"""
apartment = 1000
park = 0
restaurant = 0
i=0
while i<100 :
# and isinstance(apartment, int) and isinstance(park, int) and isinstance(restaurant, int) and apartment>=0 and park>=0 and restaurant>=0:
    # sa=int(apartment*0.1) #stay at apartment
    atp=int(apartment*0.5) # go to park
    atr=int(apartment*0.4) # go to restaurant
    apartment-=(atp+atr) #stay at apartment

    pta=int(park*0.3) # go to apartment
    ptr=int(park*0.2) # go to restaurant
    park-=(pta+ptr) #stay at park

    rtp=int(restaurant*0.1) # go to park
    rta=int(restaurant*0.8) # go to apartment
    restaurant-=(rtp+rta) #stay at restaurant

    park,apartment, restaurant= park+atp+rtp,apartment+pta+rta, restaurant+atr+ptr
    i+=1
    print("Apartment: ",apartment,", Park: ",park,", Restaurant: ",restaurant)