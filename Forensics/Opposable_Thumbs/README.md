# Opposable Thumbs
#### Zorluk: Easy

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Opposable_Thumbs/Opposable_Thumbs.png)

## Çözüm

Soruda verilen içeriği "thumbcache" ibaresini arattığımda, bu özel data setine görüntülemek için [thumbcacheviewer](https://thumbcacheviewer.github.io/) programını buldum. Promgramı indirip kurduktan sonra verilen dosyayı içine atıp verileri gözden geçiriyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Opposable_Thumbs/Screenshot_7.png)

Verileri sahip olduğu boyutlara göre sıralayıp baştan incelemeye başlıyorum ve bir kaç satır altta flagı buluyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Opposable_Thumbs/Screenshot_8.png)

```flag{human_after_all}```