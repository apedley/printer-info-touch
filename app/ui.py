# SquareLine LVGL GENERATED FILE
# EDITOR VERSION: SquareLine Studio 1.2.1
# LVGL VERSION: 8.3.4
# PROJECT: ui


import lvgl as lv
from . import ui_images
from . import ui_events

dispp = lv.disp_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
dispp.set_theme(theme)

def SetFlag( obj, flag, value):
    if (value):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

_ui_comp_table = {}
_ui_comp_prev = None
_ui_name_prev = None
_ui_child_prev = None
_ui_comp_table.clear()

def _ui_comp_del_event(e):
    target = e.get_target()
    _ui_comp_table[id(target)].remove()

def ui_comp_get_child(comp, child_name):
    return _ui_comp_table[id(comp)][child_name]

def ui_comp_get_root_from_child(child, compname):
    for component in _ui_comp_table:
        if _ui_comp_table[component]["_CompName"]==compname:
            for part in _ui_comp_table[component]:
                if id(_ui_comp_table[component][part]) == id(child):
                    return _ui_comp_table[component]
    return None
def SetBarProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def SetPanelProperty(target, id, val):
   if id == 'Position_X': target.set_x(val)
   if id == 'Position_Y': target.set_y(val)
   if id == 'Width': target.set_width(val)
   if id == 'Height': target.set_height(val)
   return

def SetDropdownProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val)
   return

def SetImageProperty(target, id, val, val2):
   if id == 'Image': target.set_src(val)
   if id == 'Angle': target.set_angle(val2)
   if id == 'Zoom': target.set_zoom(val2)
   return

def SetLabelProperty(target, id, val):
   if id == 'Text': target.set_text(val)
   return

def SetRollerProperty(target, id, val):
   if id == 'Selected':
      target.set_selected(val, lv.ANIM.OFF)
   if id == 'Selected_with_anim':
      target.set_selected(val, lv.ANIM.ON)
   return

def SetSliderProperty(target, id, val):
   if id == 'Value_with_anim': target.set_value(val, lv.ANIM.ON)
   if id == 'Value': target.set_value(val, lv.ANIM.OFF)
   return

def ChangeScreen( src, fademode, speed, delay):
    lv.scr_load_anim(src, fademode, speed, delay, False)
    return

def IncrementArc( trg, val):
    trg.set_value(trg.get_value()+val)
    lv.event_send(trg,lv.EVENT.VALUE_CHANGED, None)
    return

