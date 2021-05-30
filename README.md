#############To run the test: go to the root directory
$run.py monitor_websites

#############Packages you might need to install:
$ pip install requests
$ pip install schedule
$ pip install robotframework

#############Example of the package version
requests==2.19.1
schedule==1.1.0
robotframework==3.1.2

#############Other notes
File variablefile.py contains example URLs and configurable interval in seconds, different envs.
File monitorfile.log contains checked URLs, status codes and the server response times.
File output/log.html, after extend Test, then child keyword, you will see HTML content of the webpage
For example, after extend keyword, when search below text:
Webpage "https://stackoverflow.com/users/login" works OK; the required page content "login-form" exits, page content "
You will see corresponding HTML content
