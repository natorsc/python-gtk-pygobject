# -*- coding: utf-8 -*-
"""webkit.WebView().

sudo apt install gir1.2-webkit2-4.0
"""

import gi

gi.require_version(namespace='Gdk', version='3.0')
gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='WebKit2', version='4.0')

from gi.repository import Gdk, Gtk, GObject, WebKit2

from models import Favorite, History, Session

from BrowserHistory import BrowserHistory
from BrowserSettings import BrowserSettings
from BrowserFavorite import BrowserFavorite


class MainWindow(Gtk.ApplicationWindow):
    session = Session()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title(title='Pasco')
        display = Gdk.Display.get_default()
        primary_monitor = Gdk.Display.get_primary_monitor(display)
        monitor_geometry = primary_monitor.get_geometry()
        monitor_width = monitor_geometry.width
        monitor_height = monitor_geometry.height
        self.set_default_size(width=monitor_width / 1.2, height=monitor_height / 1.2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='icons/icon.png')
        self.connect('scroll-event', self.on_page_scrool)

        self.headerbar = Gtk.HeaderBar.new()
        self.headerbar.set_title(title='Pasco')
        self.headerbar.set_subtitle(subtitle='Bem vindo')
        self.headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=self.headerbar)

        hbox_headerbar_left = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.headerbar.pack_start(child=hbox_headerbar_left)

        hbox_headerbar_right = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.headerbar.pack_end(child=hbox_headerbar_right)

        btn_back = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        btn_back.connect('clicked', self.on_btn_back_clicked)
        # hbox_headerbar_left.pack_start(child=btn_back, expand=False, fill=True, padding=0)
        self.headerbar.pack_start(child=btn_back)

        btn_reload = Gtk.Button.new_from_icon_name(
            icon_name='view-refresh-symbolic',
            size=Gtk.IconSize.BUTTON
        )
        btn_reload.connect('clicked', self.on_btn_reload_clicked)
        # hbox_headerbar_left.pack_start(child=btn_reload, expand=False, fill=True, padding=6)
        self.headerbar.pack_start(child=btn_reload)

        btn_forward = Gtk.Button.new_from_icon_name(
            icon_name='go-previous-symbolic-rtl',
            size=Gtk.IconSize.BUTTON
        )
        btn_forward.connect('clicked', self.on_btn_forward_clicked)
        # hbox_headerbar_left.pack_start(child=btn_forward, expand=False, fill=True, padding=0)
        self.headerbar.pack_start(child=btn_forward)

        ##########
        self.liststore = Gtk.ListStore.new([GObject.TYPE_STRING])

        self.completion = Gtk.EntryCompletion.new()
        self.completion.set_match_func(self.entry_completion_match_func)
        self.completion.connect('match-selected', self.cursor_on_match)
        self.completion.set_model(model=self.liststore)
        self.completion.set_text_column(column=0)



        img_btn_menu = Gtk.Image.new_from_icon_name(
            icon_name='open-menu-symbolic',
            size=Gtk.IconSize.MENU,
        )
        btn_open_menu_popover = Gtk.MenuButton.new()
        btn_open_menu_popover.add(widget=img_btn_menu)
        # hbox_headerbar_right.pack_end(child=btn_open_menu_popover, expand=False, fill=True, padding=0)
        self.headerbar.pack_end(child=btn_open_menu_popover)

        vbox_popover = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox_popover.set_border_width(border_width=6)
        popover_menu = Gtk.Popover.new(relative_to=btn_open_menu_popover)
        popover_menu.add(widget=vbox_popover)
        btn_open_menu_popover.set_popover(popover=popover_menu)

        btn_open_cnf = Gtk.ModelButton.new()
        btn_open_cnf.set_label(label='Configurações')
        btn_open_cnf.connect('clicked', self.on_btn_open_cnf_clicked)
        vbox_popover.pack_start(child=btn_open_cnf, expand=False, fill=True, padding=0)

        btn_open_favorite = Gtk.ModelButton.new()
        btn_open_favorite.set_label(label='Favoritos')
        btn_open_favorite.connect('clicked', self.on_btn_open_favorite_clicked)
        vbox_popover.pack_start(child=btn_open_favorite, expand=False, fill=True, padding=0)

        btn_open_history = Gtk.ModelButton.new()
        btn_open_history.set_label(label='Histórico')
        btn_open_history.connect('clicked', self.on_btn_open_history_clicked)
        vbox_popover.pack_start(child=btn_open_history, expand=False, fill=True, padding=0)

        entry_uri = Gtk.Entry.new()
        entry_uri.set_completion(completion=self.completion)
        entry_uri.set_hexpand(expand=True)
        entry_uri.set_icon_from_icon_name(
            icon_pos=Gtk.EntryIconPosition.SECONDARY,
            icon_name='emblem-favorite-symbolic',
        )
        entry_uri.connect('activate', self.on_entry_activate)
        entry_uri.connect('changed', self.entry_uri_history)
        entry_uri.connect('icon-press', self.on_icon_favorite_clicked)
        # hbox_headerbar_right.pack_start(child=entry_uri, expand=False, fill=True, padding=6)
        self.headerbar.pack_end(child=entry_uri)

        self.web_view = WebKit2.WebView.new()
        self.web_view.load_uri(uri='http://127.0.0.1:8000')
        self.web_view.connect('notify::title', self.notify_title)
        self.add(widget=self.web_view)

        popover_menu.show_all()

        self.show_all()

    def on_icon_favorite_clicked(self, widget, enum, event_button):
        title = self.web_view.get_title()
        uri = self.web_view.get_uri()
        if not self.session.query(Favorite).filter_by(uri=uri).first():
            favorite = Favorite(title=title, uri=uri)
            self.session.add(favorite)
            self.session.commit()

    def on_btn_open_favorite_clicked(self, widget):
        browser_favorite = BrowserFavorite(session=self.session)
        browser_favorite.set_transient_for(parent=self)

    def on_btn_open_history_clicked(self, widget):
        browser_history = BrowserHistory(session=self.session)
        browser_history.set_transient_for(parent=self)

    def cursor_on_match(self, widget, list_store, tree_iter):
        self.web_view.load_uri(uri=list_store[tree_iter][0])

    def entry_completion_match_func(self, widget, key, iter):
        return True

    def entry_uri_history(self, widget):
        entry_text = widget.get_text()

        if entry_text:
            rows = self.session.query(History).filter(History.uri.ilike(f'%{entry_text}%')).all()
            self.liststore.clear()
            for row in rows:
                self.liststore.append(row=[row.uri])
        else:
            self.liststore.clear()

    def on_btn_open_cnf_clicked(self, widget):
        settings = BrowserSettings()
        settings.set_transient_for(parent=self)

    def on_page_scrool(self, widget, event_scroll):
        if event_scroll.direction == Gdk.ScrollDirection.DOWN:
            self.headerbar.hide()
        elif event_scroll.direction == Gdk.ScrollDirection.UP:
            self.headerbar.show()

    def notify_title(self, widget, g_param_string):
        self.headerbar.set_subtitle(subtitle=widget.get_title())

    def on_btn_back_clicked(self, widget):
        if self.web_view.can_go_back():
            self.web_view.go_back()

    def on_btn_reload_clicked(self, widget):
        self.web_view.reload()

    def on_btn_forward_clicked(self, widget):
        if self.web_view.can_go_forward():
            self.web_view.go_forward()

    def on_entry_activate(self, widget):
        uri = widget.get_text()
        if uri.startswith('http://') or uri.startswith('https://'):
            self.web_view.load_uri(uri=uri)
        else:
            uri = f'https://{uri}'
            self.web_view.load_uri(uri=uri)
        if not self.session.query(History).filter_by(uri=uri).first():
            history = History(uri=uri)
            self.session.add(history)
            self.session.commit()
