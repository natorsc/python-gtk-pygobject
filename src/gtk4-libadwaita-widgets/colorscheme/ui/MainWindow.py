# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.ColorScheme() Dark mode."""

import subprocess
import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
FILENAME = str(BASE_DIR.joinpath('MainWindow.ui'))


# Não utilizar no Gnome Builder. Configurar via meson.
# [!] O Compilador Blueprint deve estar instalado [!].
if sys.platform == 'linux':
    for data in BASE_DIR.iterdir():
        if data.is_file() and data.suffix == '.blp':
            subprocess.run(
                args=['blueprint-compiler', 'compile', f'{data}', '--output',
                      f'{BASE_DIR.joinpath(data.stem)}.ui'],
            )


@Gtk.Template(filename=FILENAME)
class ExampleWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    switch = Gtk.Template.Child(name='switch')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = kwargs.get('application')

        self.style_manager = self.application.get_style_manager()

        if self.style_manager.get_dark():
            self.switch.set_active(is_active=True)

    @Gtk.Template.Callback()
    def on_switch_active(self, widget, state):
        if widget.get_active():
            self.style_manager.set_color_scheme(
                color_scheme=Adw.ColorScheme.PREFER_DARK
            )
        else:
            self.style_manager.set_color_scheme(
                color_scheme=Adw.ColorScheme.FORCE_LIGHT
            )


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
