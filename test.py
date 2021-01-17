from bert import Ner

model = Ner("out_base/")

output1 = model.predict("The customer rating is average for the child friendly fast food place is average and its in Riverside near the Café Rouge and The Golden Curry")
output2 = model.predict("Located in the City Centre by Burger King with a one star rating from customers is a coffee shop by the name of The Eagle It's cheap and for adults only")
print(output1)
print(output2)
