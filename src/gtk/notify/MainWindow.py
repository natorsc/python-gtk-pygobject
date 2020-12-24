# -*- coding: utf-8 -*-
"""GTK Notify."""

import sys

import gi

gi.require_version(namespace='Gtk', version='3.0')
gi.require_version(namespace='Notify', version='0.7')

from gi.repository import Gio, Gtk, Notify


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='GTK Menu')
        self.set_default_size(width=1366 / 2, height=768 / 2)
        self.set_position(position=Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(filename='../../assets/icons/icon.png')

        self.application_id = kwargs['application'].get_application_id()
        Notify.init(app_name=self.application_id)

        # Criando headerbar.
        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title(title='GTK Notify')
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
        # Variável tem TEM que ter self.
        self.notification = Notify.Notification.new(
            summary='Título do aplicativo',
            body='Texto que será exibido na notificação',
            icon='appointment-soon-symbolic')
        self.notification.set_app_name(app_name=self.application_id)
        self.notification.set_urgency(urgency=Notify.Urgency.NORMAL)
        self.notification.add_action(
            action='123456',
            label='Texto do botão',
            callback=self.notification_callback,
            user_data=widget,
        )
        self.notification.connect('closed', self.on_notification_closed, widget)
        self.notification.show()
        widget.set_sensitive(sensitive=False)

    def on_notification_closed(self, widget, button):
        print('Método é executado SEMPRE que a notificação é fechada.')
        button.set_sensitive(sensitive=True)

    def notification_callback(self, widget, action, button):
        print(widget)
        print(action)
        button.set_sensitive(sensitive=True)


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
    app = Application()
    app.run(sys.argv)
