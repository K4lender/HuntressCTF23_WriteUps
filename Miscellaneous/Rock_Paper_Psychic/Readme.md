# Rock Paper Psychic(Miscellaneous)
#### Zorluk: Medium

## Soru
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Rock_Paper_Psychic/Rock_Paper_Psychic.png)

## Çözüm
Bize bir exe dosyası verildi ve bu programı her çalıştırdığımızda hangi değeri girersek girelim bilgisayarın kazandığını görüyoruz. Uygulamayı IDA ile incelemeye başladım. Fonksiyonların arasında ```PrintFlag, Computer_Win, Player_Win``` fonksiyonları bulunmaktaydı. Main dosyasına baktığımda uygulamanın bizden değer aldığını ve bu değerin rock, paper, scissors olup olmadığını kontrol ettiğini ve ona göre de seçimini yaptığını gördüm. Bu şekilde program her türlü ```Computer_Win``` fonksiyonuna gidiyordu. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Rock_Paper_Psychic/R_P_P1.PNG)

Program seçimi yaptığında aşağıdaki resimdeki gibi bir karşılaştırma noktasına geliyor ve ```jump not zero``` ile karşılaştırma yapıyor. Karşılaştırma sonrasında değer 0 çıkıyorsa ```Zero Flag(ZR)``` bitimiz 1 oluyor ve Computer_Win fonksiyonunun çağrıldığı noktaya atlıyor. Eğer ZR bit değeri 0 olursa Player_Win fonksiyonunun çağrıldığı noktaya atlıyor.

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Rock_Paper_Psychic/R_P_P2.PNG)

Biz bu karşılaştırma noktasına geldiğimizde Player_Win fonksiyonuna gidebilmek için ZR bit değerini manipule edip 1 den 0 a getiriyoruz. Bu sayede program istediğimiz noktaya gitmiş oluyor. Bu şekilde yaptığımda Player_Win fonksiyonuna gidebildim ve programın serzenişleri arasında flagı aldım. 

![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Rock_Paper_Psychic/R_P_P4.png)

```flag{35bed450ed9ac9fcb3f5f8d547873be9}```
