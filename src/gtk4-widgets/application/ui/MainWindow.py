# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.Application() ui file."""

import subprocess
import sys
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gio, Gtk

Adw.init()

BASE_DIR = Path(__file__).resolve().parent
FILENAME = str(BASE_DIR.joinpath('MainWindow.ui'))

# Não utilizar no Gnome Builder. Configurar via meson.
# [!] O Compilador Blueprint deve estar instalado [!].
if sys.platform == 'linux':
    for data in BASE_DIR.iterdir():
        if data.is_file() and data.suffix == '.blp':
            subprocess.run(
                args=['blueprint-compiler', 'compile', f'{data}', '--output',
                      f'{BASE_DIR.joinpath(data.stem)}.ui'],
            )


# Acessando o arquivo de inteface.
@Gtk.Template(filename=FILENAME)
class ExampleWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'ExampleWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # O seu código aqui:
        # ...


# Essa classe pode ser colocada em um arquivo separado (main.py).
class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='br.com.justcode.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        # Ações do Menu.
        # `<primary>q` = `Ctrl + q`.
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
        """Callback para a ação `app.preferences` do arquivo de interface."""
        print('Ação app.preferences foi ativa.')

    def exit_app(self, action, param):
        """Callback é executado quando as teclas de atalho `Ctrl + q` são
        pressionadas."""
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        """Adiciona uma ação (action) no aplicativo.

        Args:
            name (str): Nome da ação (action).
            callback (def): Função que será chamada quando a ação for ativa.
            shortcuts (list[str]): Lista de atalhos que acionam a ação.
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)
