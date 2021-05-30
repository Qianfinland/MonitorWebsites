############# To run the test: go to the root directory <br />
$run.py monitor_websites <br />

############# Packages you might need to install: <br />
$ pip install requests<br />
$ pip install schedule<br />
$ pip install robotframework<br />

############# Example of the package version <br />
requests==2.19.1 <br />
schedule==1.1.0 <br />
robotframework==3.1.2 <br />

############# Other notes <br />
File variablefile.py contains example URLs and configurable interval in seconds, different envs.<br />
File monitorfile.log contains checked URLs, status codes and the server response times. <br />
File output/log.html, after extend Test, then child keyword, you will see HTML content of the webpage <br />
For example, after extend keyword, when search below text: <br />
Webpage "https://stackoverflow.com/users/login" works OK; the required page content "login-form" exits, page content " <br />
You will see corresponding HTML content <br />
