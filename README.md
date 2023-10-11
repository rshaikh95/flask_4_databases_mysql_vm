# flask_4_databases_mysql_vm
Week 4 Homework Assignment: MySQL on VMs with Azure and GCP

## Setting up VM 
1. Go in Azure under your student account

2. Create a VM using desired specifications for lowest cost (Standard 2vcpu 8GIB) B series B1ls

3. Create username and password and do not forget. Set port rules for HTTP, HTTPS, SSH

4. Connect MYSQL to Azure via create connection in MySQL Workbench.

5. Make sure host name, username, port and passowrd are correct when connecting. Cost should be 0.0104. Then Deploy and obtain host ip address.

6. Create port 3306 in Azure via an inbound securtiy role

7. Create a DB and two tables in MySQL ![image](https://github.com/rshaikh95/flask_4_databases_mysql_vm/assets/141374132/eac1f048-5017-4d2b-acfc-31f8ca48dfce)


8. Open up Google Shell and sudo apt install packages for MySql and update packages using sudo apt-get update. then log in to mysql on the terminal.

9. use the show database commands to show databases in mysql then create user and new database in shell. grant all priveleges

10. Connect MySQL to Azure via Python using code in class

11. use the sudo nano command to enter configurtion in google shell and change bind-address to 0.0.0.0 as well as mysql address to the same. ctrl o and ctrl x to save and exit. restart. Had many problems to connect including this one![image](https://github.com/rshaikh95/flask_4_databases_mysql_vm/assets/141374132/78ec464a-26ac-4710-ba19-87cf13a76d13)


12. Setup .env file with connections to make sure it is not public

13. Put together fake data for database via faker code (had error here)  ![Screenshot 2023-10-10 234203](https://github.com/rshaikh95/flask_4_databases_mysql_vm/assets/141374132/d350dddf-1671-41b0-963e-743fe1f50120)


14. Created Flask app and insert code for faker data inside flask app code  ![Screenshot 2023-10-10 234732](https://github.com/rshaikh95/flask_4_databases_mysql_vm/assets/141374132/0aa358d1-8631-466a-8938-9e8b3f4050fa)

15. Didnt have that error when using different locale ![Screenshot 2023-10-10 231435](https://github.com/rshaikh95/flask_4_databases_mysql_vm/assets/141374132/6bf7276d-5999-40c9-a744-92fd2283d009)

