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
	p=os.getcwd()
	sc=os.path.join(p,'wrong_srt')
	des=os.path.join(p,'wrong_srt_ sample_Before_rename')
	if os.path.exists(des):
		shutil.rmtree(des)
	
	os.makedirs(os.path.dirname(des), exist_ok=True)
	
	
	shutil.copytree(sc, des)

	des_fpath=os.path.join(p,r'corrected_srt')
	if os.path.exists(os.path.dirname(des_fpath)):
		pass
	else:


	 os.makedirs(os.path.dirname(des_fpath), exist_ok=True)
	q=os.path.join(p,'corrected_srt')

	
     
	
	
	
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
		
				os.rename(src,dst)
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=1
				x='0'
				dst=folde+fr'Breaking Bad- Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}}'+'.mp4'
			
				os.rename(src,dst)
				bount+=1
		sc_fpath=os.path.join(p,folde)
		t=os.path.join(q,'Breaking Bad')
		if os.path.exists(r'corrected_srt\Breaking Bad\\'):
			shutil.rmtree(r'corrected_srt\Breaking Bad\\')
		
		shutil.copytree(sc_fpath,r'corrected_srt\Breaking Bad\\')
		shutil.rmtree(sc_fpath)
		shutil.copytree(r'wrong_srt_ sample_Before_rename\Breaking Bad\\',sc_fpath)
		
		
		
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
				
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=8
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
			
			
				dst=folder+fr'Game of Thrones - Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}} - '+st.group(1)+'.mp4'

				
				os.rename(src,dst)
				bount+=1
		
		
		sc_fpath=os.path.join(p,folder)
		t=os.path.join(q,'Game of Thrones')
		if os.path.exists(r'corrected_srt\Game of Thrones\\'):
			shutil.rmtree(r'corrected_srt\Game of Thrones\\')
		
		shutil.copytree(sc_fpath,r'corrected_srt\Game of Thrones\\')
		shutil.rmtree(sc_fpath)
		shutil.copytree(r'wrong_srt_ sample_Before_rename\Game of Thrones\\',sc_fpath)

		

		
		
          
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
				
				os.rename(src,dst)
				count+=1
			elif re.search(r'.*mp4$'	,filename):
				t=str(bount)
				u=6
				x='0'
				st=re.search(r' - [0-9x]+ - (.*?)\.',filename)
				
				dst=folderr+fr'Lucifer - Season {u:{x}>{season_padding}} Episode {t:{x}>{episode_padding}} - '+st.group(1)+'.mp4'
				
				os.rename(src,dst)
				bount+=1
		sc_fpath=os.path.join(p,folderr)
		t=os.path.join(q,'Lucifer')
		if os.path.exists(r'corrected_srt\Lucifer\\'):
			shutil.rmtree(r'corrected_srt\Lucifer\\')
		
		shutil.copytree(sc_fpath,r'corrected_srt\Lucifer\\')
		shutil.rmtree(sc_fpath)
		shutil.copytree(r'wrong_srt_ sample_Before_rename\Lucifer\\',sc_fpath)
		
		
		

regex_renamer()
 
