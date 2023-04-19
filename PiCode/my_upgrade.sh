#!/bin/bash
# Update package list
sudo apt update
# Ask the user if they want to upgrade
read -p "Do you want to upgrade? [y/N] " answer
# Check if the answer is "y" or "Y"
if [[ "$answer" =~ ^[yY]$ ]]; then
# Upgrade packages
sudo apt upgrade -y
fi
