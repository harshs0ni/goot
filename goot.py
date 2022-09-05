# Author: Harsh Soni
# Tool: Goot (Google Dork Automation Tool)
# Created on: 4-Sep-2022
# Tested on Python3
# Version 1
try: 
    try:
        from time import sleep
        import getopt, sys
    except ModuleNotFoundError:
        print("\n--------------------------------\n\tError\n--------------------------------\nModule not found\n--------------------------------\n")
    try: 
        from googlesearch import search
    except ModuleNotFoundError:
        print("\n--------------------------------\n\tError\n--------------------------------\nGoooglesearch module not found \n\nTry pip install googlesearch-python \n\nor\n\ncheck here https://pypi.org/project/googlesearch-python/\n--------------------------------\n")
    try:
        import requests
    except ModuleNotFoundError:
        print("\n--------------------------------\n\tError\n--------------------------------\nRequests module not found  \n\nTry pip install requests \n\nor\n\ncheck here https://pypi.org/project/requests/\n--------------------------------\n")
    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
    google_dork_templ = "site:"
    default_ext=["log","logs","cfg","pl","keystore","js","sql","bak","py","env","json","properties","pem","yml","yaml","aspx","sh","asp","zip","jks"]
    default_ext_str = ".log, .logs, .cfg, .pl, .keystore, .js, .sql, .bak, .py, .env, .json, .properties, .pem, .yml, .yaml, .aspx, .sh, .asp, .zip, .jks"
    def intro():
        print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Google Dork Automation Tool
        v1.00
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

by Harsh S0ni
website:- harshs0ni.com
        ''')
    def usage():
        print('''
    \nUsage: python3 goot.py -u <url> <arguement> <value>
    -u | --url <url>  || url of the target site
    -e | --everything || to print every link
    -x | --extension  || to print links with following extension '''+ default_ext_str +'''
    -c | --custom-extension <extensions> || to print all link with your desired extension || eg: -c pdf,docx,pptx
    -t | --in-title <string> || to print links if your desired string is in title 
    -l | --in-url <string> || to print links if your desired string is in url 
    -a | --all-in-text <string> || to print links if your desired string is in website
    -s | --save <desired_filename> || to save the output
    -h | --help || to print all the command
    ''')
    enum_extension = False
    exploit_everything = False
    in_title = False
    in_url = False
    all_in_text = False
    custom_extension = False
    save_output = False
    argumentList = sys.argv[1:]
    code_version = 1
    short_arg = "u:xc:et:l:a:s:h"
    
    long_arg = ["url","extension", "custom-extension=", "everything","in-title=","in-url=","all-in-text=","save=","help"]

    try:
        arguments, values = getopt.getopt(argumentList, short_arg, long_arg)
        
        for currentArgument, currentValue in arguments:
            
            if currentArgument in ("-u", "--url"):
                url = currentValue
            
            elif currentArgument in ["-x", "--extension"]:
                enum_extension = True
            
            elif currentArgument in ("-c", "--custom-extension"):
                custom_extension_str = currentValue
                custom_extension_value = currentValue
                custom_extension = True
                
            elif currentArgument in ("-e", "--everything"):
                exploit_everything = True
            
            elif currentArgument in ("-t", "--in-title"):
                in_title_query = currentValue
                in_title = True
                
            elif currentArgument in ("-l", "--in-url"):
                in_url_query = currentValue
                in_url = True
            
            elif currentArgument in ("-a", "--all-in-text"):
                all_in_text_query = currentValue
                all_in_text = True
            elif currentArgument in ("-s", "--save"):
                file_path = currentValue
                save_output = True
            elif currentArgument in ("-h", "--help"):
                usage()
    except getopt.error as err:
        usage()

    def stl(string):
        li = list(string.split(","))
        return li

    def cache(url):
        query = "https://www.google.com/search?q=cache:"+url
        response = requests.get(query, headers={'User-agent': 'your bot 0.1'}).status_code
        if str(response) == "200":
            print("\n--------------------------------\n"+query + " :Google Cache is Available\n--------------------------------\n")

    def scrape(i):
        final_url = google_dork_templ+i
        if save_output == True:
            output_file = open(file_path, "w")
            for j in search(final_url, start=0, stop=None, pause=3, user_agent='your bot 0.1'):
                print(j)
                output_file.write("\n"+j)
                sleep(0.5)
        else:
            for j in search(final_url, start=0, stop=None, pause=3, user_agent='your bot 0.1'):
                print(j)
                sleep(0.5) 

    def xa(i,ext):
        ext_len = len(ext)
        for e in range(ext_len):
            query = i + " ext:" +ext[e]
            scrape(query)

    def intitle(url,strings):
        query = url + " intitle: " + strings
        scrape(query)

    def inurl(url,strings):
        query = url + " inurl: " + strings
        scrape(query)

    def allintext(url,strings):
        query = url + " allintext: " + strings
        scrape(query)
    try: 
        if enum_extension == True and custom_extension ==True:
            usage()
        elif enum_extension == True:
            intro()
            print("Extension mode: "+ default_ext_str +"\nTarget url: "+url)
            xa(url,default_ext)
            cache(url)
        elif exploit_everything == True:
            if enum_extension == True or in_url == True or custom_extension == True or in_title == True or all_in_text == True:
                usage()
            else:
                intro()
                print("Target url: "+url)
                scrape(url)
                cache(url)
        elif custom_extension == True:
            intro()
            print("Custom Extension Mode: "+ custom_extension_str +"\nTarget url: "+url)
            custom_extension_value =  stl(custom_extension_value)
            xa(url,custom_extension_value)
            cache(url)
        elif in_title == True:
            intro()
            print("In Title: "+ in_title_query +"\nTarget url: "+url)
            intitle(url,in_title_query)
            cache(url)
        elif in_url == True:
            intro()
            print("In Url: "+ in_url_query +"\nTarget url: "+url)
            inurl(url,in_url_query)
            cache(url)
        elif all_in_text == True:
            intro()
            print("In Text: "+ all_in_text_query +"\nTarget url: "+url)
            intitle(url,all_in_text_query)
            cache(url)
    except:
        print("\nUnexpected Error Occured \nYou can contact me for help on insta:- @harshs0ni__")
except KeyboardInterrupt:
    print("^c")