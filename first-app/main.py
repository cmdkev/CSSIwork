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
import webapp2
from random import randint


class MainHandler(webapp2.RequestHandler):
    #define a function that builds our response, call that function inside get()
    # def displayPage(self):
    #     helloWorld = ["Hello World ", "Hola Mundo ", "こんにちは世界 | Kon'nichiwa sekai ", "Salvete Mundi ", "你好，世界 | Nǐ hǎo, shìjiè "]
    #     # randHello = helloWorld[0, randint(helloWorld)]
    #     # finalHello = []
    #     # for i in range(1, randint(1, 5)):
    #     return helloWorld[randint(0, len(helloWorld)-1)]
    #
    # def get(self):
    #     #this function outputs to browser
    #     response = self.displayPage()
    #     self.response.write(response)
    def get(self):
        Howdy = int(self.request.get("Howdy"))
        for i in range(Howdy):
            self.response.write(str(Howdy) + " partner <br> ")
class MilkHandler(webapp2.RequestHandler):
    # ^^^ acts as a library of sorts; maybe an API
    def get(self):
        self.response.write("He need some Milk!")
class imageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<head> <link rel='stylesheet' href='/resources/main.css'> </head>")
        self.response.write("<h1>MuaHaHa, my evil plan worked </h1>")
        self.response.write("<img src='/resources/Towing-Bolingbrook-IL.jpg'>")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/image', imageHandler)
], debug=True)
