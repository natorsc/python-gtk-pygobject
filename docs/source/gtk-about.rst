:og:author: Renato Cruz (natorsc)
:og:title: Sobre o toolkit GTK - justCode
:og:description: O GTK é um toolkit de desenvolvimento de interface gráfica do usuário (GUI - Graphical User Interface) multiplataforma, escrito na linguagem de programação C.

.. meta::
   :author: Renato Cruz (natorsc)
   :description: O GTK é um toolkit de desenvolvimento de interface gráfica do usuário (GUI - Graphical User Interface) multiplataforma, escrito na linguagem de programação C.
   :description lang=en: GTK is a cross-platform graphical user interface (GUI) development toolkit written in the C programming language.
   :keywords: Gnome, GTK, libadwaita, Python, PyGObject, Blueprint,

=====
Sobre
=====

O `GTK <https://www.gtk.org/>`__ é um toolkit de desenvolvimento de interface gráfica do usuário (GUI - Graphical User Interface) multiplataforma, escrito na linguagem de programação C.

A sigla GTK significa **GIMP Toolkit**, foi originalmente desenvolvido como parte do software de edição de imagens GIMP (GNU Image Manipulation Program), mas agora é usado em muitos outros projetos.

O GTK foi lançado pela primeira vez em 1998 como parte do GIMP 1.2 e se tornou um projeto independente em 1999, com a versão 1.0. Desde então, o GTK tem sido usado para desenvolver muitos outros aplicativos, como o `GNOME <https://www.gnome.org/>`__ (GNU Network Object Model Environment), um ambiente de desktop popular para sistemas Linux.

O GTK é escrito em C e é distribuído sob a Licença Pública Geral `GNU LGPL <https://www.gnu.org/licenses/lgpl-3.0.html>`__, que permite seu uso e distribuição livre e gratuita.

Ele também possui bindings para outras linguagens de programação:

- `C++ <https://www.cplusplus.com/>`__.
- `C# <https://docs.microsoft.com/pt-br/dotnet/csharp/>`__.
- `C <https://pt.wikipedia.org/wiki/C_(linguagem_de_programa%C3%A7%C3%A3o)>`__.
- `JavaScript <https://www.javascript.com/>`__.
- `Python <https://www.python.org/>`__.
- `Rust <https://www.rust-lang.org/pt-BR>`__.
- `Vala <https://wiki.gnome.org/Projects/Vala>`__.

.. note:: Essas são as linguagens suportadas oficialmente, contudo existem bindings não oficiais.

Bibliotecas
===========

O kit de ferramentas (toolkit) GTK tem um design modular, entre suas principais bibliotecas temos e módulos temos:

GTK
---

A biblioteca `GTK <https://docs.gtk.org/gtk4/index.html>`__ constrói o núcleo do kit de ferramentas e contém todos os widgets.

GDK
---

O `GDK <https://docs.gtk.org/gdk3/index.html>`__ fornece uma interface para desenhar gráficos em uma variedade de plataformas, incluindo X11, Wayland, Microsoft Windows e macOS. Ele oferece suporte a recursos como janelas, eventos, gráficos 2D, imagens e manipulação de cores.

GdkPixbuf
---------

A biblioteca `GdkPixbuf <https://docs.gtk.org/gdk-pixbuf/index.html>`__ permite o carregamento e manipulação de imagens (PNG, JPEG, GIF e etc).

GObject
-------

A biblioteca `GObject <https://docs.gtk.org/gobject/index.html>`__ fornece uma API para programação orientada a objetos (OOP) na linguagem de programação C.

GLib
----

`GLib <https://docs.gtk.org/glib/index.html>`__ é uma biblioteca de baixo nível que forma a base do GTK.

Ele fornece manipulação de estrutura de dados para C, wrappers de portabilidade e interfaces para funcionalidade de tempo de execução como um loop de eventos, threads, carregamento dinâmico e um sistema de objetos.

GIO
---

A biblioteca `GIO <https://docs.gtk.org/gio/index.html>`__ implementa suporte a operações de entrada e saída (I/O, networking, IPC e etc).

GSK
---

A bliblioteca `GSK <https://docs.gtk.org/gsk4/index.html>`__ é utilizada para otimizar o desenho e a atualização do widget.

Graphene
--------

A biblioteca `Graphene <https://ebassi.github.io/graphene/>`__ implementa o suporte a gráficos, vetores e matrizes.

ATK
---

A biblioteca `ATK <https://docs.gtk.org/atk/index.html>`__ implementa o suporte a leitores de tela, ampliadores de texto (lupas) e dispositivos de entrada alternativos.

Cairo
-----

`Cairo <https://www.cairographics.org/>`__ é uma biblioteca para gráficos 2D com suporte para vários dispositivos de saída (incluindo o X Window System, Win32) ao mesmo tempo em que produz uma saída consistente em todas as mídias, aproveitando a aceleração do hardware de exibição quando disponível.

pango
-----

`Pango <https://docs.gtk.org/Pango/index.html>`__ é uma biblioteca para layout e renderização de texto com ênfase na internacionalização. Ele forma o núcleo do manuseio de texto e fonte para GTK.

OpenGL e Vulkan
---------------

As bibliotecas `OpenGL <https://www.opengl.org/>`__ e `Vulkan <https://www.vulkan.org/>`__ permitem a utilizaçao da GPU.

Para sistemas Linux, existe mais uma camada de abstração entre o kit de ferramentas GTK e o hardware do computador, chamada `Wayland <https://wayland.freedesktop.org/>`__.

Wayland é um protocolo de comunicação que especifica a comunicação entre um servidor de exibição e seus clientes, bem como uma implementação da biblioteca C desse protocolo. Alguns sistemas Linux mais antigos ainda podem usar, em vez do moderno Wayland, o legado X Window System, que às vezes era chamado apenas de X11 ou X.
