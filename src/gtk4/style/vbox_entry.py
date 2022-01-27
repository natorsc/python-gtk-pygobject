"""Python e GTK 4: PyGObject Gtk.Style() Entry."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk

vbox_entry = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
entry = Gtk.Entry.new()
entry.set_placeholder_text('Entry')
vbox_entry.append(child=entry)

entry_success = Gtk.Entry.new()
entry_success.set_placeholder_text('Entry success')
entry_success.get_style_context().add_class(class_name='success')
vbox_entry.append(child=entry_success)

entry_error = Gtk.Entry.new()
entry_error.set_placeholder_text('Entry error')
entry_error.get_style_context().add_class(class_name='error')
vbox_entry.append(child=entry_error)

entry_warning = Gtk.Entry.new()
entry_warning.set_placeholder_text('Entry warning')
entry_warning.get_style_context().add_class(class_name='warning')
vbox_entry.append(child=entry_warning)
