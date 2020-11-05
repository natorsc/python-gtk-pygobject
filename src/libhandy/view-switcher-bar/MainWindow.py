# -*- coding: utf-8 -*-
"""Handy.ViewSwitcherBar()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.ViewSwitcherBar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(widget=vbox)

        stack = Gtk.Stack.new()
        # Definindo o efeito de transição.
        stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )
        # Definindo o tempo da transição (1000 = 1 segundo).
        stack.set_transition_duration(duration=1000)

        # Página 1.
        page_1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page_1.set_border_width(border_width=12)

        # Utilizando um laço de repetição para criar alguns botões.
        for n in range(5):
            botao = Gtk.Button.new_with_label(label=f'Botão {n}')
            page_1.add(botao)

        # Adicionando a página 1 no Stack Layout.
        stack.add_titled(child=page_1, name='page_1', title='Página 1')

        # Definindo um ícone para a aba da página 1.
        stack.child_set_property(
            child=page_1,
            property_name='icon-name',
            value='changes-allow-symbolic',
        )

        # Página 2.
        page_2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        page_2.set_border_width(border_width=12)

        for n in range(5):
            label = Gtk.Label.new(str=f'Linha {n}')
            page_2.add(widget=label)

        stack.add_titled(child=page_2, name='page_2', title='Página 2')
        stack.child_set_property(
            child=page_2,
            property_name='icon-name',
            value='emblem-synchronizing-symbolic',
        )

        # Adicionando o stack que contém as páginas no box layout.
        vbox.pack_start(child=stack, expand=True, fill=True, padding=0)

        # Widget que cria as abas.
        hdy_view_switcher_bar = Handy.ViewSwitcherBar.new()
        hdy_view_switcher_bar.set_reveal(reveal=True)
        hdy_view_switcher_bar.set_stack(stack=stack)
        vbox.pack_end(child=hdy_view_switcher_bar, expand=False, fill=True, padding=0)

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
