# It's Right There

Get the flag from the `flag` file.
Connect using SSH to `ctf@141.85.224.104` on port `34522`.
The account password is `n0p422w0rd`.

## Hints

1. You need privileges.
1. You need some sort of side channel.
1. You need to use the full path.

## Scenario

The `flag` file is right in the home folder of the `ctf` user.
The `ctf` user can't do much of anything on the system.
But we configured `sudo` such that you can use `sha256sum` to get the SHA256 checksum for the flag.

## Solution

Run the command below after connecting via SSH:

```
ctf@router:~$ sudo sha256sum /home/ctf/flag
59404c168e9cafda28f960d052a262803e9f1f7ce7a4c856c32fc53b0cc77d8d  /home/ctf/flag
```

Then use [CrackStation](https://crackstation.net/) to get the flag string from the hash.

## Deploy

You need to have [Docker](https://docs.docker.com/engine/) installed on the system.

Enter the `deploy` directory and then build and run the Docker container:

```
$ cd deploy/

$ make

$ make run
```
