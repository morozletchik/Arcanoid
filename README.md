# **Arcanoid**
***
**Arcanoid** - это легендарная компьютерная игра из 80-х. В ней Игрок контролирует небольшую платформу-ракетку, которую можно передвигать горизонтально от одной стенки до другой, подставляя её под шарик, предотвращая его падение вниз. Удар шарика по кирпичу приводит к разрушению кирпича.

**Arcanoid** - совершенно бесплатна, что позволяет каждому фанату ретро-гейминга окунаться с головой в игру детства.

# **Системные требования**
***
В целом, для данной игры от компьютера не требуется больших мощностей. Однако стоит отметить, 
что, так как игра была написана на версии *Python 3.9+*, то она доступна для *Windows 8+*, 
а так же для некоторых дистрибутивов *Linux* и *MacOs* (подробнее читайте ниже в этом разделе).

Для запуска вам потребуется версия *Python 3.9+* (скачать можно [здесь](https://www.python.org/downloads/)), 
а также его модули *pygame, audioplayer, numpy*.Установить их можно следующим образом:

* Откройте терминал в папке игры

* Напишите команду 

```
pip3 install -r requirements.txt
```
* Подождите, пока модули установятся

Также для корректной работы на *MacOs* и некоторых дистрибутивах *Linux* таких как *Ubuntu, Debian, Redhat, CentOS, Fedora*, 
вам стоит следовать инструкциям установки вот [тут](https://www.pypi.org/project/audioplayer).

## Установка

Чтобы установить **Arcanoid**, вы можете как скачать папку с файлами непосредственно с сайта *GitHub*, так и, при наличии git на вашем компьютере 
(скачать *Git* можно [тут](https://git-scm.com/downloads) или [тут](https://gitforwindows.org/)), воспользоваться следующей командой: 
```
git clone https://github.com/morozletchik/Arcanoid.git
```
## Запуск игры
Для запуска игры вы должны запустить файл *main.py*. Для этого можете запустить терминал в папке игры и воспользоватся командой 
```
python3 main.py
```
При запуске игры вы увидите две кнопки: "Старт", "Выход".
При нажатии кнопки "Выход" игра вы немедленно выходите из игры.
При нажатии кнопки старт, начинается игровой процесс.
При нажатии пробела шарик начинает двигаться в сторону блоков.
При нажатии Escape игра ставится на паузу. В меню паузы у вас есть выбор между выходом и продолжением игры.
***

# **Удачной игры!!!**
