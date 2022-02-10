def check(s1, s2):
	# the sorted strings are checked
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		
		

s1 = input("Enter the first String:")
s2 = input("Enter the second String:")
check(s1, s2)
