import lvgl as lv
try:
    from ili9XXX import *
    from xpt2046 import xpt2046
    
    disp = ili9341(rot=0x20, width=320, height=240)
    touch = xpt2046(cal_x0 = 3904, cal_y0 = 3744, cal_x1 = 384, cal_y1 = 312, transpose = False)

except ImportError:
    pass

from . import PrinterInfo

    
def main():
    from . import UI
    while True:
        pass
    
if __name__ == '__main__':
    main()