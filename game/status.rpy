      
## Stats UI
screen StatsUI():
    tag menu
    # This is my background image
    add "images/customUI/bg_gallery.jpg"
    
    hbox:
        ## left frame
        frame:
            style_prefix "stats"
            ysize 1080
            xsize 640
            vbox:
                xalign 0.5
                yalign 0.5
                
                textbutton _(main_1.name):
                    action SetVariable("selectedCharacter", main_1)
                    xsize 640
                textbutton _(alice_1.name):
                    action SetVariable("selectedCharacter", alice_1)
                    xsize 640
                textbutton _(anna_1.name):
                    action SetVariable("selectedCharacter", anna_1)
                    xsize 640
                textbutton _(pedro_1.name):
                    action SetVariable("selectedCharacter", pedro_1)
                    xsize 640
                textbutton _(miguel_1.name):
                    action SetVariable("selectedCharacter", miguel_1)
                    xsize 640
                textbutton _(lucas_1.name):
                    action SetVariable("selectedCharacter", lucas_1)
                    xsize 640
                textbutton _(mauricio_1.name):
                    action SetVariable("selectedCharacter", mauricio_1)
                    xsize 640
                textbutton _(isabella_1.name):
                    action SetVariable("selectedCharacter", isabella_1)
                    xsize 640
                textbutton _(luiz_1.name):
                    action SetVariable("selectedCharacter", luiz_1)
                    xsize 640
                textbutton _(julia_1.name):
                    action SetVariable("selectedCharacter", julia_1)
                    xsize 640
                textbutton "Return" action Return() 
        ## Right frame
        ## Notice that we're using selectedCharacter to show the variables here.
        frame:
            ysize 1080
            xsize 1280
            vbox:
                xoffset 20
                yoffset 20
                text "Nome: [selectedCharacter.name] [selectedCharacter.sobrenome]"
                text "Tipo Sanguíneo: [selectedCharacter.bloodType]"
                text "Profissão: [selectedCharacter.major]"
                text "Relação: [selectedCharacter.relation]"
                text "História: [selectedCharacter.history]"

                
                text "Pontos"
                ## We're creating a bar with the max affection of 10
                ## You can change the max affection to 100 or whatever value you want.
                bar value StaticValue(selectedCharacter.affection, 10) xsize 300 xoffset 80
            
            add selectedCharacter.imageName xsize 400 ysize 400 xoffset 100 yoffset 300
            
            

style stats_button_text:
    xalign 0.5