
FROM ubuntu:trusty

RUN apt-get install -y openssh-client nano

COPY run-ssh.sh /run-ssh.sh

COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
RUN chmod +x /bin/docker-entrypoint.sh

ENTRYPOINT ["/bin/docker-entrypoint.sh"]
