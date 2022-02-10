def binarySearch(arr, x):
	l = 0
	r = len(arr)
	while (l <= r):
		m = l + ((r - l) // 2)

		res = (word == arr[m])

		# Check if word is present at mid
		if (res == 0):
			return m - 1

		# If word greater, ignore left half
		if (res > 0):
			l = m + 1

		# If word is smaller, ignore right half
		else:
			r = m - 1

	return -1


if __name__ == "__main__":

	arr = ["shellscript", "python","aws", "docker"];
	word = "aws"
	result = binarySearch(arr, word)

	if (result == -1):
		print("Element not present")
	else:
		print("Element found at index" ,
								result)


