# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.FontButton() ui file."""

import subprocess
import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk, Pango

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
FILENAME = str(BASE_DIR.joinpath('MainWindow.ui'))


# Não utilizar no Gnome Builder. Configurar via meson.
# [!] O Compilador Blueprint deve estar instalado [!].
if sys.platform == 'linux':
    subprocess.run(
        args=['blueprint-compiler', 'compile',
              f'{BASE_DIR.joinpath("MainWindow.blp")}', '--output',
              f'{BASE_DIR.joinpath("MainWindow.ui")}'],
    )


@Gtk.Template(filename=FILENAME)
class ExampleWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_font_button_font_set(self, font_button):
        pango_font_description = Pango.FontDescription.from_string(
            str=font_button.get_font(),
        )

        pango_attr_font_desc = Pango.AttrFontDesc.new(
            desc=pango_font_description,
        )

        pango_attr_list = Pango.AttrList.new()
        pango_attr_list.insert(attr=pango_attr_font_desc)

        self.label.set_attributes(attrs=pango_attr_list)


class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_preferences_action(self, action, param):
        print('Ação app.preferences foi ativa.')

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
