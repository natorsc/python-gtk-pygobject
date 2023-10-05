# -*- coding: utf-8 -*-
"""Script para coletar informações dos widgets GTK."""

from pathlib import Path

from collections.abc import Callable

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, GObject, Gtk

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE = BASE_DIR.joinpath('templates', 'widget.txt')
OUTPUT = BASE_DIR.joinpath('info')
OUTPUT.mkdir(exist_ok=True)

GTK_VERSION = (
    Gtk.get_major_version(), Gtk.get_minor_version(), Gtk.get_micro_version(),
)
LIBADWAITA_VERSION = (
    Adw.get_major_version(), Adw.get_minor_version(), Adw.get_micro_version(),
)
PYGOBJECT_VERSION = GObject.pygobject_version


def get_methods_get(widget: Gtk.Widget):
    """Coletar métodos GET.

    Função coleta os métodos **get** disponíveis em um determinado widget.

    Args:
        widget (Gtk.Widget): Widget que se deseja coletar os métodos.

    Returns:
        list: Retorna uma lista com todos os métodos **get** disponíveis.
    """
    return [metodos for metodos in dir(widget) if metodos.startswith('get_')]


def get_methods_set(widget: Gtk.Widget):
    """Coletar métodos SET.

    Função coleta os métodos **set** disponíveis em um determinado widget.

    Args:
        widget (Gtk.Widget): Widget que se deseja coletar os métodos.

    Returns:
        list: Retorna uma lista com todos os métodos **set** disponíveis.
    """
    return [metodos for metodos in dir(widget) if metodos.startswith('set_')]


def open_template(template=TEMPLATE):
    with open(template, mode='r') as f:
        template = f.read()
        f.close()
    return template


def save_data(widget: Gtk.Widget):
    """Método realiza a abertura do arquivo ``template.txt``, o qual
    será preenchido com as informações coletadas e salvo em um outro
    arquivo no formato ``*.md``.
    """
    template = open_template()
    widget_name = widget.get_name()

    file_name = OUTPUT.joinpath(f'{widget_name}.md')
    file_name.write_text(
        template.format(
            widget_name=widget_name,
            gtk_version=GTK_VERSION,
            libadwaita_version=LIBADWAITA_VERSION,
            pygobject_version=PYGOBJECT_VERSION,
            widget_props='\n- '.join(sorted(dir(widget.props))),
            widget_signals='\n- '.join(
                sorted(GObject.signal_list_names(widget)),
            ),
            methods_get='\n- '.join(sorted(get_methods_get(widget=widget))),
            methods_set='\n- '.join(sorted(get_methods_set(widget=widget))),
        ),
    )


if __name__ == '__main__':
    widget = Gtk.SearchBar()
    save_data(widget=widget)
    print('[!] Concluido [!]')
