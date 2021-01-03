# -*- coding: utf-8 -*-
"""Handy.Keypad()."""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio, Pango
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Keypad')
        self.set_resizable(resizable=False)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        self.label = Gtk.Label.new(str='Digite Algo')
        self.label.set_line_wrap(wrap=True)
        self.label.set_line_wrap_mode(wrap_mode=Pango.WrapMode.CHAR)

        self.label.set_max_width_chars(n_chars=20)

        vbox.pack_start(child=self.label, expand=True, fill=True, padding=0)

        entry = Gtk.Entry.new()
        vbox.pack_start(child=entry, expand=False, fill=False, padding=0)

        button = Gtk.Button.new_with_label(label='Clique aqui')
        button.get_style_context().add_class(class_name='suggested-action')
        button.connect('clicked', self.on_button_clicked)

        self.hdy_keypad = Handy.Keypad.new(symbols_visible=True, letters_visible=True)
        self.hdy_keypad.set_entry(entry=entry)
        self.hdy_keypad.set_start_action(start_action=button)
        vbox.pack_end(child=self.hdy_keypad, expand=True, fill=True, padding=0)

        self.show_all()

    def on_button_clicked(self, widget):
        entry = self.hdy_keypad.get_entry()
        self.label.set_text(str=f'{entry.get_text()}')
        print(f'Valor digitado: {entry.get_text()}')


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
