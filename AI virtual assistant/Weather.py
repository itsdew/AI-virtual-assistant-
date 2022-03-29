#using wttr 
#wttr.in is a console-oriented weather forecast service that supports various information representation methods like terminal-oriented ANSI-sequences for console HTTP clients (curl, httpie, or wget), HTML for web browsers, or PNG for graphical viewers.
import requests
city = input('input the city name=')
print(city)


print('Displaying Weater report for: ' + city)

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

#display the result!
print(res.text) 
print(res.text)