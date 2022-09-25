# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.CheckButton() radio button.

No Gtk 4 o RadioButton é um CheckButton que possui um group.
"""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.CheckButton() radio button')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferências', 'app.preferences')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menu_button)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        check_button_01 = Gtk.CheckButton.new_with_label(label='Item 01')
        check_button_01.set_group(group=None)
        check_button_01.connect('toggled', self.on_radio_button_toggled, '1')
        vbox.append(child=check_button_01)

        check_button_02 = Gtk.CheckButton.new_with_label(label='Item 02')
        check_button_02.set_group(group=check_button_01)
        check_button_02.connect('toggled', self.on_radio_button_toggled, '2')
        vbox.append(child=check_button_02)

        check_button_03 = Gtk.CheckButton.new_with_label(label='Item 03')
        check_button_03.set_group(group=check_button_01)
        check_button_03.connect('toggled', self.on_radio_button_toggled, '3')
        vbox.append(child=check_button_03)

    def on_radio_button_toggled(self, widget, data):
        if widget.get_active():
            state = 'Marcado'
        else:
            state = 'desmarcado'
        print(f'Botão {data} {state}')


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
