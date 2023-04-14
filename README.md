# company-email-guesser
Guesses someones company email address using public linkedin info. This is a tool developed as part of an information security demo, meant to highlight how open source intelligence (OSINT) is used in crafting phishing attacks. Given basic information found on linkedin (full name, company name), this python script generates 4 possible company email addresses. An attacker might then send a phishing email to all of these addresses, because at least one of them would be accurate.

This is based on the idea that companies use the same naming conventions when giving employees emails. 
* Ex: John Smith of Evil Corp would be: jsmith@evilcorp.com, johnsmith@evilcorp.com, j.smith@evilcorp.com or john.smith@evilcorp.com

Please use this responsibly.



## input
a csv named `linkedin.csv` that looks like this:

<img width="326" alt="Screenshot 2021-05-24 at 7 32 32 PM" src="https://user-images.githubusercontent.com/24460340/119391838-ca638b80-bcc6-11eb-8db8-291485cb4659.png">
An example file is available, just fill it with your own data and run the python script

## output

a text file named `output.txt` that looks like this:
<img width="688" alt="Screenshot 2021-05-24 at 7 48 57 PM" src="https://user-images.githubusercontent.com/24460340/119393607-14e60780-bcc9-11eb-90be-55a40b4f6581.png">

## requirements
 * python 3 (2 might work though, idk)
 * pandas (run `pip install pandas`)

## usage
* clone the repo `git clone https://github.com/nick781/company-email-guesser.git`
* from inside the folder, run the script `python company_email_guesser.py`
* if successful, you should see `output.txt` in the folder now
