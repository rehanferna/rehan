# coding: utf-8
# Created by: Rehan Fernando
# Created on: September 2016
# Cretaed for: ICS3U
# This progarm is the Hello, World International program.

import ui

def english_touch_up_inside(sender):
	# english version
    view['hello_world_label'].text = ('Hello World!')

def french_touch_up_inside(sender):
	# french version
    view['hello_world_label'].text = ('Bonjour Le Monde!')

def spanish_touch_up_inside(sender):
	# spanish version
    view['hello_world_label'].text = ('¡Hola Mundo!')

view = ui.load_view()
view.present('full_sheet')
