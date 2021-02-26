# word_picker
Optimize your  word-list/dictionary.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
git clone https://github.com/mr-d3falt/word_picker.git
```
**Switch to script's directory**
```
cd word_picker
```
**Install requirments**
```
pip install -r requirements.txt

#Or

pip3 install -r requirements.txt
```
## Usage
```
python3 word_picker.py PATH_TO_WORDLIST NUMBER_OF_CHARCTERS 

```
## Usage Example
```
~/word_picker$ python3 word_picker.py ../Desktop/rockyou.txt 5 
_______  ____   ____ |  | _____.__. ____  __ __  _/  |____  ____/  |_ 
\_  __ \/  _ \_/ ___\|  |/ <   |  |/  _ \|  |  \ \   __\  \/  /\   __\
 |  | \(  <_> )  \___|    < \___  (  <_> )  |  /  |  |  >    <  |  |  
 |__|   \____/ \___  >__|_ \/ ____|\____/|____/  /\__| /__/\_ \ |__|  
                   \/     \/\/                   \/          \/       


Finished:
rockyou_5_ch.txt was succesifuly created !

~/word_picker$ ls
README.md  requirements.txt  rockyou_5_ch.txt  word_picker.py
```
As you can see rockyou_5_ch.txt was created. Script picked only 5 chacrachter length words.
