FROM ubuntu:18.04

# RUN apt update && apt install -y \ 
#     curl git \
#     libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0

# Ubuntu packages
# https://packages.ubuntu.com/search?keywords=libSDL

# Install dependencies for Python and wxPython Phoenix
RUN apt update && apt install -y \
    libwebkitgtk-3.0-dev \
    libgtk-3-dev \
    libsm-dev \
    freeglut3 \
    freeglut3-dev \
    libnotify-dev \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    dpkg-dev \
    build-essential \
    python3.7-dev \
    libjpeg-dev \
    libtiff-dev \
    # libsdl1.2-dev \
    libsdl2-dev \
    software-properties-common \
# Install Python 3.7 and pip latest versions
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt install -y python3.7 python3-pip \
    && python3.7 -m pip install -U --no-cache-dir pip \
# Install wx
    && python3.7 -m pip install -U --no-cache-dir -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxPython

# source - https://zoomadmin.com/HowToInstall/UbuntuPackage/libsdl2-2.0-0
# RUN apt update && apt install -y libsdl2-2.0-0

RUN apt install -y dos2unix

# Copy files (make sure that the pythion file is executable - chmod +x )
COPY simple_gui.py /root/python/
RUN dos2unix /root/python/simple_gui.py

WORKDIR /root/python
ENTRYPOINT ["./simple_gui.py"]