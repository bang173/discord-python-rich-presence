Перед началом использования Rich Presence внесите данные в RischPresenceData.json
---

### Получить испольняему версию (exe)
Исполняемый файл можно получить тут: https://disk.yandex.by/d/EzJ1ZBnUgfDb9g

# Данные
<{
    "appID": ""
    "desc1": "",
    "desc2": "",
    "useTimestamp": false,

    "useImages": false,
    "imageData": {
        "largeImage": {
            "key": "",
            "text": ""
        },
        "smallImage": {
            "key": "",
            "text": ""
        }
    },
    "useParty": false,
    "partyInfo": {
        "partyID": "",
        "partySize": 1,
        "partyMax": 3
    }
}>
# Приложение Discord
---
`Я не буду вам показывать как создать приложение в Discord.`
<{"appID": ""}>
В данное поле вам надо вставить Client ID вашего приложения, и оставить его в формате текста не переводя в числовой.
#### Rich Presence -> Art Assets
---
Здесь будут хранится все картинки, которые вы хотите в своем статусе. Минимальный размер картинки 512x512, а максимальный 1024x1024,
так-же соотношение сторон должно оставаться *1:1*.

### Описания
---
Первыми вас встречают **desc1** и **desc2**, это обычный текст который будет показываться в статусе.
Можете туда вписывать что угодно, только помните, что два поля для ввода даны не просто так, а именно потому, что место в статусе не бесконечное.

### Время активности
---
**useTimestamp** предназначен для того, что бы показыать таймер активности вашего статуса.
> Параметры
+ *true* = да
+ *false* = нет

## Использование картинок в статусе
---
**useImages** - переключатель. Он дает понять приложению: использовать картинки или нет.
> Параметры
+ *true* = да
+ *false* = нет

<"imageData": {
        "largeImage": {
            "key": "",
            "text": ""
        },
        "smallImage": {
            "key": "",
            "text": ""
        }
    }>

**imageData** содержит в себе объекты **largeImage** и **smallImage**.
> В каждом есть **key** и **text**:
+ *key* = название картинки в ассетах приложения
+ *text* = текст, который будет показан при наведении курсора на картинку *(так-же видно другим)*

### Пати
---
Данная опция показывает в вашем статусе размер комнаты и количество игроков в ней, но вы явно будете использовать это не по назначению :).
**useParty** - переключатель. Он дает понять приложению: показывать информацию о пати или нет.
> Параметры
+ *true* = да
+ *false* = нет

<"partyInfo": {
        "partyID": "",
        "partySize": 1,
        "partyMax": 3
    }>
Данный блок содержит в себе информацию о пати. **partyID** должен содержать в себе что угодно, но не пустую строку *(что угодно значит любой текст)*.
**partySize** показывает информацию о количестве игроков в пати, а **partyMax** показывает вместимость пати.


# Нужная информация заполнена, что дальше?
Далее вы сохраняете файл *RichPresenceData.json* и запускаете *RichPresence by bangakek.exe* (если у вас исполняемый файл). Очевидно, что статус стоит запускать пока Discord активен, иначе будет ошибка.
Если вы скачали код прямо из гитхаб, то у вас должен быть установлен Python >= 3.5 и библиотека discord-rpc, тогда вы запускаете файл *source.py*

`Приятного пользования!`
