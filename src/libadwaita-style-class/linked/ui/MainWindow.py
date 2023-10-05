# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita style class linked ui file."""

import sys
from pathlib import Path

from collections.abc import Callable

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
APPLICATION_WINDOW = str(BASE_DIR.joinpath('MainWindow.ui'))

_MODULES = BASE_DIR.parent.parent.parent.joinpath('_modules')
sys.path.append(str(_MODULES))
import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)


@Gtk.Template(filename=APPLICATION_WINDOW)
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    label = Gtk.Template.Child(name='label')
    hbox_linked = Gtk.Template.Child(name='hbox_linked')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(4):
            button = Gtk.Button.new_with_label(label=f'Button {i}')
            self.hbox_linked.append(child=button)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        if 'linked' in self.hbox_linked.get_css_classes():
            self.hbox_linked.remove_css_class(css_class='linked')
        else:
            self.hbox_linked.add_css_class(css_class='linked')
        self.label.set_text(
            str=f'Classes: {self.hbox_linked.get_css_classes()}',
        )


class ExampleApplication(Gtk.Application):

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

    def create_action(self, name: str, callback: Callable[[str, str], None],
                      shortcuts: str | None = None):
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
