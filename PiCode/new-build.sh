#! /bin/sh
# ============================================================================
# shell script to restore a Raspberry Pi after a clean 64 bit install
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/RaspberryPi
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:		new-pi-64bit-build-prep.sh
# Description:    shell script to restore a Raspberry Pi after a clean 64 bit 
#                 install, copies the shell scripts needed to build a viam rover 
# Dependencies:   
# Revision: 
#  Revision 0.02 - Updated 
#  Revision 0.01 - Created 04/25/2023
# Additional Comments: 
# see https://www.answers.com/Q/How_do_you_make_a_yes_no_command_in_cmd to add more features
# ============================================================================

echo "  _  _  ___  ___   __  ____  __  _  _  __ "
echo " ( )( )(  ,\(   \ (  )(_  _)(  )( \( )/ _) "
echo "  )()(  ) _/ ) ) )/__\  )(   )(  )  (( (/\ "
echo "  \__/ (_)  (___/(_)(_)(__) (__)(_)\_)\__/ "
cd ~
pwd
ls -l

echo "----------------------------------------------------"
echo "Running Update" $ sudo apt update
echo "----------------------------------------------------"
echo " "
sudo apt update
echo " "
echo "----------------------------------------------------"
echo "Done running update"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "Running Upgrade with -y"  $ sudo apt upgrade -y
echo "----------------------------------------------------"
echo " "
sudo apt upgrade -y
echo " "
echo "----------------------------------------------------"
echo "Done running Upgrade"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "copying github shell script to install basic tools and apps "
echo "wget -O rover_image_build_64bit.sh https://raw.githubusercontent.com/jimTheSTEAMClown/VIAM-Party-Rover-0/main/rover_image_build_64bit.sh"
echo "chmod 744 rover_image_build_64bit.sh"
echo "----------------------------------------------------"
echo " "
wget -O rover_image_build_64bit.sh https://raw.githubusercontent.com/jimTheSTEAMClown/VIAM-Party-Rover-0/main/rover_image_build_64bit.sh
chmod 744 rover_image_build_64bit.sh
echo " "
echo "----------------------------------------------------"
echo "Done copying & setting permissions to 744 for: rover_image_build_64bit.sh"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "copying github shell script to install the VIAM-SERVER "
echo "wget -O viam-new-setup.sh https://raw.githubusercontent.com/jimTheSTEAMClown/VIAM-Party-Rover-0/main/viam-new-setup.sh"
echo "chmod 744 viam-new-setup.sh"
echo "----------------------------------------------------"
echo " "
wget -O viam-new-setup.sh https://raw.githubusercontent.com/jimTheSTEAMClown/VIAM-Party-Rover-0/main/viam-new-setup.sh
sudo chmod 744 viam-new-setup.sh
echo " "
echo "----------------------------------------------------"
echo "Done copying & setting permissions to 744 for: viam-new-setup.sh"
echo " "

echo "----------------------------------------------------"
echo " ____  ____  ___  __  __  __   ____  ___ "
echo " (  _ \( ___)/ __)(  )(  )(  ) (_  _)/ __) "
echo "  )   / )__) \__ \ )(__)(  )(__  )(  \__ \ "
echo " (_)\_)(____)(___/(______)(____)(__) (___/ "
echo " "
cd ~
pwd
echo " Copied and set permissions for rover_image_build_64bit.sh"
ls -l rover_image_build_64bit.sh
echo " Copied and set permissions for viam-new-setup.sh"
ls -l viam-new-setup.sh

./rover_image_build_64bit.sh
./viam-new-setup.sh

echo " "
echo "-------------------------------------------------------"
echo "  ___    __  _  _  ___  "
echo " (   \  /  \( \( )(  _) "
echo "  ) ) )( () ))  (  ) _) "
echo " (___/  \__/(_)\_)(___) "
echo " "
echo "----------------------------------------------------"
echo "  _  _  ____  _  _  ____    ___  ____  ____  ____  ___ "
echo " ( \( )( ___)( \/ )(_  _)  / __)(_  _)( ___)(  _ \/ __) "
echo "  )  (  )__)  )  (   )(    \__ \  )(   )__)  )___/\__ \ "
echo " (_)\_)(____)(_/\_) (__)   (___/ (__) (____)(__)  (___/ "
echo " "
# echo " Run the following scripts"
# echo " ./rover_image_build_64bit.sh "
# echo " ./viam-new-setup.sh "
echo " Go to https://app.viam.com/robots"
echo " "
echo "All Done"
