# Backdoored Splunk(Forensic)
#### Zorluk: Medium

## Soru

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Backdoored_Splunk/Backdoored_Splunk.png)

## Çözüm

Soruda splunk dosyaları verilmiş ve Backdoor olayından bahsedilmiş. Bende verilen dosyalar arasında port kelimesini aratarak herhangi bir reverse shell bağlantısı var mı kontrol ediyorum.
```
grep -ir port
```
![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Backdoored_Splunk/Screenshot_2.png)

Invoke web-request fonksiyonun ile bir servere bağlantı isteği atıldığını görüyorum. Ayrıca header kısmında authorization parametresi bulunuyor. Bu parametreyi base64 ile şifrelendiğini anlayıp, veriyi [Cyberchef](https://gchq.github.io/CyberChef/)'de decode ediyorum

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Backdoored_Splunk/Screenshot_4.png)

Elimizde header'da kullanabileceğimiz bir adet kullanıcı adı ve şifremiz oldu. Şimdi bu bilgileri kullanarak dosyalarda bulunan ip adresine bir giriş isteği atalım. Yani hackerin bağlantı yolunu birebir taklit edelim.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Backdoored_Splunk/Screenshot_5.png)

Attığımız istekten dönen cevabı tekrardan decode edip flagı buluyoruz.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Backdoored_Splunk/Screenshot_6.png)

```flag{60bb3bfaf703e0fa36730ab70e115bd7}```