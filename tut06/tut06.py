import os
import re
def regex_renamer():



	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	
	if webseries_num==1:
		count=1
		bount=1
		for count,bount,filename in enumerate(os.listdir(r'\corrected_srt\Breaking Bad')):
			if re.search(r'.*srt',filename):
				m='count'
				w=1
				x='0'
				n=fr'Breaking Bad- Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}}'
				re.sub(r'^[a-z]+ [a-z]+ [a-z0-9]+ [a-z0-9.]{18}$',n, filename, flags=re.IGNORECASE)
				count+=1
			if re.search(r'.*mp4',filename):
				t='bount'
				u=1
				x='0'
				n=fr'Breaking Bad- Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}}'
				re.sub(r'^[a-z]+ [a-z]+ [a-z0-9]+ [a-z0-9.]{18}$',n, filename, flags=re.IGNORECASE)
				bount+=1
	if webseries_num==2:
		count=1
		bount=1
		for count,bount,filename in enumerate(os.listdir(r'\corrected_srt\Game of Thrones')):
			if re.search(r'.*srt',filename):
				m='count'
				w=8
				x='0'
				st=re.search(r' - (.*?)/.',filename)
				if st:
					string=st.group(1)
				n=fr'Game of Thrones - Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+string
				re.sub(r'^[a-z]+ [a-z]+ [a-z]+ - [0-9x]+ - .*?/.[a-z.]{21}$',n, filename, flags=re.IGNORECASE)
				count+=1
			if re.search(r'.*mp4',filename):
				t='bount'
				u=8
				x='0'
				st=re.search(r' - (.*?)/.',filename)
				if st:
					string=st.group(1)
				n=fr'Game of Thrones - Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+string
				re.sub(r'^[a-z]+ [a-z]+ [a-z]+ - [0-9x]+ - .*?/.[a-z.]{21}$',n, filename, flags=re.IGNORECASE)
				bount+=1
	if webseries_num==3:
		count=1
		bount=1
		for count,bount,filename in enumerate(os.listdir(r'\corrected_srt\Lucifer')):
			if re.search(r'.*srt',filename):
				m='count'
				w=6
				x='0'
				st=re.search(r' - (.*?)/.',filename)
				if st:
					string=st.group(1)
				n=fr'Lucifer- Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+string
				re.sub(r'^[a-z]+ - [0-9x]+ - .*?/.[a-z.]{13}$',n, filename, flags=re.IGNORECASE)
				count+=1
			if re.search(r'.*mp4',filename):
				t='bount'
				u=6
				x='0'
				st=re.search(r' - (.*?)/.',filename)
				if st:
					string=st.group(1)
				n=fr'Lucifer - Season {u:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+string
				re.sub(r'^[a-z]+ - [0-9x]+ - .*?/.[a-z.]{13}$',n, filename, flags=re.IGNORECASE)
				bount+=1
regex_renamer()
