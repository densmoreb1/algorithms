# https://www.hackerrank.com/challenges/migratory-birds/problem
# list of sightings 
# find the bird with the most sightings

def migratoryBirds(arr):
    # keep track of dups and their actual value
    possible_birds = [0]*6
    for bird in arr:
        possible_birds[bird] += 1
    return(possible_birds.index(max(possible_birds)))