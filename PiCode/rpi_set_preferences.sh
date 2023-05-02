#! /bin/sh


echo " _  _  ___  ___   __  ____  __  _  _  __"
echo "( )( )(  ,\(   \ (  )(_  _)(  )( \( )/ _)"
echo " )()(  ) _/ ) ) )/__\  )(   )(  )  (( (/\ "
echo " \__/ (_)  (___/(_)(_)(__) (__)(_)\_)\__/ "
cd ~
pwd
ls -l
sudo raspi-config nonint do_change_locale en_US.UTF-8
sudo raspi-config nonint do_configure_keyboard us
sudo raspi-config nonint do_change_timezone America/Los_Angeles

sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_vnc 0
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_serial 0
sudo raspi-config nonint do_onewire 0



echo "-------------------------------------------------------"
echo " ___    __  _  _  ___ "
echo "(   \  /  \( \( )(  _)"
echo " ) ) )( () ))  (  ) _)"
echo "(___/  \__/(_)\_)(___)"
echo "All Done"
sleep 10
sudo reboot
