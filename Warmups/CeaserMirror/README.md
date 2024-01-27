# CaesarMirror(Warmups)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/CeaserMirror.png)

## Çözüm

Soru'da ipucu olarak rot13 verilmiş. Metni [Cyberchef](https://gchq.github.io/CyberChef/) e koyup rot13 e göre harflerin sırasını kaydırıyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/Screenshot_5.png)

Metnin sol kısmı mantıklı hale gelsede sağ kısmı hala anlamsız gözüküyor. Sağ kısmı kopyalayıp [cipher identifier](https://www.dcode.fr/cipher-identifier)'e atıyorum

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/Screenshot_7.png)

metnin ters çevirildiğini öne sürüyor. bizde metni ters çevirelim

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/Screenshot_8.png)

son hali

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/Screenshot_12.png)

metnin içinden flagın 3 parçasını ayıklıyoruz ve sonuç

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Warmups/CeaserMirror/Screenshot_13.png)

```flag{julius_in_a_reflection}```