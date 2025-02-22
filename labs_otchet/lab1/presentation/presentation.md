---
## Front matter
lang: ru-RU
title: Лабораторная работа №1
subtitle: Работа с git
author:
  - Матюхин Павел Андреевич
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 22 февраля 2025

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Информация

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Матюхин Павел Андреевич
  * Студент
  * Российский университет дружбы народов
  * [1132226527@pfur.ru](mailto:1132226527@pfur.ru)

:::
::::::::::::::

## Цели и задачи

- Научиться взаимодействовать с git.

# Основная часть

## Подготовка и настройка git

![Настройка юзера и параметры установки окончаний строк](images/image1.1.png){#fig:001 width=50%}

## Создание проекта 

![Работа с репозиторием](images/image1.2.png){#fig:002 width=50%}

## Внесение изменений и индексация

![git commit](images/image1.4.1.png){#fig:003 width=50%}

## Работа с историей и тегами

![git log](images/image1.4.1.png){#fig:004 width=50%}
![Теги](images/image1.4.2.png){#fig:004 width=50%}

## Отмена изменений

![Испорченный файл](images/image1.6.1.png){#fig:005 width=50%}
![git reset](images/image1.6.2.png){#fig:006 width=50%}
![Проверка коммитов](images/image1.7.png){#fig:006 width=50%}

## Работа с ветками

![Создание ветки и работа с ней](images/image1.16.png){#fig:007 width=50%}
![Преключение веток](images/image1.17.png){#fig:008 width=50%}

## Слияние и разрешение конфликтов

![Слияние веток](images/image1.20.png){#fig:009 width=50%}
![История слияний и коммиты](images/image1.21.png){#fig:010 width=50%}
![Конфликт внутри текстового длкумента](images/image1.22.png){#fig:011 width=50%}

## Работа с удаленными репозиториями
![клонирование репозитория](images/image1.27.png){#fig:012 width=50%}
![Добавление репозитория](images/image1.36.png){#fig:013 width=50%}
![Git pull](images/image1.38.png){#fig:014 width=50%}
    
## Вывод
Научился взаимодейстовать с git.
