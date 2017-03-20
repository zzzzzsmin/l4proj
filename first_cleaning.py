import io
import re

with io.open('test1-1.txt', 'r', encoding='utf-8') as inFile,\
	 io.open('outputtest1.txt', 'w', encoding='utf-8') as outFile:

	 #for each file(pdftotext.txt) find the word 'Reference' using regex, find that word, specifically capital R OR 'REFERENCE' all in CAPITAL
	
	 for line in inFile:

	 		for i in range(len(num)):
	 			if line.startswith('REFERENCES') or line.startswith('References'):
	 				#DON'T ADD ANYTHING. STOP WRITING TO NEW FILE.
	 				#If 'REFERENCES' or 'References' is not found then write to file until they are found
	 				break
	 			else:
	 				line = line.replace(num[i],'')
	 				cleanline = re.sub('[^a-zA-Z]', ' ', line) #no digits but declare a-zA-Z to remove special characters
	 				cleanline = cleanline.lower()
	 				gtgline = re.sub(' +', ' ', cleanline)	 			
	 		#outFile.write(" ".join(cleanline.split()))
	 		outFile.write(unicode(' '.join(gtgline.split(' '))))


	 
