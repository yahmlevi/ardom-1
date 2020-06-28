FROM debian
# Setup enviroment variables
ENV DEBIAN_FRONTEND noninteractive

# Installing fuse filesystem is not possible in docker without elevated priviliges
# but we can fake installling it to allow packages we need to install for GNOME
RUN apt-get install libfuse2 -y && \
cd /tmp ; apt-get download fuse && \
cd /tmp ; dpkg-deb -x fuse_* . && \
cd /tmp ; dpkg-deb -e fuse_* && \
cd /tmp ; rm fuse_*.deb && \
cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \
cd /tmp ; dpkg-deb -b . /fuse.deb && \
cd /tmp ; dpkg -i /fuse.deb

# Upstart and DBus have issues inside docker.
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

# Install GNOME
RUN apt-get update && apt-get install -y xorg gnome-core gnome-session-fallback
# Pull in the hack to fix keyboard shortcut bindings for GNOME 3 
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-keybindings.pl /usr/local/etc/gnome-keybindings.pl
RUN chmod +x /usr/local/etc/gnome-keybindings.pl

# Add the script to fix and customise GNOME for docker
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-docker-fix-and-customise.sh /usr/local/etc/gnome-docker-fix-and-customise.sh
RUN chmod +x /usr/local/etc/gnome-docker-fix-and-customise.sh

RUN apt-get update -y && apt-get install -y dbus-x11 gnome-keyring evolution evolution-data-server seahorse sudo
RUN apt-get install -y libnotify-cil-dev
CMD ["evolution"]