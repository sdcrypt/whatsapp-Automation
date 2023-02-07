This project provides an automation solution for sending messages on WhatsApp Web using the Selenium library in Python.

## Major Requirements
* Python 3.x
* Selenium library
* Google Chrome or Chromium-based browser
* ChromeDriver

### ChromeDriver (installation instructions)
Download the chromeDriver from [Here](https://chromedriver.chromium.org/downloads).
Note: download chromeDriver which is same as your chrome version. Keep it in root directory.

To check the root directory, run below code in shell.
```
print(os.path.join(os.getcwd(), "chromedriver"))
```


### Usage
Clone the repository and navigate to the directory:

Copy code
```
$ git clone https://github.com/sdcrypt/whatsapp-automation.git
$ cd <whatsapp-automation.git>
```
Install the required libraries:

```
$ pip install -r requirements.txt
```
### Run the application:

* check the apis from urls.py 
* upload excel sheet with contacts in it and send message as text.
```
$ python manage.py runserver
```
* Scan the QR code on WhatsApp Web to log in
* After it gets logged in press ENTER

### Note
Please use this project for educational purposes only. Abusing this automation for spamming or any unethical behavior is not condoned and goes against the terms of service of WhatsApp.