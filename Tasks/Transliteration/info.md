В маленьком городке жили два друга, Ваня и Вова. Ваня увлекался языками и часто мечтал путешествовать по миру, а Вова был страстным читателем и предпочитал книги на родном языке. Однажды Ваня решил показать Вове интересные тексты на кириллице, которые он нашел в интернете, но их сложно было читать для тех, кто не знает русского языка.

Ваня задумался: "Как же сделать эти истории доступными для всех?" Он вспомнил о транслитерации — процессе замены кириллических букв на латинские. "Это точно поможет!" — воскликнул он, убежденный, что так его любимые тексты смогут прочитать и их иностранные друзья. Вова, заинтересованный новой идеей, предложил Ване написать программу, которая сможет провести эту транслитерацию автоматически.

Вам доступен текстовый файл cyrillic.txt, содержащий текст. Напишите программу для транслитерации этого файла, то есть замены кириллических символов на латинские в соответствии с предложенной таблицей. Все остальные символы надо оставить без изменений. Результат транслитерации требуется записать в файл transliteration.txt.

Формат ввода
На вход программе ничего не подается. У вас доступен файл cyrillic.txt.

Формат вывода
Программа должна создать файл с именем transliteration.txt в соответствии с условием задачи.

Пример 1
Ввод	Вывод
В верхнем течении Соть течёт среди высоких лесных берегов, ширина реки 8—10 метров.
В среднем течении, ниже административного центра Первомайского района посёлка Пречистое, расположенного в километре
от реки, река расширяется до 15—20 метров.
In the upper and middle reaches, the river sometimes forms small rifts and rapids, the current is quite fast.
V verhnem techenii Sot' techjot sredi vysokih lesnyh beregov, shirina reki 8—10 metrov.
V srednem techenii, nizhe administrativnogo centra Pervomajskogo rajona posjolka Prechistoe, raspolozhennogo v kilometre
ot reki, reka rasshiryaetsya do 15—20 metrov.
In the upper and middle reaches, the river sometimes forms small rifts and rapids, the current is quite fast.

Пример 2
Ввод	Вывод
Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.
Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.

Примечания
Обратите внимание, что заглавные буквы должны заменяться на соответствующие им заглавные же буквы, но если транслитерационная последовательность состоит из нескольких символов, то заглавным будет только первый из них: «С» на «S», а «Я» на «Ya». Помимо буквы «Я», есть следующие переводы:

ё - jo

ж - zh

ч - ch

ш - sh

щ - shh

ъ - *

ь - '

э - je

ю - ju