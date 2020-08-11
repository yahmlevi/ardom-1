@ECHO OFF
ECHO Python3.8 env with wxpython and run simple_gui.py

SET env_name=test_env_py3.8

if exist %env_name% (
    echo "exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & %env_name%\Scripts\activate.bat & pip install wxpython & python3.8 simple_gui.py exit"
) else (
    echo "dont exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & C:\Users\Yahm\AppData\Local\Programs\Python\Python38-32\python.exe -m venv %env_name% & %env_name%\Scripts\activate.bat & pip install wxpython & python3.8 simple_gui.py"
)
PAUSE