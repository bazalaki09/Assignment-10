#Patrick Kayanga-Bazalaki

# code to import matplotlib and json
import json
import matplotlib.pyplot as plt

#code to open and access the text file
f=open("stockshelp.txt","r")

if f.mode =="r":
    jsonData=f.read()
    d=json.loads(jsonData)
    
    x=0
    close=[]
    date=[]
    symbol=[]
    symboltwo=[]
    aigSymbolClose=[]
    aigSymbolCloseDate=[]
    
    fSymbolClose=[]
    fSymbolCloseDate=[]
    
    fbSymbolClose=[]
    fbSymbolCloseDate=[]
    
    googSymbolClose=[]
    googSymbolCloseDate=[]
    
    ibmSymbolClose=[]
    ibmSymbolCloseDate=[]
    
    mSymbolClose=[]
    mSymbolCloseDate=[]
    
    msftSymbolClose=[]
    msftSymbolCloseDate=[]
    
    rdsaSymbolClose=[]
    rdsaSymbolCloseDate=[]
    
    length=len(d)
    #print(len(d))
    ##dates are ordered latest to oldest, reverses order
    d.reverse()
    while x<length:
        #print(d[x]['Symbol'])
        symbol.append(d[x]['Symbol'])
        #print(d[x]['Date'])
        date.append(d[x]['Date'])
        #print(d[x]['Close'])
        close.append(d[x]['Close'])
        if d[x]['Symbol'] not in symboltwo:
            symboltwo.append(d[x]['Symbol'])
        if d[x]['Symbol']=='AIG':
            aigSymbolClose.append(d[x]['Close'])
            aigSymbolCloseDate.append(d[x]['Date'])
            #plt.plot(aigSymbolCloseDate,aigSymbolClose)
        if d[x]['Symbol']=='F':
            fSymbolClose.append(d[x]['Close'])
            fSymbolCloseDate.append(d[x]['Date'])
        if d[x]['Symbol']=='FB':
            fbSymbolClose.append(d[x]['Close'])
            fbSymbolCloseDate.append(d[x]['Date'])
        if d[x]['Symbol']=='GOOG':
            googSymbolClose.append(d[x]['Close'])
            googSymbolCloseDate.append(d[x]['Date'])
        if d[x]['Symbol']=='IBM':
            ibmSymbolClose.append(d[x]['Close'])
            ibmSymbolCloseDate.append(d[x]['Date'])
        if d[x]['Symbol']=='M':
            mSymbolClose.append(d[x]['Close'])
            mSymbolCloseDate.append(d[x]['Date'])
        if d[x]['Symbol']=='MSFT':
            msftSymbolClose.append(d[x]['Close'])
            msftSymbolCloseDate.append(d[x]['Date'])    
        if d[x]['Symbol']=='RDS-A':
            rdsaSymbolClose.append(d[x]['Close'])
            rdsaSymbolCloseDate.append(d[x]['Date'])
        x+=1
  
    print(close[0])
    #print(date[0])
    #print(d[0]["Close"])
    #print(d[0]["Date"])
    #prints unique symbols
    print(symboltwo)
    
    #pie chart code   
 
labels = 'rdsa', 'm', 'goog', 'fb', 'f', 'aig', 'msft'
shares = [400, 425, 125, 150, 85, 235, 85]
colors = ['green', 'purple', 'brown', 'lightskyblue', 'blue', 'red', 'yellow']
explode = (1, 1, 0, 0, 0, 0,0)  #Highest number of shares exploded with 1
 
plt.pie(shares, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
patches, texts = plt.pie(shares, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
 
plt.axis('equal')
plt.show()

