FROM wxpython-ubuntu-18.04 


RUN apt-get update && apt-get upgrade -y && apt-get install -y dos2unix

# Copy files (make sure that the pythion file is executable - chmod +x )
COPY simple_gui.py /root/python/

RUN dos2unix /root/python/simple_gui.py
RUN chmod +x /root/python/simple_gui.py

# RUN pip install wxPython==4.1.0

WORKDIR /root/python
ENTRYPOINT ["python3.7", "./simple_gui.py"]