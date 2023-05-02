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
# Program/Design Name:		rover_image_build_64bit.sh
# Description:    shell script to restore a Raspberry Pi after a clean 64 bit install 
# Dependencies:   
# Revision: 
#  Revision 0.02 - Updated 03/26/2019 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 03/26/2019
# Additional Comments: 
# see https://www.answers.com/Q/How_do_you_make_a_yes_no_command_in_cmd to add more features
# ============================================================================

echo " _  _  ___  ___   __  ____  __  _  _  __"
echo "( )( )(  ,\(   \ (  )(_  _)(  )( \( )/ _)"
echo " )()(  ) _/ ) ) )/__\  )(   )(  )  (( (/\ "
echo " \__/ (_)  (___/(_)(_)(__) (__)(_)\_)\__/ "
cd ~
pwd
ls -l

echo "----------------------------------------------------"
echo "Running Update"
echo "----------------------------------------------------"
echo " "
sudo apt update
echo " "
echo "----------------------------------------------------"
echo "Done running update"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "Running Upgrade with -y"
echo "----------------------------------------------------"
echo " "
sudo apt upgrade -y
echo " "
echo "----------------------------------------------------"
echo "Done running Upgrade"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "Installing Arduino"
echo "----------------------------------------------------"
echo " "
sudo apt install arduino -y
echo " "
echo "----------------------------------------------------"
echo "Done installing Arduino"
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "Installing git"
echo "----------------------------------------------------"
echo " "
sudo apt install git -y
echo " "
echo "----------------------------------------------------"
echo "Done installing git"
echo "----------------------------------------------------"
echo " "

echo "-------------------------------------------------------"
echo " Installing curl"
echo "-------------------------------------------------------"
sudo apt install curl -y
echo "-------------------------------------------------------"
echo "The UPGRADE will say:"
echo "   The following package was automatically installed"
RED_FG=`tput setaf 1`
GREEN_BG=`tput setab 2`
RESET=`tput sgr0`
echo "    ${RED_FG}${GREEN_BG}and is no longer required: libfuse${RESET}"
echo "    ${RED_FG}${GREEN_BG}and to use: 'sudo apt autoremove' to remove it.${RESET}"
echo "${RED_FG}DO NOT DO REMOVE IT.${RESET}  Looks like viam-server needs it"
echo "-------------------------------------------------------"
echo " "

echo "-------------------------------------------------------"
echo " ___    __  _  _  ___ "
echo "(   \  /  \( \( )(  _)"
echo " ) ) )( () ))  (  ) _)"
echo "(___/  \__/(_)\_)(___)"
echo "All Done"
