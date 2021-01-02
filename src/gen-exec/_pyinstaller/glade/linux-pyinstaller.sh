#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="Exemplo" \
--add-data="./icons/:icons" \
--add-data="./MainWindow.glade/:." \
--exclude-module="tkinter" \
--upx-dir="/usr/local/share/" \
MainWindow.py
