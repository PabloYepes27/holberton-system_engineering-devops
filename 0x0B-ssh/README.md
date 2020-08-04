# 0x0B. SSH
 
 
## Contents:open_file_folder:
 
- Project Description:newspaper:
- General Objectives:bulb:
- Instalation:wrench:
- Command Interpreter Description:computer:
 
	* How to start it
	* Commands and their usage
	* How to use it
	* examples
 
- Unittests:boom:
- Tasks:clipboard:
- Built with:hammer:
- Resources:books:
- Author:black_nib:
 
---
 
## Project Description:newspaper:
 
SSH, or secure shell, is a secure protocol and the most common way of safely administering remote servers. Using a number of encryption technologies, SSH provides a mechanism for establishing a cryptographically secured connection between two parties, authenticating each side to the other, and passing commands and output back and forth.
 
---
 
## General Objectives:bulb:
 
* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash
 
---
 
## Instalation:wrench:
 
Follow the following instructions to get a copy of the program and run in your local machine.
 
* Clone the following repository.
```
https://github.com/PabloYepes27/holberton-system_engineering-devops.git
```

 
## Tasks:clipboard:
 
### [0. Use a private key ](./0-use_a_private_key)
* Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase
 
 
### [1. Create an SSH key pair](./1-create_ssh_key_pair)
* Write a Bash script that creates an RSA key pair.

Requirements:

Name of the created private key must be holberton
Number of bits in the created key to be created 4096
The created key must be protected by the passphrase betty
 
 
### [2. Client configuration file ](./2-ssh_config)
* Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

### [3. Let me in! ]
* Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.
 
 
### [4. Client configuration file (w/ Puppet)](./4-puppet_ssh_config.pp)
* Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
 
---
 
## Built with:hammer:
 
* puppet-lint
* Bash scripts
* ssh
* ssh-keygen
* env

---
 
## Resources:books:
 
Read or watch:
* [server](https://intranet.hbtn.io/concepts/67)
* [PWhat is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
* [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](https://www.ssh.com/ssh/config/)
* [Public Key Authentication for SSH](https://www.ssh.com/ssh/public-key-authentication)
* [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
* [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc)
* [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
* [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
* [IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)
* [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force)
* [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments)

---
 
## Author:black_nib:
 
* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)