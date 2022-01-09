# -*- coding: utf-8 -*-
"""Python e GTK 4: PyGObject Gtk.EntryCompletion()."""

import gi

gi.require_version(namespace='Gtk', version='4.0')

from gi.repository import Gio, GObject, Gtk


class MainWindow(Gtk.ApplicationWindow):
    brazilian_states = [
        (1, 'Acre'), (2, 'Alagoas'), (3, 'Amapá'), (4, 'Amazonas'),
        (5, 'Bahia'), (6, 'Ceará'), (7, 'Distrito Federal'), (8, 'Espírito Santo'),
        (9, 'Goiás'), (10, 'Maranhão'), (11, 'Mato Grosso'), (12, 'Mato Grosso do Sul'),
        (13, 'Minas Gerais'), (14, 'Pará'), (15, 'Paraíba'), (16, 'Paraná'),
        (17, 'Pernambuco'), (18, 'Piauí'), (19, 'Rio de Janeiro'),
        (20, 'Rio Grande do Norte'), (21, 'Rio Grande do Sul'), (22, 'Rondônia'),
        (23, 'Roraima'), (24, 'Santa Catarina'), (25, 'São Paulo'), (26, 'Sergipe'),
        (27, 'Tocantins'),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Python e GTK 4: PyGObject Gtk.EntryCompletion()')
        # Tamanho inicial da janela.
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        # Tamanho minimo da janela.
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        # No GTK 3: set_border_width().
        vbox.set_margin_top(margin=12)
        vbox.set_margin_end(margin=12)
        vbox.set_margin_bottom(margin=12)
        vbox.set_margin_start(margin=12)
        # Adicionando o box na janela principal.
        # No GTK 3: add().
        self.set_child(child=vbox)

        label = Gtk.Label.new(str='Digite o nome de algum estado brasileiro:')
        vbox.append(child=label)

        liststore = Gtk.ListStore.new([GObject.TYPE_INT, GObject.TYPE_STRING])

        for state in self.brazilian_states:
            # insert_with_values(position:int, columns:list, values:list).
            liststore.insert_with_values(
                position=state[0],
                columns=(1,),
                values=[state[1]],
            )

        completion = Gtk.EntryCompletion.new()
        completion.set_model(model=liststore)
        completion.set_text_column(column=1)

        entry = Gtk.Entry.new()
        entry.set_completion(completion=completion)
        vbox.append(child=entry)


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
