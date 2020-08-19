# 0x10. HTTPS SSL
 
 
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
 
This is one of the last projects of the low level programming in the second quarter about makefiles, in this project you going to see what is and how to use the command "make"; also When, why and how to use Makefiles.
 
---
 
## General Objectives:bulb:
 
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

 
---
 
## Instalation:wrench:
 
Follow the following instructions to get a copy of the program and run in your local machine.
 
* Clone the following repository.
```
https://github.com/PabloYepes27/holberton-system_engineering-devops.git
```
---
 
## Tasks:clipboard:
 
### [0. HTTPS ABC]
* Requirements
 
 
### [1. World wide web]
* Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.
 
 
### [2. HAproxy SSL termination]
* “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..
 
 
### [3. No loophole in your website traffic]
* A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

---
 
## Built with:hammer:

* Bash Scripts
 
---
 
## Resources:books:
 

* [What is HTTPS?](https://www.instantssl.com/http-vs-https)
* [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
* [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
* [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
* [Bash function](http://tldp.org/LDP/abs/html/complexfunct.html)
 
---
 
## Author:black_nib:
 
* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)