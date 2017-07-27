#!/usr/bin/env python
# -*- coding: utf-8 -*-﻿
#
# Copyright 2007 Google Inc.
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
#
import jinja2
import os
import webapp2
from random import randint



#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        myName = (self.request.get("name"))
        if myName == "kev" or "kevin":
            self.response.write("kevin eleven at seven eleven")
        else:
            self.response.write("Yo! big wird <br> ")
class MilkHandler(webapp2.RequestHandler):
    # ^^^ acts as a library of sorts; maybe an API
    def get(self):
        self.response.write("He need some Milk!")

class imageHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write("He need some Milk!")
        my_template = jinja_environment.get_template("templates/hello-world.html")
        #myName = (self.request.get("name"))
        render_data = {
        'food' : self.request.get("f"),
        'myName' : self.request.get("n"),
        'count' : int(self.request.get("count"))
        }
        # if (myName == ""):
        #     myName = "unknown"
        # render_data['name'] = self.request.get("name")

        self.response.write(my_template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/image', imageHandler)
], debug=True)
