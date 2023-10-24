# -*- coding: utf-8 -*-
"""Python and GTK: PyGObject libadwaita Adw.NavigationSplitView."""

import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

BASE_DIR = Path(__file__).resolve().parent
UI = BASE_DIR.joinpath('MainWindow.ui')

_MODULES = BASE_DIR.parent.parent.parent.joinpath('_modules')
sys.path.append(str(_MODULES))

import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)

Adw.init()

from Page01 import Page01
from Page02 import Page02

@Gtk.Template(filename=str(UI))
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    adw_navigation_split_view = Gtk.Template.Child(
        name='adw_navigation_split_view',
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_list_activated(self, ListBox, ListBoxRow):
        print(ListBoxRow.get_name())
        match ListBoxRow.get_name():
            case 'page01':
                self.adw_navigation_split_view.set_content(content=Page01())
            case 'page02':
                self.adw_navigation_split_view.set_content(content=Page02())
            case _:
                print('...')


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