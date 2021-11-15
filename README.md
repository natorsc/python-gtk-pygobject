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

## [GTK 3](./docs/gtk3-index.md)

## [GTK 3 Libhandy](./docs/gtk3-libhandy-index.md)

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

- [Gtk.ActionBar](./docs/gtk4-widgets.md#gtk-actionbar).
- [Gtk.ApplicationWindow](./docs/gtk4-widgets.md#gtk-applicationwindow).
- [Gtk.Box (horizontal)](./docs/gtk4-widgets.md#gtk-box-horizontal).
- [Gtk.Box (vertical)](./docs/gtk4-widgets.md#gtk-box-vertical).
- [Gtk.Button](./docs/gtk4-widgets.md#gtk-button).
- [Gtk.Calendar](./docs/gtk4-widgets.md#gtk-calendar).
- [Gtk.CheckButton](./docs/gtk4-widgets.md#gtk-checkbutton).
- [Gtk.Dialog](./docs/gtk4-widgets.md#gtk-dialog).
- [Gtk.DragAndDrop (Gtk.DragSource e Gtk.DropTarget)](./docs/gtk4-widgets.md#gtk-drag-and-drop).
- [Gtk.Entry](./docs/gtk4-widgets.md#gtk-entry).
- [Gtk.EntryCompletion](./docs/gtk4-widgets.md#gtk-entrycompletion).
- [Gtk.FileChooserDialog (folder)](./docs/gtk4-widgets.md#gtk-filechooserdialog-folder).
- [Gtk.FileChooserDialog (open)](./docs/gtk4-widgets.md#gtk-filechooserdialog-open).
- [Gtk.FileChooserDialog (save)](./docs/gtk4-widgets.md#gtk-filechooserdialog-save).
- [Gtk.Fixed](./docs/gtk4-widgets.md#gtk-fixed).
- [Gtk.FlowBox](./docs/gtk4-widgets.md#gtk-flowbox).
- [Gtk.MenuButton](./docs/gtk4-widgets.md#gtk-menubutton).
- [Translator (gettext)](./docs/gtk4-widgets.md#translator-gettext).

---

## GTK 4 Libadwaita

> A libadwaita deve estar disponível a partir do GNOME 41, a mesma irá substituir a biblioteca libhandy.

![Python e GTK4: Libadwaita](./docs/images/gtk4-libadwaita/gtk-4-pygobject-adw-actionrow.webp)

Essa nova biblioteca é baseada na biblioteca Libhandy e tem como objetivo melhorar a experiência do usuário através de
um UI/UX mais unificada em aplicativos GNOME.

- [Documentação](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/)

## Instalação

### Arch Linux

> Testes realizados com a versão: `1.0.0alpha.2-1`.

```bash
sudo pacman -S libadwaita
```

### openSUSE Tumbleweed

```bash
sudo zypper install libadwaita
```

> Se o `sudo` não funcionar faça login como **root** e faça a instalação se o ``sudo``.

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
