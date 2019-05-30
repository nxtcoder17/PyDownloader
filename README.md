# PyDownloader

### Introduction

Python based **File Downloader**.<br/>
It makes use of Python's Multiprocessing features to make sure
you get your file downloaded, faster than other downloaders.

* **Requirements**
    >> Python Requests

- **Installing requests**
    >> `pip install requests` should do installation of Python Requests

### Executing the Downloader
>> Make an alias to the program in your BASHRC
```sh
# filename: $HOME/.bashrc
alias pydm='python3 $HOME/PyDownloader/main.py'     # Considering you clone the Repository in your HOME
```

You need to pass <b>2</b> Arguments to the PyDownloader thing 
<pre>
    First: Download Link    (preferably in quotes)
    Second: File Name       (preferably in double quotes)
</pre>

![PyDownloader Working](./pydm.png)
