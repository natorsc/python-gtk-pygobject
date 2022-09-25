:og:description: Exemplos de código da utilização das classes de estilo da biblioteca libadwaita (GTK 4).

.. meta::
   :description: Exemplos de código da utilização das classes de estilo da biblioteca libadwaita (GTK 4).
   :keywords: GTK, GTK 4, libadwaita, class, style, Python, Python 3, PyGObject, XML, Blueprint

Libadwaita classes de estilo
============================

.. caution::
   
   Para que o estilo visual seja aplicado de forma correta utilize ``Adw.init()`` no código.

.. danger::

   Ao se utilizar a biblioteca ``libadwaita`` juntamente com arquivos de interface (``*.ui``) é **obrigatório** o uso de ``Adw.init()`` no código.
   
   Caso contrario será exibido o erro:

   ``Error building template class '' for an instance of type '': .:0:0 Invalid object type ''``.

Style background
--------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650224114262/jRbVc_i_R.webp
   :alt: Python e GTK 4: PyGObject style background.

   Python e GTK 4: PyGObject style background.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/background/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/background/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/background/ui/MainWindow.blp

--------------

Style body
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650037614222/0fLwSsTJm.webp
   :alt: Python e GTK 4: PyGObject style body.

   Python e GTK 4: PyGObject style body.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/body/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/body/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/body/ui/MainWindow.blp

--------------

Style boxed-list
--------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650224088782/nPGWY4HRg.webp
   :alt: Python e GTK 4: PyGObject style boxed-list.

   Python e GTK 4: PyGObject style boxed-list.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/boxed-list/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/boxed-list/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/boxed-list/ui/MainWindow.blp

--------------

Style caption
-----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650037922421/ehlolZ4KI.webp
   :alt: Python e GTK 4: PyGObject style caption.

   Python e GTK 4: PyGObject style caption.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/caption/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/caption/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/caption/ui/MainWindow.blp

--------------

Style card
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650223992375/H180zRf3x.webp
   :alt: Python e GTK 4: PyGObject style card.

   Python e GTK 4: PyGObject style card.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/card/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/card/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/card/ui/MainWindow.blp

--------------

Style circular
------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650046152376/FEfGdXhvI.webp
   :alt: Python e GTK 4: PyGObject style circular.

   Python e GTK 4: PyGObject style circular.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/circular/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/circular/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/circular/ui/MainWindow.blp

--------------

Style colors
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650034919634/1hIGe0a8h.webp
   :alt: Python e GTK 4: PyGObject style colors.

   Python e GTK 4: PyGObject style colors.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/colors/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/colors/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/colors/ui/MainWindow.blp

--------------

Style compact
-----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650541543633/ojEoU9Lwu.webp
   :alt: Python e GTK 4: PyGObject style compact.

   Python e GTK 4: PyGObject style compact.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/compact/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/compact/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/compact/ui/MainWindow.blp

--------------

Style destructive-action
----------------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650044611907/TUn8T0ble.webp
   :alt: Python e GTK 4: PyGObject style destructive-action.

   Python e GTK 4: PyGObject style destructive-action.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/destructive-action/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/destructive-action/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/destructive-action/ui/MainWindow.blp

--------------

Style devel
---------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650044359668/y3gfrFz3F.webp
   :alt: Python e GTK 4: PyGObject style devel.

   Python e GTK 4: PyGObject style devel.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/devel/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/devel/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/devel/ui/MainWindow.blp

--------------

Style dim-label
-------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650542472763/svuag92Xi.webp
   :alt: Python e GTK 4: PyGObject style dim-label.

   Python e GTK 4: PyGObject style dim-label.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/dim-label/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/dim-label/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/dim-label/ui/MainWindow.blp

--------------

Style flat
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650044793812/lHSGU2mST.webp
   :alt: Python e GTK 4: PyGObject style flat.

   Python e GTK 4: PyGObject style flat.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/flat/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/flat/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/flat/ui/MainWindow.blp

.. Criar ou corrigir.

    Style flat headerbar
    ------------------------------

    .. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650225499901/5Yb0wyHst.png
       :alt: Python e GTK 4: PyGObject style headerbar.

       Python e GTK 4: PyGObject style headerbar.

    .. tab:: Python

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/headerbar/MainWindow.py

    .. tab:: UI

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/headerbar/ui/MainWindow.ui
      :language: html

    .. tab:: Blueprint

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/headerbar/ui/MainWindow.blp

--------------

Style frame
---------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650543428144/oYuV6Ud1n.webp
   :alt: Python e GTK 4: PyGObject style frame.

   Python e GTK 4: PyGObject style frame.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/frame/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/frame/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/frame/ui/MainWindow.blp

--------------

Style heading
-----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650037440306/HpCOUjRpf.webp
   :alt: Python e GTK 4: PyGObject style heading.

   Python e GTK 4: PyGObject style heading.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/heading/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/heading/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/heading/ui/MainWindow.blp

--------------

