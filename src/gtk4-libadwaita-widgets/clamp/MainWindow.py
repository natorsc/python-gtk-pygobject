# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.Clamp()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject libadwaita Adw.Clamp()')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferências', 'app.preferences')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menu_button)

        adw_clamp = Adw.Clamp.new()
        self.set_child(child=adw_clamp)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        vbox.set_margin_top(margin=24)
        vbox.set_margin_end(margin=24)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=24)
        adw_clamp.set_child(child=vbox)

        listbox_01 = Gtk.ListBox.new()
        listbox_01.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox_01.get_style_context().add_class(class_name='boxed-list')
        vbox.append(child=listbox_01)

        for n in range(1, 4):
            label = Gtk.Label.new(str=f'Item {n}')
            listbox_01.append(child=label)

        listbox_02 = Gtk.ListBox.new()
        listbox_02.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox_02.get_style_context().add_class(class_name='boxed-list')
        vbox.append(child=listbox_02)

        for n in range(4, 7):
            label = Gtk.Label.new(str=f'Item {n}')
            listbox_02.append(child=label)


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
