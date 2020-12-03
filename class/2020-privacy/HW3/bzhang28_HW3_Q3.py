#!/usr/bin/env python
# coding: utf-8

# In[1]:



import argparse
import json
from urllib.parse import urlparse
from tld import get_fld
from adblockparser import AdblockRules


# In[2]:


# Code is from https://gist.github.com/tomatohater/8853161
def parse_har(harfile_path):
    """Reads a har file from the filesystem, converts to CSV, then dumps to
    stdout.
    """
    urls = []
    harfile = open(harfile_path)
    harfile_json = json.loads(harfile.read())
    i = 0

    for entry in harfile_json['log']['entries']:
        i = i + 1
        url = entry['request']['url']
        urlparts = urlparse(entry['request']['url'])
        size_bytes = entry['response']['bodySize']
        size_kilobytes = float(entry['response']['bodySize'])/1024
        mimetype = 'unknown'
        if 'mimeType' in entry['response']['content']:
            mimetype = entry['response']['content']['mimeType']
        urls.append((url, mimetype))
        #print(f"{i}, {url}, {urlparts.hostname}, {size_bytes}, {mimetype}")
    return urls


# In[3]:


easylist = []
with open('./easylist.txt') as f:
    for cnt, line in enumerate(f):
        easylist.append(line.rstrip())
rules = AdblockRules(easylist) 


# In[11]:


cnn_urls = parse_har('./www.cnn.com.har')

sites = {}

for url, mimetype in cnn_urls:    
    is_script  = 'script' in mimetype
    is_image = 'image' in mimetype
    domain = 'www.cnn.com'
    try:
        url_domain = get_fld(url)
    except Exception as e:
        print(f"invalid domain in {url}")
        continue
    is_third_party = url_domain != 'cnn.com'
    options = {
        'script': is_script,
        'domain': domain, 
        'image': is_image,
        'third-party': is_third_party
    }
    
    if url_domain not in sites:
        sites[url_domain] = {
            "number_requests": 0,
            "number_requests_blocked":0
        }
        
        
    sites[url_domain]["number_requests"] += 1
    
    
    if rules.should_block(url, options):
        sites[url_domain]["number_requests_blocked"] +=1

        
#print(f"CNN had {number_requests} total requests, and {number_requests_blocked} requests blocked")


# In[12]:


macys_urls = parse_har('./www.macys.com.har')

for url, mimetype in macys_urls:    
    is_script  = 'script' in mimetype
    is_image = 'image' in mimetype
    domain = 'www.macys.com'
    try:
        url_domain = get_fld(url)
    except Exception as e:
        print(f"invalid domain in {url}")
        continue
    is_third_party = url_domain != 'macys.com'
    options = {
        'script': is_script,
        'domain': domain, 
        'image': is_image,
        'third-party': is_third_party
    }
    
    if url_domain not in sites:
        sites[url_domain] = {
            "number_requests": 0,
            "number_requests_blocked":0
        }
        
        
    sites[url_domain]["number_requests"] += 1
    
    
    if rules.should_block(url, options):
        sites[url_domain]["number_requests_blocked"] +=1


# In[13]:


print("Site, # HTTP requests, # HTTP requests blocked")
for site, requests in sites.items():
    print(f"{site}, {requests['number_requests']}, {requests['number_requests_blocked']}")


# In[ ]:




