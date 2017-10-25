#!/usr/bin/env python
import random
import sys


def encrypt(plaintext, key):
	if key == None:
		key = random_string(len(plaintext))
	else:
		key = fixkey(plaintext, key)
	alist = string_to_list_of_numbers(plaintext)
	blist = string_to_list_of_numbers(key)
	clist = add_lists(alist, blist)
	ciphertext = list_of_numbers_to_string(clist)
	return ciphertext, key

def decrypt(ciphertext, key):
	if key == None:
		err()
	key = fixkey(ciphertext, key)
	alist = string_to_list_of_numbers(ciphertext)
	blist = string_to_list_of_numbers(key)
	clist = subtract_list(alist, blist)
	plaintext = list_of_numbers_to_string(clist)
	return plaintext

def fixkey(text, key):
	try:
		while len(key) < len(text):
			key += key
		key = key[:len(text)]
	except TypeError:
		err()
	finally:
		return key

def letter_to_number(letter):
	number = ord(letter)
	return number - 65

def number_to_letter(number):
	letter = chr(number + 65)
	return letter

def list_to_string(li):
	str1 = ''.join(li)
	return str1

def string_to_list_of_numbers(str1):
	li = []
	for character in str1:
		li.append(letter_to_number(character))
	return li

def list_of_numbers_to_string(li):
	str1 = ''
	for i in li:
		if i < 0:
			i += 26
		str1 += number_to_letter(i%26)
	return str1

def add_lists(alist, blist):
	if len(alist) != len(blist):
		return None
	clist = []
	for a, b in zip(alist, blist):
		clist.append(a+b)
	return clist

def subtract_list(alist, blist):
	if len(alist) != len(blist):
		return None
	clist = []
	for a, b in zip(alist, blist):
		clist.append(a-b)
	return clist

def random_letter():
	return chr(random.randint(65,90))

def random_string(length):
	str1 = ''
	for i in range(length):
		str1 += random_letter()
	return str1


def stringify(args):
	for i in range(len(args)):
		args[i] = str(args[i])
	return args

def e(arg, larg):
	ciphertext, key = arg[2], None
	if larg >= 4:
		key = arg[3]
	ciphertext, key = encrypt(ciphertext, key)
	print "Encrypted Message: ", ciphertext
	print "Key: ", key

def d(arg, larg):
	ciphertext, key = arg[2], None
	if larg >= 4:
		key = arg[3]
	plaintext = decrypt(ciphertext,key)
	print "Decrypted Message: ", plaintext

def help():
	print "Encrypt: '-e [PLAINTEXT] [KEY]' -> CIPHERTEXT"
	print "Decrypt: '-d [CIPHERTEXT] [KEY]' -> PLAINTEXT"

def err():
	print("Invalid arguments, closing...")

def main():
	arg = stringify(sys.argv)
	larg = len(arg)

	if larg < 2:
		help()
	elif larg >= 3:
		if arg[1] == '-e':
			e(arg, larg)
		elif arg[1] == '-d':
			d(arg, larg)
		else:
			err()
	else:
		err()
		help()

if __name__ == '__main__':
	main()





