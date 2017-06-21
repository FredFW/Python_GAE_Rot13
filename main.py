# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class mainpage(webapp2.RequestHandler):
    def rot13(self, value):
        ans = ""
        cList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        for c in value:
            cap = False
            if c.isupper():
                c = c.lower()
                cap = True
            if c in cList:
                pos = cList.index(c)
                if pos > 12:
                    pos = pos % 13
                else:
                    pos += 13
                if cap:
                    ans += cList[pos].upper()
                else:
                    ans += cList[pos]
            else:
                ans += c
        return ans
  
    def get(self):
        template_values = {
            'value': "",
        }
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        value = self.request.get('text')
        
        template_values = {
        'value': self.rot13(value),
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        

app = webapp2.WSGIApplication([
    ('/', mainpage)
], debug=True)
