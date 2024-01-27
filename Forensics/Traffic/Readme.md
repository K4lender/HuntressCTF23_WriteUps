# Traffic(Forensic)
#### Zorluk: Medium

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Traffic/Traffic.png)

## Çözüm
Bize bir ağ trafiği çıktısı verilmiş. Soruda da bize rita kullanmamızı önermiş. Ben de rita'yı kurup çalıştırıyorum.

```
rita import 2021-09-08/* huntress_ctf_traffic
```

Oluşturduğumuz raporu incelemek için aşağıdaki kodu yazıyorum.

```
rita html-report huntress_ctf_traffic
```

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Traffic/Screenshot_3.png)

İşaretlenen ```sketchysite.github.io``` adresine gidiyorum. Site açıldığında flag karşımıza çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Traffic/Screenshot_4.png)

```flag{8626fe7dcd8d412a80d0b3f0e36afd4a}```
