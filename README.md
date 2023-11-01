# Paperspace Notebook Starter Script 

A little script that I've been using to start free tier Paperspace notebooks.

After you have downloaded this repo and unpacked it, first install [Python 3](https://www.python.org/downloads/) [I use Python 3 version 3.10.11] and install the missing libraries using `pip install`

```
pip install -e /path/to/unpacked/repo/gradient-cli
pip install plyer
```
because if using pip install gradient will result in an error, a modification is included in this repository so you need to install the library by
```
pip install -e /path/to/unpacked/repo/gradient-cli
```
this is just a temporary solution

Before you run main.py you need to modify it first in the section api_key dan id
```
if __name__ == "__main__":
    lock = Lock()
    api_key = "" # The API key of your Paperspace account.
    machine_types = ['Free-A4000','Free-RTX5000']
    id = '' # The id of the Gradient notebook.
    for machine_type in machine_types:
        Process(target=start_machine,args=(lock,machine_type,id,api_key)).start()
```
For api_key location
Settings > Apikey
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/api_key.png?raw=true)

For id location
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/id.png?raw=true)


The script has been created for the Youtube series: https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J

If you've found this useful please like and subscribe, it is literally my payment.