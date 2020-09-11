# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo do tipo ``txt`` com um texto
qualquer.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./MessageDialogError.ui')
class MessageDialogError(Gtk.MessageDialog):
    __gtype_name__ = 'MessageDialogError'

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    pass
