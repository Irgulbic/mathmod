---
## Front matter
title: "Лабораторная работа №2"
subtitle: "Задача о погоне"
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

Научиться решать типовые задачи о погоне

# Выполнение лабораторной работы

Запись уравнения движения катера 

![](image/image1.png){#fig:001 width=100%}

Запись уравнения движения катера 

![](image/image2.png){#fig:002 width=100%}

Начальные условия

![](image/image3.png){#fig:003 width=100%}

Решение дифференциального уравнения

![](image/image4.png){#fig:004 width=100%}

Траектории катера и лодки 

![](image/image5.png){#fig:005 width=100%}

Построение траекторий в питоне

![](image/image6.png){#fig:006 width=100%}

Ответы

![](image/image7.png){#fig:007 width=100%}

# Вывод
Научился решать типовые задачи о погоне




