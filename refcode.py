if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            top_row = PlayingField(360, 80, 200, 20)
            self.center[1] -= 20
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(0, -20)
                self.remove(sprite2)
                passive.add(sprite2)
                if pygame.sprite.collide_rect(sprite2, top_row):
                    global dead
                    dead = True
            if not block_list:
                block_list = sequence_generator()
            if not bool(self):
                self.type = block_list[-1]
                self.add(Blocks(block_list.pop()))
            passive.check_for_point()  # did a row get cleared
        return collide



def pause_menu(screen1):
    pygame.mixer.music.set_volume(0.15)
    pausemenu = pygame.image.load("img/pausemenu.png")
    pausemenurect = pausemenu.get_rect()
    screen1.blit(pausemenu, pausemenurect)
    pygame.display.flip()
    while True:
        for event1 in pygame.event.get():
            if event1.type == QUIT:
                exit()
            if event1.type == KEYDOWN and event1.key == K_SPACE:
                return
            elif event1.type == KEYDOWN and event1.key == K_q:
                exit()

 if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(20, 0)

if not pygame.sprite.collide_rect(sprite, play_field):
                collide = True
            elif pygame.sprite.groupcollide(self, passive, False, False):
                collide = True
        if collide:
            for sprite2 in iter(self):
                sprite2.rect = sprite2.rect.move(-20, 0)

for event in pygame.event.get():



    while dead:
        print("LELELELE YOU DED")
