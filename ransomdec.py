import os 
from cryptography.fernet import Fernet 
import platform

f = open("key.txt","r")
key = f.read()
print(key)

ferNet = Fernet(key)

def coz(dosya):
    with open(dosya,"rb") as readFile:
        okunanDosya = readFile.read()
    
    with open(dosya,"wb") as writeFile:
        try:
            cozulmusHal = ferNet.decrypt(okunanDosya)
            writeFile.write(cozulmusHal)
            writeFile.close()
            readFile.close()
        except:
            print("Bir hata olustu")

if platform.system() == "Windows":
   for path,gereksiz,files in os.walk(os.getcwd()+"\\sifrele"):
        for dosyalar in files:
            dosyaYolu = path + "\\" + dosyalar
            coz(dosyaYolu)
elif platform.system() == "Linux":
    for path,gereksiz,files in os.walk(os.getcwd()+"/sifrele"): 
    
        for dosyalar in files:
            dosyaYolu = path + "/" + dosyalar
            coz(dosyaYolu)
else:
    print("Kullandığınız işletim sistemi bu program tarafından desteklenmiyor.")
