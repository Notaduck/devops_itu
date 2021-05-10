# -*- mode: ruby -*-
# vi: set ft=ruby :

# -------------------------------------------------------------------
# Configuration options
# -------------------------------------------------------------------
NUM_OF_MANAGERS=1
NUM_OF_WORKERS=1
DO_REGION="fra1"
DO_IMAGE="docker-18-04"
DO_SIZE="s-1vcpu-1gb"
DO_ACCESS_TOKEN=ENV['DIGITAL_OCEAN_TOKEN']
# -------------------------------------------------------------------
# (End configuration options)

# -- Internal variables
VAGRANTFILE_API_VERSION = "2"


@initManager = <<EOD
echo initManager arguments: $*
# Todo: We have an issue here, if re-creating the machines, then the old token will be re-used, which is wrong ...
sleep 60
if [ "$2" -eq "1" ]; then
    SWARM_MANAGER_IP=$(ifconfig eth1 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')
    mkdir -p /vagrant/.vagrant/swarm-token
    ls -a /vagrant
    ls -a /vagrant/.vagrant
    ls -a /vagrant/.vagrant/swarm-token
    chmod 777 /vagrant/.vagrant/swarm-token
    echo $SWARM_MANAGER_IP > /vagrant/.vagrant/swarm-manager-ip
    echo "SWARM_MANAGER_IP: $SWARM_MANAGER_IP"
    docker swarm init --advertise-addr $SWARM_MANAGER_IP:2377
    docker swarm join-token -q manager > /vagrant/.vagrant/swarm-token/manager
    docker swarm join-token -q worker > /vagrant/.vagrant/swarm-token/worker
else
    echo "Join swarm ...";
    echo "SWARM_MANAGER_IP: `cat /vagrant/.vagrant/swarm-manager-ip`";
    docker swarm join \
      --token `cat /vagrant/.vagrant/swarm-token/manager` \
      `cat /vagrant/.vagrant/swarm-manager-ip`:2377
fi
EOD

@initWorker = <<EOD
scp -r root@your.server.example.com:/vagrant/.vagrant/swarm-token/ /vagrant/.vagrant/swarm-token/

docker swarm join \
  --token `cat  /vagrant/.vagrant/swarm-token/worker` \
  10.114.0.3:2377
EOD


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provision "docker"
  config.vm.synced_folder "./remote_files", "/vagrant", disabled: false

  # Digital Ocean Configuration
  config.vm.provider :digital_ocean do |provider, override|
    override.ssh.private_key_path = './ssh_keys/id_rsa'
    provider.ssh_key_name = 'vagrant'
    override.vm.box = 'digital_ocean'
    override.vm.box_url = "https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box"
    override.vm.allowed_synced_folder_types = :rsync
    provider.token = DO_ACCESS_TOKEN
    provider.image = DO_IMAGE
    provider.region = DO_REGION
    provider.size = DO_SIZE
    provider.ipv6 = false
    provider.private_networking = true
  end


  (1..NUM_OF_MANAGERS).each do |mgrNumber|
    config.vm.define "manager-#{mgrNumber}" do |node|

        # node.vm.provision "shell", inline: <<-SHELL
        #   docker run --rm hello-world
        #   docker rmi hello-world

        #   echo ". $HOME/.bashrc" >> $HOME/.bash_profile
        #   echo -e "\nConfiguring credentials as environment variables...\n"
        #   echo "export DOCKER_USERNAME='xxxxxxx'" >> $HOME/.bash_profile
        #   echo "export DOCKER_PASSWORD='xxxxxxxxxxx!'" >> $HOME/.bash_profile
        #   source $HOME/.bash_profile
        # SHELL

        node.vm.synced_folder "./remote_files", "/vagrant", disabled: false
        node.vm.provision "shell", inline: @initManager, args: [ "#{NUM_OF_MANAGERS}" , "#{mgrNumber}" ]

        # Todo: Does at the end of the day not work, since the rsync sync-folders are not available for the 2nd manager ...
        # node.vm.provision "shell", inline: @initManager, args: [ "#{NUM_OF_MANAGERS}" , "#{mgrNumber}" ]

      end
    end # (end each)

  (1..NUM_OF_WORKERS).each do |workerNumber|
      config.vm.define "worker-#{workerNumber}" do |node|

        # node.vm.provision "shell", inline: "sudo mkdir /vagrant"
        node.vm.synced_folder "./remote_files", "/vagrant", disabled: false

      end
    end # (end each)

end
