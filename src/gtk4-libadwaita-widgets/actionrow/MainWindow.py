# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.ActionRow()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject libadwaita Adw.ActionRow()')
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
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        listbox = Gtk.ListBox.new()
        listbox.set_selection_mode(mode=Gtk.SelectionMode.NONE)
        listbox.get_style_context().add_class(class_name='boxed-list')
        vbox.append(child=listbox)

        switch_01 = Gtk.Switch.new()
        switch_01.set_valign(align=Gtk.Align.CENTER)
        switch_01.connect('notify::active', self.on_switch_button_clicked)

        adw_action_row_01 = Adw.ActionRow.new()
        adw_action_row_01.set_icon_name(icon_name='edit-find-symbolic')
        adw_action_row_01.set_title(title='Libadwaita')
        adw_action_row_01.set_subtitle(subtitle='Adw.ActionRow()')
        adw_action_row_01.add_suffix(widget=switch_01)
        listbox.append(child=adw_action_row_01)

        switch_02 = Gtk.Switch.new()
        switch_02.set_valign(align=Gtk.Align.CENTER)
        switch_02.connect('notify::active', self.on_switch_button_clicked)

        adw_action_row_02 = Adw.ActionRow.new()
        adw_action_row_02.set_icon_name(icon_name='edit-find-symbolic')
        adw_action_row_02.set_title(
            title='Libadwaita - Ao clicar na linha widget ativa e desativa'
        )
        adw_action_row_02.set_subtitle(subtitle='Adw.ActionRow()')
        adw_action_row_02.add_suffix(widget=switch_02)
        adw_action_row_02.set_activatable_widget(widget=switch_02)
        listbox.append(child=adw_action_row_02)

    def on_switch_button_clicked(self, switch, GParamBoolean):
        if switch.get_active():
            print('Botão marcado')
        else:
            print('Botão desmarcado')


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
