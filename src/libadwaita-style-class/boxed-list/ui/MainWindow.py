# -*- coding: utf-8 -*-
"""Python and GTK: PyGObject libadwaita style class boxed-list."""

import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

BASE_DIR = Path(__file__).resolve().parent
UI = BASE_DIR.joinpath('MainWindow.ui')

_SCRIPTS = BASE_DIR.parent.parent.parent.parent.joinpath('_scripts')
sys.path.append(str(_SCRIPTS))

import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)

Adw.init()


@Gtk.Template(filename=str(UI))
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    list_box = Gtk.Template.Child(name='list_box')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        if 'boxed-list' in self.list_box.get_css_classes():
            self.list_box.remove_css_class(css_class='boxed-list')
        else:
            self.list_box.add_css_class(css_class='boxed-list')


class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.PyGObject',
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
        print('Action `app.preferences` was active.')

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name=name, parameter_type=None)
        action.connect('activate', callback)
        self.add_action(action=action)
        if shortcuts:
            self.set_accels_for_action(
                detailed_action_name=f'app.{name}',
                accels=shortcuts,
            )


if __name__ == '__main__':
    app = ExampleApplication()
    app.run(sys.argv)
