# Upass-script
A script that will request the renewal for my upass translink compass card. The original running script contains my username and password within the script.

#
- The script itself automatically performs the necessary button clicks to request for the renewal. However, it only does so when the script is manually run.
- The site, however, requires its members to log in once every month and click for renewal for the next month. This renewal option gets active on 16th of every month.

# Automating 
- Feed in your personal username/password within the script.
- Use *cronjon* to make the script run automatically on 20th midnight every month. For mac, open the terminal and type:
  - env EDITOR=nano crontab -e
  - 0 0 20 * *  /full/path/to/python /full/path/to/script.py
