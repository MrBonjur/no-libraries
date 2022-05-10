########################################################################
#                  Create key press without libraries                  #
#                      10.05.2022 create MrBonjur                      #
#                                                                      #
#                      To press a key, you can use                     #
#                       send_key(Buttons.VK_SPACE)                     #
#                                                                      #
#                        You can use to write text                     #
#                          write("Hello world")                        #
########################################################################
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)


class Buttons:
    VK_LBUTTON = 0x01  # Левая кнопка мыши
    VK_RBUTTON = 0x02  # Правая кнопка мыши
    VK_CANCEL = 0x03  # Обработка прерываний управления
    VK_MBUTTON = 0x04  # Средняя кнопка мыши (мышь с тремя кнопками)
    VK_XBUTTON1 = 0x05  # Кнопка мыши x1
    VK_XBUTTON2 = 0x06  # Кнопка мыши в x2
    VK_BACK = 0x08  # Клавиша Backspace
    VK_TAB = 0x09  # TAB - клавиша
    VK_CLEAR = 0x0C  # ОЧИСТИТЬ ключ
    VK_RETURN = 0x0D  # Ввод ключа
    VK_SHIFT = 0x10  # Клавиша SHIFT
    VK_CONTROL = 0x11  # Клавиша CTRL
    VK_MENU = 0x12  # ALT - клавиша
    VK_PAUSE = 0x13  # Приостановить ключ
    VK_CAPITAL = 0x14  # Клавиша CAPS LOCK
    VK_KANA = 0x15  # Режим "Кана" редактора метода ввода
    VK_HANGUEL = 0x15  # Режим Хангуел IME (поддерживается для совместимости; используйте VK_HANGUL )
    VK_HANGUL = 0x15  # Режим "Хангыль" редактора метода ввода
    VK_IME_ON = 0x16  # IME в
    VK_JUNJA = 0x17  # Режим "Джунджа" редактора метода ввода
    VK_FINAL = 0x18  # Последний режим редактора метода ввода
    VK_HANJA = 0x19  # Режим "Ханджа" редактора метода ввода
    VK_KANJI = 0x19  # Режим "Кандзи" редактора метода ввода
    VK_IME_OFF = 0x1A  # IME отключен
    VK_ESCAPE = 0x1B  # Клавиша ESC
    VK_CONVERT = 0x1C  # Преобразование в редакторе метода ввода
    VK_NONCONVERT = 0x1D  # Нет преобразования в редакторе метода ввода
    VK_ACCEPT = 0x1E  # Принять IME
    VK_MODECHANGE = 0x1F  # Запрос на изменение режима редактора метода ввода
    VK_SPACE = 0x20  # ПРОБЕЛ
    VK_PRIOR = 0x21  # Ключ страницы вверх
    VK_NEXT = 0x22  # Клавиша PAGE DOWN
    VK_END = 0x23  # КОНЕЧНЫЙ ключ
    VK_HOME = 0x24  # ДОМАШНИЙ ключ
    VK_LEFT = 0x25  # Клавиша со стрелкой влево
    VK_UP = 0x26  # Клавиша со стрелкой вверх
    VK_RIGHT = 0x27  # Клавиша со стрелкой вправо
    VK_DOWN = 0x28  # Клавиша со стрелкой вниз
    VK_SELECT = 0x29  # Выбор ключа
    VK_PRINT = 0x2A  # Печать ключа
    VK_EXECUTE = 0x2B  # ВЫПОЛНИТЬ ключ
    VK_SNAPSHOT = 0x2C  # Печать клавиши экрана
    VK_INSERT = 0x2D  # Ключ INS
    VK_DELETE = 0x2E  # Клавиша DEL
    VK_HELP = 0x2F  # Ключ справки
    A = 0x41  # Ключ
    B = 0x42  # Ключ B
    C = 0x43  # Ключ C
    D = 0x44  # Ключ D
    E = 0x45  # Клавиша E
    F = 0x46  # Клавиша F
    G = 0x47  # Ключ G
    H = 0x48  # Клавиша H
    I = 0x49  # Клавиша I
    J = 0x4A  # Ключ J
    K = 0x4B  # Ключ K
    L = 0x4C  # Ключ L
    M = 0x4D  # Ключ M
    N = 0x4E  # Ключ N
    O = 0x4F  # Ключ O
    P = 0x50  # Ключ P
    Q = 0x51  # Клавиша Q
    R = 0x52  # Клавиша R
    S = 0x53  # Ключ S
    T = 0x54  # Ключ T
    U = 0x55  # Ключ U
    V = 0x56  # Ключ V
    W = 0x57  # Клавиша W
    X = 0x58  # Ключ X
    Y = 0x59  # Клавиша Y
    Z = 0x5A  # Клавиша Z
    VK_LWIN = 0x5B  # клавиша Left Windows (естественная клавиатура)
    VK_RWIN = 0x5C  # правый Windows клавиша (естественная клавиатура)
    VK_APPS = 0x5D  # Ключ приложений (естественная клавиатура)
    VK_SLEEP = 0x5F  # Клавиша перевода компьютера в спящий режим
    VK_NUMPAD0 = 0x60  # Клавиша цифровой клавиатуры 0
    VK_NUMPAD1 = 0x61  # Клавиша цифровой клавиатуры 1
    VK_NUMPAD2 = 0x62  # Клавиша цифровой клавиатуры 2
    VK_NUMPAD3 = 0x63  # Клавиша цифровой клавиатуры 3
    VK_NUMPAD4 = 0x64  # Ключ цифровой клавиатуры 4
    VK_NUMPAD5 = 0x65  # Клавиша цифровой клавиатуры 5
    VK_NUMPAD6 = 0x66  # Клавиша цифровой клавиатуры 6
    VK_NUMPAD7 = 0x67  # Клавиша цифровой клавиатуры 7
    VK_NUMPAD8 = 0x68  # Клавиша цифровой клавиатуры 8
    VK_NUMPAD9 = 0x69  # Цифровая клавиатура 9 Клавиша
    VK_MULTIPLY = 0x6A  # Ключ умножения
    VK_ADD = 0x6B  # Добавить ключ
    VK_SEPARATOR = 0x6C  # Ключ разделителя
    VK_SUBTRACT = 0x6D  # Вычесть ключ
    VK_DECIMAL = 0x6E  # Десятичный ключ
    VK_DIVIDE = 0x6F  # Разделить ключ
    VK_F1 = 0x70  # Клавиша F1
    VK_F2 = 0x71  # Клавиша F2
    VK_F3 = 0x72  # Клавиша F3
    VK_F4 = 0x73  # Клавиша F4
    VK_F5 = 0x74  # Клавиша F5
    VK_F6 = 0x75  # Клавиша F6
    VK_F7 = 0x76  # Клавиша F7
    VK_F8 = 0x77  # Клавиша F8
    VK_F9 = 0x78  # Клавиша F9
    VK_F10 = 0x79  # Клавиша F10
    VK_F11 = 0x7A  # Клавиша F11
    VK_F12 = 0x7B  # Клавиша F12
    VK_F13 = 0x7C  # Ключ F13
    VK_F14 = 0x7D  # Ключ F14
    VK_F15 = 0x7E  # Ключ F15
    VK_F16 = 0x7F  # Ключ F16
    VK_F17 = 0x80  # Ключ F17
    VK_F18 = 0x81  # Ключ F18
    VK_F19 = 0x82  # Ключ F19
    VK_F20 = 0x83  # Ключ F20
    VK_F21 = 0x84  # Ключ F21
    VK_F22 = 0x85  # Ключ F22
    VK_F23 = 0x86  # Ключ F23
    VK_F24 = 0x87  # Ключ F24
    VK_NUMLOCK = 0x90  # Клавиша NUM LOCK
    VK_SCROLL = 0x91  # Прокрутить ключ блокировки
    VK_LSHIFT = 0X82  # Левая клавиша SHIFT
    VK_RSHIFT = 0xA1  # Правая клавиша SHIFT
    VK_LCONTROL = 0xA2  # Левая клавиша CONTROL
    VK_RCONTROL = 0xA3  # Правая клавиша CONTROL
    VK_LMENU = 0xA4  # Левая клавиша МЕНЮ
    VK_RMENU = 0xA5  # Правая клавиша МЕНЮ
    VK_BROWSER_BACK = 0xA6  # Клавиша возврата в браузере
    VK_BROWSER_FORWARD = 0xA7  # Клавиша перенаправления браузера
    VK_BROWSER_REFRESH = 0xA8  # Клавиша обновления браузера
    VK_BROWSER_STOP = 0xA9  # Ключ отключения браузера
    VK_BROWSER_SEARCH = 0xAA  # Ключ поиска в браузере
    VK_BROWSER_FAVORITES = 0xAB  # Ключ избранного браузера
    VK_BROWSER_HOME = 0xAC  # Начальный и домашний ключи браузера
    VK_VOLUME_MUTE = 0xAD  # Ключ отключения тома
    VK_VOLUME_DOWN = 0xAE  # Ключ уменьшения громкости
    VK_VOLUME_UP = 0xAF  # Ключ уровня громкости
    VK_MEDIA_NEXT_TRACK = 0xB0  # Ключ следующей записи
    VK_MEDIA_PREV_TRACK = 0xB1  # Ключ предыдущей записи
    VK_MEDIA_STOP = 0xB2  # Выключить ключ носителя
    VK_MEDIA_PLAY_PAUSE = 0xB3  # Воспроизвести или приостановить ключ носителя
    VK_LAUNCH_MAIL = 0xB4  # Запустить почтовый ключ
    VK_LAUNCH_MEDIA_SELECT = 0xB5  # Выбор ключа носителя
    VK_LAUNCH_APP1 = 0xB6  # Запустить ключ приложения 1
    VK_LAUNCH_APP2 = 0xB7  # Запустить ключ приложения 2
    VK_OEM_1 = 0xBA  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США — ключ ";:"
    VK_OEM_PLUS = 0xBB  # Для любой страны или региона ключ "+"
    VK_OEM_COMMA = 0xBC  # Для любой страны или региона, ключ ","
    VK_OEM_MINUS = 0xBD  # Для любой страны или региона — ключ "-"
    VK_OEM_PERIOD = 0xBE  # Для любой страны или региона ключ "."
    VK_OEM_2 = 0xBF  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США — "/?" key
    VK_OEM_3 = 0xC0  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США ` Клавиша ~
    VK_OEM_4 = 0xDB  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США [ Клавиша "{"
    VK_OEM_5 = 0xDC  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США \ | Клавиша ""
    VK_OEM_6 = 0xDD  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США — ] ключ "}"
    VK_OEM_7 = 0xDE  # Используется для прочих символов; оно может зависеть от клавиатуры. Для стандартной клавиатуры США — клавиша "одинарная кавычка/двойная кавычка"
    VK_OEM_8 = 0xDF  # Используется для прочих символов; оно может зависеть от клавиатуры.
    VK_OEM_102 = 0xE2  # <>Клавиши на стандартной клавиатуре США или \| ключ на клавиатуре, не относящейся к 102-американской клавише
    VK_PROCESSKEY = 0xE5  # Клавиша процесса IME
    VK_PACKET = 0xE7  # Используется для передачи символов в Юникоде в виде нажатия клавиш. VK_PACKETКлюч — это младшее слово 32-битного значения виртуального ключа, используемого для методов ввода, отличных от клавиатуры. Дополнительные сведения см. в разделе замечание в KEYBDINPUT , SendInput , WM_KEYDOWN и WM_KEYUP
    VK_ATTN = 0xF6  # Ключ аттн
    VK_CRSEL = 0xF7  # Ключ Крсел
    VK_EXSEL = 0xF8  # Ключ Екссел
    VK_EREOF = 0xF9  # Стереть ключ EOF
    VK_PLAY = 0xFA  # Воспроизвести ключ
    VK_ZOOM = 0xFB  # Ключ масштабирования
    VK_NONAME = 0xFC  # Зарезервированное
    VK_PA1 = 0xFD  # Ключ PA1
    VK_OEM_CLEAR = 0xFE  # Очистить ключ


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def press_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hex_key_code, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def release_key(hex_key_code):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hex_key_code, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def send_key(hex_key_code, delay=0):
    press_key(hex_key_code)
    time.sleep(delay)
    release_key(hex_key_code)


def write(text):
    for t in text:
        if t == " ":
            send_key(Buttons.VK_SPACE)
        try:
            send_key(eval(f"Buttons.{t.upper()}"))
        except SyntaxError:
            pass


# send_key(Buttons.VK_SPACE)

write("Hello world")
