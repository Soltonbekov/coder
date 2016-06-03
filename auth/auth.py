# -*- coding: utf-8 -*-

import hashlib

class User:
    login = ""
    password = ""
    email = ""
    first_name = u""
    last_name = u""
    is_active = False

    def signin(self, login, password=None):
        
        if len(login) > 6:
            self.login = login
        
        if len(password) > 8:
            self.password = password
        elif password is None:
            self.password = hashlib.md5(self.login)[:8]

        self.is_active = True

        return (self.login, self.password, self.is_active)

    def reset_password(self, login):
        pass

    def is_active(self, login):
        pass

    def change_profile_details(self, login, first_name, last_name):
        pass

    def check_password(self, login, unverified_password):
        pass

    def send_confirmation_password(self, login):
        pass


