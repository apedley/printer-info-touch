# SquareLine LVGL GENERATED FILE
# EDITOR VERSION: SquareLine Studio 1.2.1
# LVGL VERSION: 8.3.4
# PROJECT: ui
import lvgl as lv

quickStatsURL = "http://10.0.0.6:7125/printer/objects/query?webhooks=state&display_status=progress&virtual_sdcard=progress,is_active&print_stats=filename,print_duration,state&heater_bed=temperature,target&extruder=temperature,target"
tick = lv.tick_get()
def send_pause(event_struct):
    # printer_info = PrinterInfo.PrinterInfo(quickStatsURL)
    # stats = printer_info.fetch()
    # print(stats)
    return


def show_more(event_struct):
    return


def send_stop(event_struct):
    return


def send_autohome(event_struct):
    return


def page(event_struct):
    return


def update_progress(event_struct):
    return


