import random

import string


if __name__ =="__main__":

    obj1=string.ascii_uppercase
    obj2=string.ascii_lowercase

    obj3=string.digits

    obj4=string.hexdigits

    obj5=string.octdigits

    obj6=string.punctuation

    user_input=int(input("ENTER HOW MANY LENGHT OF DIGIT DO YOU WANT ?"))
    store = []

    store.extend(obj1)
    store.extend(obj2)
    store.extend(obj3)
    store.extend(obj4)
    store.extend(obj5)
    store.extend(obj6)

    random.shuffle(store)
    print("YOUR PASSWORD IS READY TO SHOW ! ")

    print("".join(store[0:user_input]))



