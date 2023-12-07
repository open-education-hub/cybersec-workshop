---
title: "Cybersecurity Workshop"
revealOptions:
  background-color: 'aquamarine'
  transition: 'none'
  slideNumber: true
  autoAnimateDuration: 0.0
---

# CyberSecurity Workshop

Cybsersecurity Education

Part of ICE Joint Master Program

December 7, 2023

Faculty of Automatic Control and Computers, UPB

----

## Resources

- Linux system, native or virtual machine
  - https://www.kali.org/
- Repository: https://github.com/open-education-hub/cybersec-workshop
- CTF Platform: https://workshop-ctf.security.cs.pub.ro

---

## Cybersecurity Buzz

----

### Issues

- 50% of people use the same password for all their logins
- Over 80% of data breaches are due to poor password security
- The password "123456" is now used by more than 23 million people.
- 24% of Americans have used passwords like "password," "Qwerty," and "123456"

----

### Jobs

https://fortune.com/education/business/articles/2022/06/30/companies-are-desperate-for-cybersecurity-workers-more-than-700k-positions-need-to-be-filled/

- The number of unfilled cybersecurity jobs worldwide grew 350% between 2013 and 2021, from 1 million to 3.5 million, according to Cybersecurity Ventures.
- The industry researcher also predicts that in five years, the same number of jobs will still be open.

---

## CTF

----

### CTFs

- Capture the Flag
- team effort
- jeopardy or attack-defense
- https://ctftime.org/
- CTF USV, DefCamp CTF
- ACS IXIA CTF, spring 2024
- Security Summer School, summer 2024
  - https://security-summer-school.github.io/

----

### Wargames

- Challenge websites
- Do it when you want
- Similar challenges to CTFs
- Aggregator: http://www.wechall.net/

---

## CTF Topics

- Exploitation
- Web (Exploitation)
- Forensics / Misc
- Crypto

---

## Exploitation

----

### Overview

- Exploit software vulnerabilities
- Exploit hardware vulnerabilities
- Exploit misconfigurations
- RCE (_Remote Code Execution_)
- PrivEsc (_Privilege Escalation_)

----

### Tools of the Trade

- [pwntools](https://docs.pwntools.com/en/stable/)
- [Nessus](https://www.tenable.com/products/nessus)
- [OpenVAS](https://www.openvas.org/)
- [Metasploit](https://www.metasploit.com/)

----

### Demo

- **Hit me Hard** challenge
- Connect remotely to SSH
- Privilege escalation

---

## Web

----

### Overview

- Web is ubiquitous
- Large attack surface
- Can get access to system
  - Then you can move on to PrivEsc
- Access to database

----

### Tools of the Trade

- Browser developer tools
- [Burp Suite](https://portswigger.net/burp)
- [dirb](https://www.kali.org/tools/dirb/)
- [Postman](https://www.postman.com/)
- [ZAP](https://www.zaproxy.org/)
- [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA)

----

### Demo

- **Ping Me** challenge
- Command injection

---

## Forensics / Misc

----

### Overview

- Post-attack analysis
- Digital forensics
- Look for tracks in filesystem, disk, memory, processes, network traffic
- Figure out attack vector
- Report for future protection and for legal actions

----

### Tools of the Trade

- Basic OS analysis tools
- [Volatility](https://www.volatilityfoundation.org/)
- [Sleuth Kit](https://www.sleuthkit.org/)
- [CAINE](https://www.caine-live.net/)

----

### Demo

- **It's Right There** challenge
- Look for configuration information, think sudo
- Use the discovered information
- Hashed information **may** be revealed with [CrackStation](https://crackstation.net/)

---

## Crypto

----

### Overview

- Cryptographic primitives for digital data / transfer protection
- confidentiality, integrity, identity / authentication
- encryption, hash functions, key exchange, random number generator
- symmetric encryption
- public key cryptography
- keys, algorithms
- plaintext, ciphertext

----

### Tools of the Trade

- [RSA algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [AES algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [openssl](https://www.openssl.org/)
- [SSL Labs](https://www.ssllabs.com/ssltest/)

----

### Demo

- **Peas in a Pod** challenge
- RSA public key
- Find components of RSA algorithm
- Recreate private key
- Connect using SSH and get flag

---

## Challenges

- CTF Platform: https://workshop-ctf.security.cs.pub.ro
- You need an account
- Get flag, submit, get points
