init python:
    g = Gallery()

    ## Created a button called foto
    g.button("foto")
    g.condition("persistent.foto")
    ## if the CG is unlocked, and the user clicks it, the foto.png will show.
    g.image("album/foto.png")

    ## Created a button called red
    g.button("red")
    g.condition("persistent.red1")
    ## if the CG is unlocked, and the user clicks it, the red.jpg will show.
    g.image("album/red.jpg")


    ## Created a button called blue
    g.button("blue")
    g.condition("persistent.blue1")
    g.image("album/blue.jpg")


    ## Created a button called green_and_orange
    g.button("green_and_orange")
    g.condition("persistent.green_orange1")
    ## This will show two images, green and orange.
    g.image("album/green.jpg")
    g.image("album/orange.jpg")


screen gallery:
    tag menu
    # This is my background image
    add "images/customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        # This is a grid containing 2 columns and 2 rows.
        grid 2 2:
            xspacing 25
            yspacing 70
            ## This will add a button that we made.
            ## "red" is the button name.
            ## "album/small/red_small.jpg" is the preview image that will show on the button.
            ## "album/small/locked.jpg" is the preview image that will show when the button is locked.
            add g.make_button("foto","album/small/foto_small.png", locked = "album/small/locked.jpg")
            add g.make_button("red","album/small/red_small.jpg", locked = "album/small/locked.jpg")
            add g.make_button("blue", "album/small/blue_small.jpg", locked = "album/small/locked.jpg")

            add g.make_button("green_and_orange", "album/small/green_small.jpg", locked = "album/small/locked.jpg")
        vbox:
            xoffset 20 #this is the space between the gridbox and the "Return" button
            textbutton "Return" action Return() 

## Gallery UI
screen GalleryUI():
    tag galleryUI
    # This is my background image
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        # This is a grid containing 2 columns and 2 rows.
        grid 2 2:
            xspacing 25
            yspacing 70
            ## This will add a button that we made.
            ## "red" is the button name.
            ## "album/small/red_small.jpg" is the preview image that will show on the button.
            ## "album/small/locked.jpg" is the preview image that will show when the button is locked.
            add g.make_button("foto","album/small/foto_small.png", locked = "album/small/locked.jpg")
            add g.make_button("red","album/small/red_small.jpg", locked = "album/small/locked.jpg")
            add g.make_button("blue", "album/small/blue_small.jpg", locked = "album/small/locked.jpg")

            add g.make_button("green_and_orange", "album/small/green_small.jpg", locked = "album/small/locked.jpg")
        vbox:
            xoffset 20 #this is the space between the gridbox and the "Return" button
            textbutton "Return" action Return() 

style stats_button_text:
    xalign 0.5