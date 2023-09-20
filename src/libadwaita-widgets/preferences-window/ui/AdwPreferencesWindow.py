# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita Adw.PreferencesWindow() ui file."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gtk

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
ADW_PREFERENCES_WINDOW = str(BASE_DIR.joinpath('AdwPreferencesWindow.ui'))


@Gtk.Template(filename=ADW_PREFERENCES_WINDOW)
class AdwPreferencesWindow(Adw.PreferencesWindow):
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
