# -*- coding: utf-8 -*-
"""Container do tipo Stack Layout com StackSidebar.

Neste tipo de container cada novo widget adicionado ao Stack layout
gera uma nova página que pode ser acessada utilizando-se o
StackSidebar().

Importante notar que Stack Layout e StackSidebar Layout devem ser
utilizado juntos, pois:

- Stack irá criar novas página para cada widget que adicionamos a ele.
- StackSidebar irá realizar a troca entre as páginas que são criadas
pelo stack.

É mais comum a utilização de um box layout horizontal com o
StackSidebar.
"""
import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Stack Layout com StackSidebar')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox.set_border_width(border_width=12)
        self.add(widget=hbox)

        page1 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Utilizando um laço de repetição para criar alguns botões.
        for n in range(5):
            button = Gtk.Button.new_with_label(label=f'Botão {n}')
            page1.add(widget=button)

        page2 = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        for n in range(5):
            label = Gtk.Label.new(str=f'Linha {n}')
            page2.add(widget=label)

        stack = Gtk.Stack.new()
        # Definindo o efeito de transição.
        stack.set_transition_type(
            transition=Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        )
        # Definindo o tempo da transição (1000 = 1 segundo).
        stack.set_transition_duration(duration=1000)
        stack.add_titled(child=page1, name='pagina1', title='Página 1')
        stack.add_titled(child=page2, name='pagina2', title='Página 2')
        hbox.pack_end(child=stack, expand=True, fill=True, padding=0)

        # Criando StackSwitcher Layout.
        # Este container é responsável por realizar as trocas.
        stack_sidebar = Gtk.StackSidebar.new()

        # Adicionando o Stack Layout que contém os
        # widgets (Páginas) No StackSwitcher Layout.
        stack_sidebar.set_stack(stack=stack)

        # Adicionando o StackSwitcher Layout no Box Layout principal.
        hbox.pack_start(child=stack_sidebar, expand=False, fill=False, padding=0)

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
    app = Application()
    app.run(sys.argv)