def IncrementBar( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    return

def IncrementSlider( trg, val, anim):
    trg.set_value(trg.get_value()+val,anim)
    lv.event_send(trg,lv.EVENT.VALUE_CHANGED, None)
    return

def KeyboardSetTarget( keyboard, textarea):
    keyboard.set_textarea(textarea)
    return

def ModifyFlag( obj, flag, value):
    if (value=="TOGGLE"):
        if ( obj.has_flag(flag) ):
            obj.clear_flag(flag)
        else:
            obj.add_flag(flag)
        return

    if (value=="ADD"):
        obj.add_flag(flag)
    else:
        obj.clear_flag(flag)
    return

def ModifyState( obj, state, value):
    if (value=="TOGGLE"):
        if ( obj.has_state(state) ):
            obj.clear_state(state)
        else:
            obj.add_state(state)
        return

    if (value=="ADD"):
        obj.add_state(state)
    else:
        obj.clear_state(state)
    return

def set_opacity(obj, v):
    obj.set_style_opa(v, lv.STATE.DEFAULT|lv.PART.MAIN)
    return

def SetTextValueArc( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueSlider( trg, src, prefix, postfix):
    trg.set_text(prefix+str(src.get_value())+postfix)
    return

def SetTextValueChecked( trg, src, txton, txtoff):
    if src.has_state(lv.STATE.CHECKED):
        trg.set_text(txton)
    else:
        trg.set_text(txtoff)
    return

# COMPONENTS

 # COMPONENT ButtonLabeled
def ui_ButtonLabeled_create(comp_parent):
    cui_ButtonLabeled = lv.btn(comp_parent)
    cui_ButtonLabeled.set_width(120)
    cui_ButtonLabeled.set_height(38)
    cui_ButtonLabeled.set_x(20)
    cui_ButtonLabeled.set_y(182)
    SetFlag(cui_ButtonLabeled, lv.obj.FLAG.SCROLLABLE, False)
    SetFlag(cui_ButtonLabeled, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
    cui_Label = lv.label(cui_ButtonLabeled)
    cui_Label.set_long_mode(lv.label.LONG.CLIP)
    cui_Label.set_text("")
    cui_Label.set_width(120)
    cui_Label.set_height(24)
    cui_Label.set_align( lv.ALIGN.CENTER)
    cui_Label.set_style_text_align( lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT )
    cui_Label.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )
    _ui_comp_table[id(cui_ButtonLabeled)]= {"ButtonLabeled" : cui_ButtonLabeled,"Label" : cui_Label, "_CompName" : "ButtonLabeled"}
    return cui_ButtonLabeled

 # COMPONENT ProgressBar
def ui_ProgressBar_create(comp_parent):
    cui_ProgressBar = lv.bar(comp_parent)
    cui_ProgressBar.set_value(35,lv.ANIM.OFF)  # need refresh: 0,100
    if 'NORMAL' is 'RANGE': cui_ProgressBar.set_start_value(0, lv.ANIM.OFF)
    cui_ProgressBar.set_width(280)
    cui_ProgressBar.set_height(32)
    cui_ProgressBar.set_x(20)
    cui_ProgressBar.set_y(20)
    cui_LabelProgressBar = lv.label(cui_ProgressBar)
    cui_LabelProgressBar.set_long_mode(lv.label.LONG.CLIP)
    cui_LabelProgressBar.set_text("100%")
    cui_LabelProgressBar.set_width(280)
    cui_LabelProgressBar.set_height(24)
    cui_LabelProgressBar.set_align( lv.ALIGN.CENTER)
    cui_LabelProgressBar.set_style_text_color( lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT )
    cui_LabelProgressBar.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
    cui_LabelProgressBar.set_style_text_align( lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT )
    cui_LabelProgressBar.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )
    _ui_comp_table[id(cui_ProgressBar)]= {"ProgressBar" : cui_ProgressBar,"LabelProgressBar" : cui_LabelProgressBar, "_CompName" : "ProgressBar"}
    return cui_ProgressBar

def ProgressBar1_eventhandler(event_struct):
   event = event_struct.code
   if event == lv.EVENT.CLICKED and True:
      ui_events.update_progress( event_struct )
   return

def StopButtonLabeled_ButtonLabeled_eventhandler(event_struct):
   event = event_struct.code
   if event == lv.EVENT.CLICKED and True:
      ModifyFlag( ui_StopButtonLabeled, lv.obj.FLAG.HIDDEN, "ADD")
      ModifyFlag( ui_StopConfirmationButtonLabeled, lv.obj.FLAG.HIDDEN, "REMOVE")
   return

def StopConfirmationButtonLabeled_ButtonLabeled_eventhandler(event_struct):
   event = event_struct.code
   if event == lv.EVENT.CLICKED and True:
      ui_events.send_stop( event_struct )
      ModifyFlag( ui_StopConfirmationButtonLabeled, lv.obj.FLAG.HIDDEN, "ADD")
      ModifyFlag( ui_StopButtonLabeled, lv.obj.FLAG.HIDDEN, "REMOVE")
   return

def MoreButtonLabeled_ButtonLabeled_eventhandler(event_struct):
   event = event_struct.code
   if event == lv.EVENT.CLICKED and True:
      ChangeScreen( ui_Screen2, lv.SCR_LOAD_ANIM.MOVE_LEFT, 350, 0)
   return

ui_Screen1 = lv.obj()
SetFlag(ui_Screen1, lv.obj.FLAG.SCROLLABLE, False)
ui_Screen1.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

ui_ProgressBar1 = lv.bar(ui_Screen1)
ui_ProgressBar1.set_value(35,lv.ANIM.OFF)  # need refresh: 0,100
if 'NORMAL' is 'RANGE': ui_ProgressBar1.set_start_value(0, lv.ANIM.OFF)
ui_ProgressBar1.set_width(280)
ui_ProgressBar1.set_height(32)
ui_ProgressBar1.set_x(20)
ui_ProgressBar1.set_y(20)

ui_LabelProgressBar1 = lv.label(ui_ProgressBar1)
ui_LabelProgressBar1.set_long_mode(lv.label.LONG.CLIP)
ui_LabelProgressBar1.set_text("100%")
ui_LabelProgressBar1.set_width(280)
ui_LabelProgressBar1.set_height(24)
ui_LabelProgressBar1.set_align( lv.ALIGN.CENTER)
ui_LabelProgressBar1.set_style_text_color( lv.color_hex(0xFFFFFF), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_LabelProgressBar1.set_style_text_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )
ui_LabelProgressBar1.set_style_text_align( lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_LabelProgressBar1.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_ProgressBar1.add_event_cb(ProgressBar1_eventhandler, lv.EVENT.ALL, None)
ui_LabelFilename = lv.label(ui_Screen1)
ui_LabelFilename.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
ui_LabelFilename.set_text("Filename goes here.gcode")
ui_LabelFilename.set_width(280)
ui_LabelFilename.set_height(24)
ui_LabelFilename.set_x(20)
ui_LabelFilename.set_y(64)
ui_LabelFilename.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_LabelEta = lv.label(ui_Screen1)
ui_LabelEta.set_text("ETA: 00:00:00")
ui_LabelEta.set_width(280)
ui_LabelEta.set_height(24)
ui_LabelEta.set_x(20)
ui_LabelEta.set_y(102)
ui_LabelEta.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_LabelPrintInfo = lv.label(ui_Screen1)
ui_LabelPrintInfo.set_long_mode(lv.label.LONG.CLIP)
ui_LabelPrintInfo.set_text("Layer 30/120 Height 120mm")
ui_LabelPrintInfo.set_width(280)
ui_LabelPrintInfo.set_height(24)
ui_LabelPrintInfo.set_x(20)
ui_LabelPrintInfo.set_y(138)
ui_LabelPrintInfo.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )

ui_StopButtonLabeled = ui_ButtonLabeled_create(ui_Screen1)
ui_StopButtonLabeled.set_x(20)
ui_StopButtonLabeled.set_y(182)

ui_comp_get_child(ui_StopButtonLabeled, "Label").set_text("Stop")

ui_StopButtonLabeled.add_event_cb(StopButtonLabeled_ButtonLabeled_eventhandler, lv.EVENT.ALL, None)
ui_StopConfirmationButtonLabeled = ui_ButtonLabeled_create(ui_Screen1)
ui_StopConfirmationButtonLabeled.set_x(20)
ui_StopConfirmationButtonLabeled.set_y(182)
SetFlag(ui_StopConfirmationButtonLabeled, lv.obj.FLAG.HIDDEN, True)
ui_StopConfirmationButtonLabeled.set_style_bg_color( lv.color_hex(0xCC0000), lv.PART.MAIN | lv.STATE.DEFAULT )
ui_StopConfirmationButtonLabeled.set_style_bg_opa(255, lv.PART.MAIN| lv.STATE.DEFAULT )

ui_comp_get_child(ui_StopConfirmationButtonLabeled, "Label").set_text("Confirm")

ui_StopConfirmationButtonLabeled.add_event_cb(StopConfirmationButtonLabeled_ButtonLabeled_eventhandler, lv.EVENT.ALL, None)
ui_MoreButtonLabeled = ui_ButtonLabeled_create(ui_Screen1)
ui_MoreButtonLabeled.set_x(180)
ui_MoreButtonLabeled.set_y(182)

ui_comp_get_child(ui_MoreButtonLabeled, "Label").set_text("More")

ui_MoreButtonLabeled.add_event_cb(MoreButtonLabeled_ButtonLabeled_eventhandler, lv.EVENT.ALL, None)

def BackButtonLabeled_ButtonLabeled_eventhandler(event_struct):
   event = event_struct.code
   if event == lv.EVENT.CLICKED and True:
      ChangeScreen( ui_Screen1, lv.SCR_LOAD_ANIM.MOVE_RIGHT, 350, 0)
   return

ui_Screen2 = lv.obj()
SetFlag(ui_Screen2, lv.obj.FLAG.SCROLLABLE, False)

ui_LoadButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_LoadButtonLabeled.set_x(20)
ui_LoadButtonLabeled.set_y(68)

ui_comp_get_child(ui_LoadButtonLabeled, "Label").set_text("Load")

ui_UnloadButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_UnloadButtonLabeled.set_x(180)
ui_UnloadButtonLabeled.set_y(68)

ui_comp_get_child(ui_UnloadButtonLabeled, "Label").set_text("Unload")

ui_HeatButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_HeatButtonLabeled.set_x(20)
ui_HeatButtonLabeled.set_y(124)

ui_comp_get_child(ui_HeatButtonLabeled, "Label").set_text("Heat")

ui_CoolButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_CoolButtonLabeled.set_x(180)
ui_CoolButtonLabeled.set_y(124)

ui_comp_get_child(ui_CoolButtonLabeled, "Label").set_text("Cool")

ui_BackButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_BackButtonLabeled.set_x(20)
ui_BackButtonLabeled.set_y(182)

ui_comp_get_child(ui_BackButtonLabeled, "Label").set_text("Back")

ui_BackButtonLabeled.add_event_cb(BackButtonLabeled_ButtonLabeled_eventhandler, lv.EVENT.ALL, None)
ui_ExtrudeButtonLabeled = ui_ButtonLabeled_create(ui_Screen2)
ui_ExtrudeButtonLabeled.set_x(180)
ui_ExtrudeButtonLabeled.set_y(182)

ui_comp_get_child(ui_ExtrudeButtonLabeled, "Label").set_text("Extrude")

ui_LabelTempInfo = lv.label(ui_Screen2)
ui_LabelTempInfo.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
ui_LabelTempInfo.set_text("Extruder: 240/240 Bed: 80/80")
ui_LabelTempInfo.set_width(280)
ui_LabelTempInfo.set_height(24)
ui_LabelTempInfo.set_x(20)
ui_LabelTempInfo.set_y(20)
ui_LabelTempInfo.set_style_text_align( lv.TEXT_ALIGN.CENTER, lv.PART.MAIN | lv.STATE.DEFAULT )
ui_LabelTempInfo.set_style_text_font( lv.font_montserrat_22, lv.PART.MAIN | lv.STATE.DEFAULT )

lv.scr_load(ui_Screen1)
