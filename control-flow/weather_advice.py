#weather chek

while True:
    weather=input("What's the weather like today? (sunny/rainy/cold or 'exit' to quit):").lower()

    if weather== "sunny":
        print ("Wear a t-shirt and sunglasses.\n")

    elif weather== "rainy":
        print("Don't forget your umbrella and a raincoat.\n")

    elif weather== "cold":
        print("Make sure to wear a warm coat and a scarf.\n")

    elif weather == "exit":
        print("Goodbye!")
        break

    else:
        print("Sorry, I don't have recommendations for this weather.\n")
