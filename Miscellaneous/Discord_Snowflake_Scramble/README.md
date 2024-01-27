# Discord Snowflake Scramble(Miscellaneous)
#### Zorluk: Easy

## Soru 
![Soru](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Discord_Snowflake_Scramble/Discord_Snowflake_Scramble.png)

## Çözüm

Soruda verilen url'i inceledeğimiz zaman "discord.com/channels/115..." diye giden kısım guild numarasını temsil ediyor. Yani discord serverinin id numarasınıdır. Bu numarayı [Guild Lookup](https://discordlookup.com/guild) sitesine yerleştrip invite url'si oluşturuyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Discord_Snowflake_Scramble/Screenshot_2.png)

Url'li kullanarak sunucuya üye oluyorum.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Discord_Snowflake_Scramble/Screenshot_3.png)

Ve flag karşımıza çıkıyor.

![](https://github.com/K4lender/HuntressCTF23_WriteUps/blob/main/Miscellaneous/Discord_Snowflake_Scramble/Screenshot_4.png)

``` flag{bb1dcf163212c54317daa7d1d5d0ce35}```