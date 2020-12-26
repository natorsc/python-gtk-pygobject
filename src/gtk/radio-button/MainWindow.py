# -*- coding: utf-8 -*-
"""Gtk.RadioButton()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, Gio


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Gtk.RadioButton')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        button_box = Gtk.ButtonBox.new(orientation=Gtk.Orientation.VERTICAL)
        button_box.set_layout(Gtk.ButtonBoxStyle.CENTER)
        button_box.set_spacing(spacing=6)
        button_box.set_border_width(border_width=12)
        self.add(widget=button_box)

        radio_button_01 = Gtk.RadioButton.new_with_label(
            group=None,
            label='Radio button 01',
        )
        radio_button_01.connect('toggled', self.on_radiobutton_toggled)
        button_box.add(widget=radio_button_01)

        radio_button_02 = Gtk.RadioButton.new_with_label_from_widget(
            radio_group_member=radio_button_01,
            label='Radio button 02',
        )
        radio_button_02.connect('toggled', self.on_radiobutton_toggled)
        button_box.add(widget=radio_button_02)

        radio_button_03 = Gtk.RadioButton.new_with_label_from_widget(
            radio_group_member=radio_button_01,
            label='Radio button 03',
        )
        radio_button_03.connect('toggled', self.on_radiobutton_toggled)
        button_box.add(widget=radio_button_03)

        radio_button_04 = Gtk.RadioButton.new_with_label_from_widget(
            radio_group_member=radio_button_01,
            label='Radio button 04',
        )
        radio_button_04.connect('toggled', self.on_radiobutton_toggled)
        button_box.add(widget=radio_button_04)

        self.show_all()

    def on_radiobutton_toggled(self, widget):
        if widget.get_active():
            print(f'{widget.get_label()} - MARCADO')
        else:
            print(f'{widget.get_label()} - DESMARCADO')


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
