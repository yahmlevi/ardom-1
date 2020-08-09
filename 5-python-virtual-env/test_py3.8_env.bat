@ECHO OFF
ECHO Python3.8 env with wxpython and run simple_gui.py

SET env_name=test_env_py3.8

if exist %env_name% (
    echo "exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & %env_name%\Scripts\activate.bat & python3.8 simple_gui.py"
) else (
    echo "dont exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & python -m venv %env_name% & %env_name%\Scripts\activate.bat & python3.8 simple_gui.py"
)
PAUSE