#!/usr/bin/env python
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
import re


form = """
<!DOCTYPE html>
<html>
    <head>
        <title>Sign Up</title>
        <style type="text/css">
        div {
            margin: 1em 0;
        }
        input {
            margin: 0 1em;
        }

        </style>
    </head>
    <body>
    <h1>Sign Up</h1>
        <form method="post">
            <div>
            <label for="username">Username</label>
                <input name="username" value='%(username)s' type="text" pattern="[a-zA-Z0-9_-]{3,20}$" required></input>
            </div>
            <div>
            <label for="password">Password</label>
                <input name="password" type="password" pattern=".{3,20}$" required></input>
                <span style="color:red">%(password)s</span>
            </div>
            <div>
            <label for="confirm_password">Confirm Password</label>
                <input name="confirm_password"  type="password" pattern=".{3,20}$" required></input>

            </div>
            <div>
            <label for="email">Email (optional)</label>
                <input name="email" value='%(email)s' type="email" pattern="[\S]+@[\S]+.[\S]+$"></input>

            </div>
            <input type="submit">
        </form>
</html>
"""

def password_check(password, con_pass):
    if password == con_pass:
        return True

class MainHandler(webapp2.RequestHandler):
    def write_form(self, username="", password="", email=""):
        values = {
        'username': username,
        'password': password,
        'email': email
         }

        response = form % values
        self.response.write(response)

    def get(self):
        self.write_form()

    def post(self):
        user_name = self.request.get("username")
        user_password = self.request.get("password")
        user_con_pass = self.request.get("confirm_password")
        user_email = self.request.get("email")


        passwords = password_check(user_password, user_con_pass)

        if not(passwords):
            self.write_form(user_name, "Passwords must match.", user_email)
        else:
            self.write_form()











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
