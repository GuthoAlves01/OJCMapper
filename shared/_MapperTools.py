import string
from ctypes import windll, wintypes, pointer


def get_free_drive():
    letters = set(string.uppercase)
    used = set(get_drives())
    return list(letters - used)[-1]


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


def get_taskbar_hw():
    rect = wintypes.RECT()

    windll.user32.SystemParametersInfoW(48, 0, pointer(rect), 0)

    screen_width = windll.user32.GetSystemMetrics(0)
    screen_height = windll.user32.GetSystemMetrics(1)

    taskbar_height = screen_height - (rect.bottom - rect.top)
    taskbar_width = screen_width - (rect.right - rect.left)

    return taskbar_width, taskbar_height