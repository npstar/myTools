#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
    @author chengqiang.hu
    @date 2017-04-06
'''

import urllib
import urllib2
import json
import antoto

try:
    response = None
    data = antoto.Antutu().runtest()
    url_values = urllib.urlencode(data)
    url = "http://172.24.218.40:8008/antutu_write_interface"
    full_url = url + '?' + url_values
    request = urllib2.Request(url, url_values)
    response = urllib2.urlopen(request)
    result = json.loads(response.read())
    if not result.get('state'):
        print "Error => %s"%result['errorMsg']

except urllib2.HTTPError, e:
    print 'Error code: %s'%e.code
except urllib2.URLError, e:
    print 'Error reason: %s'%e.reason

finally:
    if response:
        response.close()