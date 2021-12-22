# DeVon Williams Alta3 Research Cert #

I've created two files. One of which utilizes flask to render HTML pages and set routes. The other utilizes the request library to send a GET request to a public API and parse the response. 

### Requirements ###
Install pyyaml, flask, and requests libraries

## alta3research-flask01.py - FOODIMAL FUSION ##
This script accepts user input from a GET request or from a generated HTML page to combine one food and one animal together into a new species. The foodimal images use are generated via Google's Emoji Kitchen: https://blog.google/products/android/emoji-kitchen-new-mashups-mixing-experience

### How to Use ###
Begin by starting the server using `python3 alta3research-flask01.py`. 
For generating a foodimal via manual input, navigate to the host url that server has been started on OR add the path /start to it: `<host_url>/start`

This should generate a page for selecting one of 3 animals and one of 3 foods. Once selected, click FUSE to combine the two and you will be provided a name, image, and info on that foodimal.

For generating a foodimal via GET request use the path `<host_url>/fuse` and add parameters for animal and food. For example:
`http://10.84.202.230:2224/fuse?animal=octopus&food=pineapple`

This shoud return the name of the foodimal along with the link to more information on it. Please provide valid inputs for these parameters. If not, the response will show what inputs are valid.

Animal Options:
- Deer
- Octopus
- Scorpion

Food Options:
- Cake
- Pineapple
- Hotdog

## alta3research-requests02.py - ACTIVITY GENERATOR ##
This script accepts user input and calls the Bored API (https://www.boredapi.com/about) to generate an activity to kill your boredom.

### How to Use ###
Begin the script by using `python3 alta3research-requests02.py`. After you will be prompted to input a number for which type of activity you want, then how many participants that activity will take. If it doesn't matter how many participants are allowed, simply pass 0 as the input.

The script will send the request to the Bored API and print out the response activity, along with info on the required participants, how accessible it is, and how costly the price can be.
