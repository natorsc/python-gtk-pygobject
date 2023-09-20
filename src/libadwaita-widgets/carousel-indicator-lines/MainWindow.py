# -*- coding: utf-8 -*-
"""Python e GTK: PyGObject libadwaita Adw.CarouselIndicatorLines()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(
            title='Python e GTK: PyGObject libadwaita Adw.CarouselIndicatorLines()')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)

        menu_button_model = Gio.Menu()
        menu_button_model.append(
            label='Preferences',
            detailed_action='app.preferences',
        )

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)

        overlay = Gtk.Overlay.new()
        self.set_child(child=overlay)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_top(12)
        vbox.set_margin_end(12)
        vbox.set_margin_bottom(12)
        vbox.set_margin_start(12)
        self.set_child(child=vbox)

        label = Gtk.Label.new(
            str='Drag or use the mouse scroller to change pages.'
        )
        vbox.append(child=label)

        separator = Gtk.Separator.new(orientation=Gtk.Orientation.HORIZONTAL)
        vbox.append(child=separator)

        adw_carousel = Adw.Carousel.new()
        adw_carousel.set_vexpand(True)
        adw_carousel.set_hexpand(True)
        adw_carousel.set_spacing(spacing=24)
        adw_carousel.connect('page-changed', self.on_carousel_page_changed)
        vbox.append(child=adw_carousel)

        # Loop de repetição para criar os widgets.
        for n in range(1, 11):
            page = Gtk.Box.new(
                orientation=Gtk.Orientation.VERTICAL, spacing=12)
            adw_carousel.insert(child=page, position=n)

            label = Gtk.Label.new(str=f'Page {n}')
            page.append(child=label)

        adw_carousel_indicator_dots = Adw.CarouselIndicatorLines.new()
        adw_carousel_indicator_dots.set_carousel(carousel=adw_carousel)
        vbox.append(child=adw_carousel_indicator_dots)

    def on_carousel_page_changed(self, carousel, index):
        print(f'Position: {carousel.get_position()}')
        print(f'índice: {index}')


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
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
