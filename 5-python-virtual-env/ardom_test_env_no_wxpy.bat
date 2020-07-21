@ECHO OFF
ECHO Python env with no wxPython.

CMD /k "cd D:\projects & ardom_test_env_2\Scripts\activate.bat & cd D:\projects\ardom-1\5-python-virtual-env & python simple_gui.py & pip list" 
PAUSE