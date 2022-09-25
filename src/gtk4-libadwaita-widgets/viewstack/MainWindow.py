# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject libadwaita Adw.ViewStack()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject libadwaita Adw.ViewStack()')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        adw_headerbar = Adw.HeaderBar.new()
        self.set_titlebar(titlebar=adw_headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferências', 'app.preferences')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        adw_headerbar.pack_end(child=menu_button)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        adw_view_stack = Adw.ViewStack.new()
        adw_view_stack.set_vexpand(True)
        vbox.append(child=adw_view_stack)

        page_01 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)

        label_page_01 = Gtk.Label(label='Página 01')
        page_01.append(child=label_page_01)

        adw_view_stack.add_titled(
            child=page_01,
            name='page-01',
            title='Página 01',
        )

        page_02 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        label_page_02 = Gtk.Label(label='Página 02')
        page_02.append(child=label_page_02)

        adw_view_stack.add_titled(
            child=page_02,
            name='page-02',
            title='Página 02',
        )

        self.adw_view_switcher_title = Adw.ViewSwitcherTitle.new()
        self.adw_view_switcher_title.set_stack(stack=adw_view_stack)
        self.adw_view_switcher_title.set_title(
            title='Python e GTK 4: PyGObject libadwaita Adw.ViewStack()',
        )
        adw_headerbar.set_title_widget(self.adw_view_switcher_title)

        self.adw_view_switcher_bar = Adw.ViewSwitcherBar.new()
        self.adw_view_switcher_bar.set_stack(stack=adw_view_stack)
        self.adw_view_switcher_bar.set_reveal(True)
        self.adw_view_switcher_bar.connect(
            'notify::title-visible',
            self.on_notify_title_visible,
        )
        vbox.append(child=self.adw_view_switcher_bar)

    def on_notify_title_visible(self, *data):
        if self.adw_view_switcher_title.get_title_visible():
            self.adw_view_switcher_bar.set_reveal(True)
        else:
            self.adw_view_switcher_bar.set_reveal(False)


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
