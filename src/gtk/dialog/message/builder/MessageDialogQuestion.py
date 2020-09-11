# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo do tipo ``txt`` com um texto
qualquer.
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./MessageDialogQuestion.glade')
class MessageDialogQuestion(Gtk.MessageDialog):
    __gtype_name__ = 'MessageDialogQuestion'

    btn_yes = Gtk.Template.Child(name='btn_yes')
    bnt_no = Gtk.Template.Child(name='bnt_no')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Adicionando class action nos botões.
        self.btn_yes.get_style_context().add_class(class_name='suggested-action')
        self.btn_no.get_style_context().add_class(class_name='destructive-action')




if __name__ == '__main__':
    pass
