# I Wont Let You Down(Miscellaneous)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/I_Wont_Let_You_Down/I_Wont_Let_You_Down.png)

## Çözüm
Bu soruya özel olarak nmap kullanmamıza izin verilmiş. Bende hızlı bir şekilde "nmap -A -F <ip>" taraması yapıyorum. Burda "-A" parametresi agrasif taramayı temsil ediyor ve otomatik olarak servis, script gibi taramaları yapıyor. "-F" Parametresi ile ise hızlı bir tarama yapmasını belirtiyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/I_Wont_Let_You_Down/Screenshot_2.png)

Sonuca baktığımız zaman 22, 25, 80, 8888 portlarının açık olduğunu görüyoruz. En ilgi çeken 8888 portu, hacker camiasının en sevdidği şarkısı [never gonna give you up](https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D)'ın sözlerini görüyoruz. Hemen basit bir şekilde netcat bağlantısı atıp sonucu bekliyorum.
```
nc <ip> 8888
```
Şarkının sonlarında flag ortaya çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/I_Wont_Let_You_Down/Screenshot_3.png)

```flag{93671c2c38ee872508770361ace37b02}```