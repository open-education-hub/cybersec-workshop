FROM ubuntu:18.04

RUN apt -y update
RUN apt -y install openssh-server

RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN passwd -n 999 ctf

COPY flag /home/ctf
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN chmod 440 /home/ctf/flag

RUN mkdir /home/ctf/.ssh
COPY public/authorized_keys /home/ctf/.ssh
RUN chown root:ctf /home/ctf/.ssh/authorized_keys
RUN chmod 640 /home/ctf/.ssh/authorized_keys

COPY deploy/run.sh /usr/local/bin/
CMD ["/usr/local/bin/run.sh"]
