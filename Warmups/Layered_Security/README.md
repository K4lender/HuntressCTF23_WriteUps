# Layered Security(Warmups)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Layered_Security/layeredsecurity.png)

## Çözüm
Dosyayı ilk indirdiğimizde herhangi bir uzantıya sahip olmadığı için dosyanın ne olduğunu anlamakta zorluk çekebiliriz. Bu sorunu çözmek için "file" komutu ile dosyanın ne olduğunu öğrenmeye çalışabiliriz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Layered_Security/Screenshot_1.png)
Dosyanın gimp tarafından oluşturulmuş bir fotoğraf olduğunu söylüyor. Gimp'i açıklamak gerekirse, gimp linux ortamında çalışan fotoğraf düzenleme uygulamasıdır. şimdi ise verilen dosyayı gimp ile açıp ne olduğuna bakıyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Layered_Security/Screenshot_2.png)

Yukarıdaki fotoğrafa dikkatli baktığımızda fotoğraf birbiri üstüne yerleştirilmiş bir sürü katmana sahip olduğunu görüyoruz(sağ alt kısma bakınız). Katmanları teker teker kaldırdığımda ise flagı buluyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Layered_Security/Screenshot_3.png)

``` flag{9a64bc4a390cb0ce31452820ee562c3f}```