# -*- coding: utf-8 -*-
"""."""

import sys
import pathlib

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk


UI = BASE_DIR.joinpath('Page02.ui')








Adw.init()


@Gtk.Template(filename=str(UI))
class Page02(Adw.NavigationPage):
    __gtype_name__ = 'Page02'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

