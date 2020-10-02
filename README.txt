DESCRIPTION:
Rhyme-Viz displays a graph of words that are related to the word you search for.
Your search word is displayed in the center of the page.  Related words are
displayed surrounding the search word.  You can explore the graph by Double
clicking on nodes to display the related words.  In this way you can rhymes,
synonyms, and antonyms.  Rhyme-viz also displays genres of music that are
closely associated with each word.  You can view these by hovering your mouse
over words.

INSTALLATION:
1.) Create a (free) account on Google Cloud Platform (GCP).  You will receive
  $300 in free credits.  If you have a GMail address you can use this address
  for your GCP account.  Under normal conditions this app should not generate
  any monthly spend.
2.) Log in to the GCP console at http://console.cloud.google.com
3.) Create a new GCP project by clicking the dropdown in the top menu bar
  and clicking the + symbol.
4.) Type a project name and click Create.
5.) In the main menu, Navigate to App Engine->Dashboard
6.) Under Your First App, click Language and select Python.
7.) Optionally select a region for your app to run in.
8.) Click Next.  App Engine will begin initializing
9.) In the upper right corner, click the icon that says Activate Cloud Shell
  when you hover the mouse over it.  This will activate a terminal in your
  web browser
10.)  At the terminal prompt, type:
  "git clone https://github.gatech.edu/rmartin95/cse6242project.git"
11.) Type "cd cse6242project"
12.) First you will deploy the API.  Type "cd api"
13.) Type "./deploy.sh"
14.) Type "gcloud app browse" to get the URL of your API.  Copy this value to
  the clipboard.
15.) Now you will deploy the UI.  Type "cd ../RhymeViz\ Vizualizations/"
16.) Edit the file "RhymeVizV.2.4.html" in the src subdirectory.  Do a search
  and replace on the string "https://romartin-cse6242a.appspot.com" with the
  URL you copied in step 14.
17.) Deploy the app by typing "./deploy.sh" in the "RhymeViz Vizualizations" directory
18.) Now you will deploy your database.  First you need to authenticate your
  account to issue API calls.
19.) Type "gcloud auth login".  Follow the prompts, select your login account,
  and click "Allow".  A token will be generated that you need to copy and
  paste back into the command line prompt.  Hit enter and you should be
  logged in.
20.) Time to deploy the database.  Type "cd ../db"
21.) Type "./unzip_syn.sh" to unzip your data files.
22.) Get your project id by typing "gcloud config get-value project"
23.) Copy the id of your project.  You will use it as a parameter in the next
  step.
24.) Deploy the database by typing "python deploy_db.py <project-id>"
25.) From the main menu select App Engine->Services
26.) Click "ui" to display the user interface
27.) Have fun rhyming!

NOTE:  If you wish to eliminate any possibility of monthly spend,
  you can delete your GCP project when you are done.  Select the project
  dropdown at the top bar of the screen.  Click the small folder icon (that
  says Manage Resources when you hover over it).  Check the box next to your
  project.  Click Delete.  Type in the project_id and then click Shut Down.

EXECUTION:
1.) Once the UI is displayed, check the "Explore Mode" checkbox
2.) Enter a word into the textbox.  Try "simulate"
3.) Click "Submit"
4.) The word graph for simulate will be displayed.  Red lines are synonyms.
  Blue lines are antonyms.  Green lines are rhymes.
5.) Hover your mouse over the word you searched for.  The definition and
  parts of speech will be displayed in a tooltip.  You can also view the
  genres of music that this word is often found in (located in the tooltip as
  well).
5.)  Double click one of the other words.  This will browse to the new word.
6.)  You can drag words around to help see the connections clearly.
7.)  If you uncheck Explore Mode when you load a word, you can pin nodes
  by double-clicking them.
8.)  If there are too many results you can uncheck synonyms, antonyms, or
  rhymes, choose a word, and click Submit.
