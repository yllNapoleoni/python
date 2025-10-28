# contact_info={
#     "alice":"044 123 123"
#     "bob":"044 132 132"
# }
# alice_phone=contact_info['alice']
# print(alice_phone)
#
# contact_info['daris']='04587632'
#
# print(contact_info)
#
# keys=contact_info.keys()
# print(keys)
#
# values=contact_info.values()
# print(values)
#
# items=contact_info.value()
# print(items)


# contact_info={
#     "alice":{
#         "phone":"555 12345",
#         "email":"alice@gmail.com"
#     }
# }




contact_info={
    "alice":("555 12345","alice@gmail.com")

}

alice_info=contact_info['alice']
phone=alice_info[0]
print(phone)
a