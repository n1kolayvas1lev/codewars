# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.
# For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = "cnet"
import re


def domain_name(url):
    # result = re.findall(r'[/|\.][a-z0-9-]+[\.]', url)
    # if len(result) == 0:
    #     result = url
    # result = result[0].strip('/.')
    # return result
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    url = url[:url.find('.')]
    # if url.find('/') > 0:
    #     url = url[url.find('/') + 2:url.find('.')]
    # elif url.find('.') > 0 and url.find('.') != url.rindex('.'):
    #     url = url[url.find('.') + 1:url.rindex('.')]
    # else:
    #     url = url[:url.find('.')]
    print(url)



if __name__ == '__main__':
    domain_name('www.2spfvv6e21b5wg0zy4kwsdxa8')
    domain_name("http://google.com")
    domain_name("http://google.co.jp")
    domain_name("www.xakep.ru")
    domain_name("sfoobar.ru")
    domain_name("https://youtube.com")
