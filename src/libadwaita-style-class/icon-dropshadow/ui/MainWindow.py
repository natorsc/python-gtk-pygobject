# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita style class icon-dropshadow ui file."""

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
TEXT = (
    'GNOME application icons require a shadow to be readable '
    'on a light background. The style classes .icon-dropshadow and .lowres-icon '
    'provide this when used with GtkImage or any other widget that '
    'contains an image.\n'
    '.lowres-icon should be used for icons of 32×32 or smaller, and '
    '.icon-dropshadow should be used otherwise.\n'
    'Classes: {}'
)

_MODULES = BASE_DIR.parent.parent.parent.joinpath('_modules')
sys.path.append(str(_MODULES))
import _tools

_tools.compile_blueprint_ui(ui_dir=BASE_DIR)


@Gtk.Template(filename=APPLICATION_WINDOW)
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    label = Gtk.Template.Child(name='label')
    image_icon_dropshadow = Gtk.Template.Child(name='image_icon_dropshadow')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        if 'icon-dropshadow' in self.image_icon_dropshadow.get_css_classes():
            self.image_icon_dropshadow.remove_css_class(
                css_class='icon-dropshadow')
        else:
            self.image_icon_dropshadow.add_css_class(
                css_class='icon-dropshadow')
        self.label.set_text(
            str=TEXT.format(self.image_icon_dropshadow.get_css_classes()),
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
