def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        0,
        -50)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy(effects.star_field, 500)
    otherSprite.destroy(effects.star_field, 500)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_countdown_end():
    game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap2(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

myEnemy: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
scene.set_background_color(8)
game.splash("Move your spaceship and destroy the flying asteroids to the spaceship. Stay alive in 10 seconds to win",
    "Pressed A to start game!")
mySprite = sprites.create(assets.image("""
    spaceship
"""), SpriteKind.player)
mySprite.say("start!!", 1000)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
info.start_countdown(10)

def on_update_interval():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(img("""
            . . . . . . . . . c c 8 . . . . 
                    . . . . . . 8 c c c f 8 c c . . 
                    . . . c c 8 8 f c a f f f c c . 
                    . . c c c f f f c a a f f c c c 
                    8 c c c f f f f c c a a c 8 c c 
                    c c c b f f f 8 a c c a a a c c 
                    c a a b b 8 a b c c c c c c c c 
                    a f c a a b b a c c c c c f f c 
                    a 8 f c a a c c a c a c f f f c 
                    c a 8 a a c c c c a a f f f 8 a 
                    . a c a a c f f a a b 8 f f c a 
                    . . c c b a f f f a b b c c 6 c 
                    . . . c b b a f f 6 6 a b 6 c . 
                    . . . c c b b b 6 6 a c c c c . 
                    . . . . c c a b b c c c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        0,
        50)
    myEnemy.x = randint(5, 155)
    myEnemy.set_kind(SpriteKind.enemy)
game.on_update_interval(1000, on_update_interval)
