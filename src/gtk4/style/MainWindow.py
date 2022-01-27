# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.ApplicationWindow()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, Gtk

from vbox_entry import vbox_entry


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.ApplicationWindow()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        headerbar = Gtk.HeaderBar.new()
        headerbar.set_show_title_buttons(setting=True)
        self.set_titlebar(titlebar=headerbar)

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        # vbox.set_homogeneous(homogeneous=True)
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        self.set_child(child=vbox)

        # vbox_entry = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # entry = Gtk.Entry.new()
        # entry.set_placeholder_text('Entry')
        # vbox_entry.append(child=entry)
        #
        # entry_success = Gtk.Entry.new()
        # entry_success.set_placeholder_text('Entry success')
        # entry_success.get_style_context().add_class(class_name='success')
        # vbox_entry.append(child=entry_success)
        #
        # entry_error = Gtk.Entry.new()
        # entry_error.set_placeholder_text('Entry error')
        # entry_error.get_style_context().add_class(class_name='error')
        # vbox_entry.append(child=entry_error)
        #
        # entry_warning = Gtk.Entry.new()
        # entry_warning.set_placeholder_text('Entry warning')
        # entry_warning.get_style_context().add_class(class_name='warning')
        # vbox_entry.append(child=entry_warning)

        stack = Gtk.Stack.new()
        stack.add_titled(child=vbox_entry, name='entry', title='Entry')
        # stack.add_titled(child=page1, name='button', title='Button')
        # stack.add_titled(child=page1, name='progressbar', title='ProgressBar')
        vbox.append(child=stack)

        stack_switcher = Gtk.StackSwitcher.new()
        stack_switcher.set_stack(stack=stack)
        headerbar.set_title_widget(title_widget=stack_switcher)

        # O seu código aqui:
    #     label = Gtk.Label.new('Label')
    #     vbox.append(child=label)
    #
    #     label_monospace = Gtk.Label.new('Label monospace')
    #     label_monospace.get_style_context().add_class(class_name='monospace')
    #     vbox.append(child=label_monospace)
    #
    #     label_numeric = Gtk.Label.new('Label numeric (1234567890)')
    #     label_numeric.get_style_context().add_class(class_name='numeric')
    #     vbox.append(child=label_numeric)
    #
    #     entry = Gtk.Entry.new()
    #     entry.set_placeholder_text('Entry')
    #     vbox.append(child=entry)
    #
    #     entry_success = Gtk.Entry.new()
    #     entry_success.set_placeholder_text('Entry success')
    #     entry_success.get_style_context().add_class(class_name='success')
    #     vbox.append(child=entry_success)
    #
    #     entry_error = Gtk.Entry.new()
    #     entry_error.set_placeholder_text('Entry error')
    #     entry_error.get_style_context().add_class(class_name='error')
    #     vbox.append(child=entry_error)
    #
    #     entry_warning = Gtk.Entry.new()
    #     entry_warning.set_placeholder_text('Entry warning')
    #     entry_warning.get_style_context().add_class(class_name='warning')
    #     vbox.append(child=entry_warning)
    #
    #     button = Gtk.Button.new_with_label(label='Botão')
    #     vbox.append(child=button)
    #
    #     button_flat = Gtk.Button.new_with_label(label='Botão flat')
    #     button_flat.get_style_context().add_class(class_name='flat')
    #     vbox.append(child=button_flat)
    #
    #     button_destructive_action = Gtk.Button.new_with_label(label='Botão destructive action')
    #     button_destructive_action.get_style_context().add_class(class_name='destructive-action')
    #     vbox.append(child=button_destructive_action)
    #
    #     button_suggested_action = Gtk.Button.new_with_label(label='Botão suggested action')
    #     button_suggested_action.get_style_context().add_class(class_name='suggested-action')
    #     vbox.append(child=button_suggested_action)
    #
    #     button_opaque = Gtk.Button.new_with_label(label='Botão opaque')
    #     button_opaque.get_style_context().add_class(class_name='opaque')
    #     vbox.append(child=button_opaque)
    #
    #     button_circular = Gtk.Button.new_with_label(label='Botão circular')
    #     button_circular.get_style_context().add_class(class_name='circular')
    #     vbox.append(child=button_circular)
    #
    #     button_pill = Gtk.Button.new_with_label(label='Botão pill')
    #     button_pill.set_halign(align=Gtk.Align.CENTER)
    #     button_pill.set_valign(align=Gtk.Align.CENTER)
    #     button_pill.get_style_context().add_class(class_name='pill')
    #     vbox.append(child=button_pill)
    #
    #     self.progressbar = Gtk.ProgressBar.new()
    #     vbox.append(child=self.progressbar)
    #
    #     self.progressbar_osd = Gtk.ProgressBar.new()
    #     self.progressbar_osd.get_style_context().add_class(class_name='osd')
    #     vbox.append(child=self.progressbar_osd)
    #
    #     self.timeout_id = GLib.timeout_add(2000, self.start_progressbar, None)
    #
    # def start_progressbar(self, user_data):
    #     self.progressbar.pulse()
    #     self.progressbar_osd.pulse()
    #     # Retornar True para que a execução seja continue.
    #     return True


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
