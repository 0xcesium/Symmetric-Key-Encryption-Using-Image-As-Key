#-*-coding:utf-8-*-

from PIL import Image

class ProcessingError(RuntimeError):
	pass

class NSKEI:

	def __init__(self, image):
		self.im = Image.open(image).convert('L')
		self.enc_file_name = "encrypted.enc"
		self.dec_file_name = "recovered_stream.bin"

	def __version__(self):
		return "1.0.0"

	def getColData(self):
		width = self.im.size[0]
		height = self.im.size[1]
		load = self.im.load()
		return [load[w,h] for w in range(width) for h in range(height)]

	def read(self, data, keystream):
		cleartext = ''
		for k in keystream.split('.'):
			index = int(k, 2)
			cleartext += chr(data[index])
		return cleartext

	def write(self, data, cleartext):
		enc_keystream = []
		for c in cleartext:
			flag = False
			for index in range(len(data)):
				if data[index] == c and index not in enc_keystream:
					new_key = bin(index)[2:].zfill(8)
					enc_keystream.append(new_key)
					flag = True
					break
			if not flag:
				raise ProcessingError("<-> Not enough space in this key/image to embed all characters.")
		return '.'.join(enc_keystream)

	def encrypt(self, tohide):
		data = self.getColData()
		cleartext = [ord(c) for c in tohide]
		ciphertext = self.write(data, cleartext)
		assert self.read(data, ciphertext) == tohide
		open(self.enc_file_name, "wb").write(ciphertext + "\n")
		return ciphertext

	def decrypt(self, keystream):
		data = self.getColData()
		cleartext = self.read(data, keystream)
		open(self.dec_file_name, "wb").write(cleartext + '\n')
		return cleartext

