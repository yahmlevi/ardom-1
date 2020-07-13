FROM wxpython4/build:ubuntu-18.04

# RUN apt-get install -y dos2unix
RUN sudo apt-get update
RUN sudo apt-get install dos2unix

# Copy files (make sure that the pythion file is executable - chmod +x )
COPY simple_gui.py /root/python/

RUN sudo dos2unix /root/python/simple_gui.py
RUN sudo chmod +x /root/python/simple_gui.py

# RUN pip install wxPython==4.1.0

WORKDIR /root/python
ENTRYPOINT ["python3.7", "./simple_gui.py"]