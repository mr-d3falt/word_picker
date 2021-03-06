# word_picker
Optimize your  word-list/dictionary.
## Installation

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
python3 word_picker.py PATH_TO_WORDLIST NUMBER_OF_CHARACTERS
```
Or
```
python3 word_picker.py PATH_TO_WORDLIST MIN_NUMBER_OF_CHARACTERS  MAX_NUMBER_OF_CHARACTERS 
```
## Usage Example
```
~/word_picker$ python3 word_picker.py ../Desktop/rockyou.txt 5 
                      __                           __            __   
_______  ____   ____ |  | _____.__. ____  __ __  _/  |____  ____/  |_ 
\_  __ \/  _ \_/ ___\|  |/ <   |  |/  _ \|  |  \ \   __\  \/  /\   __\
 |  | \(  <_> )  \___|    < \___  (  <_> )  |  /  |  |  >    <  |  |  
 |__|   \____/ \___  >__|_ \/ ____|\____/|____/  /\__| /__/\_ \ |__|  
                   \/     \/\/                   \/          \/       

100%|████████████████████████████████████████████████| 14445388/14445388 [00:04<00:00, 3160596.90it/s]

Finished:
rockyou_5_ch.txt was succesifuly created !

~/word_picker$ ls
README.md  requirements.txt  rockyou_5_ch.txt  word_picker.py
```
As you can see 'rockyou_5_ch.txt' was created. Script picked only 5 character length words and wrote them to the 'rockyou_5_ch.txt' .
##
You also can specify 2 numbers. ```MIN_NUMBER_OF_CHARACTERS  MAX_NUMBER_OF_CHARACTERS```
```
~/word_picker$ python3 word_picker.py ../Desktop/rockyou.txt 8 10
                      __                           __            __   
_______  ____   ____ |  | _____.__. ____  __ __  _/  |____  ____/  |_ 
\_  __ \/  _ \_/ ___\|  |/ <   |  |/  _ \|  |  \ \   __\  \/  /\   __\
 |  | \(  <_> )  \___|    < \___  (  <_> )  |  /  |  |  >    <  |  |  
 |__|   \____/ \___  >__|_ \/ ____|\____/|____/  /\__| /__/\_ \ |__|  
                   \/     \/\/                   \/          \/       

100%|████████████████████████████████████████████████| 14445388/14445388 [00:05<00:00, 2542176.72it/s]

Finished:
rockyou_8-10_ch.txt was succesifuly created !

~/word_picker$ ls
README.md  requirements.txt  rockyou_5_ch.txt  rockyou_8-10_ch.txt  word_picker.py
```
In this case script picked 8 to 10 character length words and wrote them to the 'rockyou_8-10_ch.txt' .

