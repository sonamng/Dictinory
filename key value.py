# a={"name":"sonam","age":20,"city":"ghazipur","a":{"name":"anjali"}}
# # for x,y in a.items():
# #      print(x,y)



s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}

a={'python':20,"gaurav":300,'dev':34,"karan":43}

c={}

for i in (s,a):

    c.update(i)

print(c)