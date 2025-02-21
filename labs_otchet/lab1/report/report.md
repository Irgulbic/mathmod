---
## Front matter
title: "Лабораторная работа №1"
subtitle: "Работа с git"
author: "Матюхин Павел"

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

# Цель работы

Научиться работать с git.

# Выполнение лабораторной работы

Установка имени и электронной почты 

![](images/image1.1.png){#fig:001 width=100%}

Создание проекта

![](images/image1.2.png){#fig:002 width=100%}

Внесение изменений

![](images/image1.3.png){#fig:003 width=100%}

Индексация изменений

![](images/image1.4.1.png){#fig:004 width=100%}

![](images/image1.4.2.png){#fig:005 width=100%}

Отмена локальных изменений (до индексации)

![](images/image1.5.png){#fig:006 width=100%}

Отмена проиндексированных изменений (перед коммитом)

![](images/image1.6.1.png){#fig:007 width=100%}

![](images/image1.6.2.png){#fig:008 width=100%}

Отмена коммитов

![](images/image1.7.png){#fig:009 width=100%}

Удаление коммиттов из ветки

![](images/image1.8.png){#fig:010 width=100%}

Удаление тега oops

![](images/image1.9.png){#fig:011 width=100%}

Внесение изменений в коммиты

![](images/image1.10.png){#fig:012 width=100%}

Перемещение файлов

![](images/image1.11.png){#fig:013 width=100%}

Второй способ перемещения файлов

![](images/image1.12.png){#fig:014 width=100%}

Подробнее о структуре

![](images/image1.13.1.png){#fig:015 width=100%}

Git внутри: Каталог .git

![](images/image1.14.png){#fig:016 width=100%}

Работа непосредственно с объектами git

![](images/image1.15.png){#fig:017 width=100%}

Создание ветки

![](images/image1.16.png){#fig:018 width=100%}

Навигация по веткам

![](images/image1.17.png){#fig:019 width=100%}

Изменения в ветке master

![](images/image1.18.png){#fig:020 width=100%}

Сделайте коммит изменений README.md в ветку master.

![](images/image1.19.png){#fig:021 width=100%}

Слияние

![](images/image1.20.png){#fig:022 width=100%}

Создание конфликта

![](images/image1.21.png){#fig:023 width=100%}

Разрешение конфликтов

![](images/image1.22.png){#fig:024 width=100%}

Сброс ветки style

![](images/image1.23.png){#fig:025 width=100%}

Сброс ветки master

![](images/image1.24.png){#fig:026 width=100%}

Перебазирование

![](images/image1.25.png){#fig:027 width=100%}

Слияние в ветку master

![](images/image1.26.png){#fig:028 width=100%}

Клонирование репозиториев

![](images/image1.27.png){#fig:029 width=100%}

Просмотр клонированного репозитория

![](images/image1.28.png){#fig:030 width=100%}

Что такое origin?

![](images/image1.29.png){#fig:031 width=100%}

Удаленные ветки

![](images/image1.30.png){#fig:032 width=100%}

Изменение оригинального репозитория

![](images/image1.31.png){#fig:033 width=100%}

Слияние извлеченных изменений

![](images/image1.32.png){#fig:034 width=100%}

Добавление ветки наблюдения

![](images/image1.33.png){#fig:035 width=100%}

Добавление удаленного репозитория

![](images/image1.35.png){#fig:036 width=100%}

Отправка изменений
![](images/image1.36.png){#fig:037 width=100%}

Извлечение общих изменений

![](images/image1.37.png){#fig:038 width=100%}

Добавление ветки наблюденияr

![](images/image1.38.png){#fig:039 width=100%}


# Вывод

Научился работать с git с каталогами ветками.


