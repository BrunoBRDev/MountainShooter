#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Enemy):
    def __init__(self, position: tuple):
        super().__init__('Enemy3', position)
        self.vertical_speed = ENTITY_SPEED['Enemy3']  # Velocidade de movimento vertical
        self.direction_y = 1  # 1: subindo, -1: descendo
        self.rect.centerx = WIN_WIDTH  # Começar na borda direita
        self.rect.centery = random.randint(100, WIN_HEIGHT - 100)  # Posição vertical aleatória

    def move(self):
        # Movimento horizontal (para a esquerda)
        self.rect.centerx -= self.vertical_speed

        # Movimento vertical
        if self.rect.top <= 0:  # Borda superior
            self.direction_y = -1  # Descer com velocidade dobrada
        elif self.rect.bottom >= WIN_HEIGHT:  # Borda inferior
            self.direction_y = 1  # Subir com velocidade normal

        self.rect.centery += self.vertical_speed * self.direction_y

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
