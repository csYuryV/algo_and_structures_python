'''

2019-12-04 Sikorskiy Yuriy
cs.yury.v@pm.me

1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
'''

# Операционная система: Kubuntu 19.10
# Версия KDE Plasma: 5.16.5
# Версия KDE Frameworks: 5.62.0
# Версия Qt: 5.12.4
# Версия ядра: 5.3.0-24-generic
# Архитектура: 64-битная
# Процессоры: 16 × AMD Ryzen 7 2700X Eight-Core Processor
# Память: 31,4 ГиБ ОЗУ

import cv2 as cv
import glob
from memory_profiler import profile


@profile
def color_to_gray(fl_nm_pic):
    img = cv.imread(fl_nm_pic)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    del img
    out_fl_nm = './gray/' + fl_nm_pic
    cv.imwrite(out_fl_nm, gray)
    del gray


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     22     71.5 MiB     71.5 MiB   @profile
#     23                             def color_to_gray(fl_nm_pic):
#     24     74.1 MiB      2.6 MiB       img = cv.imread(fl_nm_pic)
#     25     74.1 MiB      0.0 MiB       gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     26     74.1 MiB      0.0 MiB       del img
#     27     74.1 MiB      0.0 MiB       out_fl_nm = './gray/' + fl_nm_pic
#     28     74.1 MiB      0.0 MiB       cv.imwrite(out_fl_nm, gray)
#     29     71.5 MiB      0.0 MiB       del gray


def main():
    list_fl_nm_pic = glob.glob('*.jpg')
    for fl_nm_pic in list_fl_nm_pic:
        color_to_gray(fl_nm_pic)


if __name__ == '__main__':
    main()
