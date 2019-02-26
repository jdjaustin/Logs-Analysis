# Logs-Analysis

 Logs Analysis is an exercise in the Udacity Full Stack Web Developer Nanodegree Program used to teach data extraction and reporting methods. The python script for this exercise contains SQL queries which return the three most popular articles, the three most popular authors, and days on which more than 1% of requests led to errors.
 
 ## Setup
 
 Follow the steps in the Udacity course module to install VirtualBox and Vagrant, and to start the Vagrant VM. Also download the `newsdata.sql` file from the Udacity course module and place the file into the shared `vagrant` directory. In my instance, after I launched a vagrant session using `vagrant ssh`, I was defaulted into the wrong `/vagrant` directory and had to `cd ..` a couple times back into the root directory to find the shared `/vagrant` directory, so be on the lookout for this issue. When you are in the correct directory with the `newsdata.sql` file, run `psql -d news -f newsdata.sql` to create the tables and populate the data into the `news` database.
 
 ## Generating Results
 
 Run the `logsanalysis.py` script by entering `python logsanalysis.py` at the Vagrant command line. Your results should look like this:
 
 ```
What are the most popular three articles of all time?
        1 . Candidate is jerk, alleges rival - 338647  views
        2 . Bears love berries, alleges bear - 253801  views
        3 . Bad things gone, say good people - 170098  views

Who are the most popular article authors of all time?
        1 . Ursula La Multa - 507594  views
        2 . Rudolf von Treppenwitz - 423457  views
        3 . Anonymous Contributor - 170098  views

On which days did more than 1% of requests lead to errors?
        1 . 2016-07-17 - 2.26 %
```

## Having Trouble?

If you are experiencing `psql` errors try installing the VM in a fresh directory. Some errors can also be resolved by running `vagrant reload --provision`. 
