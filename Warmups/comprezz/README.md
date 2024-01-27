# Comprezz(Warmups)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/comprezz/comprezz.png)

## Çözüm
Verilen doysanın türün anlamak için ilk başta "file" komutunu kullanıyoruz ve compress edilmiş(sıkıştırılmış) bir dosyaya ait olduğunu öğreniyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/comprezz/file_command.png)

Dosyanın uzantısını .z olarak değiştirip, "uncompress" komutu ile sıkıştırılmış dosyayı çıkartıyoruz. Ve flag çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/comprezz/Screenshot_1.png)

```flag{196a71490b7b55c42bf443274f9ff42b}```