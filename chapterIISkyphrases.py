

try:
	#opening
	print ("opening pastebin1.txt")
	Filewithskyphrases=open("pastebin1.txt","r")
	IncludingOfFile = Filewithskyphrases.read()
	#print "so this is the input: \n\n", IncludingOfFile[:100], "(...)\n\n etc, you know."
	
	#searching the lines/where each line ends
	Lines=[]
	ActualLine=""
	for i in range(len(IncludingOfFile)):
		if IncludingOfFile[i]=="\n":
			Lines.append(ActualLine)
			ActualLine=""
		else:
			ActualLine+=IncludingOfFile[i]
	#print "list, which each element is one line of pastebin1.txt \n\n", Lines[:6], "(...)\n\n etc, you know."

	#checking if the line is valid
	CounterOfValidLines=0
	for i in range(len(Lines)): 

		#identyfiing "words" within the line
		ActualLine=Lines[i]
		StartOfPrevWord=0
		Words=[]
		for j in range(len(ActualLine)):
			if ActualLine[j]==" ":
				#print "found a word"
				Words.append(ActualLine[StartOfPrevWord:j])
				StartOfPrevWord=j+1
		Words.append(ActualLine[StartOfPrevWord:j+1]) #to add the last word in the line
		print ("line: ", i, "words: ", Words)

		#checking if the Words has duplicates
		Valid="YES"
		for k1 in range(len(Words)):
			#print "actual word: ", Words[k1]
			for k2 in range(len(Words)-k1-1):
				#print "analized word: ", Words[k1+k2+1]
				if Words[k1]==Words[k1+k2+1]:
					#print "invalid line"
					Valid="NO"
		if Valid=="YES":
			CounterOfValidLines+=1
			#print "dodana do puli"
	
	#result
	print ("\n FINISHED! \n Found: ", CounterOfValidLines,  " valid 'Skyphrases' ;) Have a nice day!")
	Filewithskyphrases.close()

except IOError:
	print ("Error, probably cant find pastebin1.txt in the current directory")
