@ECHO OFF
ECHO Python env with no wxPython.

CMD /k "cd D:\projects & python -m venv env-test-1 & env-test-1\Scripts\activate.bat & cd D:\projects\ardom-1\5-python-virtual-env & pip install wxPython==4.1.0 & python simple_gui.py & pip list" 
PAUSE

## add 'run.bat' and 'simply_gui.py' to python zip file and try running from there