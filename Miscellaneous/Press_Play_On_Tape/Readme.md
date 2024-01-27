# Press Play On Tape(Miscellaneous)
#### Zorluk: Easy

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Press_Play_On_Tape/Press_Play_On_Tape.png)

## Çözüm
Bize bir waw dosyası verilmiş ve soruda da Commador64 dönemine bir ithafta bulunulmuş. İnternette biraz araştırma yaptığımda waw dosyasından c64 dosyasına çeviren bir [Tool](https://github.com/lunderhage/c64tapedecode) buldum. Bu toolu kullanarak elimdeki waw dosyasını Commmador64 de çalışabilecek tape dosyasına çevirdim.

```wav2tap tape.wav | c64tapedecode -T -v```

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Press_Play_On_Tape/pressplayon.PNG)

Ardından çevrilen dosyayı tekrardan tap dosyasına çevirdim çünkü çevrilen dosyayı çalıştıramadım. Dosyayı çevirdikten sonra ```cat``` ile baktığımda flagı elde ettim.

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Press_Play_On_Tape/pressplaytape.png)

```flag{32564872d760263d52929ce58cc40071}```
