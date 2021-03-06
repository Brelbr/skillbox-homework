# SkillBox - Приложение мини-чат на Python
# С изменениями на основании домашнего задания:

К работающему серверу добавить следующий функционал:

1. При попытке подключения клиента под логином, который уже есть в чате:
    - Отправлять клиенту текст с ошибкой "Логин {login} занят, попробуйте другой"
    - Отключать от сервера соединение клиента
    - Исправления будут в методе data_received у сервера

2. При успешном подключении клиента в чат:
    - Отправлять ему последние 10 сообщений из чата
    - Создать отдельный метод send_history и вызывать при успешой авторизации в data_received у сервера
    
3. Сдача домашних работ производится через Github.
    - Создать аккаунт (если еще нет)
    - Загрузить работу в репозиторий
    - Проверить, что у него открытый доступ (можете открыть в режиме инкогнито)
    - Прикрепить ссылку на репозиторий в форму SkillBox для сдачи работы (Google Формы)

В данном репозитории находятся материалы и примеры кода с онлайн интенсива по разработке на **Python** для [SkillBox](https://skillbox.ru)


## Структура репозитория

- **src** - примеры кода с вебинаров
    - **day_01** - основы языка, работа с данными, синтаксис и операции, начало ООП
    - **day_02** - работа с ООП, создание сервера чата
    - **day_03** - работа с интерфейсами Qt, создание клиента чата
- **examples** - дополнительные примеры программ
- **resources** - материалы с вебинара
- **app** - готовый проект мини-чата

## Установка

#### Для установки зависимостей проекта необходимо выполнить

```
pip install -r requirements.txt
```

#### Для просмотра списка установленных пакетов

```
pip list
```

#### Для установки Telnet

MacOS (понадобится инструмент [Homebrew](https://brew.sh/)):
```
brew install telnet
```

Ubuntu:
```
sudo apt-get install telnet
```

Windows: [инструкция](https://help.keenetic.com/hc/ru/articles/213965809-%D0%92%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D1%83%D0%B6%D0%B1-Telnet-%D0%B8-TFTP-%D0%B2-Windows)

## Полезные книги

- Программирование на Python (Марк Лутц - O'Reilly)
- Простой Python. Современный стиль программирования (Любанович Билл - O'Reilly)
- Python. Карманный справочник (Марк Лутц - O'Reilly)
- Изучение сложных систем с помощью Python (Аллен Б. Дауни - O'Reilly)
- Приемы объектно-ориентированного проектирования. Паттерны проектирования (Гамма Эрих, Джонсон Р., Хелм Ричард, Влиссидес Джон - Питер)
- Совершенный код. Мастер-класс (Стив Макконнелл - БХВ-Петербург)
