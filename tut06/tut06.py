#SURESH SAHU 
#1901CE52
#TUT 6

import os
import re
import shutil
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
		folde=r'wrong_srt\Breaking Bad\\'
		dirs=os.listdir(folde)
		for filename in dirs:
			src=folde+filename
			if re.search(r'.*srt$',filename):
				m=str(count)
				w=1
				x='0'
				dst=folde+fr'Breaking Bad- Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}}'+'.srt'
				#re.sub(r'^[a-z]+ [a-z]+ [a-z0-9]+ [a-z0-9.]{18}$',dst, filename, flags=re.IGNORECASE)
				os.rename(src,dst)
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=1
				x='0'
				dst=folde+fr'Breaking Bad- Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}}'+'.mp4'
				#re.sub(r'^[a-z]+ [a-z]+ [a-z0-9]+ [a-z0-9.]{18}$',dst, filename, flags=re.IGNORECASE)
				os.rename(src,dst)
				bount+=1
	if webseries_num==2:
		count=1
		bount=1
		folder=r'wrong_srt\Game of Thrones\\'
		dirs=os.listdir(folder)
		for filename in dirs:
			src=folder+filename
			if re.search(r'.*srt$',filename):
				m=str(count)
				w=8
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
				
                
				dst=folder+fr'Game of Thrones - Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+ st.group(1)+'.srt'
				os.rename(src,dst)
				#re.sub(r'^[a-z]+ [a-z]+ [a-z]+ - [0-9x]+ - .*?\.[a-z.]{21}$',dst, filename, flags=re.IGNORECASE)
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=8
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
			
			
				dst=folder+fr'Game of Thrones - Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}} - '+st.group(1)+'.mp4'

				#re.sub(r'^[a-z]+ [a-z]+ [a-z]+ - [0-9x]+ - .*?\.[a-z.]{21}$',dst, filename, flags=re.IGNORECASE)
				os.rename(src,dst)
				bount+=1
	if webseries_num==3:
		count=1
		bount=1
		folderr=r'wrong_srt\Lucifer\\'
		
		dirs=os.listdir(folderr)
		for filename in dirs:
		
			src=folderr+filename
			if re.search(r'.*srt$',filename):
				m=str(count)
				w=6
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
				
				dst=folderr+fr'Lucifer- Season {w:{x}>{season_padding}} Episode {m:{x}>{episode_padding}} - '+st.group(1)+'.srt'
				#re.sub(r'^[a-z]+ - [0-9x]+ - .*?\.[a-z.]{13}$',dst, filename, flags=re.IGNORECASE)
				os.rename(src,dst)
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=6
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
				
				dst=folderr+fr'Lucifer - Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}} - '+st.group(1)+'.mp4'
				#re.sub(r'^[a-z]+ - [0-9x]+ - .*?\.[a-z.]{13}$',dst, filename, flags=re.IGNORECASE)
				os.rename(src,dst)
				bount+=1

print('Have u renamed all 3 webseries?')
print('*'*25)
print('--(1)if yes---type(y)  All Renmaed files will be copied to new directory \'corrected_srt\'')
print('*'*25)
print('--(2)   Else--type(n) Rename all given 3 webseries once orderly Then press y')
print('*'*25)
ans=(input('y/n---->'))
if ans=="y":
  p=os.getcwd()

  src_fpath=os.path.join(p,'wrong_srt')
  des_fpath=os.path.join(p,r'corrected_srt')
  
  os.makedirs(os.path.dirname(des_fpath), exist_ok=True)
  shutil.copytree(src_fpath, des_fpath)
else:
 regex_renamer()
 
