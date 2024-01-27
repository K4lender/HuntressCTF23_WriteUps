# Query Code(Warmups)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Query_code/Query_Code.png)

## Çözüm
Soruda verilen dosyanın türünü öğrenmek için "file" komutu kullanıyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Query_code/Screenshot_1.png)

Dosyanın png türüne ait bir fotoğraf olduğunu belirtiyor. fotoğrafın uzantısını .png olarak değiştirip fotoğrafı görüntülüyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Query_code/Screenshot_2.png)

Karşımıza bir QR kod geldi. QR kodu parse etmek için [Cyberchef](https://gchq.github.io/CyberChef/#recipe=Parse_QR_Code(false))'e atıyorum ve bayrak karşımıza çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/Query_code/Screenshot_3.png)

```flag{3434cf5dc6a865657ea1ec1cb675ce3b}```