
FROM ubuntu:trusty

RUN apt-get update && apt-get install -y openssh-client nano dos2unix

RUN apt-get install python -y
COPY run-ssh-python.sh /run-ssh-python.sh

COPY run-ssh.sh /run-ssh.sh

COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
RUN chmod +x /bin/docker-entrypoint.sh

# use dos2unix
RUN dos2unix /run-ssh.sh
RUN dos2unix /bin/docker-entrypoint.sh

ENTRYPOINT ["/bin/docker-entrypoint.sh"]
