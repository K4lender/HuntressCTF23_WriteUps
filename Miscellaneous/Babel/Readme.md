# Babel(Miscellaneous)
#### Zorluk: Medium

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Babel/Babel.png)

## Çözüm
Bize obfuscate edilmiş bir C# kodu verilmiş. Bu kodda iki string verilmiş ve bu iki string bir fonksiyon vasıtasıyla çıktı elde ediliyor. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Babel/Babel1.PNG)

Kodu obfuscate ettim ve [Online C# Compiler](https://www.programiz.com/csharp-programming/online-compiler/) sitesini kullanarak kodu çalıştırdım. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Babel/Babel2.PNG)

Program Base64 ile encode edilmiş bir çıktı verdi. Bu çıktıyı Cyberchef sitesine atıp decode ettiğimizde bir Exe dosyası olduğunu gördüm. Exeyi indirip ```Bintext``` programı yardımıyla stringlerine baktığımda flagı elde ettim. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Babel/Babel3.png)

```flag{b6cfb6656ea0ac92849a06ead582456c}```
