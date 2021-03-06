﻿# Приливные силы и задача двух тел
Tide effects modelling & 2 bodies problem demonstration 

Программа позволяет изучать задачу двух тел и приливные силы в системе двух тел

Использованные библиотеки языка *Python*
1. Стандартная библиотека
2. Встроенная библиотека tkinter
3. Библиотека numpy

Прогамма работает на Windows, MacOS, Linux

## Содержание

1. [Как запускать нашу программу]
2. [Как добавить объекты на поле]
3. [Отслеживание скорости объектов]
4. [Скорость течения времени и пауза]
5. [Регулировка положения и параметров объектов]
6. [Наблюдение приливных эффектов]
7. [Как сохранить текущие параметры объектов и их орбит в файл]
8. [Как изменить масштаб изображения]
9. [Как поменять область обзора]

## 1.Как запускать нашу программу

Для начала нужно установить *Python* с сайта [Python web]. Для этого, пожалуйста, выполните следующие шаги:

1. Зайдите на официальный сайт *Python*: [Python web]
2. Нажмите на *Downloads*: 
![image 1](https://thumb.tildacdn.com/tild6630-6634-4835-b864-653434316537/-/format/webp/1.png)
3. Выберите операционную систему, на которой работаете, нажмите на ссылку с последней версией *Python*, 
   выберите версию для Вашего процессора. Начнётся загрузка *Python* на Ваш компьютер
6. Запустите установщик *Python*:
![image 5](https://thumb.tildacdn.com/tild3539-3539-4235-b339-366566373230/-/format/webp/5.png)
7. Если вы желаете настроить установку, нажмите на *Customize installation*. 
Если Вы желате настроить установку, то убедитесь, что Вы устанавливаете tkinter:
![image 7](https://thumb.tildacdn.com/tild3137-3437-4862-a266-303164303237/-/format/webp/7.png)
После настройки установки нажмите на "Install".
Если вы не желаете настроить установку, нажмите на "Install now"
8. Дождитесь конца установки *Python* на Ваш компьютер
9. В Windows PowerShell установите библиотеку numpy:
![image 9](https://thumb.tildacdn.com/tild3135-3962-4634-b736-366631303761/-/format/webp/9.png)
10. Скачайте программу на свой компьютер:
![image 10](https://thumb.tildacdn.com/tild6333-6236-4231-a266-623530393235/-/format/webp/10.png)
11. Разархивируйте программу и в папке ***tide_rep*** нажмите на файл ***main***
После этого программа запуститься                                                                                                                                        
[Назад к содержанию]

## 2.Как добавить объекты на поле

В данной программе изначальные параметры объектов подгружаются из файла. Поэтому для того, чтобы добавить элементы на поле, 
1. Нажмите на ***Open file...***
![image 11](https://thumb.tildacdn.com/tild3135-6138-4739-a363-663136663139/-/format/webp/11.png)
2. Выберите нужный файл (изначально в папке уже есть файл ***planets data***):
![image 12](https://thumb.tildacdn.com/tild3334-3633-4332-b339-313866366435/-/format/webp/12.png)
Он содержит всё необходимое для достижения целей проекта.
3. После этого вы увидете соответсвующие объекты на поле
![image 13](https://thumb.tildacdn.com/tild3964-3439-4162-b564-613839636436/-/format/webp/13.png)
[Назад к содержанию]

## 3.Отслеживание скорости объектов

В процессе работы программы скорости обоих объектов будут отображаться на соответсвующих ползунках справа
![image 14](https://thumb.tildacdn.com/tild3862-3363-4163-a236-636636643662/-/format/webp/14.png)
[Назад к содержанию]

## 4.Скорость течения времени и пауза

1. Увеличить скорость течения времени можна с помощью ползунка ***FPS***
![image 15](https://thumb.tildacdn.com/tild3639-3664-4966-b661-363134333033/-/format/webp/15.png)

2. Временно приостановить процесс можно с помощью кнопки ***Pause***
![image 16](https://thumb.tildacdn.com/tild3763-6432-4833-b534-616437353433/-/format/webp/16.png)

3. Продолжить работу программы можно с помощью кнопки ***Start***
![image 17](https://thumb.tildacdn.com/tild6432-3765-4666-b438-323834323039/-/format/webp/17.png)
[Назад к содержанию]

## 5.Регулировка положения и параметров объектов

1. Для того, чтобы переместить объект, нужно навести на него курсор и зажать левую кнопку мыши. После этого,
до отпускания левой кнопки, объект будет перемещаться вслед за курсором. 

Перемещать объекты можно как в режиме работы,                                                                                                                                                      
![image 18](https://static.tildacdn.com/tild3966-6264-4461-b234-626565356462/181.gif)

так и в режиме паузы                                                                                                                                                                                                        
![image 19](https://static.tildacdn.com/tild6631-3337-4365-b932-393763626633/191.gif)

2. Регулировать массу объектов можно с помощью соответсвующих ползунков
![image 20](https://thumb.tildacdn.com/tild3234-3430-4930-b630-333037396266/-/format/webp/20.png)

3. Также можно искусственно регулировать скорости объектов с помощью соответсвующих ползунков
![image 14](https://thumb.tildacdn.com/tild3862-3363-4163-a236-636636643662/-/format/webp/14.png)
[Назад к содержанию]

## 6.Наблюдение приливных эффектов

Для того, чтобы наблюдать приливные эффекты, нужно включить соответсвующую функцию посредством галочки возле ***Ocean On/Off***
![image 21](https://thumb.tildacdn.com/tild3030-3935-4634-b265-666537626535/-/format/webp/21.png)
[Назад к содержанию]

## 7. Как сохранить текущие параметры объектов и их орбит в файл
1. Нажмите на ***Save data to file***
![image 22](https://thumb.tildacdn.com/tild3733-6431-4364-b533-366565646532/-/format/webp/22.png)

2. Выберите файл, в который хотите сохранить параметры
![image 23](https://thumb.tildacdn.com/tild3032-3265-4537-b164-646534393730/-/format/webp/23.png)
[Назад к содержанию]

## 8. Как изменить масштаб изображения

Чтобы изменять масштаб изображения, прокручивайте среднюю кнопку мыши. Прокрутка вверх уменьшит масштаб, вниз - увеличит.                                                
[Назад к содержанию]

## 9. Как поменять область обзора
Чтобы поменять область обзора, наведите курсор на то место на полотне, где нет объектов. Зажмите левую кнопку мыши и перетащите полотно в нужную вам сторону.                  
Перемещать полотно можно как в режиме работы                                                                                                                                                                                                                         
![image 24](https://static.tildacdn.com/tild6231-3535-4861-b064-373164393634/241.gif)

так и в режиме паузы                                                                                                                                                                                         
![image 25](https://static.tildacdn.com/tild6666-6362-4165-b634-303566333433/251.gif)                                                                   
[Назад к содержанию]

[Python web]:https://www.python.org/
[Как запускать нашу программу]:https://github.com/davidkirakosyan/tide_rep#1%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D1%82%D1%8C-%D0%BD%D0%B0%D1%88%D1%83-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%83
[Как добавить объекты на поле]:https://github.com/davidkirakosyan/tide_rep#2%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D1%8B-%D0%BD%D0%B0-%D0%BF%D0%BE%D0%BB%D0%B5
[Отслеживание скорости объектов]:https://github.com/davidkirakosyan/tide_rep#3%D0%BE%D1%82%D1%81%D0%BB%D0%B5%D0%B6%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D0%B8-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
[Скорость течения времени и пауза]:https://github.com/davidkirakosyan/tide_rep#4%D1%81%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C-%D1%82%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%B8-%D0%B8-%D0%BF%D0%B0%D1%83%D0%B7%D0%B0
[Регулировка положения и параметров объектов]:https://github.com/davidkirakosyan/tide_rep#5%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
[Наблюдение приливных эффектов]:https://github.com/davidkirakosyan/tide_rep#6%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%B8%D0%B2%D0%BD%D1%8B%D1%85-%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%BE%D0%B2
[Как сохранить текущие параметры объектов и их орбит в файл]:https://github.com/davidkirakosyan/tide_rep/blob/main/README.md#7-%D0%BA%D0%B0%D0%BA-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C-%D1%82%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2-%D0%B8-%D0%B8%D1%85-%D0%BE%D1%80%D0%B1%D0%B8%D1%82-%D0%B2-%D1%84%D0%B0%D0%B9%D0%BB
[Как изменить масштаб изображения]:https://github.com/davidkirakosyan/tide_rep/blob/main/README.md#8-%D0%BA%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BC%D0%B0%D1%81%D1%88%D1%82%D0%B0%D0%B1-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F
[Как поменять область обзора]:https://github.com/davidkirakosyan/tide_rep/blob/main/README.md#9-%D0%BA%D0%B0%D0%BA-%D0%BF%D0%BE%D0%BC%D0%B5%D0%BD%D1%8F%D1%82%D1%8C-%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C-%D0%BE%D0%B1%D0%B7%D0%BE%D1%80%D0%B0
[Назад к содержанию]:https://github.com/davidkirakosyan/tide_rep#%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D0%BD%D0%B8%D0%B5
