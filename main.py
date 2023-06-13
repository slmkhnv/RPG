import random
import time


class Player:
    def __init__(self, name, hp, damage, mana):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana = mana
        self.lvl = 1
        self.exp = 0
        self.skill = []

    def create_hero(name, race, prof):
        hp = 0
        damage = 0
        mana = 0
        name = name
        if race == race_list[0]:
            hp += 200
            damage += 25
            mana += 150
        elif race == race_list[1]:
            hp += 150
            damage += 20
            mana += 350
        elif race == race_list[2]:
            hp += 250
            damage += 35
            mana += 125
        elif race == race_list[3]:
            hp += 450
            damage += 50
            mana += 200
        elif race == race_list[4]:
            hp += 220
            damage += 25
            mana += 500
        elif race == race_list[5]:
            hp += 245
            damage += 32
            mana += 225
        elif race == race_list[6]:
            hp += 375
            damage += 40
            mana += 310
        else:
            print('Такой расы не существует. Попробуйте ещё раз: ')
            quit()
        if prof == prof_list[0]:
            hp -= 30
            damage += 15
            mana += 30
        elif prof == prof_list[1]:
            hp += 30
            damage += 20
            mana -= 20
        elif prof == prof_list[2]:
            hp -= 20
            damage -= 5
            mana += 50
        elif prof == prof_list[3]:
            hp += 15
            damage += 5
            mana -= 20
        elif prof == prof_list[4]:
            hp -= 10
            damage += 0
            mana += 30
        elif prof == prof_list[5]:
            hp += 0
            damage += 0
            mana += 0
        else:
            print('Такой профессии не существует. Попробуйте ещё раз: ')
            quit()
        return Player(name, hp, damage, mana)

    def ability(self):
        if player.skill == player.skill[0]:
            if player.skill[0] == 'Замораживание':
                print('Вы заморозили монстра. Теперь он не атакует! ')
                enemy.damage = 0
            elif player.skill[0] == 'Исцеление':
                print('Вы восстановили себе 10 здоровья!')
                player.hp += 10

    def lvlup(self, max_exp):
        self.exp -= max_exp
        self.lvl += 1
        self.hp += self.lvl * 5
        self.mana += self.lvl * 10
        self.damage += self.lvl * 4
        print(f'{self.name}, ваш уровень повысился! Уровень: {self.lvl}. ')

    def attack(self, victim, ability=None):
        max_exp = 100
        rnd_attack = random.randrange(1, 5)
        if rnd_attack == 1:
            print('Вы нанесли критический урон. ')
            victim.hp -= self.damage * 2
        elif rnd_attack == 2 or 3 or 4:
            victim.hp -= self.damage
        elif rnd_attack == 5:
            print('Вы промахнулись. ')
            victim.hp -= 0
        if victim.hp <= 0:
            print('Монстр повержен. Вы получили 20 опыта. ')
            self.exp += 20
            if self.exp >= max_exp:
                self.lvlup(max_exp)
            self.skill = self.skill.append(random.choice(powers))
            if len(list(self.skill, ability=None)) == 3:
                del self.skill[0]
            print(f'Теперь у вас есть способности: {self.skill}. ')
            thing = random.randint(0, 9)
            if thing == 0 or thing == 1:
                weapon = self.create_weapon()
                print(f'Вам выпало {weapon[1]} - {weapon[0]}. ')
            elif thing == 5 or thing == 8:
                armor = self.create_armor()
                print(f'Вам выпало {armor[1]} - {armor[0]}. ')
            else:
                print('Вам ничего не выпало. 😜 ')

            return False
        else:
            if len(list(self.skill)) != 0:
                ability()
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}. ')
            return True

    def create_weapon(self):
        wpn = weapon_list[random.randint(0, 4)]
        wpn_rare = random.choice(list(weapon_dict.keys()))
        if wpn == weapon_list[0]:
            self.damage += 3 * wpn_rare
        elif wpn == weapon_list[1]:
            self.damage += 4 * wpn_rare
        elif wpn == weapon_list[2]:
            self.damage += 2 * wpn_rare
        elif wpn == weapon_list[3]:
            self.damage += 6 * wpn_rare
        elif wpn == weapon_list[4]:
            self.damage += 1 * wpn_rare
        return wpn, weapon_dict[wpn_rare]

    def create_armor(self):
        arm = armor_list[random.randint(0, 4)]
        arm_rare = random.choice(list(armor_dict.keys()))
        if arm == armor_list[0]:
            self.hp += 4 * arm_rare
        elif arm == armor_list[1]:
            self.hp += 5 * arm_rare
        elif arm == armor_list[2]:
          self.hp += 3 * arm_rare
        elif arm == armor_list[3]:
          self.hp += 1 * arm_rare
        elif arm == armor_list[4]:
          self.hp += 2 * arm_rare
        return arm, armor_dict[arm_rare]




