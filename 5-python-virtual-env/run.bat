@ECHO OFF
ECHO simple_gui.py run with temp env path change
SET SAVE=%PYTHONPATH%
SET PYTHONPATH=d:\projects\python-exec\python-zipped\lib
ECHO %PYTHONPATH%
CMD /k "cd d:\projects\python-exec\python-zipped & python simple_gui.py"
SET PYTHONPATH=%SAVE%
PAUSE