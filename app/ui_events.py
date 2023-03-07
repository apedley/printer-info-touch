# SquareLine LVGL GENERATED FILE
# EDITOR VERSION: SquareLine Studio 1.2.1
# LVGL VERSION: 8.3.4
# PROJECT: ui
import lvgl as lv
import urequests

stopURL = "http://10.0.0.6:7125/printer/emergency_stop"
tick = lv.tick_get()

def send_pause(event_struct):
    return


def show_more(event_struct):
    return


def send_stop(event_struct):
    response = urequests.post(stopURL)
    print(response.json())
    response.close()
    return


def send_autohome(event_struct):
    return


def page(event_struct):
    return


def update_progress(event_struct):
    return

