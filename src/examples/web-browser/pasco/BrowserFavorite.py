# -*- coding: utf-8 -*-
"""."""

import gi

gi.require_version(namespace='Gtk', version='3.0')

from gi.repository import Gtk, GObject, Pango

from models import Favorite


class BrowserFavorite(Gtk.Window):
    def __init__(self, session):
        super().__init__()
        self.session = session

        self.set_default_size(width=1366 / 2, height=768 / 2)

        self.headerbar = Gtk.HeaderBar.new()
        self.headerbar.set_title(title='Editar')
        self.headerbar.set_subtitle(subtitle='favoritos')
        self.headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=self.headerbar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        scrolledwindow = Gtk.ScrolledWindow.new()
        vbox.pack_end(child=scrolledwindow, expand=True, fill=True, padding=0)

        self.list_store = Gtk.ListStore.new(
            [GObject.TYPE_INT, GObject.TYPE_STRING, GObject.TYPE_STRING],
        )
        for data in self.session.query(Favorite).all():
            self.list_store.append(row=[data.id, data.title, data.uri])

        treeview = Gtk.TreeView.new_with_model(model=self.list_store)
        scrolledwindow.add(widget=treeview)
        cols = ('ID', 'Título', 'URI')
        for i, col in enumerate(cols):
            cellrender = Gtk.CellRendererText.new()
            cellrender.props.editable = True
            cellrender.connect('edited', self.on_cell_edited, i)
            if i == 0:
                cellrender.props.editable = False
                cellrender.props.weight_set = True
                cellrender.props.weight = Pango.Weight.BOLD
            treeviewcolumn = Gtk.TreeViewColumn(
                title=col,
                cell_renderer=cellrender,
                text=i,
            )
            treeview.append_column(column=treeviewcolumn)

        self.show_all()

    def on_cell_edited(self, widget, row, value, column):
        row_id = self.list_store[row][0]
        keys = Favorite.__table__.columns.keys()
        data = {keys[column]: value}
        self.list_store[row][column] = value
        self.session.query(Favorite).filter_by(id=row_id).update(data)
        self.session.commit()
