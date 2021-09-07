# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject internacionalização com gettext()."""

import configparser
import gettext
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk

APPLICATION_ID = 'br.natorsc.Exemplo'

BASE_DIR = Path(__file__).resolve().parent
LOCALES_DIR = BASE_DIR.joinpath('locales')
CONFIG_FILE = BASE_DIR.joinpath('config.ini')

window_title = 'Python e GTK 4: Gtk.ApplicationWindow()'

gettext.bindtextdomain(APPLICATION_ID, LOCALES_DIR)
gettext.textdomain(APPLICATION_ID)
_ = gettext.gettext

config = configparser.ConfigParser()
if CONFIG_FILE.exists():
    config.read(CONFIG_FILE)
    language = config[APPLICATION_ID]['language']
    if language != 'default':
        lang = gettext.translation(APPLICATION_ID, localedir=LOCALES_DIR, languages=[language])
        lang.install()
        _ = lang.gettext


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(
            _('Python e GTK 4: PyGObject internacionalização com gettext().'),
        )
        # Tamanho inicial da janela.
        self.set_default_size(width=1366 / 2, height=768 / 2)
        # Tamanho minimo da janela.
        self.set_size_request(width=1366 / 2, height=768 / 2)

        # O seu código aqui:
        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        vbox.set_margin_bottom(12)
        vbox.set_margin_end(12)
        vbox.set_margin_start(12)
        vbox.set_margin_top(12)
        self.set_child(child=vbox)

        label = Gtk.Label.new()
        label.set_text(_('Após trocar o idioma reinicie o aplicativo.'))
        label.set_vexpand(True)
        vbox.append(child=label)

        combobox_text = Gtk.ComboBoxText()
        combobox_text.append_text(_('Selecione um idioma.'))
        combobox_text.set_active(0)
        combobox_text.connect('changed', self.combobox_text_changed)
        vbox.append(child=combobox_text)

        langs = ['en_US', 'pt_BR']
        for lang in langs:
            combobox_text.append_text(lang)

    def combobox_text_changed(self, combobox):
        row = combobox.get_active()
        if row != 0:
            text = combobox.get_active_text()
            print(f'O idioma selecionado foi: {text}')
            if text == 'pt_BR':
                text = 'default'

            config[APPLICATION_ID] = {'language': text}
            with open(CONFIG_FILE, 'w+') as f:
                config.write(f)
                f.close()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id=APPLICATION_ID,
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
