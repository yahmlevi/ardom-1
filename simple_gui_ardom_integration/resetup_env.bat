@ECHO OFF
ECHO Batch script to update env - just update requirements.txt file and run this
ECHO Template is compatible with all python3 and above versions

SET env_name=ardom_wx_test_env
SET py_ver=pythonw
SET script_name=simple_gui.py

REM delete env_folder in order to create a new one with the updated requirements.txt
@RD /S /Q "%env_name%"

if exist %env_name% (
    echo "env exists"
    CMD /k "cd %cd% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name%"
) else (
    echo "env doesn't exist"
    CMD /k "cd %cd% & python -m venv %env_name% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name%"
)
EXIT