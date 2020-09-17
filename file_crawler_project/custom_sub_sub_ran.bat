@ECHO OFF
ECHO Custom Sub-Sub-Root Analysis

SET env_name=crawler_env
SET py_ver=python
SET script_name=file_crawler.py
SET analysis_type="custom sub-sub"

if exist %env_name% (
    echo "env exists"
    CMD /k "cd %cd% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name% %analysis_type%"
) else (
    echo "env doesn't exist"
    CMD /k "cd %cd% & python -m venv %env_name% & %env_name%\Scripts\activate.bat & pip install -r requirements.txt & %py_ver% %script_name% %analysis_type%"
)
PAUSE