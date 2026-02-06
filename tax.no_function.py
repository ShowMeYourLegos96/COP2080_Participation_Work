#creating no_input()
def no_input(b,c):
    done = False
    while not done:
     sen = str.upper(input(f'Enter Q to quit or or any other key to compute tax'))
     if sen == 'Q':
        done = True
        print(sen,done)
        continue
     else:
      print("Compute tax")
      price = float(input("What is the price? "))
      tax = float(input("What is the tax rate? "))
     return price, tax 

def calculate_tax(price,tax):

   calculate_price = price * (100 + tax) / 100
   print(f'The calculated price is {calculate_price}')

no_input(400,2)
calculate_tax(400,2)

