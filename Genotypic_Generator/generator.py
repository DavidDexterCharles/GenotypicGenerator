# David Charles
import numpy 

#User enters number of characteristics and then number of generations
#and a number of alleles is allowed to be entered for each characteristic, based on how the problem
#was worded it was unclear to know whether the user uses the same number of alleles for each characteristics
#but because i'm not a Biology major,so base on research i built the program to allow it.
#The probabilities in the probability distribution vector was calculated using the punnett square 

Storage={}
a={}
ch =int(raw_input("Please enter number of Characteristics"))
for realm in range(0,ch):
    print "For Characteristic ",realm+1
    a[realm] =int (raw_input("Please enter number of Alleles"))
f =int(raw_input("Please enter number of Filial generations"))   
#a =int (raw_input("Please enter number of Alleles"))
allow=True
if ch>0:
    for realm in range(0,ch):
        alleles=[]
        pdVector=[]
        pdVector2=[]
        reproMatrix=[]
        

        
        arr1=[]
        arr2=[]
    
        for var in range(0,a[realm]):
            alleles.insert(var,str(realm)+str(var))
      
        
        #print "Allele",realm+1, alleles
        
        i=0
        x=0
        
        repeat=[]
        pdv1={}
        pdv2={}
        for var1 in range(0,a[realm]):
            for var2 in range(x,a[realm]):
                if alleles[x]==alleles[var2]:
            
                    pdv1[i]= alleles[x]
                    pdv2[i]=alleles[var2]
                
                    repeat.insert(i,int(1)) 
                else:
           
                    pdv1[i]= alleles[x]
                    pdv2[i]=alleles[var2]
                    repeat.insert(i,int(2)) 
                i=i+1
                
            x=x+1
          
           
            
        #print"Prob. Distribution vector", pdVector 
        #print"PDV1", pdv1 
        #print"PDV2", pdv2 
        #print "Repeat= " ,repeat
        denominator=float(a[realm]*a[realm])
        #print denominator
       
        for var in range(0,len(pdv1)):
            pdVector2.insert(var,float(repeat[var]/denominator) )
        
        k=0
        
        for varq in range(0,len(pdv1)):
            for vart in range(0,len(pdv1)):
                list1Top=pdv1[varq] 
                list1Bottom= pdv2[varq]
                list2Top=pdv1[vart] 
                list2Bottom= pdv2[vart]
            
                # All pure
                if list1Top==list2Top and list1Top==list2Bottom and list1Bottom==list2Top and list1Bottom==list2Bottom:
                    reproMatrix.insert(k, float(1))
                #cross by itself is 1/2
                elif list1Top==list2Top and list1Bottom==list2Bottom:
                    reproMatrix.insert(k, float(.5))
                #A pure by a different pure
                elif list1Top==list1Bottom and list2Top==list2Bottom and list1Top + list1Bottom!=list2Top + list2Bottom:
                    reproMatrix.insert(k,float(0) )
                #A CROSS by a pure parent is 1/4
                elif list1Top!=list1Bottom and list2Top==list2Bottom and list1Top==list2Top and list1Top==list2Bottom or list2Bottom==list2Top and list1Bottom==list2Bottom:
                    reproMatrix.insert(k,float(.25))
                else:
                    reproMatrix.insert(k,float(0))
                k=k+1
               
                    
        
       
        
        v=numpy.array(reproMatrix).reshape(len(pdv1),len(pdv1))
        
        # print v
        
        distributionvector=numpy.array(pdVector2)
      
        
        temp=v
        
        for var in range(0,f):
            temp=v.dot(temp)
        
        
        myvary=numpy.dot(distributionvector,temp)
        total=0 
        for check in range(0,len(myvary)):
            total=total+ myvary[check] 
        #print "The Dvecs For each Phenotype", total   
        
        Storage[realm] = myvary
        
        
        
        
        
    #print Storage
    FinalDistribution=[] 
    
    final=0
    x=1
    thesum=0
    i=0
    newvec=[]
    #for realm1 in range(0,len(Storage
    final=1
    if ch==1:FinalDistribution=Storage[0]
    else:
        while True:
            #for var in range(0,len(Storage[realm2])):
                if i==0:
                    stemp=Storage[0]
                    tstemp=Storage[1]
                else:
                    stemp=numpy.array(newvec)
                    tstemp=Storage[final]
                    newvec=[]
                    i=0
                #print stemp[var]
                #for realm3 in range(x,len(Storage)):
                for realm2 in range(0,len(stemp)):
                    for realm3 in range(0,len(tstemp)):
                        #print "stemp[realm2],tstemp[realm3]", stemp[realm2],tstemp[realm3]
                        thesum=stemp[realm2]*tstemp[realm3]
                        newvec.insert(i,thesum)
                        i=i+1
                    #print "The sum",thesum   
                    #print"_________________________________________________________________"
                    thesum=0
                
                #print "New Vector", newvec
                final=final+1
                #print "Final",final
                #print "Storage Size",len(Storage)
                if final==len(Storage):
                    break
                #realm1=realm1+1
                
                
                
                
                
       
    if ch!=1:FinalDistribution=newvec
    total=0 
    print "Distribution Vector of nth Generation"
    print FinalDistribution
    for check in range(0,len(FinalDistribution)):
        total=total+ FinalDistribution[check] 
    print"Total probability", total  
    print"Number of elements in distribution vector", len(FinalDistribution)

else: print " Invalid entry"