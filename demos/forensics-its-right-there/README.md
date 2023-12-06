# It's Right There

Access the `141.85.224.104` system via SSH on port `34522` using the credentials `ctf:n0p422w0rd`.
Get the flag and submit it on the [CTF platform](https://workshop-ctf.security.cs.pub.ro/challenges).

## Walkthrough

We use the command below to log in to the system (the password is `n0p422w0rd`):

```console
$ ssh ctf@141.85.224.104 -p 34522
ctf@141.85.224.104's password:

ctf@6945c409945f:~$
```

After logging in, you see the flag in the home directory of the `ctf` user, i.e. `/home/ctf`:

```console
ctf@6945c409945f:~$ pwd
/home/ctf

ctf@6945c409945f:~$ ls
flag

ctf@6945c409945f:~$ ls -l
total 4
-r-------- 1 root ctf 30 Mar  4 04:26 flag

ctf@6945c409945f:~$ cat flag
cat: flag: Permission denied
```

The `flag` file is only accessible to the `root` user.
We must figure out how to get `root`-like privileges.
Possible options are:

* There is a copy or left over part of the file somewhere in the filesystem.
* There is a (faulty) service that allows us to gain `root`-like privileges, by doing something similar to a privilege escalation attack.
* There is a misconfiguration that allows us to gain `root`-like privileges.
* We are able to log in as `root`, by knowing the password.

All of these require careful investigation of the filesystem, executables and processes.

We would be looking for:

* Recently modified files: we use `find` for that.
* Executables that may have the `setuid` bit enabled, or a capability: we use `find`, `ls` and / or `getcap` for that.
* Interesting services / processes: we use `ps`, `pstree`, `top` for that.
* Interesting updates to configuration files: we look in `/etc/`.
* We try different commands that tie in to the `root` user: `su`, `sudo`.

Among the different items to try, we use the `sudo -l` command to list potential `sudo` commands:

```console
ctf@6945c409945f:~$ sudo -l
[sudo] password for ctf:
Matching Defaults entries for ctf on 6945c409945f:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ctf may run the following commands on 6945c409945f:
    (ALL : ALL) /usr/bin/sha256sum /home/ctf/flag
```

We discover that we can use the `/usr/bin/sha256sum` command on the flag.
We run it:

```console
ctf@6945c409945f:~$ sudo /usr/bin/sha256sum /home/ctf/flag
59404c168e9cafda28f960d052a262803e9f1f7ce7a4c856c32fc53b0cc77d8d  /home/ctf/flag
```

We were able to extract the cryptographic hash of the flag, using the [SHA-2](https://en.wikipedia.org/wiki/SHA-2) function.
We want to reverse the hash to its original text message.
This is typically very hard to do, as hash functions are [one-way functions](https://en.wikipedia.org/wiki/One-way_function), but maybe we are lucky and there is a precomputed set of hashes we can use.

So we head to [CrackStation](https://crackstation.net/).
We introduce the hash in the form and cross our fingers.
Hurray! The flag is revelead:

**all your base are belong to us**

We submit it to the [CTF platform](https://workshop-ctf.security.cs.pub.ro/challenges).
