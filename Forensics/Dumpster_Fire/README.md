# Dumpster Fire(Forensic)
#### Zorluk: Easy

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Dumpster_Fire/Dumpster_Fire.png)

## Çözüm
İlk başta verilen dosyaları verilen tar'dan çıkartıyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Dumpster_Fire/Screenshot_4.png)

Dosyaları incelediğimde linux kök diziniyle aynı olduğunu farkediyorum ve araştırma yapmaya başlıyorum. İlk merak ettiğim kısım sisteme ait user'ların dosyaları olduğundan hemen home dizinine giriyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Dumpster_Fire/Screenshot_5.png)

Challange user'ına ait dosyalarına baktığım zaman ".mozilla" dosyası buluyorum. Bu dosya, cihazda çalışan Mozilla Firefox tarayıcısının önbellek dosyalarını bulunduruyor. Bu dosyalarının bana kalırsa en önemli özelliği, tarayıcıda kayıt edilmiş şifrelere erişebilmemiz.
Bunun için öncellikle [firefox_decrypt](https://github.com/unode/firefox_decrypt) toolunu indirip kuruyorum.

Sonrasında indirdiğim toola .mozilla klasörünün yolunu belirterek programı çalıştırıyorum.
```
python3 firefox_decrypt.py ~/path/to/.mozilla/file/...
```
![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Dumpster_Fire/Screenshot_6.png)

```flag{35446041dc161cf5c9c325a3d28af3e3}```