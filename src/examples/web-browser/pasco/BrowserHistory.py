# -*- coding: utf-8 -*-
"""."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, GObject, Pango

from models import History


class BrowserHistory(Gtk.Window):
    def __init__(self, session):
        super().__init__()
        self.session = session

        self.set_default_size(width=1366 / 2, height=768 / 2)

        self.headerbar = Gtk.HeaderBar.new()
        self.headerbar.set_title(title='Histórico')
        self.headerbar.set_subtitle(subtitle='de navegação')
        self.headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=self.headerbar)

        btn_clear_history = Gtk.Button.new_with_label(label='Limpar histórico')
        btn_clear_history.get_style_context().add_class(class_name='destructive-action')
        btn_clear_history.connect('clicked', self.on_button_clear_history_clicked)
        self.headerbar.pack_start(child=btn_clear_history)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_end(child=scrolledwindow, expand=True, fill=True, padding=0)

        self.list_store = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])
        for data in self.session.query(History).all():
            self.list_store.append(row=[data.id, data.uri])

        treeview = Gtk.TreeView.new_with_model(model=self.list_store)
        scrolledwindow.add(widget=treeview)

        cols = ('ID', 'URI')
        for i, col in enumerate(cols):
            cellrender = Gtk.CellRendererText.new()
            if i == 0:
                cellrender.props.weight_set = True
                cellrender.props.weight = Pango.Weight.BOLD
            treeviewcolumn = Gtk.TreeViewColumn(
                title=col,
                cell_renderer=cellrender,
                text=i,
            )
            treeview.append_column(column=treeviewcolumn)

        self.show_all()

    def on_button_clear_history_clicked(self, widget):
        self.session.query(History).delete()
        self.session.commit()
        self.list_store.clear()
