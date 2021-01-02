# -*- coding: utf-8 -*-
"""Script para coletar informações dos widgets.

Informações que são coletadas:

- Versão do GTK+ 3.
- versão do PyGObject.
- Informações sobre o widget:
    - Método.
    - Props.
    - Sinais (signals).

As informações são salvas em um arquivo ``*.md`` no diretório onde o
script é executado.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
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


def save_data():
    """Método realiza a abertura do arquivo ``template.txt``, o qual
    será preenchido com as informações coletadas e salvo em um outro
    arquivo no formato ``*.md``.
    """
    # Abrindo o template.
    with open('template.txt', mode='r') as f:
        # Lendo o conteudo do arquivo.
        template = f.read()
        # Fechando o arquivo que foi aberto.
        f.close()

    # Nome do arquivo *.md.
    filename = ('info-%s.md' % widget_name)
    # Criando o arquivo em modo de escrita.
    with open(filename, mode='w') as arquivo:
        # Preenchedo tempalte com os dados e salvando.
        arquivo.write(template.format(
            widget_name, gtk_versao,
            gtk_versao1, pygobject_versao,
            '\n- '.join(sorted(widget_props)),
            '\n- '.join(sorted(widget_signals)),
            '\n- '.join(sorted(widget_metodos_get)),
            '\n- '.join(sorted(widget_metodos_set)))
        )
        arquivo.close()


if __name__ == '__main__':
    # Widget que se deseja as informações
    widget = Gtk.ListBoxRow()

    # Forma 1 de se coletar a versão do GTK+.
    gtk_versao = '%d.%d.%d' % (Gtk.MAJOR_VERSION, Gtk.MINOR_VERSION,
                               Gtk.MICRO_VERSION)

    # Forma 2 de se coletar a versão do GTK+.
    gtk_versao1 = '%d.%d.%d' % (Gtk.get_major_version(), Gtk.get_minor_version(),
                                Gtk.get_micro_version())

    # Versão do PyGObject.
    pygobject_versao = GObject.pygobject_version

    # Nome do Widget.
    widget_name = widget.get_name()

    # Props do widget.
    widget_props = dir(widget.props)

    # Signals do widget.
    widget_signals = GObject.signal_list_names(widget)

    # Métodos get do widget.
    widget_metodos_get = get_methods_get(widget)

    # Métodos set do widget.
    widget_metodos_set = get_methods_set(widget)

    save_data()

    print('[!] Salvo com sucesso [!]')
