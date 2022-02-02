#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--name='br.natorsc.Exemplo' \
--exclude-module='tkinter' \
--add-data='./icons/:icons' \
--add-data='./ui/:ui' \
MainWindow.py