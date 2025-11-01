# Basics
## Components
* containerd
* runc
* iptables
* virtual bridging
* linux cgroups
* linux namespaces
* linux capabilities
* secure computing mode
* filesystem drivers
  
## Tools
Swarm Mode
Compose


## Installation
Refer to https://docs.docker.com/engine/install/
## Docker Server
### Portocol:
* Unix Socket
* TCP:
  * 2375 - unencrypted
  * 2376 - encrypted
  * 2377 - Docker Swarm Mode

### Configuration
|OS and configuration|File location|
|----|----|
|Linux, regular setup|/etc/docker/daemon.json|
|Linux, rootless mode|~/.config/docker/daemon.json|

The available configure keys are same as dockerd command options (If the options value is a list, then the corresponding configuration key name is suffixed with 's', for example, `--host` -> `hosts`).

## Docker Client
Profiles - docker context