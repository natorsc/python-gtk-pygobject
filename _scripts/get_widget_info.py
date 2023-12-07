# -*- coding: utf-8 -*-
"""Script para coletar informações dos widgets GTK."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, GObject, Gtk

Adw.init()


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.joinpath('data')

GTK_VERSION = (
    Gtk.get_major_version(), Gtk.get_minor_version(), Gtk.get_micro_version(),
)
LIBADWAITA_VERSION = (
    Adw.get_major_version(), Adw.get_minor_version(), Adw.get_micro_version(),
)
PYGOBJECT_VERSION = GObject.pygobject_version


WIDGET = Gtk.Button.new()

methods_get = [method for method in dir(WIDGET) if method.startswith('get_')]
methods_set = [method for method in dir(WIDGET) if method.startswith('set_')]

data = open(file=DATA_DIR.joinpath('widget.md'), mode='r', encoding='utf-8')
template = data.read()

widget_name = WIDGET.get_name()

output = DATA_DIR.joinpath(f'{widget_name}.md')
output.write_text(
    encoding='utf-8',
    data=template.format(
        widget_name=widget_name,
        gtk_version=GTK_VERSION,
        libadwaita_version=LIBADWAITA_VERSION,
        pygobject_version=PYGOBJECT_VERSION,
        widget_props='\n- '.join(sorted(dir(WIDGET.props))),
        widget_signals='\n- '.join(sorted(GObject.signal_list_names(WIDGET))),
        methods_get='\n- '.join(sorted(methods_get)),
        methods_set='\n- '.join(sorted(methods_set)),
    ),
)

print('[!] Concluido [!]')
