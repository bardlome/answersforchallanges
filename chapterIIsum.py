import pastebin2

def WelcomeToTheList(Lista,ListWithNumbers):
	for i in range(len(Lista)):
		#print(Lista[i])
		if (isinstance(Lista[i], dict)): 
			WelcomeToTheDict(Lista[i],ListWithNumbers)
		elif (isinstance(Lista[i], list)): 
			WelcomeToTheList(Lista[i],ListWithNumbers)
		elif (isinstance(Lista[i], int)):
			Numbers.append(Lista[i])


def WelcomeToTheDict(Slownik,ListWithNumbers):
        for i in Slownik:
                #print(Slownik[i]) 
                if (isinstance(Slownik[i], dict)): 
	                WelcomeToTheDict(Slownik[i],ListWithNumbers)
                elif (isinstance(Slownik[i], list)): 
	                WelcomeToTheList(Slownik[i],ListWithNumbers)
                elif (isinstance(Slownik[i], int)):
	                Numbers.append(Slownik[i])


Numbers=[]
#print (pastebin2.PASTEBIN_JSON)


for i in pastebin2.PASTEBIN_JSON:
	if (isinstance(pastebin2.PASTEBIN_JSON[i], int)): 
		Numbers.append(pastebin2.PASTEBIN_JSON[i])
	elif (isinstance(pastebin2.PASTEBIN_JSON[i], list)): 
		WelcomeToTheList(pastebin2.PASTEBIN_JSON[i],Numbers)
	elif (isinstance(pastebin2.PASTEBIN_JSON[i], dict)): 
		WelcomeToTheDict(pastebin2.PASTEBIN_JSON[i],Numbers)

FinValue=0
for i in range(len(Numbers)):
	FinValue+=Numbers[i]
print ("And here we go - I think that the total sum = ", FinValue)
#And here we go - I think that the total sum =  111754


