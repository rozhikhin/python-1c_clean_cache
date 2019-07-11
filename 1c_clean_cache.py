import os
import shutil

# print(os.getlogin())

# Путь к C:\Users\username\AppData\Roaming\
APPDATA = os.getenv('APPDATA')
# Путь к C:\Users\username\AppData\Local
LOCALAPPDATA = os.getenv('LOCALAPPDATA')
# Путь к C:\Users\username\AppData\Roaming\1C\1cv8
APPDATA_1C = os.path.join(APPDATA, '1C\\1cv8')
# Путь к C:\Users\username\AppData\Roaming\1C\1cv8
LOCALAPPDATA_1C = os.path.join(LOCALAPPDATA, '1C\\1cv8')

# Списки файйлов и катологов, которые не нужно удадялть
APPDATA_EX = ['1cv8.pfl', '1cv8c.pfl', '1cv8strt.pfl', '1cv8u.pfl', 'ExtCompT']
LOCALAPPDATA_EX = ['1cv8u.pfl', 'dumps']
#
RES_EX = APPDATA_EX + LOCALAPPDATA_EX


def clear_cache(path_to_cache):
    for i in os.listdir(path_to_cache):
        if i not in RES_EX:
            # print(os.path.join(path_to_cache, i))
            shutil.rmtree(os.path.join(path_to_cache, i))


clear_cache(APPDATA_1C)
clear_cache(LOCALAPPDATA_1C)
