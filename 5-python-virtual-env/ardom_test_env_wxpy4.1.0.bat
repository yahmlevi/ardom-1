@ECHO OFF
ECHO Python env with wxPython version 4.1.0

CMD /k "pip install wxPython==4.1.0 & cd D:\projects & ardom_test_env\Scripts\activate.bat & cd D:\projects\ardom-1\5-python-virtual-env & python simple_gui.py & pip list" 
PAUSE