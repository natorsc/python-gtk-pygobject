# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita Adw.PreferencesWindow() ui file."""

import sys
from pathlib import Path



import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
UI = str(BASE_DIR.joinpath('MainWindow.ui'))

_MODULES = BASE_DIR.parent.parent.parent.joinpath('_modules')
sys.path.append(str(_MODULES))
import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)


@Gtk.Template(filename=UI)
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PreferencesWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        print('Button pressed.')

    @Gtk.Template.Callback()
    def on_switch_button_clicked(self, switch, GParamBoolean):
        if switch.get_active():
            print('Button checked')
        else:
            print('Button unchecked')
