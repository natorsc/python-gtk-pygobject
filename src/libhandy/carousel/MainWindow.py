# -*- coding: utf-8 -*-
"""Handy.Carousel()."""
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Carousel')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        label = Gtk.Label.new(str='Arraste com o mouse')
        vbox.pack_start(child=label, expand=False, fill=True, padding=0)

        hdy_carousel = Handy.Carousel.new()
        hdy_carousel.set_spacing(spacing=100)
        vbox.pack_end(child=hdy_carousel, expand=True, fill=True, padding=0)

        # Loop de repetição para criar os widgets.
        for n in range(10):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)

            label = Gtk.Label.new(str=f'Página {n}')
            page.pack_start(child=label, expand=True, fill=True, padding=0)
            hdy_carousel.insert(child=page, position=n)

        self.show_all()


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
