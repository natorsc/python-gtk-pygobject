# -*- coding: utf-8 -*-
"""Handy.ViewSwitcherTitle()."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version('Handy', '1')

from gi.repository import Gtk, Gio
from gi.repository import Handy


class MainWindow(Gtk.ApplicationWindow):
    icon_list = ['go-home-symbolic', 'system-search-symbolic',
                 'contact-new-symbolic', 'mail-unread-symbolic']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Handy.ViewSwitcherTitle')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hdy_header_bar = Handy.HeaderBar.new()
        hdy_header_bar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=hdy_header_bar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(widget=vbox)

        stack = Gtk.Stack.new()
        # Definindo o tempo da transição (1000 = 1 segundo).
        stack.set_transition_duration(duration=1000)
        # Definindo o efeito de transição.
        stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )

        # Criando o conteúdo dos stacks.
        for i in range(4):
            page = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            page.set_border_width(border_width=12)

            # Utilizando um laço de repetição para criar alguns botões.
            for n in range(5):
                botao = Gtk.Button.new_with_label(label=f'Botão {n}')
                page.add(botao)

            # Adicionando a página 1 no stack.
            stack.add_titled(child=page, name=f'page_{i}', title=f'Página {i}')
            # Adicionando ícone apenas para ver o comportamento.
            # stack.child_set_property(
            #     child=page,
            #     property_name='icon-name',
            #     value=self.icon_list[i],
            # )

        # Adicionando o stack que contém as páginas no box layout.
        vbox.pack_start(child=stack, expand=True, fill=True, padding=0)

        # Widget que cria as abas.
        hdy_view_switcher_title = Handy.ViewSwitcherTitle.new()
        hdy_view_switcher_title.set_title(title='Handy')
        hdy_view_switcher_title.set_subtitle(subtitle='ViewSwitcherTitle')
        # Alterando a politica para que a barra inferior apareça antes.
        hdy_view_switcher_title.set_policy(policy=Handy.ViewSwitcherPolicy.WIDE)
        hdy_view_switcher_title.set_stack(stack=stack)
        # Monitorando o evento de alteração de visibilidade do título.
        hdy_view_switcher_title.connect('notify::title-visible', self.on_mobile_app)
        # Adicionando o switcher no centro da janela.
        hdy_header_bar.set_custom_title(title_widget=hdy_view_switcher_title)

        hdy_header_bar.pack_end(
            child=Gtk.Button.new_from_icon_name(
                icon_name='open-menu-symbolic', size=Gtk.IconSize.MENU,
            )
        )

        # Barra que será exibida quando a janela do aplicativo estiver pequena.
        self.hdy_view_switcher_bar = Handy.ViewSwitcherBar.new()
        self.hdy_view_switcher_bar.set_policy(policy=Handy.ViewSwitcherPolicy.NARROW)
        self.hdy_view_switcher_bar.set_stack(stack=stack)
        # vbox.pack_end(child=self.hdy_view_switcher_bar, expand=False, fill=True, padding=0)
        vbox.add(widget=self.hdy_view_switcher_bar)

        self.show_all()

    def on_mobile_app(self, widget, param):
        if self.hdy_view_switcher_bar.get_reveal():
            self.hdy_view_switcher_bar.set_reveal(reveal=False)
        else:
            self.hdy_view_switcher_bar.set_reveal(reveal=True)


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
