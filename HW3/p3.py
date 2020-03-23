def maxNumberOfWords(text,word):
	#Change both text and word to lower
	word=word.lower()
	text=text.lower()

	#create two dictionaries 
	word_dict=dict()
	text_dict=dict()

	#Input letters and their corresponding numbers
	#Worst case is sum(1+...+n)  n*(n+1)/2 O(n^2)
	for i in word:
		if i not in word_dict:
			word_dict[i]=1
		else:
			word_dict[i]+=1
	
	#Creating dictionary for text
	for i in text:
		if i in word_dict:
			if i not in text_dict:
				text_dict[i]=1
			else:
				text_dict[i]+=1

	#Dividing the first with the second list and taking the min	
	values_list=[int(text_dict[i]/word_dict[i]) for i in word_dict]
	print (min(values_list))


text="wwoo"
word="wow"
maxNumberOfWords(text,word)