#Dictionary max:
    
    
character = {'name': 'max', 'age':'28', 'company':'redbull', 'role':'media manager'}
print(character)


#change: changing the value of a key

character['age'] = 20
print(character)


#add: adds a new key


character['pension'] = 120000
print(character)


#keys: shows all keys


print(character.keys())



#items: shows all items


print(character.items())




#copy: creates a copy of the dictionary


NewCharacter = character.copy()
print(NewCharacter)



#clear: clears all keys


character.clear()
print(character)