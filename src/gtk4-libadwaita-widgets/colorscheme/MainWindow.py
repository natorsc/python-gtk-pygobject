# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.ColorScheme() Dark mode."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = kwargs.get('application')
        self.style_manager = self.application.get_style_manager()

        self.set_title(
            title='Python e GTK 4: PyGObject libadwaita Adw.ColorScheme()'
        )
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
        hbox.set_margin_top(margin=12)
        hbox.set_margin_end(margin=12)
        hbox.set_margin_bottom(margin=12)
        hbox.set_margin_start(margin=12)
        self.set_child(child=hbox)

        text = 'Clique no switch para ativar ou desativar o modo escuro (dark mode)'
        label = Gtk.Label.new(str=text)
        hbox.append(child=label)

        self.switch = Gtk.Switch.new()
        self.switch.set_valign(align=Gtk.Align.CENTER)
        if self.style_manager.get_dark():
            self.switch.set_active(is_active=True)
        self.switch.connect('notify::active', self.on_switch_active)
        hbox.append(child=self.switch)

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
