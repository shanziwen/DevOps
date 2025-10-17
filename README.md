# DevOps
The project is used to deploy a knowledge base site for DevOps.

# How to Deploy Locally
The project can be deployed locally with Vagrant. It will come with all of prerequistes. 
1. run the following commands in the host machine.
    ```
    $ vagrant up
    $ vagrant ssh
    ```
2. run the following commands in the guest machine
    ```
    $ cd /vagrant/kb
    $ mkdocs serve
    ```
3. access the site via http://192.168.100.2:8000/

# Deploy to AWS 
The project includes a solution to deploy the knowledge base site to AWS. It uses S3 and CloudFront to host the sites.

1. run the following commands in the host machine.
    ```
    $ vagrant up
    $ vagrant ssh
    ```
2. run the following commands in the guest machine.
   ```
   $ cd /vagrant/kb
   $ mkdocs build
   $ cd cdk
   $ cdk deploy
   ```
# References
1. [mkdocs](https://www.mkdocs.org/)
2. [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
4. [mkdocs-literate-nav](https://oprypin.github.io/mkdocs-literate-nav/reference.html)