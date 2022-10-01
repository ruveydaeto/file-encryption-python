import os 
from cryptography.fernet import Fernet 
import platform

key = Fernet.generate_key() 
print(key)

key = str(key)[2:-1]

f = open("key.txt","w") 
f.write(key)
f.close()

ferNet = Fernet(key)

def sifrele(dosya):
    with open(dosya,"rb") as readFile:
        okunanDosya = readFile.read()

    with open(dosya,"wb") as writeFile:
        try:
            sifreliHal = ferNet.encrypt(okunanDosya)
            writeFile.write(sifreliHal)
            writeFile.close()
            readFile.close()
        except:
            print("Bir hata oluştu")

if platform.system() == "Windows":
   for path,gereksiz,files in os.walk(os.getcwd()+"\\sifrele"): 
        
       for dosyalar in files:
           dosyaYolu = path + "\\" + dosyalar
           sifrele(dosyaYolu)

elif platform.system() == "Linux":
    for path,gereksiz,files in os.walk(os.getcwd()+"/sifrele"): 
        #print(path,gereksiz,files)
        for dosyalar in files:
            dosyaYolu = path + "/" + dosyalar
            sifrele(dosyaYolu)
else:
    print("Kullandığınız işletim sistemi bu program tarafından desteklenmiyor.")
