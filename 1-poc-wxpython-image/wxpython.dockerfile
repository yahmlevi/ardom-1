FROM ubuntu:18.04

# RUN apt update && apt install -y \ 
#     curl git \
#     libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0

# Ubuntu packages
# https://packages.ubuntu.com/search?keywords=libSDL

# source - https://github.com/wxWidgets/Phoenix/issues/1640
RUN apt update && apt install -y \
    libwxgtk-webview3.0-gtk3-0v5 \
    libwxgtk-webview3.0-gtk3-dev \
    libwebkit2gtk-4.0-37 \
    libwebkit2gtk-4.0-37-gtk2 \
    libwebkit2gtk-4.0-dev

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


# RUN apt install -y libwebkit2gtk-4.0-dev 
# RUN apt install -y libwebkit2gtk-4.0-37 libwebkit2gtk-4.0-37-gtk2

# https://forums.wxwidgets.org/viewtopic.php?t=47296&p=199557
# RUN apt install -y libwebkit2gtk-4.0-37 libwebkit2gtk-4.0-dev

# apt-get install libxcomposite-dev

# https://forums.wxwidgets.org/viewtopic.php?t=47296&p=199557
# https://packages.debian.org/stretch-backports/mips64el/libwxgtk-webview3.0-gtk3-0v5/filelist
RUN mkdir /usr/local/lib/wx && \
    mkdir /usr/local/lib/wx/3.1.4 && \
    mkdir /usr/local/lib/wx/3.1.4/web-extensions && \
    cp /usr/lib/x86_64-linux-gnu/wx/3.0/web-extensions/webkit2_extu-3.0.so /usr/local/lib/wx/3.1.4/web-extensions/webkit2_extu-3.0.so


RUN apt install -y dos2unix nano locate locales locales-all


# Set the locale
# http://jaredmarkell.com/docker-and-locales/
# https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-debian-ubuntu-docker-container
# RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    # locale-gen en_US.UTF-8 
RUN locale-gen "en_US.UTF-8" 
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 

# verify locales (can be removed in the future)
RUN locale

# Copy files (make sure that the pythion file is executable - chmod +x )
COPY simple_gui.py /root/python/

RUN dos2unix /root/python/simple_gui.py
RUN chmod +x /root/python/simple_gui.py

# RUN pip install wxPython==4.1.0

# to fix error logs on simple_gui.py run ------------------------------------- run in interactive container
# RUN apt install -y mesa-utils nvidia-340

# source - https://askubuntu.com/questions/361862/nvidia-drivers-synaptic
RUN apt install -y ubuntu-drivers-common

# glxinfo | grep render
# LIBGL_DEBUG=verbose glxgears

ENV LIBGL_DEBUG=verbose

# https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update
# ENV LD_PRELOAD=/usr/lib/libGL.so

WORKDIR /root/python
# ENTRYPOINT ["python3.7", "./simple_gui.py"]