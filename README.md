[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Please do not theme this app](https://stopthemingmy.app/badge.svg)](https://stopthemingmy.app)

# Criando interfaces gráficas com Python (PyGObject) e GTK

Repositório com diversos exemplos de código e alguns tutoriais sobre a construção de interfaces gráficas com a linguagem
de programão Python e o toolkit gráfico GTK.

## O que estou publicando?

A ideia é apenas **estudar** e documentar a construção de interfaces gráficas com a linguagem de programação Python e o
toolkit para construção de interfaces gráficas GTK.

> **OBS**: Em caso de problemas entre em contato para que o material possa ser melhorado.

---

## GTK

O GTK é um toolkit multiplataforma para a criação de interfaces gráficas.

O mesmo utiliza licença GNU LGPL, o que permite a sua utilização para construção de softwares que sejam livres ou
proprietários.

Foi desenvolvido inicialmente para o GIMP (GNU Image Manipulation Program), por isso foi batizado de GIMP Toolkit ou
simplesmente GTK.

Originalmente criado por, Peter Mattis, Spencer Kimball e Josh MacDonald.

O GTK é comumente utilizado na elaboração de aplicativos para o ambiente de desktop GNOME, contudo por ser
multiplataforma pode ser executado sem problemas em diversos sistemas operacionais e ambientes gráficos.

O toolkit é escrito em C e o seu design é orientado a objeto com base no sistema de objetos da biblioteca GLib.

Existe o suporte a diversas linguagens de programação (bindings), contudo as linguagem que são suportadas oficialmente (
até o momento que escrevo) são:

- C++.
- C#.
- C.
- JavaScript.
- Python.
- Rust.
- Vala.

As diretrizes de estilo do GNOME (HIG) podem ser vistas em:

- [https://developer.gnome.org/hig/](https://developer.gnome.org/hig/).

---

## Tutoriais 🤓

- [https://blog.codigoninja.dev/](https://blog.codigoninja.dev/).

---

## [GTK 3](./docs/gtk3-index.md)

## [GTK 3 Libhandy](./docs/gtk3-libhandy-index.md)

> 📝 Conteúdo não está mais sendo atualizado. Focando no GTK 4.

---

## Arquitetura

### Gtk 4

![Arquitetura do GTK 4](./docs/images/gtk4/gtk-architecture.webp)

#### bibliotecas:

##### [GLib](https://docs.gtk.org/glib/)

GLib é uma biblioteca central de baixo nível que forma a base do GTK. Ele fornece manipulação de estrutura de dados para C, wrappers de portabilidade e interfaces para funcionalidade de tempo de execução como um loop de eventos, threads, carregamento dinâmico e um sistema de objetos.

##### [Pango](https://docs.gtk.org/Pango/)

Pango é uma biblioteca para layout e renderização de texto com ênfase na internacionalização. Ele forma o núcleo do manuseio de texto e fonte para GTK.

##### [Cairo](https://www.cairographics.org/)

Cairo é uma biblioteca para gráficos 2D com suporte para vários dispositivos de saída (incluindo o X Window System, Win32) ao mesmo tempo em que produz uma saída consistente em todas as mídias, aproveitando a aceleração do hardware de exibição quando disponível.

##### [GdkPixbuf](https://docs.gtk.org/gdk-pixbuf)

GdkPixbuf é uma biblioteca para carregar ativos gráficos como ícones em vários formatos, como PNG, JPEG e GIF.

##### [ATK](https://docs.gtk.org/atk/)

ATK é uma biblioteca para um conjunto de interfaces que fornecem acessibilidade. Ao suportar as interfaces ATK, um aplicativo ou kit de ferramentas pode ser usado com ferramentas como leitores de tela, ampliadores e dispositivos de entrada alternativos.

---

## GTK 4

> 🚜 Em construção 🏭.

![Python e GTK4: Gtk.ApplicationWindow](./docs/images/gtk4/gtk-4-pygobject-applicationwindow.webp)

O GTK 4 foi lançado em 16 de dezembro 2020.

No GTK 4 é desencorajado o uso do Gnome Glade, isso porque o Gnome Builder fornece uma forma padronizada e moderna de se
criar e gerenciar os projetos.

### Widgets

- [Gtk.ActionBar](./docs/gtk4-widgets.md#gtk-actionbar).
- [Gtk.ApplicationWindow](./docs/gtk4-widgets.md#gtk-applicationwindow).
- [Gtk.Box (horizontal)](./docs/gtk4-widgets.md#gtk-box-horizontal).
- [Gtk.Box (vertical)](./docs/gtk4-widgets.md#gtk-box-vertical).
- [Gtk.Button](./docs/gtk4-widgets.md#gtk-button).
- [Gtk.Calendar](./docs/gtk4-widgets.md#gtk-calendar).
- [Gtk.CheckButton](./docs/gtk4-widgets.md#gtk-checkbutton).
- [Gtk.ComboBoxText](./docs/gtk4-widgets.md#gtk-comboboxtext).
- [Gtk.Dialog](./docs/gtk4-widgets.md#gtk-dialog).
- [Gtk.DragAndDrop (Gtk.DragSource e Gtk.DropTarget)](./docs/gtk4-widgets.md#gtk-drag-and-drop).
- [Gtk.Entry](./docs/gtk4-widgets.md#gtk-entry).
- [Gtk.EntryCompletion](./docs/gtk4-widgets.md#gtk-entrycompletion).
- [Gtk.FileChooserDialog (folder)](./docs/gtk4-widgets.md#gtk-filechooserdialog-folder).
- [Gtk.FileChooserDialog (open)](./docs/gtk4-widgets.md#gtk-filechooserdialog-open).
- [Gtk.FileChooserDialog (save)](./docs/gtk4-widgets.md#gtk-filechooserdialog-save).
- [Gtk.Fixed](./docs/gtk4-widgets.md#gtk-fixed).
- [Gtk.FlowBox](./docs/gtk4-widgets.md#gtk-flowbox).
- [Gtk.Grid](./docs/gtk4-widgets.md#gtk-grid).
- [Gtk.Image](./docs/gtk4-widgets.md#gtk-image).
- [Gtk.ListBox](./docs/gtk4-widgets.md#gtk-listbox).
- [Gtk.MenuButton](./docs/gtk4-widgets.md#gtk-menubutton).
- [Gtk.Overlay](./docs/gtk4-widgets.md#gtk-overlay).
- [Gtk.Picture](./docs/gtk4-widgets.md#gtk-picture).
- [Translator (gettext)](./docs/gtk4-widgets.md#translator-gettext).
- [Gtk.TreeView editable.](./docs/gtk4-widgets.md#treeview-editable).
- [Gtk.TreeView filter.](./docs/gtk4-widgets.md#treeview-filter).
- [Gtk.TreeView sort.](./docs/gtk4-widgets.md#treeview-sort).
- [Gtk.Video](./docs/gtk4-widgets.md#gtk-video).

---

## GTK 4 Libadwaita

> A libadwaita deve estar disponível a partir do GNOME 41, a mesma irá substituir a biblioteca libhandy.

![Python e GTK4: Libadwaita](./docs/images/gtk4-libadwaita/gtk-4-pygobject-adw-actionrow.webp)

Essa nova biblioteca é baseada na biblioteca Libhandy e tem como objetivo melhorar a experiência do usuário através de
um UI/UX mais unificada em aplicativos GNOME.

- [Documentação](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/)

## Instalação

### Arch Linux

```bash
sudo pacman -S libadwaita
```

> Se o `sudo` não funcionar faça login como **root** e faça a instalação se o ``sudo``.

### Fedora

> 🚨 Fedora 35 ou superior.

```bash
sudo dnf install libadwaita
```

### openSUSE Tumbleweed

```bash
sudo zypper install libadwaita-devel
```

### Widgets

- [Adw.ActionRow](./docs/gtk4-widgets-libadwaita.md#actionrow).
- [Adw.animation].
- [Adw.ApplicationWindow].
- [Adw.Avatar](./docs/gtk4-widgets-libadwaita.md#avatar).
- [Adw.Bin].
- [Adw.Carousel](./docs/gtk4-widgets-libadwaita.md#carousel).
- [Adw.CarouselIndicatorDots](./docs/gtk4-widgets-libadwaita.md#carouselindicatordots).
- [Adw.CarouselIndicatorLines](./docs/gtk4-widgets-libadwaita.md#carouselindicatorlines).
- [Adw.ClampLayout].
- [Adw.ClampScrollable].
- [Adw.Clamp].
- [Adw.ComboRow].
- [Adw.DeprecationMacros].
- [Adw.EnumListModel].
- [Adw.EnumValueObject].
- [Adw.Enums].
- [Adw.ExpanderRow].
- [Adw.Flap].
- [Adw.HeaderBar].
- [Adw.Leaflet].
- [Adw.Main].
- [Adw.NavigationDirection].
- [Adw.PreferencesGroup].
- [Adw.PreferencesPage].
- [Adw.PreferencesRow].
- [Adw.PreferencesWindow].
- [Adw.Squeezer].
- [Adw.StatusPage].
- [Adw.SwipeGroup].
- [Adw.SwipeTracker].
- [Adw.Swipeable].
- [Adw.Types].
- [Adw.ValueObject].
- [Adw.Version].
- [Adw.ViewSwitcherBar].
- [Adw.ViewSwitcherTitle].
- [Adw.ViewSwitcher].
- [Adw.WindowTitle].
- [Adw.Window].

---

## Mockups

Reimaginando a interface de alguns aplicativos famosos com GTK.

> Em construção.

---

## Exemplos

> Em construção.

---
