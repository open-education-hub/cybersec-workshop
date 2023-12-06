FROM ubuntu:18.04

RUN apt -y update
RUN apt -y install openssh-server
RUN apt -y install sudo

RUN useradd -m -d /home/ctf -s /bin/bash ctf
RUN echo "ctf:n0p422w0rd" | chpasswd
RUN passwd -n 999 ctf

COPY flag /home/ctf
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf
RUN chmod 400 /home/ctf/flag

RUN echo 'ctf ALL=(ALL:ALL) /usr/bin/sha256sum /home/ctf/flag' | sudo EDITOR='tee -a' visudo

COPY deploy/run.sh /usr/local/bin/
CMD ["/usr/local/bin/run.sh"]
