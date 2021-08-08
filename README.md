[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Please do not theme this app](https://stopthemingmy.app/badge.svg)](https://stopthemingmy.app)

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

- [https://developer.gnome.org/hig/stable/](https://developer.gnome.org/hig/stable/).

---

## bibliotecas:

- **GLib**: Biblioteca com utilitários de uso geral, não é específica para interfaces gráficas. GLib fornece muitos
  tipos de dados úteis, macros, conversões de tipo, utilitários de string, utilitários de arquivo, uma abstração de loop
  principal e assim por diante.
- **GObject**: Biblioteca que fornece um sistema de tipos.
- **GIO**: Uma API VFS (Virtual file system) moderna e fácil de usar, incluindo abstrações para arquivos, drives,
  volumes, fluxo de IO, bem como programação de rede e comunicação DBus.
- **cairo**: Cairo é uma biblioteca de gráficos 2D com suporte para vários dispositivos de saída.
- **Pango**: Pango é uma biblioteca para manipulação de texto internacionalizada. Ele gira em torno do objeto
  PangoLayout, representando um parágrafo de texto. Pango fornece o motor para GtkTextView, GtkLabel, GtkEntry e outros
  widgets que exibem texto.
- **ATK**: ATK é o Kit de ferramentas de acessibilidade. Ele fornece um conjunto de interfaces genéricas que permitem
  que tecnologias de acessibilidade interajam com uma interface gráfica de usuário. Por exemplo, um leitor de tela usa
  ATK para descobrir o texto em uma interface e lê-lo para usuários cegos. Os widgets GTK possuem suporte integrado para
  acessibilidade usando a estrutura ATK.
- **GdkPixbuf**: Esta é uma pequena biblioteca que permite criar objetos GdkPixbuf (“buffer de pixel”) a partir de dados
  de imagem ou arquivos de imagem. Use um GdkPixbuf em combinação com GtkImage para exibir imagens.
- **graphene**: Esta é uma pequena biblioteca que fornece operações e tipos de dados vetoriais e matriciais. O graphene
  fornece implementações otimizadas usando vários conjuntos de instruções SIMD, como SSE.
- **GDK**: GDK é a camada de abstração que permite ao GTK oferecer suporte a vários sistemas de janelas. O GDK fornece
  recursos de sistema de janelas no Wayland, X11, Windows e OSX.
- **GSK**: GSK é uma biblioteca para criar um gráfico de cena a partir de nós de renderização e renderizá-lo usando
  diferentes APIs de renderização. GSK fornece renderizadores para OpenGL, Vulkan e Cairo.

---

## Tutoriais

- [https://codigoninja.dev/](https://codigoninja.dev/).

---

## GTK 3

### Gio

- [Gio.Menu](./docs/gtk3-widgets.md#gio-menu).
- [Gio.SimpleAction](./docs/gtk3-widgets.md#gio-simple-action).

### Widgets

- [Gtk.ActionBar](./docs/gtk3-widgets.md#gtk-actionbar).
- [Gtk.ApplicationWindow](./docs/gtk3-widgets.md#gtk-applicationwindow).
- [Gtk.Box horizontal](./docs/gtk3-widgets.md#gtk-box-horizontal).
- [Gtk.Box vertical](./docs/gtk3-widgets.md#gtk-box-vertical).
- [Gtk.Button](./docs/gtk3-widgets.md#gtk-button).
- [Gtk.ButtonBox](./docs/gtk3-widgets.md#gtk-buttonbox).
- [Gtk.Calendar](./docs/gtk3-widgets.md#gtk-calendar).
- [Gtk.CheckButton](./docs/gtk3-widgets.md#gtk-checkbutton).
- [Gtk.Dialog](./docs/gtk3-widgets.md#gtk-dialog).
- [Gtk.DragAndDrop](./docs/gtk3-widgets.md#gtk-drag-and-drop).
- [Gtk.Entry](./docs/gtk3-widgets.md#gtk-entry).
- [Gtk.EntryCompletion](./docs/gtk3-widgets.md#gtk-entrycompletion).
- [Gtk.EventBox](./docs/gtk3-widgets.md#gtk-eventbox).
- [Gtk.FileChooserDialog folder](./docs/gtk3-widgets.md#gtk-filechooserdialog-folder).
- [Gtk.FileChooserDialog open](./docs/gtk3-widgets.md#gtk-filechooserdialog-open).
- [Gtk.FileChooserDialog save](./docs/gtk3-widgets.md#gtk-filechooserdialog-save).
- [Gtk.Fixed](./docs/gtk3-widgets.md#gtk-filechooserdialog-save).
- [Gtk.FlowBox](./docs/gtk3-widgets.md#gtk-flowbox).
- [Gtk.Grid](./docs/gtk3-widgets.md#gtk-grid).
- [Gtk.HeaderBar](./docs/gtk3-widgets.md#gtk-headerbar).
- [Gtk.Image](./docs/gtk3-widgets.md#gtk-image).
- [Gtk.InfoBar](./docs/gtk3-widgets.md#gtk-infobar).
- [Gtk.Layout](./docs/gtk3-widgets.md#gtk-layout).
- [Gtk.LinkButton](./docs/gtk3-widgets.md#gtk-linkbutton).
- [Gtk.ListBox](./docs/gtk3-widgets.md#gtk-listbox).
- [Gtk.Menu](./docs/gtk3-widgets.md#gtk-menu).
- [Gtk.MenuBar](./docs/gtk3-widgets.md#gtk-menubar).
- [Gtk.MenuButton](./docs/gtk3-widgets.md#gtk-menubutton).
- [Gtk.MessageDialog](./docs/gtk3-widgets.md#gtk-messagedialog).
- [Gtk.Notebook](./docs/gtk3-widgets.md#gtk-notebook).
- [Gtk.Notify](./docs/gtk3-widgets.md#gtk-notify).
- [Gtk.Overlay](./docs/gtk3-widgets.md#gtk-overlay).
- [Gtk.Paned horizontal](./docs/gtk3-widgets.md#gtk-paned-horizontal).
- [Gtk.Paned vertical](./docs/gtk3-widgets.md#gtk-paned-vertical).
- [Gtk.Popover](./docs/gtk3-widgets.md#gtk-popover).
- [Gtk.PrintOperation](./docs/gtk3-widgets.md#gtk-printoperation).
- [Gtk.RadioButton](./docs/gtk3-widgets.md#gtk-radiobutton).
- [Gtk.Revealer](./docs/gtk3-widgets.md#gtk-revealer).
- [Gtk.SearchBar](./docs/gtk3-widgets.md#gtk-searchbar).
- [Gtk.SearchEntry](./docs/gtk3-widgets.md#gtk-searchentry).
- [Gtk.Separator](./docs/gtk3-widgets.md#gtk-separator).
- [Gtk.Spinner](./docs/gtk3-widgets.md#gtk-spinner).
- [Gtk.StackSidebar](./docs/gtk3-widgets.md#gtk-stacksidebar).
- [Gtk.StackSwitcher](./docs/gtk3-widgets.md#gtk-stackswitcher).
- [Gtk.Statusbar](./docs/gtk3-widgets.md#gtk-statusbar).
- [Gtk Style add class](./docs/gtk3-widgets.md#gtk-style-add-class).
- [Gtk Style css provider](./docs/gtk3-widgets.md#gtk-style-css-provider).
- [Gtk Style dark mode](./docs/gtk3-widgets.md#gtk-style-dark-mode).
- [Gtk Style set name](./docs/gtk3-widgets.md#gtk-style-set-name).
- [Gtk.Switch](./docs/gtk3-widgets.md#gtk-switch).
- [Gtk.ToggleButton](./docs/gtk3-widgets.md#gtk-togglebutton).
- [Gtk.Toolbar](./docs/gtk3-widgets.md#gtk-toolbar).
- [Gtk.TreeView editable](./docs/gtk3-widgets.md#gtk-treeview-editable).
- [Gtk.TreeView filter](./docs/gtk3-widgets.md#gtk-treeview-filter).
- [Gtk.TreeView sort](./docs/gtk3-widgets.md#gtk-treeview-sort).
- [Gtk.TreeView TreeStore](./docs/gtk3-widgets.md#gtk-treeview-treestore).
- [Gtk.Window](./docs/gtk3-widgets.md#gtk-window).

---

## GTK 4

> Em construção.

![Python e GTK4: Gtk.ApplicationWindow](./docs/images/gtk4/gtk-4-pygobject-applicationwindow.webp)

O GTK 4 foi lançado em 16 de dezembro 2020.

No GTK 4 é desencorajado o uso do Gnome Glade, isso porque o Gnome Builder fornece uma forma padronizada e moderna de se
criar e gerenciar projetos.

Os widgets que foram criados ou passaram por grandes aprimoramentos são:

- Data transfers.
- Event controllers.
- Layout managers.
- Render nodes.
- Media playback.
- Scalable lists.
- Shaders.
- Accessibility.

### Widgets

- [Gtk.ApplicationWindow](./docs/gtk4-widgets.md#gtk-applicationwindow).
- [Gtk.Box (horizontal)](./docs/gtk4-widgets.md#gtk-box-horizontal).

---

## GTK 4 Libadwaita

> A libadwaita deve estar disponível a partir do GNOME 41, a mesma irá substituir a biblioteca libhandy.

![Python e GTK4: Libadwaita](./docs/images/gtk4-libadwaita/gtk-4-pygobject-adw-applicationwindow.webp)

Essa nova biblioteca é baseada na biblioteca Libhandy e tem como objetivo melhorar a experiência do usuário através de
um UI/UX mais unificada em aplicativos GNOME.

Alguns exemplos de design podem ser vistos em:

- [https://gitlab.gnome.org/Teams/Design/os-mockups/-/blob/master/lists/list-design-patterns.png](https://gitlab.gnome.org/Teams/Design/os-mockups/-/blob/master/lists/list-design-patterns.png)
  .

Documentação da biblioteca libadwaita:

- [https://gnome.pages.gitlab.gnome.org/libadwaita/doc/](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/)

### Widgets

- [Adw.ActionRow](#).
- [Adw.animation](#).
- [Adw.ApplicationWindow](./docs/gtk4-libadwaita-widgets.md#libadwaita-applicationwindow).
- [Adw.Avatar](#).
- [Adw.Bin](#).
- [Adw.CarouselIndicatorDots](#).
- [Adw.CarouselIndicatorLines](#).
- [Adw.Carousel](#).
- [Adw.ClampLayout](#).
- [Adw.ClampScrollable](#).
- [Adw.Clamp](#).
- [Adw.ComboRow](#).
- [Adw.DeprecationMacros](#).
- [Adw.EnumListModel](#).
- [Adw.EnumValueObject](#).
- [Adw.Enums](#).
- [Adw.ExpanderRow](#).
- [Adw.Flap](#).
- [Adw.HeaderBar](#).
- [Adw.Leaflet](#).
- [Adw.Main](#).
- [Adw.NavigationDirection](#).
- [Adw.PreferencesGroup](#).
- [Adw.PreferencesPage](#).
- [Adw.PreferencesRow](#).
- [Adw.PreferencesWindow](#).
- [Adw.Squeezer](#).
- [Adw.StatusPage](#).
- [Adw.SwipeGroup](#).
- [Adw.SwipeTracker](#).
- [Adw.Swipeable](#).
- [Adw.Types](#).
- [Adw.ValueObject](#).
- [Adw.Version](#).
- [Adw.ViewSwitcherBar](#).
- [Adw.ViewSwitcherTitle](#).
- [Adw.ViewSwitcher](#).
- [Adw.WindowTitle](#).
- [Adw.Window](#).

---

## GTK 3 Libhandy

> De prefeirencia por utilizar a biblioteca [libadwaita](#gtk-4-Libadwaita).

### Instalação

#### Fedora

```bash
sudo apt install libhandy
```

#### Ubuntu

```bash
sudo apt install libhandy-1
```

![Python e GTK 3: libhandy 1](docs/images/gtk3-libhandy/pygobject-hdy-actionrow.webp)
*Python e GTK 3: libhandy 1*

### Widgets

- [Handy.ActionRow](./docs/gtk3-libhandy-widgets.md#handy-actionrow).
- [Handy.ApplicationWindow](./docs/gtk3-libhandy-widgets.md#handy-applicationwindow).
- [Handy.Avatar](./docs/gtk3-libhandy-widgets.md#handy-avatar).
- [Handy.Carousel](./docs/gtk3-libhandy-widgets.md#handy-avatar).
- [Handy.CarouselIndicatorDots](./docs/gtk3-libhandy-widgets.md#handy-carousel-indicator-dots).
- [Handy.CarouselIndicatorLines](./docs/gtk3-libhandy-widgets.md#handy-carousel-indicator-lines).
- [Handy.Clamp](./docs/gtk3-libhandy-widgets.md#handy-clamp).
- [Handy.ComboRow](./docs/gtk3-libhandy-widgets.md#handy-comborow).
- [Handy.Deck](./docs/gtk3-libhandy-widgets.md#handy-deck).
- [Handy.ExpanderRow](./docs/gtk3-libhandy-widgets.md#handy-expanderrow).
- [Handy.HeaderBar](./docs/gtk3-libhandy-widgets.md#handy-headerbar).
- [Handy.HeaderGroup](./docs/gtk3-libhandy-widgets.md#handy-headergroup).
- [Handy.Leaflet](./docs/gtk3-libhandy-widgets.md#handy-leaflet).
- [Handy.SearchBar](./docs/gtk3-libhandy-widgets.md#handy-searchbar).
- [Handy.Squeezer](./docs/gtk3-libhandy-widgets.md#handy-squeezer).
- [Handy.ViewSwitcher](./docs/gtk3-libhandy-widgets.md#handy-view-switcher).
- [Handy.ViewSwitcherBar](./docs/gtk3-libhandy-widgets.md#handy-view-switcher-bar).
- [Handy.ViewSwitcherTitle](./docs/gtk3-libhandy-widgets.md#handy-view-switcher-title).
- [Handy.Window](./docs/gtk3-libhandy-widgets.md#handy-window).
- [Handy.WindowHandle](./docs/gtk3-libhandy-widgets.md#handy-window-handle).

---

## Mockups

Reimaginando a interface de alguns aplicativos famosos com GTK.

> Em construção.

---

## Exemplos

### Navegador web (WebKit2.WebView)

* [WebKit2.WebView com Python](https://github.com/natorsc/gui-python-gtk/tree/master/src/gtk/examples/web-browser).

![WebKit2 WebView](https://codigoninja.dev/images/pygobject-gtk3-webkit2-webview.webp)

---
