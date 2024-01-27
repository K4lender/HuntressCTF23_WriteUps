# Dialtone(Warmups)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/F12/Screenshot_1.png)

## Çözüm
Soruda verilen sesi dinlediğimiz zaman eski tip telefonların tuş basma sesine benzediğini farkediyorum. Bu yüzden verilen sesi [DTMF Decoder](https://dtmf.netlify.app/) sitesine atıp sesin içindeki mesajı çıkarmaya çalışıyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Dialtone/Screenshot_1.png)

Site en aşağıda bize decimal bir değer verildi bu değeri anlaşılabilir hale getirmek için ilk başta [Hexadecimal](https://www.rapidtables.com/convert/number/decimal-to-hex.html)'e dönüştürüyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Dialtone/Screenshot_2.png)

Çıkan hexadecimal değeri de [Cyberchef](https://gchq.github.io/CyberChef/)'de decode ediyorum. 

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Dialtone/Screenshot_3.png)

İşte flag.

```flag{6c733ef09bc4f2a4313ff63087e25d67}```

## DTMF (Dial tone multi frequency) nedir ?
DTMF'i Bir örnekle anlatmak gerekirse; operatörünüzün müşteri hizmetlerini aradığınızda telesekreter tarafından size söylenen “Devam etmek için 1 tuşuna basın” cümlesinin ardından basmış olduğunuz 1 tuşunu algılayan DTMF sensörlerdir. Teknik olarak telefonunuzda bulunan her numeric sayı için benzersiz bir ses tonuna sahiptir. Siz bir görüşme esnasında bu tuşlara bastığınız zaman, karşı tarafa bastığınız tuşun ses tonu gitmektedir ve dtmf sensörleri bunu algılayıp hangi tuşa bastığınız anlayabilir. Bu sayede ise kolay ve basit bir şekilde uzaktan kumanda edebiliriz.

Daha fazlası için [DTMF Nedir](https://www.muhendisbeyinler.net/dtmf-nedir/)
