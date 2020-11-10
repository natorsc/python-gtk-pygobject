# -*- coding: utf-8 -*-
"""Handy.Squeezer()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Squeezer')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hdy_header_bar = Handy.HeaderBar.new()
        hdy_header_bar.set_title(title='Handy.ViewSwitcher')
        hdy_header_bar.set_subtitle(subtitle='Handy.ViewSwitcher')
        hdy_header_bar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=hdy_header_bar)

        hdy_squeezer = Handy.Squeezer.new()
        hdy_squeezer.connect("notify", self.on_headerbar_squeezer_notify)
        hdy_header_bar.set_custom_title(title_widget=hdy_squeezer)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(widget=vbox)

        stack = Gtk.Stack.new()
        hdy_header_bar.connect("notify", self.on_headerbar_squeezer_notify)
        stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )
        stack.set_transition_duration(duration=1000)

        # Página 1.
        page_1 = Gtk.Label.new(str='Página 1')
        stack.add_titled(child=page_1, name='page_1', title='Página 1')
        stack.child_set_property(
            child=page_1,
            property_name='icon-name',
            value='changes-allow-symbolic',
        )

        # Página 2.
        page_2 = Gtk.Label.new(str='Página 2')
        stack.add_titled(child=page_2, name='page_2', title='Página 2')
        stack.child_set_property(
            child=page_2,
            property_name='icon-name',
            value='emblem-synchronizing-symbolic',
        )

        vbox.pack_start(child=stack, expand=True, fill=True, padding=0)

        self.hdy_view_switcher_top = Handy.ViewSwitcher.new()
        self.hdy_view_switcher_top.set_stack(stack=stack)
        hdy_squeezer.add(widget=self.hdy_view_switcher_top)

        hdy_view_switcher_bar = Handy.ViewSwitcherBar.new()
        hdy_view_switcher_bar.set_reveal(reveal=True)
        hdy_view_switcher_bar.set_stack(stack=stack)
        vbox.pack_end(child=hdy_view_switcher_bar, expand=False, fill=True, padding=0)

        self.show_all()

    def on_headerbar_squeezer_notify(self, squeezer, event):
        print(squeezer)
        print(event)

        # child = squeezer.get_visible_child()
        # # self.bottom_switcher.set_reveal(child != self.headerbar_switcher)


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
