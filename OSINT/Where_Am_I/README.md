# Where Am I(Osint)
#### Zorluk: Easy

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/OSINT/Where_Am_I/Where_Am_i.png)

## Çözüm

Soruda fotoğraftan konum bulmamız isteniyor. Bu yüzden ilk yapacağımız iş "exiftool" ile fotoğrafın metadata'larına bakıyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/OSINT/Where_Am_I/Screenshot_1.png)

image description kısmında base64 ile şifrelenmiş bir yazı var. Yazıyı decode etmek için cyberchef'e atıyorum ve flag çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/OSINT/Where_Am_I/Screenshot_4.png)

```flag{b11a3f0ef4bc170ba9409c077355bba2}```