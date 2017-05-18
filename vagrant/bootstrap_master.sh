#!/usr/bin/env bash

echo "Installing update"
yum -y update
echo "Installing WGET"
yum -y install wget
echo "Downloading epel"
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
echo "Installing epel"
rpm -Uvh epel-release-7-9.noarch.rpm
echo "Installing Ansible"
yum -y install ansible