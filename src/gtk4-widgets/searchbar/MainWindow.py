# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.SearchBar()."""
import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.SearchBar()')
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

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        button_show_searchbar = Gtk.ToggleButton.new()
        button_show_searchbar.set_icon_name(icon_name='system-search-symbolic')
        button_show_searchbar.connect(
            'clicked',
            self.on_button_show_searchbar_clicked,
        )
        headerbar.pack_start(child=button_show_searchbar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        entry = Gtk.Entry.new()
        entry.set_placeholder_text(text='GtkSearchBar')
        entry.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.PRIMARY,
            icon_name='system-search-symbolic',
        )
        entry.connect('activate', self.on_key_enter_pressed)
        entry.connect('icon-press', self.on_icon_pressed)

        self.searchbar = Gtk.SearchBar.new()
        self.searchbar.set_show_close_button(visible=True)
        self.searchbar.set_child(child=entry)
        self.searchbar.get_style_context().add_class(class_name='inline')
        vbox.append(child=self.searchbar)

    def on_button_show_searchbar_clicked(self, widget):
        if self.searchbar.get_search_mode():
            self.searchbar.set_search_mode(search_mode=False)
        else:
            self.searchbar.set_search_mode(search_mode=True)

    def on_icon_pressed(self, widget, EntryIconPosition):
        print('Ícone pressionado.')

    def on_key_enter_pressed(self, widget):
        print('Enter pressionando.')


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
