useful commands -

create virtual env: python -m venv env-name

activate virtual env: env-name\Scripts\activate.bat

deactivate virtual env: deactivate

show pip installtions: pip list

current directory in batch: %CD%

pip install to specified folder - pip install --target=d:\somewhere\other\than\the\default package_name 
https://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip

pip install multiple to specified folder - pip install -r requirements.txt -t <path-to-the-lib-directory>
https://stackoverflow.com/questions/53925660/installing-python-dependencies-locally-in-project

# source for setting up python embeded windows dist - https://dev.to/fpim/setting-up-python-s-windows-embeddable-distribution-properly-1081

# source for making exe file (pyinstaller) - https://www.youtube.com/watch?v=UZX5kH72Yx4&t=310s
