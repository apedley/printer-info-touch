import lvgl as lv
from . import PrinterInfo
from uasyncio import Loop, run

lv.init()

HORIZONTAL_RES = 320
VERTICAL_RES = 240
quickStatsURL = "http://10.0.0.6:7125/printer/objects/query?webhooks=state&display_status=progress&virtual_sdcard=progress,is_active&print_stats=filename,print_duration,state&heater_bed=temperature,target&extruder=temperature,target"

try:
    from ili9XXX import ili9341
    from xpt2046 import xpt2046

    
    disp = ili9341(rot=0x20, width=HORIZONTAL_RES, height=VERTICAL_RES, asynchronous=False, initialize=True)
    touch = xpt2046(cal_x0 = 3904, cal_y0 = 3744, cal_x1 = 384, cal_y1 = 312, transpose = False)

except ImportError:
    pass


try:
    
    import SDL
    SDL.init(w=HORIZONTAL_RES, h=VERTICAL_RES, auto_refresh=True)

    # Register SDL display driver.

    draw_buf = lv.disp_draw_buf_t()
    buf1_1 = bytearray(HORIZONTAL_RES * 10)
    draw_buf.init(buf1_1, None, len(buf1_1)//4)
    disp_drv = lv.disp_drv_t()
    disp_drv.init()
    disp_drv.draw_buf = draw_buf
    disp_drv.flush_cb = SDL.monitor_flush
    disp_drv.hor_res = HORIZONTAL_RES
    disp_drv.ver_res = VERTICAL_RES
    disp_drv.register()

    # Regsiter SDL mouse driver

    indev_drv = lv.indev_drv_t()
    indev_drv.init()
    indev_drv.type = lv.INDEV_TYPE.POINTER
    indev_drv.read_cb = SDL.mouse_read
    indev_drv.register()
except ImportError:
    pass

from . import ui


printer_info = PrinterInfo.PrinterInfo(quickStatsURL)

# timer = lv.timer_create(printer_info.fetch, 5000, None)
# def fetch_stats(timer):
#     print('fetching..')

def main():
    
    while True:
        pass
if __name__ == '__main__':
    main()
