import random
from time import sleep

class pokemon:
    
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = self.level * 10
        self.max_health = self.level * 10 
        self.if_knocked_out = False
        
  
    def lose_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:   
            print("{} just lost {} health points and is now on {} health points.".format(self.name, damage, self.health))
    
    def gain_health(self , more_health):
        self.health += more_health
        if not self.health <= self.max_health:
            self.health = self.max_health
        return "{} is now at {} health!".format(self.name, self.health)
        
    def knock_out(self):
        self.if_knocked_out = True
        print("KO! {}'s health is now zero. Please revive.".format(self.name))

    
    def revive(self):
        if self.if_knocked_out is True:
            print("{} is reviving. Please wait...".format(self.name))
            sleep(3)
            self.health = self.max_health
            self.if_knocked_out = False
            print("{} has been revived! Health is at {}.".format(self.name, self.health))
        else:
            print("{} doesn't need reviving! Try using a potion instead.".format(self.name))
      
            
    def attack(self, other_pokemon):
        grass_type = {"grass" : 0.5, "water" : 2, "fire" : 0.5}
        water_type = {"grass" : 0.5, "water" : 0.5, "fire" : 2 }
        fire_type = {"grass" : 2, "water" : 0.5, "fire" :  0.5}
        type_dict = {"grass" : grass_type, "water" : water_type, "fire" : fire_type}
        
        effectiveness = type_dict[self.type][other_pokemon.type]
        damage = effectiveness * self.level * random.randint(1,5) 
        
        if self.if_knocked_out == True:
            print("{} is knocked out. Please revive before attacking.".format(self.name))
        else:
            if effectiveness == 0.5:
                print("{} attacked {}! The attack was not very effective. {} dealt {} damage!".format(self.name , other_pokemon.name , self.name, damage))
            else:
                print("{} attacked {}! The attack was very effective! {} dealt {} damage!".format(self.name , other_pokemon.name , self.name, damage))
            
            other_pokemon.lose_health(damage)
            

class trainer:
    
    def __init__(self, name, pokemon_owned, currently_active_pokemon, potions=None, revives=None):
        self.name = name
        self.pokemon_owned = pokemon_owned
        self.currently_active_pokemon = currently_active_pokemon
        self.potions = potions
        self.revives = revives
        
    def __repr__(self):
        print("Trainer {name} owns the following pokemon:".format(name=self.name))
        for pokemon in self.pokemon_owned:
            print("Name: {}, Type: {}, Level: {}, Current HP: {}".format(pokemon.name, pokemon.type, pokemon.level, pokemon.health))
        return "Trainer {}'s currently active pokemon is {}! Let's commence the battle!".format(self.name, self.currently_active_pokemon.name)
        
        
    def use_potion(self, potion_used):
        all_potions = {"potion" : 20 , "super potion" : 50 , "hyper potion" : 200}
        if self.currently_active_pokemon.if_knocked_out == True:
            print("{} is knocked out. Please use a revive instead of a potion!".format(self.currently_active_pokemon.name))
        else:
            if potion_used in self.potions and potion_used in all_potions:
                self.currently_active_pokemon.gain_health(all_potions[potion_used]) 
                self.potions.remove(potion_used)
                print("{} was used! {} has been restored to {} HP! You have these potions remaining: {}".format(potion_used, self.currently_active_pokemon.name, self.currently_active_pokemon.health,', '.join(self.potions)))
            elif potion_used in self.potions:
                #for max potion
                self.currently_active_pokemon.gain_health(float("inf"))
                self.potions.remove(potion_used)
                print("{} was used! {} has been fully restored to {} HP! You have these potions remaining: {}".format(potion_used, self.currently_active_pokemon, self.currently_active_pokemon.health,', '.join(self.potions))) 
            else:
                print("Please use a potion from your collection. These are : {}".format(', '.join(self.potions)))
            
    def use_revive(self, pokemon_to_revive):
        if pokemon_to_revive in self.pokemon_owned:
            if self.revives > 0:
                pokemon_to_revive.revive()
            else:
                print("You don't have any revives.")
        else:
            print("That pokemon isn't in your collection!")
            
    def switch_pokemon(self, new_pokemon):
        if new_pokemon not in self.pokemon_owned:
            print("You don't own that pokemon. Please choose one from your collection")
        elif new_pokemon.if_knocked_out == True:
            print("This pokemon is currently knocked out! Please revive before taking it to battle!")
        else:
            self.currently_active_pokemon = new_pokemon
            print("{} is now your currently active pokemon! Current HP level is at {}.".format(self.currently_active_pokemon.name, self.currently_active_pokemon.health))
            
    def attack_trainer(self, other_trainer):
        if self.currently_active_pokemon.if_knocked_out == False and other_trainer.currently_active_pokemon.if_knocked_out == False:
            self.currently_active_pokemon.attack(other_trainer.currently_active_pokemon)
        else:
            print("A battle cannot occur if either pokemon is knocked out!")
        
    
    
         
   
            
            
 #SOME TESTS TO CHECK CODE   
            
a = pokemon("a", 20, "water")
b = pokemon("b",19, "water")
c = pokemon("c", 18, "water")
d = pokemon("d", 22, "fire")
e = pokemon("e", 20, "fire")
f = pokemon("f", 21, "earth")
g = pokemon("g", 20, "earth")


t_1 = trainer("chloe", [a, b, d], a, ["super potion", "max potion", "potion"], 2)
t_2 = trainer("fergel", [c, e, f, g], c, ["hyper potion", "hyper potion"], 1)         
         

print(t_1)
print(t_2)

t_1.switch_pokemon(b)   

t_1.attack_trainer(t_2)
t_2.attack_trainer(t_1)
t_1.attack_trainer(t_2)
t_2.attack_trainer(t_1)



t_2.use_potion("hyper potion")
        
t_1.switch_pokemon(a)

print(t_1)
print(t_2)
        
t_1.attack_trainer(t_2)      
t_1.attack_trainer(t_2)  
t_1.attack_trainer(t_2)    
t_1.switch_pokemon(d)

t_1.attack_trainer(t_2)      
t_1.attack_trainer(t_2)  
t_1.attack_trainer(t_2)   



print(t_1)
print(t_2)


t_2.use_revive(c)

        
    
          

        
        
        
            
        
    



 


