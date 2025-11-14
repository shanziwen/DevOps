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
* libcontainer - a GO library to provide a standard interface for linux container management from applications
  
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
- Profiles - docker context
- Commands
  - `attach`      (Attach local standard input, output, and error streams to a running container)
  - `bake`        (Build from a file)
  - `build`       (Build an image from a Dockerfile)
  - `builder`     (Manage builds)
  - `buildx`      (Docker Buildx)
  - `checkpoint`  (Manage checkpoints)
  - `commit`      (Create a new image from a container's changes)
  - `compose`     (Docker Compose)
  - `config`      (Manage Swarm configs)
  - `container`   (Manage containers)
  - `context`     (Manage contexts)
  - `cp`          (Copy files/folders between a container and the local filesystem)
  - `create`      (Create a new container)
  - `diff`        (Inspect changes to files or directories on a container's filesystem)
  - `events`      (Get real time events from the server)
  - `exec`        (Execute a command in a running container)
  - `export`      (Export a container's filesystem as a tar archive)
  - `help`        (Help about the command)
  - `history`     (Show the history of an image)
  - `image`       (Manage images)
  - `images`      (List images)
  - `import`      (Import the contents from a tarball to create a filesystem image)
  - `info`        (Display system-wide information)
  - `inspect`     (Return low-level information on Docker objects)
  - `kill`        (Kill one or more running containers)
  - `load`        (Load an image from a tar archive or STDIN)
  - `login`       (Authenticate to a registry)
  - `logout`      (Log out from a registry)
  - `logs`        (Fetch the logs of a container)
  - `manifest`    (Manage Docker image manifests and manifest lists)
  - `network`     (Manage networks)
  - `node`        (Manage Swarm nodes)
  - `pause`       (Pause all processes within one or more containers)
  - `plugin`      (Manage plugins)
  - `port`        (List port mappings or a specific mapping for the container)
  - `ps`          (List containers)
  - `pull`        (Download an image from a registry)
  - `push`        (Upload an image to a registry)
  - `rename`      (Rename a container)
  - `restart`     (Restart one or more containers)
  - `rmi`         (Remove one or more images)
  - `rm`          (Remove one or more containers)
  - `run`         (Create and run a new container from an image)
  - `save`        (Save one or more images to a tar archive (streamed to STDOUT by default))
  - `search`      (Search Docker Hub for images)
  - `secret`      (Manage Swarm secrets)
  - `service`     (Manage Swarm services)
  - `stack`       (Manage Swarm stacks)
  - `start`       (Start one or more stopped containers)
  - `stats`       (Display a live stream of container(s) resource usage statistics)
  - `stop`        (Stop one or more running containers)
  - `swarm`       (Manage Swarm)
  - `system`      (Manage Docker)
  - `tag`         (Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE)
  - `top`         (Display the running processes of a container)
  - `trust`       (Manage trust on Docker images)
  - `unpause`     (Unpause all processes within one or more containers)
  - `update`      (Update configuration of one or more containers)
  - `version`     (Show the Docker version information)
  - `volume`      (Manage volumes)
  - `wait`        (Block until one or more containers stop, then print their exit codes)
## Docker Images
- Dockerfile
  - Directives
    - ARG
    - LABEL
    - FROM
    - WORKDIR
    - USER
    - ENV
    - CMD
    - ENTRYPOINT
    - ADD
    - COPY
    - EXPOSE
  - Practice
    - Do not use the commands that're not idempotent in the final image's Dockerfile
    - Do not run main process using `root` user
    - Due to layer caching mechanism, order commands so that the things that change between every single build are closer to the bottom
      - use `#syntax=docker/dockerfile:1` to tell docker to use a newer version of the Dockerfile frontend.
    - Keep Image Small
      - Combine related commands into one RUN with && and clean up temp files.
      - Use .dockerignore to exclude unnecessary files from COPY.
      - Prefer slim base images (alpine, debian:bullseye-slim, etc.).
      - Avoid installing dev tools in production images.
      - Use multi-stage builds to separate build-time and runtime dependencies.

  - Tools
    - [Dive](https://github.com/wagoodman/dive): Analyze Diva Image for each layer  
  - How To
    - How To Build MultiStage Image
      - User `FROM <image_name> as <stage_name>` and `COPY --from <stage_name>` Directive to build multistage images
    - How To Build Multi Architecture Image
      - Use buildx plugin to create builder instance and build image
        - `docker buildx create --name container-builde --driver docker-container --bootstrap --use`
        - `docker build --builder <builder_instance_name> --platform linux/arm64 --tag <tag_name> --push .`
      - Use manifest to create a manifest with multiple images, annotate the image for architect and os version and then push to registry
  - Things to know
    - There're some zero length files in the layers which are required for all linux container and will be mounted from host
    - Layers are additive and deleting file in the higher layer won't remove them from the lower layer and won't reduce the image size
    - 
## Docker Registry
### How to Setup a Private Registry

##