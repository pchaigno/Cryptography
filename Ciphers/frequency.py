#!/usr/bin/python
import sys;
import os;

"""Computes the number of occurrences for each letter.

Args:
	lowlet: The string of lowercase characters to analyse.

Returns:
	A map of characters to occurrences.
"""
def occurrence_one_letters(lowlet):
	occurrences = {}
	for character in lowlet:
		if character in occurrences:
			occurrences[character] += 1
		else:
			occurrences[character] = 0
	return occurrences


"""Computes the frequency for each letter.

Args:
	lowlet: The string of lowercase characters to analyse.

Returns:
	A map of characters to frequencies.
"""
def frequency_one_letters(lowlet):
	frequencies = occurrence_one_letters(lowlet)
	total = len(lowlet)
	for character, occurrence in frequencies.iteritems():
		frequencies[character] = 100.0 * occurrence / total
	return frequencies


"""Computes the frequencies of each characters in a text.

Args:
	source: Can be a file or a string.
"""
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: frequency.py <source>")
		sys.exit(2)

	source = sys.argv[1]

	string = source
	if os.path.isfile(source):
		string = open(source, 'r').read()

	lowlet = string.lower()
	frequencies = frequency_one_letters(lowlet)

	# Prints the frequencies:
	for character, frequency in frequencies.iteritems():
		print("%c: %0.1f" %(character, frequency))
