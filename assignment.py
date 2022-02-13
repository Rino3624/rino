
'''If a rino has go to shopping mall and he purchase 2 shirts and 1 pant.he had pay bill for his Dresses. he need help to go for parking area.
Write a code for these situation '''


from typing import DefaultDict

try:
    def shopping():

            allsections=("kids","mens","womens","accessories")
            print(allsections)
        
            section=input("In Which Category do you want to Shopping??")
            if(section==allsections[0]):
                
                print("You selected a Kids Section. So, please go to Ground Floor...")
        
                    
                y=("Shirt","Pant","Traditional dresses","Inners")
                print("We have",y,"for You...")
                print("Kindly! Start your Purchase")

                def check():
                    purchasing=input("Are you finished Purchase??")
                    if(purchasing=="yes"):
                        #billing 
                        no_shirts=float(input("enter no.of Shirt :"))
                        no_pants=float(input("enter no.of Pant :"))
                        no_iner=float(input("enter no.of Inner:"))
                        no_trad=float(input("enter no.of Traditional Dresses:"))
                        total=no_shirts*100.25+no_iner*50.63+no_trad*200.00+no_pants*200.00
                        print("Total Bill Amount is Rs.",total)
                        #exit mall
                        vehicle=input("Are you came with vehicle for shopping??") 
                        if(vehicle=="yes"):
                            print("Kindly! Go to the parking area to pickup your Vehicle and THANKS FOR YOUR SHOPPING!!")
                        elif(vehicle=="no"):
                            print("Kindly please go the Infront of our building.The bus will arrive in a few minutes and THANKS FOR YOUR SHOPPING!!")
                        else:
                            print("Please Enter Proper Answer...")
                    elif(purchasing=="no"):
                        print("Sorry!! Carry on your Shopping...")
                        return check()
                    
                
            
                    else:
                        print("Please Enter Proper Answer...")
                check()
            elif(section=="womens"):
                print("You selected a Womens Section. So, please go to First Floor...")
        
                    
                y=("Shirt","Pant","Traditional Sarees","Inners")
                print("We have",y,"for You...")
                print("Kindly! Start your Purchase")

                def check():
                    purchasing=input("Are you finished Purchase??")
                    if(purchasing=="yes"):
                        #billing
                        no_shirts=float(input("enter no.of Shirt :"))
                        no_pants=float(input("enter no.of Pant :"))
                        no_iner=float(input("enter no.of Inner:"))
                        no_trad=float(input("enter no.of Traditional Sarees:"))
                        total=no_shirts*100.25+no_iner*50.63+no_trad*200.00+no_pants*200.00
                        print("Total Bill Amount is Rs.",total)
                        #exit mall
                        vehicle=input("Are you came with vehicle for shopping??") 
                        if(vehicle=="yes"):
                            print("Kindly! Go to the parking area to pickup your Vehicle and THANKS FOR YOUR SHOPPING!!")
                        elif(vehicle=="no"):
                            print("Kindly please go the Infront of our building.The bus will arrive in a few minutes and THANKS FOR YOUR SHOPPING!!")
                        else:
                            print("Please Enter Proper Answer...")
                    elif(purchasing=="no"):
                        print("Sorry!! Carry on your Shopping...")
                        return check()
                    
                
            
                    else:
                        print("Please Enter Proper Answer...")
                check()
            elif(section=="mens"):
                print("You selected a Mens Section. So, please go to Second Floor...")
        
                    
                y=("Shirt","Pant","Traditional Dresses","Inners")
                print("We have",y,"for You...")
                print("Kindly! Start your Purchase")

                def check():
                    purchasing=input("Are you finished Purchase??")
                    if(purchasing=="yes"):
                        #billing
                        no_shirts=float(input("enter no.of Shirt :"))
                        no_pants=float(input("enter no.of Pant :"))
                        no_iner=float(input("enter no.of Inner:"))
                        no_trad=float(input("enter no.of Traditional Dressres:"))
                        total=no_shirts*100.25+no_iner*50.63+no_trad*200.00+no_pants*200.00
                        print("Total Bill Amount is Rs.",total)
                        #exit mall
                        vehicle=input("Are you came with vehicle for shopping??") 
                        if(vehicle=="yes"):
                            print("Kindly! Go to the parking area to pickup your Vehicle and THANKS FOR YOUR SHOPPING!!")
                        elif(vehicle=="no"):
                            print("Kindly please go the Infront of our building.The bus will arrive in a few minutes and THANKS FOR YOUR SHOPPING!!")
                        else:
                            print("Please Enter Proper Answer...")
                    elif(purchasing=="no"):
                        print("Sorry!! Carry on your Shopping...")
                        return check()
                    
                
            
                    else:
                        print("Please Enter Proper Answer...")
                check()
                
            else:
                print("Please Enter Proper a Section")
    shopping()  
except:
    print("An Error occurred")
finally:
    print("Program for shopping")
 