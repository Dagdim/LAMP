#!/usr/bin/env python2
import os

print("Launching Terminal User Interface")
print("\t\tWELCOME TO INSTALL LAMP\t\t")
print("\t-------------------------------------------------\t")
print("Entering for Setup")
while True:
    print("""
    1.System update
    2.Apache2
    3.Php
    4.PhpMyAdmin
    5.Mariadb
    6.MySql
    7.Reboot
    8.Exit
    """)
    ch = int(input("Enter your choice: "))
    if (ch == 1):
        os.system("sudo apt-get -y update")
    elif ch == 2:
        os.system("sudo apt-get install -y apache2")
        os.system("sudo ufw allow 80/tcp")
        os.system("sudo ufw allow 443/tcp")
        os.system("sudo ufw reload")
        os.system("sudo systemctl start apache2")
        os.system("sudo systemctl enable apache2")
    elif ch == 3:
        os.system("sudo apt-get install -y language-pack-en-base")
        os.system("sudo LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php")
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
            os.system("sudo apt-get install -y php5.4 php5.4-mbstring php5.4-mysql php5.4-xml")
        elif ch == 2:
            os.system("sudo apt-get install -y php7.0 php7.0-mbstring php7.0-mysql php7.0-xml")
        elif ch == 3:
            os.system("sudo apt-get install -y php7.1 php7.1-mbstring php7.1-mysql php7.1-xml")
        elif ch == 4:
            os.system("sudo apt-get install -y php7.2 php7.2-mbstring php7.2-mysql php7.2-xml")
        elif ch == 5:
            os.system("sudo apt-get install -y php7.3 php7.3-mbstring php7.3-mysql php7.3-xml")
        elif ch == 6:
            os.system("sudo apt-get install -y php7.4 php7.4-mbstring php7.4-mysql php7.4-xml")
        elif ch == 7:
            os.system("sudo apt-get install -y php8.0 php8.0-mbstring php8.0-mysql php8.0-xml")
        elif ch == 8:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 4:
        print("First Install Php and Database")
        os.system("sudo wget https://files.phpmyadmin.net/phpMyAdmin/5.1.0/phpMyAdmin-5.1.0-all-languages.zip")
        os.system("sudo apt install -y unzip")
        os.system("sudo unzip phpMyAdmin-5.1.0-all-languages.zip")
        os.system("sudo mv phpMyAdmin-5.1.0-all-languages /usr/share/phpMyAdmin")
        os.system("sudo mv phpMyAdmin.conf.example /etc/apache2/sites-enabled/phpMyAdmin.conf")
        os.system("sudo apt-get install -y php-mysql libjs-sphinxdoc dbconfig-mysql php-php-gettext")
        os.system("sudo apt-get install -y dbconfig-no-thanks")
        os.system("sudo systemctl restart apache2")
    elif ch == 5:
        os.system("sudo apt-key adv --fetch-keys 'https://mariadb.org/mariadb_release_signing_key.asc'")
        print("""
        1.mariadb10.5
        2.mariadb10.4
        3.mariadb10.3
        4.mariadb10.2
        5.Exit
        """)
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            os.system(
                "sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] https://mirror.terrahost.no/mariadb/repo/10.5/ubuntu bionic main'")
            os.system("sudo apt update")
            os.system("sudo apt install -y mariadb-server-10.5")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system(
                "sudo mysql_secure_installation <<EOF\n y\n y\n y\n kiRtZuiMzoT3cEci\n kiRtZuiMzoT3cEci\n y\n y\n y\n y\n EOF")
            print('Mariadb Password is : kiRtZuiMzoT3cEci')
        elif ch == 2:
            os.system(
                "sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] https://mirror.terrahost.no/mariadb/repo/10.4/ubuntu bionic main'")
            os.system("sudo apt update")
            os.system("sudo apt-get install -y mariadb-server-10.4")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system(
                "sudo mysql_secure_installation <<EOF\n y\n y\n y\n kiRtZuiMzoT3cEci\n kiRtZuiMzoT3cEci\n y\n y\n y\n y\n EOF")
            print('Mariadb Password is : kiRtZuiMzoT3cEci')
        elif ch == 3:
            os.system("sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] https://mirror.terrahost.no/mariadb/repo/10.3/ubuntu bionic main'")
            os.system("sudo apt update")
            os.system("sudo apt-get install -y mariadb-server-10.3")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system(
                "sudo mysql_secure_installation <<EOF\n y\n y\n y\n kiRtZuiMzoT3cEci\n kiRtZuiMzoT3cEci\n y\n y\n y\n y\n EOF")
            print('Mariadb Password is : kiRtZuiMzoT3cEci')
        elif ch == 4:
            os.system(
                "sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] https://mirror.terrahost.no/mariadb/repo/10.2/ubuntu bionic main'")
            os.system("sudo apt update")
            os.system("sudo apt-get install -y mariadb-server-10.2")
            os.system("sudo systemctl start mariadb")
            os.system("sudo systemctl enable mariadb")
            os.system(
                "sudo mysql_secure_installation <<EOF\n y\n y\n y\n kiRtZuiMzoT3cEci\n kiRtZuiMzoT3cEci\n y\n y\n y\n y\n EOF")
            print('Mariadb Password is : kiRtZuiMzoT3cEci')
        elif ch == 5:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 6:
        os.system("sudo apt-get install wget")
        print("""
            1.MySQL-server-8.0
            2.MySQL-server-5.7
            3.Exit
            """)
        ch = int(input("Enter your choice: "))
        if (ch == 1):
            os.system("sudo wget https://repo.mysql.com//mysql-apt-config_0.8.16-1_all.deb")
            os.system("sudo dpkg -i mysql-apt-config_0.8.16-1_all.deb")
            os.system("sudo apt update")
            os.system("sudo apt-get install -y mysql-server")
            os.system("sudo mysql_secure_installation")
        elif ch == 2:
            os.system("sudo apt install -y mysql-server")
            os.system("sudo systemctl start  mysqld")
            os.system("sudo systemctl enable  mysqld")
            os.system("sudo mysql_secure_installation")
        elif ch == 3:
            print("Exiting application")
            exit()
        else:
            print("Invalid entry")
    elif ch == 7:
        os.system("sudo reboot")
    elif ch == 8:
        print("Exiting Script")
        exit()
    else:
        print("Invalid entry")
