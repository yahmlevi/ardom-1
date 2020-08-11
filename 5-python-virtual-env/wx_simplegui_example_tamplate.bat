@ECHO OFF
ECHO Python3.8 env with wxPython simple_gui.py
ECHO Template is compatible with all python3 and above versions

SET env_name=ardom_wx_test_env
SET py_ver=python3.8
SET script_name=simple_gui.py

if exist %env_name% (
    echo "env exists"
    CMD /k "cd %cd% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name%"
) else (
    echo "env doesn't exist"
    CMD /k "cd %cd% & python -m venv %env_name% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name%"
)
PAUSE