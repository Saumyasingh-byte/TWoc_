cp=int(input(" enter the cost price :"))
sp=int(input(" enter the selling price :"))
profit=sp-cp
p=profit*0.05
newprofit=profit+p
newsp=newprofit+cp
print(" profit is :",profit)
print(" selling price after 5% increase in profit is :",newsp)
