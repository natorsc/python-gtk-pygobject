# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Calendar()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Calendar()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_homogeneous(homogeneous=True)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        calendar = Gtk.Calendar.new()
        # calendar.connect('day-selected-double-click', self.day_double_click)
        calendar.connect('day-selected', self.day_double_click)
        vbox.append(child=calendar)

    def on_day_selected(self, calendar):
        date = calendar.get_date()
        print(f'Dia: {date.get_day_of_month()}')
        print(f'Mês: {date.get_month()}')
        print(f'Ano: {date.get_year()}')


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
