@ECHO OFF
ECHO Python env with no wxPython.

CMD /k "cd %CD% & python.exe -m venv test-1 & test-1\Scripts\activate.bat & pip install wxPython==4.1.0 & pip list & python.exe simple_gui.py"
PAUSE
