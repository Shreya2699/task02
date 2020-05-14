test_dict = {'physics':88,'math':75,'chemistry':72,'basic electrical':89 }
print("The original dictionary is : " + str(test_dict))


res = [key for key in test_dict if
       all(test_dict[temp] >= test_dict[key]
           for temp in test_dict)]


print("Keys with minimum values are : " + str(res))