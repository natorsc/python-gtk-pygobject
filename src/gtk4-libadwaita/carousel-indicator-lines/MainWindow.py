# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Adw.CarouselIndicatorLines()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gio, Gtk
from gi.repository import Adw


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Adw.CarouselIndicatorLines()')
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_bottom(12)
        vbox.set_margin_end(12)
        vbox.set_margin_start(12)
        vbox.set_margin_top(12)

        overlay = Gtk.Overlay.new()
        self.set_child(child=overlay)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_margin_bottom(12)
        vbox.set_margin_end(12)
        vbox.set_margin_start(12)
        vbox.set_margin_top(12)
        overlay.add_overlay(widget=vbox)

        label = Gtk.Label.new(str='Arraste com o mouse ou clique nos botões laterais')
        vbox.append(child=label)

        self.adw_carousel = Adw.Carousel.new()
        self.adw_carousel.set_vexpand(True)
        self.adw_carousel.set_spacing(spacing=24)
        self.adw_carousel.connect('page-changed', self.on_page_changed)
        vbox.append(child=self.adw_carousel)

        # Loop de repetição para criar os widgets.
        for n in range(1, 11):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
            self.adw_carousel.insert(child=page, position=n)

            label = Gtk.Label.new(str=f'Página {n}')
            page.append(child=label)

        hdy_carousel_indicator_dots = Adw.CarouselIndicatorLines.new()
        hdy_carousel_indicator_dots.set_carousel(carousel=self.adw_carousel)
        vbox.append(child=hdy_carousel_indicator_dots)

        # Botões para movimentar o carousel.
        button_previous = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
        )
        button_previous.connect('clicked', self.on_button_previous_clicked)
        button_previous.set_halign(align=Gtk.Align.START)
        button_previous.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_previous)

        button_next = Gtk.Button.new_from_icon_name(
            icon_name='go-next-symbolic',
        )
        button_next.connect('clicked', self.on_button_next_clicked)
        button_next.set_halign(align=Gtk.Align.END)
        button_next.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_next)

    def on_page_changed(self, carousel, index):
        print(f'Posição: {carousel.get_position()}')
        print(f'índice: {index}')

    def on_button_previous_clicked(self, button):
        position = self.adw_carousel.get_position()
        if position > 0:
            next_page = self.adw_carousel.get_nth_page(position - 1)
            self.adw_carousel.scroll_to(widget=next_page)

    def on_button_next_clicked(self, button):
        position = self.adw_carousel.get_position()
        pages = self.adw_carousel.get_n_pages()
        if position < (pages - 1):
            next_page = self.adw_carousel.get_nth_page(position + 1)
            self.adw_carousel.scroll_to(widget=next_page)


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
