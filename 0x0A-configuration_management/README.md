# 0x0A Configuration management
 
 
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
 
As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.
 
---
 
## General Objectives:bulb:

 
---
 
## Instalation:wrench:
 
Follow the following instructions to get a copy of the program and run in your local machine.
 
* Clone the following repository.
```
https://github.com/PabloYepes27/holberton-system_engineering-devops.git
```

 
## Tasks:clipboard:
 
### [0. Create file](./0-create_a_file.pp)
* Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/holberton
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
 
 
### [1. Install a package](./1-install_a_package.pp)
* Using Puppet, install puppet-lint.

Requirements:

Install puppet-lint
Version must be 2.1.1
 
 
### [2. Execute a command](./2-execute_a_command.pp)
* Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
 
---
 
## Built with:hammer:
 
 * puppet-lint
---
 
## Resources:books:
 
Read or watch:
* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://puppet.com/docs/puppet/3.8/types/file.html)
* [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
* [Puppet lint](http://puppet-lint.com/)
* [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
 
---
 
## Author:black_nib:
 
* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)