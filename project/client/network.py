import requests
import setting


class Network():

    def register(self, inf):
        if inf['password'] != inf['confpass']:
            return(False, 'password does not match the confirm password')
        elif (' ' in inf['password']) or ('   ' in inf['password']):
            return(False, inf['password'])
        elif len(inf['password'])< 6 or len(inf['password'])>30 :
            return (False,'password too long or too short')
        elif len(inf['username'])> 30:
            return (False, 'Invalid username')
        elif not(inf['username'],inf['password']):
            return(False,'all informations are reqiured')
        else:
            r = self.session.post(setting.url['register'], data=inf)
            if r.status_code == 200:
                return (True, "")
            else:
                return (False, str(r.content)[2:-1])

    def login(self, inf):
        r = self.session.post(setting.url['login'], data=inf)
        if r.status_code == 200:
            return (True,"")
        else:
            return (False,str(r.content)[2:-1])

    def logout(self):
        r = self.session.get(setting.url['logout'])
        if r.status_code == 200:
            return (True,"")
        else:
            return (False,'log out unsuccessful')

