#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Easy Anticheat Switcher

#__author__ = "Sebastian Carusso Noje"
#__copyright__ = "Copyright 2019, BODYWORKStm-"
#__license__ = "GPL"
#__version__ = "0.0.1"
#__maintainer__ = "Sebastian Carusso Noje"
#__email__ = "body2pgl@gmail.com"
#__status__ = "Production Beta"

import os
import sys
import ctypes
import subprocess as sp
from subprocess import call
from infi.systray import SysTrayIcon

# ===== Settings =====

# Tray Menu Settings
icon_path = "icon5.ico"
hover_app_title = "bodyowns.io- Anticheat Switcher"

# Tray Menu Anti Cheats
faceit_mname = "Faceit Anticheat" 
esea_mname = "ESEA Anticheat"

# Anticheats Msgbox
faceit_msgbox = 'Activating Faceit Anti-Cheat!'
esea_msgbox = 'Activating ESEA Anti-Cheat !'
msgbox_title = 'AC Switcher'

# Anticheats Paths
faceit_ap = r'C:\Users\Fresh\AppData\Local\FACEITApp\FACEIT.exe'
faceit_ap_close = "faceit.exe"
esea_ap = r'C:\Program Files\ESEA\ESEA Client\eseaclient.exe'
esea_ap_close = "eseaclient.exe"

# ===== Application =====

# Activation of Anti-Cheats
def activate_faceit(systray):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, faceit_msgbox, msgbox_title, 0)
    print ("---Faceit Anticheat Activated !---")
    # Deactivate ESEA
    deactivate_esea(systray)
    # Open Application
    sp.Popen([faceit_ap])
#    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, faceit_ap, None, 1)


def activate_esea(systray):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, esea_msgbox, msgbox_title, 0)
    print ("---ESEA Anticheat Activated !---")
    # Deactivate Faceit
    deactivate_faceit(systray)
    # Open Application
    sp.Popen([esea_ap])
#    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, esea_ap, None, 1)

# Deactivation of other Anti-Cheats
def deactivate_faceit(systray):
    print ("Faceit Deactivated !")
#3    os.system("taskkill /im " + faceit_ap_close)
    call(['taskkill','/F','/IM',faceit_ap_close])

def deactivate_esea(systray):
    print ("ESEA Deactivated !")
#    os.system("taskkill /im " + esea_ap_close)
    call(['taskkill','/F','/IM',esea_ap_close])

menu_options = ((faceit_mname, None, activate_faceit),(esea_mname, None, activate_esea),)

systray = SysTrayIcon(icon_path, hover_app_title, menu_options)

systray.start()
