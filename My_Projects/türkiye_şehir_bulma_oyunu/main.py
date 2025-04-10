import pandas
import turtle

screen = turtle.Screen()
screen.title("Türkiye Haritası")

image = "türkiye-haritası.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("şehirlerin_koordinatları.csv")
all_city = [city.lower() for city in data["şehirler"]]

all_answer = []
all_not_answer = []

total = 0
while total < len(all_city):
    answer = screen.textinput(title=f"{total} / {len(all_city)} Doğru", prompt="Bir şehir adı giriniz: ").lower()

    if not answer:
        continue
    if answer == "exit":
        break

    if answer in all_city and answer not in all_answer:
        city_name = turtle.Turtle()
        city_name.hideturtle()
        city_name.penup()
        point = turtle.Turtle()
        point.penup()
        point.hideturtle()

        city_row = data[data["şehirler"] == answer]
        city_x = city_row["x"].item()
        city_y = city_row["y"].item()

        point.goto(city_x,city_y - 7)
        point.dot(5, "red")
        city_name.goto(city_x,city_y - 5)
        city_name.write(city_row["şehirler"].item().title(), align="center", font=("Arial", 8, "normal"))

        total += 1
        all_answer.append(city_row["şehirler"].item())


for city in data["şehirler"]:
    if city not in all_answer:
        all_not_answer.append(city)

pandas.DataFrame(all_not_answer).to_csv("bulamadıklarım.csv")

screen.exitonclick()