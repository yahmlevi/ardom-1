@ECHO OFF
ECHO Python3.7 env

SET env_name=test_env_py3.7

if exist %env_name% (
    echo "exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & %env_name%\Scripts\activate & python3.7"
) else (
    echo "dont exsists"
    CMD /k "cd d:\projects\ardom-1\5-python-virtual-env & python3.7 -m virtualenv %env_name% & %env_name%\Scripts\activate & & python3.7"
)
PAUSE