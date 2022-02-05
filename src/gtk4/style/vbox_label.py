"""Python e GTK 4: PyGObject get_style_context().add_class() Label."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gtk

vbox_label = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)

label = Gtk.Label.new('Label')
vbox_label.append(child=label)

label_monospace = Gtk.Label.new('Label monospace')
label_monospace.get_style_context().add_class(class_name='monospace')
vbox_label.append(child=label_monospace)

label_numeric = Gtk.Label.new('Label numeric (1234567890)')
label_numeric.get_style_context().add_class(class_name='numeric')
vbox_label.append(child=label_numeric)

label_large_title = Gtk.Label.new('Label large-title')
label_large_title.get_style_context().add_class(class_name='large-title')
vbox_label.append(child=label_large_title)

label_title_1 = Gtk.Label.new('Label title-1')
label_title_1.get_style_context().add_class(class_name='title-1')
vbox_label.append(child=label_title_1)

label_accent = Gtk.Label.new('Label accent')
label_accent.get_style_context().add_class(class_name='accent')
vbox_label.append(child=label_accent)

label_success = Gtk.Label.new('Label success')
label_success.get_style_context().add_class(class_name='success')
vbox_label.append(child=label_success)

label_warning = Gtk.Label.new('Label warning')
label_warning.get_style_context().add_class(class_name='warning')
vbox_label.append(child=label_warning)

label_error = Gtk.Label.new('Label error')
label_error.get_style_context().add_class(class_name='error')
vbox_label.append(child=label_error)

label_heading = Gtk.Label.new('Label heading')
label_heading.get_style_context().add_class(class_name='heading')
vbox_label.append(child=label_heading)

label_body = Gtk.Label.new('Label body')
label_body.get_style_context().add_class(class_name='body')
vbox_label.append(child=label_body)

label_caption_heading = Gtk.Label.new('Label caption-heading')
label_caption_heading.get_style_context().add_class(class_name='caption-heading')
vbox_label.append(child=label_caption_heading)

label_caption = Gtk.Label.new('Label caption')
label_caption.get_style_context().add_class(class_name='caption')
vbox_label.append(child=label_caption)
