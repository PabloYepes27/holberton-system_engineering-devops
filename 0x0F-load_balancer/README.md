# 0x0F. Load balancer
 
<gif  width="520"  alt="image"  src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png">
 
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
 
You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.
 
---
 
## General Objectives:bulb:
 

 
---
 
## Instalation:wrench:
 
Follow the following instructions to get a copy of the program and run in your local machine.
 
* Clone the following repository.
```
https://github.com/PabloYepes27/holberton-system_engineering-devops.git
```

---
 
## Tasks:clipboard:
 
### [0. Double the number of webservers ]
* Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02
 
 
### [1. Install your load balancer]
* Install and configure HAproxy on your lb-01 server.
 
 
### [2. Add a custom HTTP header with Puppet]
* Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
 
---
 
## Built with:hammer:

-	Puppets
-	nginx
-	HAproxy
-	Shell script
 
---
 
## Resources:books:
 
Read or watch:
* [Load Balancer](https://intranet.hbtn.io/concepts/46)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
 
---
 
## Author:black_nib:
 
* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)