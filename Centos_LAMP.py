#!/usr/bin/env python2
# importing the module 
import os
import random
print("Launching Terminal User Interface")
print("\t\tWELCOME TO INSTALL LAMP\t\t")
print("\t-------------------------------------------------\t")
print("Entering for Setup")
random_string = ''
for _ in range(16):
    # Considering only upper and lowercase letters
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    # Convert to lowercase if the flip bit is on
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))
while True:
    print(""" 
        1.Install wget vim net-tools
        2.Disable Selinux
        3.Install epel-release
        4.remi-release
        5.System update
        6.Httpd
        7.Php
        8.PhpMyAdmin
        9.Maridb
        10.MySql
        11.Reboot
        12.Exit
        """)
    ch = int(input("Enter your choice: "))
    if (ch == 1):
        os.system("sudo yum install wget vim net-tools -y")
    elif ch == 2:
        a_file = open("/etc/selinux/config", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[6] = "SELINUX=disabled\n"
        a_file = open("/etc/selinux/config", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        print("Done")
    elif ch == 3:
        os.system("sudo wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
        os.system("sudo rpm -Uvh epel-release-latest-7.noarch.rpm")
        os.system("sudo yum install -y epel-release")
    elif ch == 4:
        os.system("sudo wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm")
        os.system("sudo rpm -Uvh remi-release-7.rpm")
        os.system("sudo yum install -y yum-utils")
    elif ch == 5:
        os.system("yum install update -y")
    elif ch == 6:
        os.system("sudo yum install httpd -y")
        os.system("sudo firewall-cmd --permanent --add-service=http")
        os.system("sudo firewall-cmd --permanent --add-service=https")
        os.system("sudo firewall-cmd --reload")
        os.system("sudo systemctl start httpd")
        os.system("sudo systemctl enable httpd")
        os.system("sudo systemctl status httpd")
    elif ch == 7:
        print("First check remi-repo installed")
        print("""
        1.php54
        2.php70
        3.php71
        4.php72
        5.php73
        6.php74
        7.php80
        8.Exit
        """)
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            os.system("sudo yum install -y php")
        elif ch == 2:
            os.system("yum-config-manager --enable remi-php70")
            os.system("sudo yum install -y php")
        elif ch == 3:
            os.system("yum-config-manager --enable remi-php71")
            os.system("sudo yum install -y php")
        elif ch == 4:
            os.system("yum-config-manager --enable remi-php72")
            os.system("sudo yum install -y php")
        elif ch == 5:
            os.system("yum-config-manager --enable remi-php73")
            os.system("sudo yum install -y php")
        elif ch == 6:
            os.system("yum-config-manager --enable remi-php74")
            os.system("sudo yum install -y php")
        elif ch == 7:
            os.system("yum-config-manager --enable remi-php80")
            os.system("sudo yum install -y php")
        elif ch == 8:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 8:
        print("First Install Php")
        os.system("sudo yum --enablerepo=remi install -y phpMyAdmin")
        a_file = open("/etc/httpd/conf.d/phpMyAdmin.conf", "r")
        list_of_lines = a_file.readlines()
        list_of_lines[12] = "Require all granted\n"
        list_of_lines[13] = "#Require local\n"
        a_file = open("/etc/httpd/conf.d/phpMyAdmin.conf", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        os.system("sudo systemctl restart httpd")
    elif ch == 9:
        print("""
        1.mariadb10.5
        2.mariadb10.4
        3.mariadb10.3
        4.mariadb10.2
        5.Exit
        """)
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            textlist1 = ["[mariadb10.5]", "name = MariaDB 10.5", "baseurl = http://yum.mariadb.org/10.5/centos7-amd64",
                         "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB", "gpgcheck=1", "enabled=1"]
            file = open("/etc/yum.repos.d/mariadb.repo", "w+")
            for line in textlist1:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum install -y MariaDB-server")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system("sudo firewall-cmd --add-service=mysql --permanent")
            os.system("sudo firewall-cmd --reload")
            os.system("sudo mysql_secure_installation <<EOF\n y\n db_user\n db_pwd\n y\n y\n y\n y\n EOF")
            os.system(str("mysqladmin -u root -p'' password ") + str(random_string))
            print('MariaDB Password is :', random_string)
        elif ch == 2:
            print('Wait for setup Maridb')
            textlist2 = ["[mariadb10.4]", "name = MariaDB 10.4", "baseurl = http://yum.mariadb.org/10.4/centos7-amd64",
                         "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB", "gpgcheck=1", "enabled=1"]
            file = open("/etc/yum.repos.d/mariadb.repo", "w+")
            for line in textlist2:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum install -y MariaDB-server")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system("sudo firewall-cmd --add-service=mysql --permanent")
            os.system("sudo firewall-cmd --reload")
            os.system("sudo mysql_secure_installation <<EOF\n y\n db_user\n db_pwd\n y\n y\n y\n y\n EOF")
            os.system(str("mysqladmin -u root -p'' password ") + str(random_string))
            print('MariaDB Password is :', random_string)
        elif ch == 3:
            print('Wait for setup Maridb')
            textlist3 = ["[mariadb10.3]", "name = MariaDB 10.3", "baseurl = http://yum.mariadb.org/10.3/centos7-amd64",
                         "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB", "gpgcheck=1", "enabled=1"]
            file = open("/etc/yum.repos.d/mariadb.repo", "w+")
            for line in textlist3:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum install -y MariaDB-server")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system("sudo firewall-cmd --add-service=mysql --permanent")
            os.system("sudo firewall-cmd --reload")
            os.system("sudo mysql_secure_installation <<EOF\n y\n db_user\n db_pwd\n y\n y\n y\n y\n EOF")
            os.system(str("mysqladmin -u root -p'' password ") + str(random_string))
            print('MariaDB Password is :', random_string)
        elif ch == 4:
            print('Wait for setup Maridb')
            textlist4 = ["[mariadb10.2]", "name = MariaDB 10.2", "baseurl = http://yum.mariadb.org/10.2/centos7-amd64",
                         "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB", "gpgcheck=1", "enabled=1"]
            file = open("/etc/yum.repos.d/mariadb.repo", "w+")
            for line in textlist4:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum install -y MariaDB-server")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system("sudo firewall-cmd --add-service=mysql --permanent")
            os.system("sudo firewall-cmd --reload")
            os.system("sudo mysql_secure_installation <<EOF\n y\n db_user\n db_pwd\n y\n y\n y\n y\n EOF")
            os.system(str("mysqladmin -u root -p'' password ") + str(random_string))
            print('MariaDB Password is :', random_string)
        elif ch == 5:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 10:
        print("""
        1.MySQL-server-8.0
        2.MySQL-server-5.7
        3.MySQL-server-5.6
        4.Exit
        """)
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            textlist21 = ["[mysql80-community]", "name=MySQL 8.0 Community Server",
                          "baseurl=http://repo.mysql.com/yum/mysql-8.0-community/el/7/$basearch/",
                          "gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql", "gpgcheck=0", "enabled=1"]
            file = open("/etc/yum.repos.d/mysql-community.repo", "w+")
            for line in textlist21:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum module disable mysql")
            os.system("sudo yum install -y mysql-community-server")
            os.system("sudo systemctl start  mysqld")
            os.system("sudo systemctl enable  mysqld")
            pwd = os.system("sudo grep 'temporary password' /var/log/mysqld.log")
            print("SQL Temporary Password")
            os.system("echo $pwd")
        elif (ch == 2):
            textlist21 = ["[mysql57-community]", "name=MySQL 5.7 Community Server",
                          "baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/",
                          "gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql", "gpgcheck=0", "enabled=1"]
            file = open("/etc/yum.repos.d/mysql-community.repo", "w+")
            for line in textlist21:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum module disable mysql")
            os.system("sudo yum install -y mysql-community-server")
            os.system("sudo systemctl start  mysqld")
            os.system("sudo systemctl enable  mysqld")
            pwd = os.system("sudo grep 'temporary password' /var/log/mysqld.log")
            print("SQL Temporary Password")
            os.system("echo $pwd")
        elif (ch == 3):
            textlist22 = ["[mysql56-community]", "name=MySQL 5.6 Community Server",
                          "baseurl=http://repo.mysql.com/yum/mysql-5.6-community/el/7/$basearch/",
                          "gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql", "gpgcheck=0", "enabled=1"]
            file = open("/etc/yum.repos.d/mysql-community.repo", "w+")
            for line in textlist22:
                file.write(line)
                file.write("\n")
            file.close()
            os.system("sudo yum module disable mysql")
            os.system("sudo yum install -y mysql-community-server")
            os.system("sudo systemctl start  mysqld")
            os.system("sudo systemctl enable  mysqld")
            pwd = os.system("sudo grep 'temporary password' /var/log/mysqld.log")
            print("SQL Temporary Password")
            os.system("echo $pwd")
        elif ch == 5:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 11:
        os.system("sudo reboot")
    elif ch == 12:
        print("Exiting application")
        exit()
    else:
        print("Invalid entry")
