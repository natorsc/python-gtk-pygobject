"""Python e GTK 4: PyGObject get_style_context().add_class() ProgressBar."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import GLib, Gtk

vbox_progressbar = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)

progressbar = Gtk.ProgressBar.new()
progressbar.set_text(text='ProgressBar')
vbox_progressbar.append(child=progressbar)

progressbar_osd = Gtk.ProgressBar.new()
progressbar.set_text(text='ProgressBar OSD')
progressbar_osd.get_style_context().add_class(class_name='osd')
vbox_progressbar.append(child=progressbar_osd)


def start_progressbar(user_data):
    progressbar.pulse()
    progressbar_osd.pulse()
    # Retornar True para que a execução seja continue.
    return True


timeout_id = GLib.timeout_add(2000, start_progressbar, None)
