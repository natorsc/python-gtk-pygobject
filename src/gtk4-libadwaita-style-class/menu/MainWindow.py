# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita style class menu."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class Popover01(Gtk.Popover):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        button_01 = Gtk.Button.new_with_label(label='Item 01')
        vbox.append(child=button_01)

        button_02 = Gtk.Button.new_with_label(label='Item 02')
        vbox.append(child=button_02)

        button_03 = Gtk.Button.new_with_label(label='Item 03')
        vbox.append(child=button_03)


class Popover02(Gtk.Popover):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.get_style_context().add_class(class_name='menu')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        button_01 = Gtk.Button.new_with_label(label='Item 01')
        vbox.append(child=button_01)

        button_02 = Gtk.Button.new_with_label(label='Item 02')
        vbox.append(child=button_02)

        button_03 = Gtk.Button.new_with_label(label='Item 03')
        vbox.append(child=button_03)


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject style classe menu')
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

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hbox.set_homogeneous(homogeneous=True)
        hbox.set_margin_top(margin=12)
        hbox.set_margin_end(margin=12)
        hbox.set_margin_bottom(margin=12)
        hbox.set_margin_start(margin=12)
        self.set_child(child=hbox)

        button_popover = Gtk.MenuButton.new()
        button_popover.set_label(label='Popover')
        button_popover.set_valign(align=Gtk.Align.CENTER)
        button_popover.set_popover(popover=Popover01())
        hbox.append(child=button_popover)

        button_popover_class_menu = Gtk.MenuButton.new()

        button_popover_class_menu.set_label(
            label='Popover com a classe menu'
        )
        button_popover_class_menu.set_valign(align=Gtk.Align.CENTER)
        button_popover_class_menu.set_popover(popover=Popover02())
        hbox.append(child=button_popover_class_menu)


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
