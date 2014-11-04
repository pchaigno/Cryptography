#!/usr/bin/python
import sys
import os
import re

"""Search for a character in the cipher text.

The character must be present twice with an offset of n.

Args:
	n: The offset between the two instances of the character.

Return:
	The character.
"""
def search_for_character(cipher, n):
	regex = r"(?P<char>.).{" + re.escape(str(n - 1)) + "}(?P=char)"
	return re.findall(regex, cipher)


"""Search for a character in the cipher text.

Search for two identical characters separated by n other characters.
For example, FLAG-1234-1234 (search for the dashes with 5).

Args:
	source: Can be a file or a string.
	n: The number of characters separating the two identical characters.
"""
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: substitution.py <source> <n>")
		sys.exit(2)

	source = sys.argv[1]
	n = int(sys.argv[2])

	cipher = source
	if os.path.isfile(source):
		cipher = open(source, 'r').read()

	lowlet = cipher.lower()
	matches = search_for_character(cipher, n)
	print(matches)
