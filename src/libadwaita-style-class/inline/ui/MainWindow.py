# -*- coding: utf-8 -*-
"""Python and GTK: PyGObject libadwaita style class inline."""

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

    search_bar = Gtk.Template.Child(name='search_bar')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def on_button_search_clicked(self, toggle_button):
        if self.search_bar.get_search_mode():
            self.search_bar.set_search_mode(search_mode=False)
        else:
            self.search_bar.set_search_mode(search_mode=True)

    @Gtk.Template.Callback()
    def on_search_entry_changed(self, search_entry):
        print(search_entry.get_text())

    @Gtk.Template.Callback()
    def on_button_clicked(self, button):
        if 'inline' in self.search_bar.get_css_classes():
            self.search_bar.remove_css_class(css_class='inline')
        else:
            self.search_bar.add_css_class(css_class='inline')


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
