#file to have functions to encrypt and decrypt image using pycrypto (an encryption library) 
from Crypto.Cipher import AES
from Crypto import Random 

key=Random.new().read(AES.block_size)
iv=Random.new().read(AES.block_size)

fileName="Wolf_pic-1.jpg"; #name of the file to encrypt 
f=open(fileName).read()

def encrypt(f): 
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    enc_data = cfb_cipher.encrypt(f)

    enc_file = open("encrypted.enc", "w")
    enc_file.write(enc_data)
    enc_file.close()

def decrypt(f): 
    enc_file2=open("encrypted.enc")
    data=enc_file2.read()
    enc_file2.close()

    cfb_decipher=AES.new(key, AES.MODE_CFB, iv)
    plain_data=cfb_decipher.decrypt(data)

    outputFile=open("output.jpg", "w")
    outputFile.write(plain_data)
    outputFile.close()
