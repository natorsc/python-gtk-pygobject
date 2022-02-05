"""Python e GTK 4: PyGObject get_style_context().add_class() Button."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk

vbox_button = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)

button = Gtk.Button.new_with_label(label='Botão')
vbox_button.append(child=button)

button_flat = Gtk.Button.new_with_label(label='Botão flat')
button_flat.get_style_context().add_class(class_name='flat')
vbox_button.append(child=button_flat)

button_destructive_action = Gtk.Button.new_with_label(label='Botão destructive action')
button_destructive_action.get_style_context().add_class(class_name='destructive-action')
vbox_button.append(child=button_destructive_action)

button_suggested_action = Gtk.Button.new_with_label(label='Botão suggested action')
button_suggested_action.get_style_context().add_class(class_name='suggested-action')
vbox_button.append(child=button_suggested_action)

button_opaque = Gtk.Button.new_with_label(label='Botão opaque')
button_opaque.get_style_context().add_class(class_name='opaque')
vbox_button.append(child=button_opaque)

button_circular = Gtk.Button.new_with_label(label='Botão Circular')
button_circular.set_halign(align=Gtk.Align.CENTER)
button_circular.set_valign(align=Gtk.Align.CENTER)
button_circular.get_style_context().add_class(class_name='circular')
vbox_button.append(child=button_circular)

button_pill = Gtk.Button.new_with_label(label='Botão pill')
button_pill.set_halign(align=Gtk.Align.CENTER)
button_pill.set_valign(align=Gtk.Align.CENTER)
button_pill.get_style_context().add_class(class_name='pill')
vbox_button.append(child=button_pill)
