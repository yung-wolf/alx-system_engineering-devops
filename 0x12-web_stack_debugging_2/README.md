# 0x12-web_stack_debugging_2
Another installment of the debugging series.

NGINX master process is usually started with root privileges to listen on ports 80 and 443. However, to improve web server security, it is recommended to run NGINX as a non-root user with only necessary privileges. This can be achieved by creating a unique, unprivileged user and group for the server application. 

Running NGINX as a non-root user limits the potential impact of an attack, as the permissions of the NGINX user are significantly less than those of the root user. It is essential to avoid running web servers as root, which is often the default configuration. By doing so, you can reduce the risk of an attacker logging in as root and gaining complete control over your Unix machine. Therefore, always follow the best practice of running the NGINX process as the less privileged NGINX user.

## Environment
- OS: Ubuntu 20.04 LTS
- Language: Bash Script
- Web Server: Nginx
- Style Guide: Shellcheck

## Author
yung-wolf
