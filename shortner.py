#!/usr/bin/python


import requests
import json


class api_request():
    apiUrl = "https://www.googleapis.com/urlshortener/v1/url"
    payload = {"key": "<API KEY>"}
    longUrl = ""
    shortUrl = ""

    def make_short(self):
        request = requests.post(self.apiUrl,
                                headers={'Content-Type': 'application/json'},
                                params=self.payload,
                                data=json.dumps({'longUrl': self.longUrl}))
        return request

    def make_request(self):
        request = requests.get(self.apiUrl,
                               params=self.payload)
        return request


def menu():
    options = ['Shorten', 'Expand', 'Stats', 'History']
    print "Select from the following: \n"
    for count, value in enumerate(options):
        print "%d: %s" % (count, value)

    user_input = raw_input("Selection: ")
    return user_input


def main():
    selection = menu()
    r = api_request()

    if selection == "0":
        api_request.longUrl = raw_input("URL to shorten: ")
        answer = r.make_short()
        print "Shortened URL: %s" % (answer.json()['id'])
        exit()
    elif selection == "1":
        api_request.shortUrl = raw_input("URL to expand: ")
        r.payload['shortUrl'] = api_request.shortUrl
        answer = r.make_request()
        print "Expanded URL: %s" % (answer.json()['longUrl'])
        exit()
    elif selection == "2":
        api_request.shortUrl = raw_input("Short URL to get analytics for: ")
        r.payload['shortUrl'] = api_request.shortUrl
        r.payload['projection'] = "FULL"
        answer = r.make_request()
        print json.dumps(answer.json()['analytics'])
        exit()
    else:
        print "Please select from the provided options"
        exit()


if __name__ == "__main__":
    main()
