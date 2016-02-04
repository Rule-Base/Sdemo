Welcome
=======

Roles
=====
Review these roles:

* common
* app_server_django
* python_stack
* web_server_nginx
* loadbalancer_nginx


Run This Ansible Playbook
=========================
1. Run ansible-playbook Stest_main.yml
2. Log into the two AppServer and run next CLI; sudo su - webuser; cd /home/webuser/sample_project; python manage.py runserver
3. Go to external IP of load balancer via a web browser to test by refreshing the pages; each GET request is served in a round-robin mode between the two app servers.
