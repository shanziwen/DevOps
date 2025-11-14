# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "generic/ubuntu2204"
  config.ssh.insert_key = false
  config.vm.box_version = "4.3.12"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # Disable the default share of the current code directory. Doing this
  # provides improved isolation between the vagrant box and your host
  # by making sure your Vagrantfile isn't accessible to the vagrant box.
  # If you use this you may want to enable additional shared subfolders as
  # shown above.
  # config.vm.synced_folder ".", "/vagrant", disabled: true

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.synced_folder "./", "/vagrant"
  config.vm.define "vagrant-kb" do |kb|
    kb.vm.synced_folder "~/.aws/", "/home/vagrant/.aws"
    kb.vm.network "private_network", ip: "192.168.100.2"
    kb.vm.provider "vmware_desktop" do |vm|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
  
    # Customize the amount of memory on the VM:
      vm.vmx["memsize"] = "4096"
      vm.vmx["numvcpus"] = "2"
    end
    kb.vm.provision "shell", privileged: false, inline: <<-SHELL
      sudo apt-get update
      # Install nodejs, npm and aws-cdk package
      wget -qO /tmp/node-v22.14.0-linux-x64.tar.xz https://nodejs.org/dist/v22.14.0/node-v22.14.0-linux-x64.tar.xz
      sudo tar -C /usr --strip-components=1 -xvf /tmp/node-v22.14.0-linux-x64.tar.xz
      sudo npm install -g aws-cdk
      # Install python3.11, mkdoc and aws-cdk-lib package
      sudo apt-get install -y python3.11-full
      wget -qP /tmp https://bootstrap.pypa.io/get-pip.py
      sudo python3.11 /tmp/get-pip.py
      sudo pip3.11 install mkdocs aws-cdk-lib
      # Install aws cli
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -so "/tmp/awscliv2.zip"
      unzip -d /tmp /tmp/awscliv2.zip
      sudo /tmp/aws/install
      # Install mkdocs and plugins
      sudo pip3.11 install -r /vagrant/requirements.txt
    SHELL
  end

  config.vm.define "vagrant-docker-master" do |dm|
    dm.vm.network "private_network", ip: "192.168.100.3"
    dm.vm.provider "vmware_desktop" do |vm|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
  
    # Customize the amount of memory on the VM:
      vm.vmx["memsize"] = "4096"
      vm.vmx["numvcpus"] = "2"
    end
    dm.vm.provision "shell", privileged: false, inline: <<-SHELL
      sudo apt-get update
      for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc
      do
        sudo apt-get remove $pkg
      done
      # Add Docker's official GPG key:
      sudo apt-get install -y ca-certificates curl
      sudo install -m 0755 -d /etc/apt/keyrings
      sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
      sudo chmod a+r /etc/apt/keyrings/docker.asc

      # Add the repository to Apt sources:
      echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      sudo apt-get update
      sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

      sudo install -g root -o root -m 660 /vagrant/docker/master/daemon.json /etc/docker/
      sudo sed -i -e 's#ExecStart=.*#ExecStart=/usr/bin/dockerd --config-file /etc/docker/daemon.json#' /lib/systemd/system/docker.service
      sudo systemctl daemon-reload
      sudo systemctl restart docker.service
      sudo docker context create master --docker "host=tcp://127.0.0.1:2375"
      sudo docker context use master
    SHELL
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
end