# Symmetric Key Encryption Using Image As Key 
[![python](https://img.shields.io/badge/Python-2.7-blue.svg?style=style=flat-square)](https://www.python.org/downloads/)  [![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=style=flat-square)](https://github.com/0xcesium/Symmetric-Key-Encryption-Using-Image-As-Key/blob/master/LICENSE)

Description : Implementation of a Symmetric Key Encryption using an Image as a vector of encryption.

Author twitter: @133_cesium

### Tested with JPG, PNG, BMP magic formats.

Implementation of the algorithm proposed by Mazhar Islam, Mohsin Shah and Zakir Khan for educational purpose.

## Main advantage:

This encryption technique cannot be defeated without the key, therefore the picture used. Please see the abstract below.

## Abstract (from the white paper published under the IEEE seal late 2015):

```
Symmetric key cryptography is a common cryptographic technique using the same key at both the transmitter and receiver side.
The main advantage of symmetric key encryption is its less computational cost compared to its counterpart-public key encryption.
In this work a new symmetric key encryption scheme is proposed.
Rather than using normal binary secret keys, our technique uses images as secret keys.
Message letters are converted into their corresponding 8-bit binary codes.
These 8-bit codes are scanned for image pixel values which are represented by the same 8-bit codes.
When a match is found between the message 8-bit code and pixel values codes that location of the pixel is saved in a separate file.
Instead of saving pixel locations as (x, y) coordinates, their locations are saved as one value column wise.
After having all matches, pixels locations are transmitted as cipher text.
The receiver side will scan the same image for those locations and will pick values at those locations which represent message codes.
The main advantage of this scheme is its high security as its key size is very large.
```

## The Class

#### 0) Using an image as entry object to work on.

#### 1) Converting the picture colors into gray pixels (without altering the original sample).

#### 2) Extracting the column wise pixel stream.


#### 3. Encryption)

3.1) Finding every pixel value that matches each byte values of the secret message to cipher.

3.2) Ensuring each value extracted is not present twice in the stream to avoid frequency analysis technics.

3.3) Converting integer value into binary format, separated with a point (idk, why not?).


#### 3. Decryption)

3.1) Converting each binary values from a cipher stream found in a file into integers.

3.2) Matching every value as an index in the pixel stream extracted.

3.3) Converting each value found into an ascii character if possible, either a byte.

#### Finally, any encryption and decryption process succeeded is saving the resulted output in a file in the current directory.


## Exemple of use

```python
from argparse import ArgumentParser,FileType
from NSKEI import NSKEI

def get_args():
  parser = ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  parser.add_argument('-k',"--key",
    metavar="IMAGE",action="store",required=True)
  group.add_argument("-r","--read",
    metavar="SECRET_STREAM",type=FileType("rb"),action="store")
  group.add_argument("-w","--write",
    metavar="TEXT_TO_HIDE",type=FileType("rb"),action="store")
  return parser.parse_args()

if __name__ == "__main__":
  args = get_args()
  nskei = NSKEI(args.key)

  if args.write:
    print "[+] Encryption result (automatically saved as {}):".format(nskei.enc_file_name)
    print nskei.encrypt(args.write.read())
  else:
    print "[+] Decryption result (automatically saved as {}):".format(nskei.dec_file_name)
    print nskei.decrypt(args.read.read())

  nskei.im.close
```

Please do not hesitate to signal anything, good or bad, about this work, thank you.
Ces[133]
