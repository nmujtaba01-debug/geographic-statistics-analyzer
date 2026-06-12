places = [ {'name':'Delhi', 'population':19000000, 'rainfall':80},
          {'name':'Mumbai', 'population':20000000, 'rainfall':220},
           {'name':'Jaipur', 'population':4000000, 'rainfall':60},
           {'name':'Shillong', 'population':500000, 'rainfall':250},
            {'name':'Chennai', 'population':11000000, 'rainfall':140} ]
            
            
            
print('Geographic Extreme Analyzer') 
print('---------------------------------') 
             
             
             
highest_population = places[0]['population'] 
lowest_population = places[0]['population'] 
highest_rainfall = places[0]['rainfall']
lowest_rainfall = places[0]['rainfall'] 
             
for place in places: 
 if place['population'] > highest_population:
  highest_population = place['population'] 
                 
                 
 if place['population'] < lowest_population: 
  lowest_population = place['population'] 
  
                   
for place in places: 
   if place['rainfall'] > highest_rainfall:
    highest_rainfall = place['rainfall'] 
                       
                       
   if place['rainfall'] < lowest_rainfall: 
    lowest_rainfall = place['rainfall'] 

print('highest_population:',highest_population)
print('lowest_population:',lowest_population)
print('highest_rainfall:',highest_rainfall) 
print('lowest_rainfall:',lowest_rainfall)