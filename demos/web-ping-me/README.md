# Web: Ping Me

Access http://141.85.224.104:40002/index.php to interact with the applicaion.
Notice the application executes `ping` command to an IP address provided by the user.

You can assume the command used by the application is:

```console
ping <input>
```

where `<input>` is the string provided by the user in the page web form.

As such, a user can **inject a command** directly into a command line to a remote system.
Knowing that the `;` operator separates commands and is able to run multiple commands in a single line, we can use `8.8.8.8 ; whoami` as input.
So, we can cause the running of the command:

```console
ping 8.8.8.8; whoami
```

Validate these assumptions in the web application at http://141.85.224.104:40002/index.php

The goal is to get the contents of the `/flag` file on the server.
Use the `cat` command lie tool for that.

Once you find the flag, submit it to the [CTF platform](https://workshop-ctf.security.cs.pub.ro/).
