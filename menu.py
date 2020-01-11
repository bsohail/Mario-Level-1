from pygame import *
init()
##########################################################image load
marioMenu=image.load("images/marioMenu.png")
marioRule=image.load("images/marioRule.png")
background=image.load("images/wallpaper.jpg")
border=image.load("images/border.png")
marioMenuTransformed=transform.scale(marioMenu,(250,450))
marioRuleTransformed=transform.scale(marioRule,(250,450))
backgroundTransformed=transform.scale(background,(1000,600))
borderTransformed=transform.scale(border,(250,450))
#################################################################
click=False
screen=display.set_mode((1000,600))
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click=True
        if evt.type==MOUSEBUTTONUP:
            click=False
    mx,my=mouse.get_pos()
########################################################colide
    marioRect=Rect(375,75,250,450)
    screen.blit(backgroundTransformed,(0,0))
    screen.blit(marioMenuTransformed,marioRect)
########################################################hover
    if marioRect.collidepoint(mx,my):
        screen.blit(marioRuleTransformed,marioRect)
########################################################press
    if marioRect.collidepoint(mx,my) and click==True:
        import mario
    screen.blit(borderTransformed,marioRect)
    display.flip()
quit()
