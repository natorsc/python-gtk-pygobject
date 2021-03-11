#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="br.natorsc.CodigoNinja" \
--exclude-module="tkinter" \
--add-data="./icons/:icons" \
--add-data="./ui/:ui" \
--upx-dir="/usr/local/share/" \
MainWindow.py
