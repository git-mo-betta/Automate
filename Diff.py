Diff.py

2. Practical programming idea, make a script that can check the differences between files. Once, I was handed some numbers, 3 lists. If I wanted to check one of those lists against a master list to find out if the master list contained the smaller one, what could I do? 
	
	#Diff.py
	
	input1 = input("Give me the first filepath")       - Asking user for the filepaths they want to compare
	input2 = input("Give me the second filepath")    
	import difflib - This imports the module that allows diff classes and functions for comparison
	
	with open(input1, 'r') as file1, open(input2, 'r') as file2:       -  block opens the two files specified by the user in read                                                                                                                                                                                                            
													mode ('r'), and assigns them to file1 and file2 respectively.
	    content1 = file1.read()
	    content2 = file2.read()         -This reads through the files and turns them into variables 
	
	d = difflib.Differ() -Creates a "differ" object that is used to compute differences between sequences. 
	
	differences = d.compare(content1, content2)  -uses the "compare" method of differ to compute the differences between the two files that were read (content1+2)
	
	if content1 == content2:                                    If both of the files have the same content print same
	    print("These files are the same")
	else:                                                                    If differences print the difference. 
	    print('\n' .join(differences))                  the \n = a new line. You can put what you want in the '  '

