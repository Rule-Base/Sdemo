# Sdemo
Sdemo - 1 Nginx LB + 2 Nginx AppServer (RoundRobin)
CREDIT - Codes used in this demo includes original codes from Glen Jarvis https://github.com/glenjarvis A New Nginx Load Balancer Role Added by me to load balance Round Robin between 2 Nginx App Server ( as required for this demo test) A live demo is currently available in AWS to show the required Round Robin feature (IP Addresses available upon request)

1. Clone this repo.

    prompt> git clone  https://github.com/Rule-Base/Sdemo.git

    

2. Change to the src directory.

    ```bash
    prompt> Sdemo/src

    ```

3. Configure the repo for your account and settings

    ```bash
    prompt> ( cd src; python configure.py )

    This script creates configuration files for using Ansible to
    configure a newly-created virtual machine.
    It has been tested by the author on an AWS free tier VM.
    This has the best chance of working on an AWS free tier VM, or
    failing that, on a VM with a recent version of CentOS.

        No configuration file found. Let me ask questions so that we can configure.

    What is the path to your .pem key file for  the virtual machine?
    --> ~/example_key.pem

    What user to use to ssh to the remote system [ec2-user]?
    -->
    Configuring `ansible_hosts` file ./ansible_hosts...

    What is the IP address of the virtual machine?
    --> <<Enter your external IP here>>

    Configuration is complete.

4. Change to the src directory.

    ```bash
    prompt> Sdemo/src/Sdemo_roles

    ```

   Then read the README.txt in Sdemo/src/Sdemo_roles  before running Stest_main.yml
   
5. Then run Stest_main.yml by following the instructions in  Sdemo/src/Sdemo_roles/README.txt

