#makes a list with empty elements
def make_empty_offspring(how_big):
    offspring = []
    for i in range(how_big):
        offspring.append("")
    return offspring

#PMX
def partially_mapped_crossover(p1, p2):

    #makes empty offspring
    offspring = make_empty_offspring(10)
    start = 2 #this could be random 
    end = 7 #this could be random

    #this for loop slices into the offspring
    for i in range(len(p1)):
        if i >= start and i < end:
            offspring[i] = p1[i]
    print(offspring)

    #this for loop looks at p2 to see if is in offspring, if not then adds it from front
    for i in range(start):
        for j in p2:
            if j in offspring: #returns true if found
                continue
            else:
                offspring[i] = j
                break
    print(offspring)

    #this for loop looks at p2 again after the slice placed in offspring to see if in
    for i in range(end, len(p2)):
        for j in p2:
            if j in offspring:
                continue
            else:
                offspring[i] = j
                break
    print(offspring)

#OX
def order_crossover(p1, p2):

    #makes empty offspring
    offspring = make_empty_offspring(10)
    print(offspring)
    start = 1 #could be random
    end = 6 #could be random
    count = end #need for later as a counter

    #for loop slices from p2 into offspring
    for i in range(start,end):
        offspring[i] = p1[i]
    print(offspring)

    #for loop adding elements after slice in offspring was added
    for i in range(end, len(offspring)):
        while True:
            try: #.index will return error if not found
                found = offspring.index(p2[count])
                if count == len(offspring)-1:
                    count = 0 #need this so i do not get an out bounds error
                else:
                    count += 1
            except ValueError: #if not found than error
                offspring[i] = p2[count]
                break
    print(offspring)

    #adds elements to empty elements in front of slice in offspring
    while True: #same thing as before
        counter = 0
        if offspring[counter] != '':
            break
        else:
            for i in range(start):
                while True:
                    try:
                        found = offspring.index(p2[count])
                        count += 1
                    except ValueError:
                        offspring[i] = p2[count]
                        break
            counter = counter + 1
    print(offspring)



#CX
def cycle_crossover( p1, p2):
    #empty offspring
    offspring = make_empty_offspring(10)
    print(offspring)
    position = 0

    #while loop that keeps going till no empty elements in the cycle
    while True:
        if offspring[position] != "":
            break #breaks when not " "
        offspring[position] = p1[position] #places element into offspring
        position = p1.index(p2[position]) #find where to go next
    print(offspring)

    #this is looking for the empty spot left over after the cycle and filling them 
    count = 0
    for j in p2:
            if j in offspring:
                count += 1
                continue
            else:
                offspring[count] = j
                count += 1
    print(offspring)



parent_one = ["J", "B", "F", "C", "A", "D", "H", "G", "I", "E"]
parent_two = ["F", "A", "G", "D", "H", "C", "E", "B", "J", "I"]

print("Parent 1: ", parent_one)
print("Parent 2: ", parent_two)

while True:
  ask = int(input("Which crossover would you like, 1: Partially Mapped 2: Order 3: Cycle "))
  if ask == 1:
    partially_mapped_crossover(parent_one,parent_two)
  elif ask == 2:
    order_crossover(parent_one,parent_two)
  elif ask == 3:
    cycle_crossover(parent_one,parent_two)
  else:
    print("Not a choice, bye!")