try:
	import sys
	from bs4 import BeautifulSoup
	import requests
	banner=""" 
		
		$$$$$$      $$$$$$$$$$$$ $$$$$$$$$$$$$ $$$$$$$$$$$$ $$$$$       $$$       $$$
		$$$  $$$    $$$$$$$$$$$$ $$$$$$$$$$$$$ $$$$$$$$$$$$ $$$   $$$     $$$    $$$
		$$$     $$$      $$$     $$$		   $$$      $$$     $$$     $$$$$$
		$$$     $$$      $$$     $$$		   $$$      $$$     $$$       $$$
		$$$     $$$      $$$     $$$		   $$$      $$$   $$$         $$$
		$$$     $$$      $$$     $$$		   $$$      $$$$$             $$$
		$$$   $$$   $$$$$$$$$$$$ $$$$$$$$$$$$$ 	   $$$      $$$               $$$
		$$$$$$      $$$$$$$$$$$$ $$$$$$$$$$$$$ 	   $$$      $$$               $$$
															
															
		Coded by: pr0fsr
		
		A small tool created using python to find the meaning of the word
		All the definitions are from Dictionary.com 
		
		Usage: python dictpy.py [Your word]
				
		In case of any problem mail me at pr0fsr007@gmail.com 
			
		"""
	url="https://www.dictionary.com/browse/"+str(sys.argv[1])
	req=requests.get(url)
	soup=BeautifulSoup(req.text, "html.parser")
	try:
		defi=soup.find('div',attrs={'class':'css-kg6o37 e1q3nk1v3'})
		print("Dictionary.com\n")
		print("Definition: "+str(sys.argv[1]))
		print("\t"+defi.text+"\n")
	except AttributeError:
		print("\t"+"No definition found!"+"\n")
except IndexError:
	print(banner) 
except requests.exceptions.ConnectionError:
	print("\nNo internet connection!\n")
	print("Tip: Have a strong internet connection") 
except ModuleNotFoundError:
	print("\nRequirement not satisfied!\n")
	print("Tip: Windows/Linux - on terminal type\npip install beautifulsoup4")
