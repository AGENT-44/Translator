from fnmatch import translate
from deep_translator import GoogleTranslator

langs = GoogleTranslator().get_supported_languages(as_dict=True)


while True:
	inp = input("Enter Text You Want to Translate\n")
	if (inp == ""):
		print("Enter Text And Try Again")
		continue

	for keys,values in langs.items():
		print(f'''Lang Name -> {keys} 
Lang Code -> {values}\n''')

	src = input("Enter Source Language (for auto Detection : Type 'auto'!\n").lower()
	if (src==""):
		print("Please Enter At Least 1 Argument!")
		continue
	elif (src == "auto"):
		dest = input("Enter To Which lang you want to Translate Your Text\n").lower()
		if (dest==""):
			print("Please Enter At Least 1 Argument!")
			continue
		elif (src in langs.keys() or src in langs.values()):
			tran = GoogleTranslator(src,dest).translate(text=inp)
			print(tran)
		elif (src not in langs.keys() or src not in langs.values()):
			print("Invalid Language Passed!")
			continue
	elif (src in langs.keys() or src in langs.values()):
		dest = input("Enter To Which lang you want to Translate Your Text\n").lower()
		if (dest==""):
			print("Please Enter At Least 1 Argument!")
			continue
	
		elif (src in langs.keys() or src in langs.values()):
			tran = GoogleTranslator(src,dest).translate(text=inp)
			print(tran)
		elif (src not in langs.keys() or src not in langs.values()):
			print("Invalid Dest Language Passed!")

			continue
	else:
		print("Please Enter a Valid Src Language!")
		continue

	ask = input("Do you want to Continue or Exit? (Press --'Y' or 'N')").lower()

	if ask == "y":
		continue
	else:
		break
