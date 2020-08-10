@ECHO OFF
ECHO Python3.8 env with wxPython simple_gui.py

SET env_name=ardom_wx_test_env

if exist %env_name% (
    echo "env exists"
    CMD /k "cd %cd% & %env_name%\Scripts\activate.bat & pip install wxpython & python simple_gui.py"
) else (
    echo "env doesn't exist"
    CMD /k "cd %cd% & python -m venv %env_name% & %env_name%\Scripts\activate.bat & pip install wxpython & python simple_gui.py"
)
PAUSE