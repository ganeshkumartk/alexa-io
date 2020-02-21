<h1 align="center">
  <br>
  <a href="https://github.com/CoDeRgAnEsh/alexa-io"><img src="docs/alexa.png" alt="pic2pill" width="200"></a>
  <br>
  AlexaIO
  <br>
</h1>
<h4 align="center">Alexa Triggered LED via Adafruit Python IO in Raspberry Pi & IFTTT !</h4>


## Usage

* Open CLI(cmd prompt)/Terminal

* Git Clone this repo
~~~bash
git clone https://github.com/CoDeRgAnEsh/alexa-io.git
~~~
* Do not have GIT? Download this as zip folder from Right Corner Option and extract it

* Open the directory of Cloned repo/Extracted folder
~~~bash
cd alexa-io
~~~
* Install dependencies
~~~bash
pip install -r 'requirements.txt'
~~~
* Open [led.py](https://github.com/CoDeRgAnEsh/alexa-io/blob/master/led.py) & Place Your Adafruit IO Credentials and Save.
~~~python
aio = Client('YOUR_AIO_USERNAME', 'YOUR_AIO_KEY')
~~~
* LED pin set at GPIO.PIN 18 by Default, if you wish to change you can update
~~~python
G.setup(<YOUR_PIN_HERE>,G.OUT)
~~~
* Run Python script to get working at Raspberry Pi
~~~bash
python led.py
~~~

## Issues ?

Facing issues, Pour [here](https://github.com/CoDeRgAnEsh/alexa-io/issues).

## Contribute ?

Fixing issues and Upgrade, Pull out [PRs](https://github.com/CoDeRgAnEsh/alexa-io/pulls).
