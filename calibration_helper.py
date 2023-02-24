import lvgl as lv
import time
try:
    from ili9XXX import *
    from xpt2046 import xpt2046
    
    w = 320
    h = 240
    r = 0x20
#     disp = ili9341(width = 320, height = 240, rot = MADCTL_MV)
#     disp = ili9341(width = 320, height = 240, rot = REVERSE_LANDSCAPE)
#     disp = ili9341(height = 320, width = 240, rot = PORTRAIT)

    disp = ili9341(rot=r, width=w, height=h) 
    
    
    
    x0 = 3904
    y0 = 3744
    x1 = 384
    y1 = 312
    transp = False
    
    touch = xpt2046(cal_x0 = x0, cal_y0 = y0, cal_x1 = x1, cal_y1 = y1, transpose = transp)
    
except ImportError:
    pass


import lvgl as lv

def slider_event_cb(e):
    slider = e.get_target()

    # Refresh the text
    label.set_text(str(slider.get_value()))

#
# Create a slider and write its value on a label.
#

# Create a slider in the center of the display
slider = lv.slider(lv.scr_act())
slider.set_width(200)                                              # Set the width
slider.center()
slider.add_event_cb(slider_event_cb, lv.EVENT.VALUE_CHANGED, None) # Assign an event function
# 
# # Create a label above the slider
label = lv.label(lv.scr_act())
label.set_text("0")
label.align_to(slider, lv.ALIGN.OUT_TOP_MID, 0, -15)               # Align below the slider

while True:
    med_coords = touch.get_med_coords(3)
    if med_coords:
        if transp:
            raw_y, raw_x = med_coords
        else:
            raw_x, raw_y = med_coords
        if int(raw_x) != 0 and int(raw_y) != 0:
            x = (int(raw_x) - x0) * w // (x1 - x0)
            y = (int(raw_y) - y0) * h // (y1 - y0)
            print(f"rawx: {raw_x} rawy: {raw_y}  |  x: {x} y: {y}")
            print(f"disp = ili9341(rot=0x{r:02x}, width={w}, height={h})")
            print(f"touch = xpt2046(cal_x0 = {x0}, cal_y0 = {y0}, cal_x1 = {x1}, cal_y1 = {y1}, transpose = {transp})")
    time.sleep(0.25)
    pass


#
# ORIGINAL MADCTL HELPER:
#
# ili9341 example
# disp = ili9341(
#     mosi=18, clk=19, cs=13, dc=12, rst=4, backlight=15, backlight_on=1,
#     width=128, height=160, colormode=COLOR_MODE_RGB, invert=False, rot=0)

# st7789 example
# disp = st7789(
#   mosi=19, clk=18, cs=5, dc=16, rst=23, backlight=4, backlight_on=1,
#   width=240, height=320, colormode=COLOR_MODE_RGB, invert=False, rot=0)

# style = lv.style_t()
# style.init()
# style.set_bg_color(lv.palette_main(lv.PALETTE.RED))
# 
# btn = lv.btn(lv.scr_act())
# btn.set_size(int(disp.width/3), int(disp.height/3))
# btn.align(lv.ALIGN.CENTER,0+int(disp.width/6),0+int(disp.height/6))
# btn.add_style(style, 0)
# 
# label = lv.label(btn)
# label.set_text("F");
# label.center()


