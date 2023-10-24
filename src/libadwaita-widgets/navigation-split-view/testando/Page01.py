# -*- coding: utf-8 -*-
"""."""

import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

BASE_DIR = Path(__file__).resolve().parent
UI = BASE_DIR.joinpath('Page01.ui')

_MODULES = BASE_DIR.parent.parent.parent.joinpath('_modules')
sys.path.append(str(_MODULES))

import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)

Adw.init()


@Gtk.Template(filename=str(UI))
class Page01(Adw.NavigationPage):
    __gtype_name__ = 'Page01'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

