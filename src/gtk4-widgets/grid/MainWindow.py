# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Grid()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()


class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.Grid()')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=headerbar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('Preferências', 'app.preferences')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        headerbar.pack_end(child=menu_button)

        grid = Gtk.Grid.new()
        grid.set_margin_top(margin=12)
        grid.set_margin_end(margin=12)
        grid.set_margin_bottom(margin=12)
        grid.set_margin_start(margin=12)
        grid.set_row_spacing(spacing=12)
        grid.set_column_spacing(spacing=12)
        self.set_child(child=grid)

        button1 = Gtk.Button.new_with_label(label='Botão 1')
        button2 = Gtk.Button.new_with_label(label='Botão 2')
        button3 = Gtk.Button.new_with_label(label='Botão 3')
        button4 = Gtk.Button.new_with_label(label='Botão 4')
        button5 = Gtk.Button.new_with_label(label='Botão 5')
        button6 = Gtk.Button.new_with_label(label='Botão 6')

        # Adicionando de forma sequencial.
        # grid.add(widget=button1)
        # grid.add(widget=button2)
        # grid.add(widget=button3)
        # grid.add(widget=button4)
        # grid.add(widget=button5)
        # grid.add(widget=button6)

        # Posicionamento utilizando attach()
        # Determinando a posição com base em colunas e linhas.
        # grid.attach(child=button1, left=0, top=0, width=1, height=1)
        # grid.attach(child=button2, left=1, top=0, width=1, height=1)
        # grid.attach(child=button3, left=0, top=1, width=1, height=1)
        # grid.attach(child=button4, left=1, top=1, width=1, height=1)
        # grid.attach(child=button5, left=0, top=2, width=1, height=1)
        # grid.attach(child=button6, left=1, top=2, width=1, height=1)

        # Posicionamento utilizando attach_next_to()
        # Neste posicionamento utilizamos outros widget como referencia.
        # Botão 1 está na coluna 0 e linha 0
        grid.attach(child=button1, column=0, row=0, width=1, height=1)
        # Botão 2 está na coluna 1 e linha 0 e mescla 2 colunas e 1 linha.
        grid.attach(child=button2, column=1, row=0, width=2, height=1)
        # Botão 3 tem como referencia o botão 1, ele deve ficar a baixo do
        # botão 1 (BOTTOM), ele mescla 1 coluna e 2 linhas.
        grid.attach_next_to(
            child=button3,
            sibling=button1,
            side=Gtk.PositionType.BOTTOM,
            width=1, height=2
        )
        # Botão 4 tem como referência o botão 3, ele deve ficar a direita do
        # botão 3 (RIGHT), ele mescla 2 colunas e 1 linha.
        grid.attach_next_to(
            child=button4,
            sibling=button3,
            side=Gtk.PositionType.RIGHT,
            width=2,
            height=1
        )
        # Botão 5 está na coluna 1, linha 2 e mescla 1 coluna e 1 linha.
        grid.attach(child=button5, column=1, row=2, width=1, height=1)
        # Botão 6 tem mo referencia o botão 5, ele deve ficar a direita do
        # botão 5 (RIGHT), ele mescla 1 colunas e 1 linha.
        grid.attach_next_to(
            child=button6,
            sibling=button5,
            side=Gtk.PositionType.RIGHT,
            width=1,
            height=1
        )


class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_preferences_action(self, action, param):
        print('Ação app.preferences foi ativa.')

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
