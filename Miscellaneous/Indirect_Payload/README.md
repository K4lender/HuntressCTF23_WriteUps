# Indirect Payload(Miscellaneous)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/F12/Screenshot_1.png)

## Çözüm
![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Indirect_Payload/Screenshot_1.png)

Sitedeki butona basıldığı zaman bir sürü istek dönüyor ama çok hızlı olduğu için hiçbirini göz ile yakalayamıyorum. Bu yüzden burp ile araya girip giden gelen istekleri inceliyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Indirect_Payload/Screenshot_2.png)

İsteklere baktığımız zaman birbirinden farklı pathlere sırayla yönlendirme yaptığını görüyoruz. Bu pathlerin içeriğine baktığımız zaman "character 0 of the payload is f" yazsını görüyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Indirect_Payload/Screenshot_3.png)

Yani bir dizi karakterlerin yerlerini gösteriyor. Sırayla isteklere baktığımız zaman ve harfleri birleştirdiğimiz zaman flag ortaya çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Indirect_Payload/Screenshot_4.png)

```flag{448c05ab3e3a7d68e3509eb85e87206f}```