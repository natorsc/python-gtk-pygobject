# -*- coding: utf-8 -*-
"""Python and GTK: PyGObject libadwaita style class colors."""

import sys
import pathlib

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk


UI = BASE_DIR.joinpath('MainWindow.ui')








Adw.init()


@Gtk.Template(filename=str(UI))
class ExampleWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    label_accent = Gtk.Template.Child(name='label_accent')
    label_success = Gtk.Template.Child(name='label_success')
    label_warning = Gtk.Template.Child(name='label_warning')
    label_error = Gtk.Template.Child(name='label_error')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        if 'accent' in self.label_accent.get_css_classes():
            self.label_accent.remove_css_class(css_class='accent')
            self.label_success.remove_css_class(css_class='success')
            self.label_warning.remove_css_class(css_class='warning')
            self.label_error.remove_css_class(css_class='error')

        else:
            self.label_accent.add_css_class(css_class='accent')
            self.label_success.add_css_class(css_class='success')
            self.label_warning.add_css_class(css_class='warning')
            self.label_error.add_css_class(css_class='error')


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
