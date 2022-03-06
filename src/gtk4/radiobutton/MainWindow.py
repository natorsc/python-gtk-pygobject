# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.CheckButton() radio button.

No Gtk 4 o RadioButton é um CheckButton que possui um group.
"""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.CheckButton() radio button')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

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