class Enemy:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage

  def create_enemy(self):
    rnd_name = random.choice(enemy_list)
    rnd_hp = random.randint(80, 250)
    rnd_damage = random.randint(15, 50)
    return Enemy(rnd_name, rnd_hp, rnd_damage)

  def attack(self, victim):
    rnd_attack = random.randrange(1, 5)
    if rnd_attack == 1:
      print(f'{self.name} наносит вам критический урон! ')
      victim.hp -= self.damage * 2
    elif rnd_attack == 2 or 3 or 4:
      victim.hp -= self.damage
    elif rnd_attack == 5:
      print(f'{self.name} промахивается! ')
      victim.hp -= 0
    if victim.hp <= 0:
      print('Вы погибли. ')
      quit()
    else:
      print(f'{victim.name}, оставшееся здоровье: {victim.hp}. ')


def fight_choice():
  question = input(f'Готов ли ты сразиться с монстром - {enemy.name}? Да или Нет?').capitalize()
  if question == 'Да':
    result = player.attack(enemy)
    if result == True:
      enemy.attack(player)
      fight_choice()
  elif question == 'Нет':
    escape = random.randint(1, 2)
    if escape == 1:
      print(f'Вы убежали от монстра - {enemy.name}. ')
    elif escape == 2:
      print(f'Вам не удалось сбежать от монстра - {enemy.name}. ')
      enemy.attack(player)
      fight_choice()
  else:
    print('Такого варианта ответа нет, попробуйте снова: ')
    fight_choice()


race_list = ['Человек', 'Гном', 'Оборотень', 'Гигант', 'Целитель', 'Разбойник', 'Зверь']
prof_list = ['Маг', 'Воин', 'Лучник', 'Всадник', 'Профессор', 'Обычный' ]
enemy_list = ['Таракан', 'Чёртик', 'Колдун', 'Шахтёр', 'Дракон', 'Змей']
weapon_list = ['Меч', 'Лук', 'Кирка', 'Ружье', 'Рогатка']
weapon_dict = {1: 'Обычное оружие', 2: 'Редкое оружие', 3: 'Эпическое оружие'}
armor_list = ['Шлем', 'Нагрудник', 'Поножи', 'Резиновые тапочки', 'Наручи']
armor_dict = {1: 'Обычная броня', 2: 'Редкая броня', 3: 'Эпическая броня'}
powers = ['Замораживание', 'Исцеление']
my_name = input('Введи имя для своего героя: ').capitalize()
race = input(f'К какой расе ты принадлежишь: {race_list}? ').capitalize()
prof = input(f'К какой профессии ты относишься: {prof_list}? ').capitalize()
player = Player.create_hero(my_name, race, prof)
print('Вы попали в подземелье! ')
while True:
  time.sleep(2)
  event = random.randint(1, 3)
  if event == 1:
    print('Тебе никто не встретился. ')
  elif event == 2:
    print('Вы нашли зелье увеличения здоровья! Ваше здоровье увеличилось на 10. ')
    player.hp += 10
    print(f'{player.name}, здоровье: {player.hp}. ')
  elif event == 3:
    enemy = Enemy.create_enemy()
    print(f'Тебе встретился монстр - {enemy.name}! ')
    print(f'{player.name}, здоровье: {player.hp}; урон: {player.damage}; мана: {player.mana}; уровень: {player.lvl}; опыт: {player.exp}. ')
    print(f'Монстр - {enemy.name}, здоровье: {enemy.hp}; урон: {enemy.damage}. ')
    fight_choice()