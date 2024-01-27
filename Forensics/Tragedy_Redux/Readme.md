# Tragedy Redux(Forensic)
#### Zorluk: Medium

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Tragedy_Redux/Tragedy_Redux.png)

## Çözüm
Bize Zararlı macrolar içeren bir word dosyası verilmiş. [Oledump.py](https://blog.didierstevens.com/programs/oledump-py/) toolu ile VBA macrolarını çıkarttım.

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Tragedy_Redux/Tragedy1.PNG)

Çıkan VBA macrolarını incelediğimde ```Apple``` adında bir string olduğunu ve bu stringin belirli işlemlerden geçtiğini gördüm. Fonksiyonları pythona çevirdim ve çalıştırdım. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Forensics/Tragedy_Redux/Tragedy2.PNG)

Elde edilen çıktı: ``` powershell -enc JGZsYWc9ImZsYWd7NjNkY2M4MmMzMDE5Nzc2OGY0ZDQ1OGRhMTJmNjE4YmN9Ig== ```

Decode ettiğimde flagı buldum.

```flag{63dcc82c30197768f4d458da12f618bc}```
