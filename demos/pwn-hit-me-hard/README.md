# Pwn: Hit Me Hard

Privilege escalation means you start from a non-privileged account and you access a privileged account.
This can be achieved by exploiting software vulnerabilities or misconfigurations.

For this demo, we'll solve the **Hit Me Hard** challenge.
We start by accessing a non-privileged account.
The goal is to be able to find ways to list the contents of the `/home/ctf/flag` file.

Use SSH to connect to the `141.85.224.104`, port `10002` with the username `ctf` and password `hit-me-hard-0`:

```console
$ ssh ctf@141.85.224.104 -p 10002
ctf@141.85.224.104's password:
[...]
ctf@f9e1eaefca06:~$
```

The flag is, by default, not accessible:

```console
ctf@f9e1eaefca06:~$ cat /home/ctf/flag
cat: /home/ctf/flag: Permission denied
```

Once you find the flag, submit it to the [CTF platform](https://workshop-ctf.security.cs.pub.ro/).
