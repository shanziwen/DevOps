# Concepts
`Docker Client`
:

- The Docker client is the command-line tool (docker) or GUI that users interact with.
- It sends commands like docker build, docker run, or docker pull to the Docker daemon.
- The client can communicate with a local or remote Docker server using REST APIs.

`Docker Server (Docker Daemon)`
:

- The Docker daemon (dockerd) is the background service that does the heavy lifting.
- It listens for Docker API requests and manages container lifecycle: building images, running containers, networking, and volumes.
- It can run locally or on a remote host, allowing centralized container management.

`Docker Images/OCI Images`
:

- A Docker image is a read-only template that contains everything needed to run an application: code, runtime, libraries, environment variables, and configuration files.
- OCI (Open Container Initiative) images are a standardized format derived from Docker’s image specification (specifically Docker v2.2).
- Most modern container tools (like Podman, containerd, CRI-O) support OCI images, ensuring interoperability across platforms.

`Containers`
:

- A container is a running instance of an image.
- It’s an isolated process with its own filesystem, network stack, and resource limits.
- Containers are lightweight and share the host OS kernel, making them faster and more efficient than virtual machines.

`Image Registry`
:

- A server-side application that hosts and serves container images. 
- These images are used to create containers on any system that supports container runtimes like Docker or containerd.

`Image Repository`
:

- A collection of related images.

`Image Tags`
: 

- Labels that identify specific versions of an image.