#!/bin/bash

#pyinstaller -y \
#    --log-level DEBUG --onedir --specpath info \
#    --hidden-import PySide2.QtWidgets \
#    --hidden-import PySide2.QtCore \
#    --hidden-import numpy \
#    --hidden-import scipy.optimize \
#    -r lib.* \
#    --windowed main.py

pyinstaller -y \
    --log-level DEBUG \
    --onedir \
    --hidden-import PySide2.QtWidgets \
    --hidden-import PySide2.QtCore \
    --hidden-import numpy \
    --hidden-import scipy.optimize \
    --resource lib.* \
    main.py
