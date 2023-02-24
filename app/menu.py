import lvgl

Menu = lvgl.menu( lvgl.scr_act() )
Menu.set_size( 320, 240 )
Menu.set_style_bg_color( lvgl.color_hex( 0xA0A0A0 ), 0 )

#Main page
Main_pg = lvgl.menu_page( Menu, 'Welcome' )

#Main page content
section = lvgl.obj( Main_pg )
section.set_size( 200, 200 )

intro = lvgl.label( section )
intro.set_width( 172 )
intro.set_long_mode( lvgl.label.LONG.WRAP )
intro.set_flex_grow( 1 )
intro.set_text( 'These buttons will act like links.' )

link1 = lvgl.btn( section )
link1.set_size( 55, 20 )
link1.align( lvgl.ALIGN.CENTER, -45, 0 )
link1_label = lvgl.label( link1 )
link1_label.set_text( 'Page 1' )
link1_label.center()

link2 = lvgl.btn( section )
link2.set_size( 55, 20 )
link2.align( lvgl.ALIGN.CENTER, 45, 0)
link2_label = lvgl.label( link2 )
link2_label.set_text( 'Page 3' )
link2_label.center()

#Main page side bar
Main_Sidebar = lvgl.menu_page( Menu, 'Files' )
Sidebar_section = lvgl.obj( Main_Sidebar )
Sidebar_section.set_size( 60, 200 )

Main_link = lvgl.label( Sidebar_section )
Main_link.set_text( 'Main' )

seperator = lvgl.line( Sidebar_section )
pt = [{'x':0,'y': 28},{'x': 30, 'y': 28}]
seperator.set_points( pt, 2 )

Page_link1 = lvgl.label( Sidebar_section )
Page_link1.set_text( 'Pg 1' )
Page_link1.set_y( 40 )

seperator = lvgl.line( Sidebar_section )
pt = [{'x':0,'y': 68},{'x': 30, 'y': 68}]
seperator.set_points( pt, 2 )

Page_link2 = lvgl.label( Sidebar_section )
Page_link2.set_text( 'Pg 2' )
Page_link2.set_y( 80 )

seperator = lvgl.line(Sidebar_section)
pt = [{'x':0,'y': 108},{'x': 30, 'y': 108}]
seperator.set_points( pt,2 )

Page_link3 = lvgl.label( Sidebar_section )
Page_link3.set_text( 'Pg 3' )
Page_link3.set_y( 120 )
#End of main page

#Page 1
Page1 = lvgl.menu_page( Menu, None )
Page1_label = lvgl.label( Page1 )
Page1_label.set_text( 'This is page 1' )

#page2
Page2 = lvgl.menu_page( Menu, None )
Page2_label = lvgl.label( Page2 )
Page2_label.set_text( 'This is page 2' )

#page3
Page3 = lvgl.menu_page( Menu, None )
Page3_label = lvgl.label( Page3 )
Page3_label.set_text( 'This is page 3' )

#setup all the links
Menu.set_load_page_event( link1, Page1 )
Menu.set_load_page_event( link2, Page3 )
Menu.set_load_page_event( Main_link, Main_pg )
Menu.set_load_page_event( Page_link1, Page1 )
Menu.set_load_page_event( Page_link2, Page2 )
Menu.set_load_page_event( Page_link3, Page3 )

#start Main Page
Menu.set_page( Main_pg )
Menu.set_sidebar_page( Main_Sidebar )