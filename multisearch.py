



import webbrowser



wheretogo = input(("Where would you like to go?: "))
wheretogo = wheretogo.lower()
if wheretogo == "youtube" or wheretogo == "yt":
  giblinkdumbass = input(("Ok! What would you like to search?: "))
  giblinkdumbass.replace(" ", "+")
  webbrowser.open("http://youtube.com/results?search_query=" + giblinkdumbass , new=1)
  


if wheretogo == "reddit":
    whattosearch = input(("What would you like to search?: "))
    webbrowser.open("https://www.reddit.com/search/?q=" + whattosearch , new=1)



if wheretogo == "github":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://github.com/search?q=" + searchterm , new=1)





if wheretogo == "tiktok":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://www.tiktok.com/search?q=" + searchterm , new=1)


if wheretogo == "twitter":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://twitter.com/search?q=" + searchterm , new=1)





if wheretogo == "google":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://www.google.com/search?q=" + searchterm , new=1)


if wheretogo == "duckduckgo" or  wheretogo == "ddg":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://duckduckgo.com/?q=" + searchterm , new=1)





if wheretogo == "amazon":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://www.amazon.com/s?k=" + searchterm , new=1)





  



if wheretogo == "n11":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://www.n11.com/arama?q=" + searchterm , new=1)







if wheretogo == "hepsiburada":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://www.hepsiburada.com/ara?q=" + searchterm , new=1)












if wheretogo == "brave" or wheretogo == "bravesearch" or wheretogo == "brave search":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://search.brave.com/search?q=" + searchterm , new=1)







if wheretogo == "firefoxaddons" or wheretogo == "firefox addons":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://addons.mozilla.org/en-US/firefox/search/?q=" + searchterm , new=1)






if wheretogo == "chromewebstore" or wheretogo == "chrome web store":
  searchterm = input(("What would you like to search?: "))
  webbrowser.open("https://chrome.google.com/webstore/search/" + searchterm , new=1)








