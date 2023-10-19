#!/usr/bin/env python3
my_fav_things={}
my_fav_things["book"]="The Molecule of More"
my_fav_things["song"]="Born this way"
my_fav_things["Tree"]="Cedar"
my_fav_things["organisms"]="none,hate them all"

print("book",my_fav_things["book"],sep="\t")
print("song",my_fav_things["song"],sep="\t")
print("Tree",my_fav_things["Tree"],sep="\t")

print(my_fav_things)

print("organisms",my_fav_things["organisms"],sep="\t")


#adding for loop

for fav_things in my_fav_things:

 print(fav_things,my_fav_things[fav_things],sep="\t")

print(fav_things)

x=input()

print("fav_things " +x)



my_fav_things["fav_things_user_cmdline"]=x

print(my_fav_things["fav_things_user_cmdline"],sep="\t")
