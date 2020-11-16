# -*- coding: utf-8 -*-
"""Handy.Deck()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    # Variável auxiliar
    deck_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.Deck')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        overlay = Gtk.Overlay.new()
        self.add(widget=overlay)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        overlay.add_overlay(widget=vbox)

        label = Gtk.Label.new(str='Não sei implementar.')
        vbox.pack_start(child=label, expand=False, fill=True, padding=0)

        hdy_deck = Handy.Deck.new()
        hdy_deck.set_can_swipe_back(can_swipe_back=True)
        hdy_deck.set_can_swipe_forward(can_swipe_forward=True)
        hdy_deck.set_transition_duration(duration=1000)
        vbox.pack_start(child=hdy_deck, expand=True, fill=True, padding=0)

        # Loop de repetição para criar os widgets.
        for n in range(10):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)

            label = Gtk.Label.new(str=f'Página {n}')
            page.pack_start(child=label, expand=True, fill=True, padding=0)

            # Adicionando os widgets a uma lista.
            self.deck_list.append(page)
            hdy_deck.add(widget=page)

        # Botões para movimentar o carousel.
        button_previous = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON,
        )
        button_previous.connect(
            'clicked',
            self.on_button_previous_clicked,
            hdy_deck,
        )
        button_previous.set_halign(align=Gtk.Align.START)
        button_previous.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_previous)

        button_next = Gtk.Button.new_from_icon_name(
            icon_name='go-next-symbolic',
            size=Gtk.IconSize.BUTTON,
        )
        button_next.connect(
            'clicked',
            self.on_button_next_clicked,
            hdy_deck,
        )
        button_next.set_halign(align=Gtk.Align.END)
        button_next.set_valign(align=Gtk.Align.CENTER)
        overlay.add_overlay(widget=button_next)

        self.show_all()

    def on_button_previous_clicked(self, button, deck):
        deck.set_visible_child(visible_child=self.deck_list[0])

    def on_button_next_clicked(self, button, deck):
        deck.set_visible_child(visible_child=self.deck_list[1])


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
