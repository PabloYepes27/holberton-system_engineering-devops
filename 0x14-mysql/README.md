# 0x14. MySQL
 
 
## Contents:open_file_folder:
 
- Project Description:newspaper:
- General Objectives:bulb:
- Instalation:wrench:
- Tasks:clipboard:
- Built with:hammer:
- Resources:books:
- Author:black_nib:
 
---
 
## Project Description:newspaper:
 
A database is a collection of information that is organized so that it can be easily accessed, managed and updated. Computer databases typically contain aggregations of data records or files, containing information about sales transactions or interactions with specific customers.
 
---
 
## General Objectives:bulb:
 
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

 
---
 
## Instalation:wrench:
 
Follow the following instructions to get a copy of the program and run in your local machine.
 
* Clone the following repository.
```
https://github.com/PabloYepes27/holberton-system_engineering-devops.git
```
---
 
## Tasks:clipboard:
 
### [0. Install MySQL ]
* First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

MySQL distribution must be 5.7.x
Make sure that task #3 of your SSH project is completed for web-01 and web-02. The checker will connect to your servers to check MySQL status
Please make sure you have your README.md pushed to Github.
 
 
### [1. Let us in! ]
* In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.
Make sure that holberton_user has permission to check the primary/replica status of your databases.
In addition to that, make sure that task #3 of your SSH project is completed for web-01 and web-02. You will likely need to add the public key to web-02 as you only added it to web-01 for this project. The checker will connect to your servers to check MySQL status
 
 
### [2. If only you could see what I've seen with your eyes ]
* In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

Create a database named tyrell_corp.
Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.

### [3. Quite an experience to live in fear, isn't it?]
* Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
replica_user must have the appropriate permissions to replicate your primary MySQL server.
holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.


### [4. Setup a Primary-Replica infrastructure using MySQL]
* MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
* MySQL replica must be hosted on web-02
* Setup replication for the MySQL database named tyrell_corp
* Provide your MySQL primary configuration as answer file(my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary
* Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica


### [5. MySQL backup]
* Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

Requirements:

The MySQL dump must contain all your MySQL databases
The MySQL dump must be named backup.sql
The MySQL dump file has to be compressed to a tar.gz archive
This archive must have the following name format: day-month-year.tar.gz
The user to connect to the MySQL database must be root
The Bash script accepts one argument that is the password used to connect to the MySQL database



---
 
## Built with:hammer:

* Bash Scripts
* Mysql
 
---
 
## Resources:books:
 

* [What is a database](https://searchsqlserver.techtarget.com/definition/database)
* [What is a database master slave cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL master slave setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/features/mssql/developing-a-sql-server-backup-strategy.html)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)
* [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/features/mssql/developing-a-sql-server-backup-strategy.html)

 
---
 
## Author:black_nib:
 
* **Juan Pablo Yepes Tamayo**
 - [GitHub](https://github.com/PabloYepes27)
 - [Linkedin](https://www.linkedin.com/in/pablo-yepes-120495)
 - [Twitter](https://twitter.com/pabloyepes27)