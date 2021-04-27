# -*- coding: utf-8 -*-
"""Gio.Notification() com Gio.Application().

No Microsoft Windows é exibido:

```bash
(MainWindow.py:6376): GLib-GIO-WARNING **: 15:10:59.027: Notifications are not yet supported on Windows.
```
"""

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='Notify', version='0.7')

from gi.repository import Gio, Gtk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = kwargs['application']

        self.set_title(title='Gio.Notification')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='Gio Notification')
        headerbar.set_subtitle(subtitle='Exibindo notificações.')
        headerbar.set_show_close_button(setting=True)
        self.set_titlebar(titlebar=headerbar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_border_width(border_width=12)
        self.add(widget=vbox)

        self.button = Gtk.Button.new_with_label(label='Abrir notificação')
        self.button.connect('clicked', self.show_notification)
        vbox.pack_start(child=self.button, expand=False, fill=False, padding=0)

        self.show_all()

    def show_notification(self, widget):
        notification = Gio.Notification.new(title='Título do aplicativo')
        self.application.send_notification(None, notification)


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='br.natorsc.Exemplo',
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
