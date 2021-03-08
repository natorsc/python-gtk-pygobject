@ECHO OFF
rem Não utilize esse script, o mesmo ainda não é funcional.
pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="CodigoNinja" ^
--exclude-module="tkinter" ^
--add-data="icons/;icons" ^
--add-data="ui/;ui" ^
--add-data="C:/msys64/mingw64/lib/girepository-1.0;lib/girepository-1.0" ^
--add-data="C:/msys64/mingw64/lib/gdk-pixbuf-2.0;lib/gdk-pixbuf-2.0" ^
--add-data="C:/msys64/mingw64/lib/gtk-3.0;lib/gtk-3.0" ^
--add-data="C:/msys64/mingw64/share/glib-2.0;share/glib-2.0" ^
--icon="icons/icon.ico" ^
MainWindow.py
