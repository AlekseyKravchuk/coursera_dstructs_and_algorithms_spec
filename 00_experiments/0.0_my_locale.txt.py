as output of command locale:
LANG=en_US.UTF-8
LANGUAGE=en_US
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC=ru_RU.UTF-8
LC_TIME=ru_RU.UTF-8
LC_COLLATE="en_US.UTF-8"
LC_MONETARY=ru_RU.UTF-8
LC_MESSAGES="en_US.UTF-8"
LC_PAPER=ru_RU.UTF-8
LC_NAME=ru_RU.UTF-8
LC_ADDRESS=ru_RU.UTF-8
LC_TELEPHONE=ru_RU.UTF-8
LC_MEASUREMENT=ru_RU.UTF-8
LC_IDENTIFICATION=ru_RU.UTF-8
LC_ALL=


via configuring "/etc/default/locale":
LANG=en_US.utf8
LC_NUMERIC=ru_RU.UTF-8
LC_TIME=ru_RU.UTF-8
LC_MONETARY=ru_RU.UTF-8
LC_PAPER=ru_RU.UTF-8
LC_NAME=ru_RU.UTF-8
LC_ADDRESS=ru_RU.UTF-8
LC_TELEPHONE=ru_RU.UTF-8
LC_MEASUREMENT=ru_RU.UTF-8
LC_IDENTIFICATION=ru_RU.UTF-8


update/change the current default locale:
    sudo update-locale LANG=en_US.UTF-8
    sudo update-locale LANG="en_US.UTF-8" LANGUAGE="en_US"
    sudo dpkg-reconfigure locales

via configuring ".bashrc":
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

via configuring "/etc/environment":
    LC_ALL=en_US.UTF-8
    LANG=en_US.UTF-8

another way:
    sudo locale-gen en_US en_US.UTF-8
    sudo dpkg-reconfigure locales



You also have to edit /etc/profile:

    export LANG="en_US.utf8"
    export LANGUAGE="en_US.utf8"
    export LC_ALL="en_US.utf8"

From Ubuntu 18.04 upwards, you should issue "localectl status" to see the current locale and change it with
    "sudo localectl set-locale en_US.UTF-8"
My output:
kav@zeus:~$ localectl status
   System Locale: LANG=en_US.utf8
                  LC_NUMERIC=ru_RU.UTF-8
                  LC_TIME=ru_RU.UTF-8
                  LC_MONETARY=ru_RU.UTF-8
                  LC_PAPER=ru_RU.UTF-8
                  LC_NAME=ru_RU.UTF-8
                  LC_ADDRESS=ru_RU.UTF-8
                  LC_TELEPHONE=ru_RU.UTF-8
                  LC_MEASUREMENT=ru_RU.UTF-8
                  LC_IDENTIFICATION=ru_RU.UTF-8
       VC Keymap: n/a
      X11 Layout: us
       X11 Model: pc105


