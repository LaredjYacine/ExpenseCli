# ExpenseCliTracker

this was a test for me to learn new things and re-affirm things i learned before if you check the commits of this file youll see that it was a function to check Expenses->Checking and adding from Cli -> made it to a Class 

#CliFetchStoregithub 
i unintentionally made a github repo scraper that works from the CLI  either fetches the repos or straightly insert them into your database
##how it works
(py + Name of the file)  py .\CliFetchStoregithub.py +(command i  have store or fetch ) store -u Username -dbusername postgres  -hostname localhost   -password PasswordOfDatabase    -port 5432 -db NameOfDatabase  -gittoken (your GithubToken to have)

this will go to the usernames repo and store all of them in your database it will create the table if it didnt exist as gitrepo 

#githubrestapi

This is the same thing as CLI but you just run it immediatly    i made it to learn how async works so its not really professionally structured and thats my bad 
