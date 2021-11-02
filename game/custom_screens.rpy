## Screen with Stats Button
screen Gallery_UI:

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/gallery_%s.png"
        action ShowMenu("GalleryUI")
screen Stats_UI:

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 90
        auto "UI/stats_%s.png"
        action ShowMenu("StatsUI")


style stats_button_text:
    xalign 0.5


        
