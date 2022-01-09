# -*- coding: utf-8 -*-
"""Script para coletar informações dos widgets (GTK 4)."""

from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='4.0')
from gi.repository import Gtk, GObject


def get_methods_get(widget):
    """Coletar métodos GET.

    Está função coleta os métodos GET disponíveis
    para um determinado widget.

    :param widget: (Gtk.Widget) Widget que se deseja coletar os métodos.
    :return: É retornada uma lista com todos os métodos **get** disponíveis.
    """
    return [metodos for metodos in dir(widget) if metodos.startswith('get_')]


def get_methods_set(widget):
    """Coletar métodos SET.

    Está função coleta os métodos SET disponíveis para um determinado
    widget

    :param widget: (Gtk.Widget) Widget que se deseja coletar os métodos.
    :return: É retornada uma lista com todos os métodos **set** disponíveis.
    """
    return [metodos for metodos in dir(widget) if metodos.startswith('set_')]


def open_template(template='templates/gtk-widgets.txt'):
    with open(template, mode='r') as f:
        # Lendo o conteudo do arquivo.
        template = f.read()
        # Fechando o arquivo que foi aberto.
        f.close()
    return template


def save_data(widget):
    """Método realiza a abertura do arquivo ``template.txt``, o qual
    será preenchido com as informações coletadas e salvo em um outro
    arquivo no formato ``*.md``.
    """
    MAJOR = str(Gtk.MAJOR_VERSION)
    MINOR = str(Gtk.MINOR_VERSION)
    MICRO = str(Gtk.MICRO_VERSION)
    gtk_version = f'Marjor: {MAJOR}. Minor: {MINOR}. Micro: {MICRO}.'
    pygobject_version = GObject.pygobject_version

    widget_name = 'widget.get_name()'
    # Props do widget.
    widget_props = dir(widget.props)
    # Signals do widget.
    widget_signals = GObject.signal_list_names(widget)
    # Métodos get do widget.
    widget_metodos_get = get_methods_get(widget=widget)
    # Métodos set do widget.
    widget_metodos_set = get_methods_set(widget=widget)

    template = open_template()

    path = Path().joinpath('docs', f'gtk-{MAJOR}-widgets-info')
    Path(path).mkdir(parents=True, exist_ok=True)

    file_path = path.joinpath(f'{widget_name}.md')
    with open(file_path, mode='w') as f:
        f.write(
            template.format(
                widget_name,
                gtk_version,
                pygobject_version,
                '\n- '.join(sorted(widget_props)),
                '\n- '.join(sorted(widget_signals)),
                '\n- '.join(sorted(widget_metodos_get)),
                '\n- '.join(sorted(widget_metodos_set)),
            ),
        )
        f.close()


if __name__ == '__main__':
    widget = Gtk.Button()
    save_data(widget=widget)
    print('[!] Concluido [!]')
