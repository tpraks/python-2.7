import os
rootdir = raw_input("Enter Dir to read:")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print os.path.join(subdir, file)
		f=open(file,'r')
		lines=f.readlines()
		for line in lines:
			line=re.sub(src_str,repl_str,line)
		f=open(file,'w')
			
		
	print ("--------------")
	for dir in dirs:
		print dir