Style icon-dropshadow
-------------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650546842247/wXVWmOYMt.webp
   :alt: Python e GTK 4: PyGObject style icon-dropshadow.

   Python e GTK 4: PyGObject style icon-dropshadow.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/icon-dropshadow/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/icon-dropshadow/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/icon-dropshadow/ui/MainWindow.blp

--------------

Style inline
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650551049650/TmFBg9DUi.webp
   :alt: Python e GTK 4: PyGObject style inline.

   Python e GTK 4: PyGObject style inline.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/inline/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/inline/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/inline/ui/MainWindow.blp

--------------

Style linked
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650554859402/WiZsTvIIN.webp
   :alt: Python e GTK 4: PyGObject style linked.

   Python e GTK 4: PyGObject style linked.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/linked/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/linked/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/linked/ui/MainWindow.blp

--------------

Style lowres-icon
---------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650547130476/0cVoDA-GC.webp
   :alt: Python e GTK 4: PyGObject style lowres-icon.

   Python e GTK 4: PyGObject style lowres-icon.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/lowres-icon/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/lowres-icon/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/lowres-icon/ui/MainWindow.blp

--------------

Style menu
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650664906063/U3P2jpLdp.webp
   :alt: Python e GTK 4: PyGObject style menu.

   Python e GTK 4: PyGObject style menu.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/menu/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/menu/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/menu/ui/MainWindow.blp

--------------

Style monospace
-------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650041606019/7gHG791jj.webp
   :alt: Python e GTK 4: PyGObject style monospace.

   Python e GTK 4: PyGObject style monospace.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/monospace/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/monospace/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/monospace/ui/MainWindow.blp

.. Criar ou corrigir.

    Style sidebar
    -----------------------

    .. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650570701667/58FK2ompQ.webp
       :alt: Python e GTK 4: PyGObject style sidebar.

       Python e GTK 4: PyGObject style sidebar.

    .. tab:: Python

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/sidebar/MainWindow.py

    .. tab:: UI

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/sidebar/ui/MainWindow.ui
        :language: html

    .. tab:: Blueprint

       ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/sidebar/ui/MainWindow.blp

--------------

Style numeric
-----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650664874579/tYuUxVMY6.webp
   :alt: Python e GTK 4: PyGObject style numeric.

   Python e GTK 4: PyGObject style numeric.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/numeric/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/numeric/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/numeric/ui/MainWindow.blp

--------------

Style opaque
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650044999606/A5nijTUiA.webp
   :alt: Python e GTK 4: PyGObject style opaque.

   Python e GTK 4: PyGObject style opaque.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/opaque/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/opaque/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/opaque/ui/MainWindow.blp

--------------

Style pill
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650034986010/9jZHh9wr2.webp
   :alt: Python e GTK 4: PyGObject style pill.

   Python e GTK 4: PyGObject style pill.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/pill/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/pill/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/pill/ui/MainWindow.blp

--------------

Style raised
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650561555844/3o8NigdEU.webp
   :alt: Python e GTK 4: PyGObject style raised.

   Python e GTK 4: PyGObject style raised.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/raised/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/raised/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/raised/ui/MainWindow.blp

--------------

Style selection-mode
------------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650622855809/z3UPgn68D.webp
   :alt: Python e GTK 4: PyGObject style selection-mode.

   Python e GTK 4: PyGObject style selection-mode.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/selection-mode/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/selection-mode/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/selection-mode/ui/MainWindow.blp

--------------

Style spacer
----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650560885219/vacp2aSfW.webp
   :alt: Python e GTK 4: PyGObject style spacer.

   Python e GTK 4: PyGObject style spacer.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/spacer/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/spacer/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/spacer/ui/MainWindow.blp

--------------

Style suggested-action
--------------------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650574917400/4Bfg8lKN8.webp
   :alt: Python e GTK 4: PyGObject style suggested-action.

   Python e GTK 4: PyGObject style suggested-action.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/suggested-action/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/suggested-action/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/suggested-action/ui/MainWindow.blp

--------------

Style title
---------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650036356705/QraITYAlG.webp
   :alt: Python e GTK 4: PyGObject style title.

   Python e GTK 4: PyGObject style title.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/title/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/title/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/title/ui/MainWindow.blp

--------------

Style toolbar
-----------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650626901962/9WyMP_8j1.webp
   :alt: Python e GTK 4: PyGObject style toolbar.

   Python e GTK 4: PyGObject style toolbar.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/toolbar/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/toolbar/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/toolbar/ui/MainWindow.blp

--------------

Style view
--------------------

.. figure:: https://cdn.hashnode.com/res/hashnode/image/upload/v1650575348625/4QGklJa_t.webp
   :alt: Python e GTK 4: PyGObject style view.

   Python e GTK 4: PyGObject style view.

.. tab:: Python

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/view/MainWindow.py

.. tab:: UI

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/view/ui/MainWindow.ui
      :language: html

.. tab:: Blueprint

   ..  literalinclude:: ../../src/gtk4-libadwaita-style-class/view/ui/MainWindow.blp
