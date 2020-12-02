# Appdynamics - Instrument Python application

### WSGI Python application

#### Docker

**Build image**

`docker build -t wsgiapp .`


**Run container**

`docker run -p 8080:8080 wsgiapp`


**Custom Business Transactions**

- http://localhost:8080
- http://localhost:8080/orders


#### Run application on local env (only Linux)

```bash
cd app
pip3 install -r requirements.txt
pyagent run -c appd.cfg -- python3 wsgisam.py
```

_The Python agent operates on any Linux distribution based on glibc 2.5+ and the x86 32-bit or x86 64-bit architecture._

More information: https://docs.appdynamics.com/display/PRO45/Python+Supported+Environments


---

Example uwsgi

`pyagent run -c appd.cfg -- uwsgi --ini uwsgi.ini -w example`
