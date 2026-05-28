import enchant
import time
class pipso:
  def __init__(self):
    self.emotionList = ["Happy", "Sad", "Angry", "Bored", "Glorp"]
    self.emotion = self.emotionList[0]
    self.hunger = 0
    self.energy = 100
    self.boredom = 0
    self.foods = enchant.Dict("en_US")
  def feed(self, food):
    self.food = food
    if self.foods.check(food) and self.hunger >= 10:
      print("Your Pipso liked the food!")
      self.hunger -= 10
      if self.hunger < 0:
        self.hunger = 0
      self.energy += 10
      if self.energy > 100:
        self.energy = 100
    elif self.foods.check(food) and self.hunger < 10:
      print("Your Pipso is too full to eat right now")
  def play(self):
    if self.energy >= 10:
      print("You played with your Pipso!")
      self.energy -= 10
      self.boredom = 0
    else:
      print("Your Pipso is too tired to play.")
  def update_emotion(self):
    if self.hunger >= 100:
      self.emotion = "Glorp"
    elif self.energy <= 20:
      self.emotion = "Sad"
    elif self.boredom >= 30:
      self.emotion = "Bored"
    elif self.energy < 50:
      self.emotion = "Angry"
    else:
      self.emotion = "Happy"
  def display_expression(self):
    expressions = {
      "Happy": "°ω°",
      "Sad": "°̆ ︿ °̆",
      "Angry": "ಠ╭╮ಠ",
      "Bored": "-_-",
      "Glorp": "◉_◉"
    }
    print(expressions.get(self.emotion, "°ω°"))

Pipso = pipso()
while True:
  time.sleep(5)
  Pipso.hunger += (3 / (Pipso.hunger + 1)) * 100
  Pipso.boredom += 5
  Pipso.energy -= 2
  if Pipso.energy < 0:
    Pipso.energy = 0
  Pipso.update_emotion()
  action = input("What do you do with Pipso? (feed/play/none) ")
  if action.lower() == "feed":
    foodToFeed = input("Feed your Pipso what? ")
    Pipso.feed(foodToFeed)
  elif action.lower() == "play":
    Pipso.play()
  Pipso.update_emotion()
  Pipso.display_expression()
