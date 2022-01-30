# Main Script


#Main Character
define yn = Character("[yn]",color="#0000FF")
define y = Character("??",color="#0000FF")
define y = yn



#Auxiliar
define anon = Character("??",color="#fff")

#NPC
define mom = Character("Mãe")
define lucas = Character("[lucas_1.name]")
define anna = Character("[anna_1.name]")
define miguel = Character("[miguel_1.name]")
define alice = Character("[alice_1.name]")
define pedro = Character("[pedro_1.name]")
define policial = Character("Policial")

#Definição de variaveis

default var_anna = False
default var_miguel = False
default var_pedro = False
default var_lucas = False
default var_alice = False
default var_mauricio = False

# images

#mapa
image mapa_cidade = "/images/mapa.png"

#background
image pink = "#FFC1D7"

#album
image album_1 = "/images/album/red.jpg"
image foto_1 = "/images/album/foto.png"


# alice
image alice_normal = "/images/Characters/Alice/normal.png"
image alice_feliz = "/images/Characters/Alice/feliz.png"
image alice_confusa = "/images/Characters/Alice/confusa.png"
image alice_medo = "/images/Characters/Alice/medo.png"
image alice_neko = "/images/Characters/Alice/neko.png"
image alice_sexy = "/images/Characters/Alice/sexy.png"
image alice_apaixonada = "/images/Characters/Alice/apaixonada.png"
image alice_raiva = "/images/Characters/Alice/raiva.png"

# miguel
image miguel_normal = "/images/Characters/Miguel/normal.png"
image miguel_feliz = "/images/Characters/Miguel/feliz.png"
image miguel_confusa = "/images/Characters/Miguel/confusa.png"
image miguel_medo = "/images/Characters/Miguel/medo.png"
image miguel_neko = "/images/Characters/Miguel/neko.png"
image miguel_sexy = "/images/Characters/Miguel/sexy.png"
image miguel_apaixonada = "/images/Characters/Miguel/apaixonada.png"
image miguel_raiva = "/images/Characters/Miguel/raiva.png"

# anna
image anna_normal = "/images/Characters/Anna/normal.png"
image anna_feliz = "/images/Characters/Anna/feliz.png"
image anna_confusa = "/images/Characters/Anna/confusa.png"
image anna_medo = "/images/Characters/Anna/medo.png"
image anna_neko = "/images/Characters/Anna/neko.png"
image anna_sexy = "/images/Characters/Anna/sexy.png"
image anna_apaixonada = "/images/Characters/Anna/apaixonada.png"
image anna_raiva = "/images/Characters/Anna/raiva.png"

# pedro
image pedro_normal = "/images/Characters/Pedro/normal.png"
image pedro_feliz = "/images/Characters/Pedro/feliz.png"
image pedro_confusa = "/images/Characters/Pedro/confusa.png"
image pedro_medo = "/images/Characters/Pedro/medo.png"
image pedro_neko = "/images/Characters/Pedro/neko.png"
image pedro_sexy = "/images/Characters/Pedro/sexy.png"
image pedro_apaixonada = "/images/Characters/Pedro/apaixonada.png"
image pedro_raiva = "/images/Characters/Pedro/raiva.png"


# isabella
image isabella_normal = "/images/Characters/Isabella/normal.png"
image isabella_feliz = "/images/Characters/Isabella/feliz.png"
image isabella_confusa = "/images/Characters/Isabella/confusa.png"
image isabella_medo = "/images/Characters/Isabella/medo.png"
image isabella_neko = "/images/Characters/Isabella/neko.png"
image isabella_sexy = "/images/Characters/Isabella/sexy.png"
image isabella_apaixonada = "/images/Characters/Isabella/apaixonada.png"
image isabella_raiva = "/images/Characters/Isabella/raiva.png"

# lucas
image lucas_normal = "/images/Characters/Lucas/normal.png"
image lucas_feliz = "/images/Characters/Lucas/feliz.png"
image lucas_confusa = "/images/Characters/Lucas/confusa.png"
image lucas_medo = "/images/Characters/Lucas/medo.png"
image lucas_neko = "/images/Characters/Lucas/neko.png"
image lucas_sexy = "/images/Characters/Lucas/sexy.png"
image lucas_apaixonada = "/images/Characters/Lucas/apaixonada.png"
image lucas_raiva = "/images/Characters/Lucas/raiva.png"

# The game starts here.

label start:    
    #Warning content
    scene pink
    
    $ renpy.movie_cutscene("/images/videos/content-warningfull.webm")

    # Episódio 0 - Introdução

    "Você acorda em um onibus"
    "Os passageiros começam a sair e você pega sua malas"
    "Sua familia está te esperando do lado de fora"
    $ yn = renpy.input("Seu nome")
    $ main_1.sobrenome = renpy.input("Seu sobrenome")
    $ yn = yn.strip()
    $ main_1.name = yn
    if yn == "Clara":
        "Você de novo... Sentimos sua falta..."

    show isabella_normal
    mom "[yn] que saudade!"
    y "Oi mãe!"
    $isabella_1.relation = "Mãe"
    "Vocês duas se abraçam"
    "Vocês vão indo para casa"
    "Pela janela você ve a cidade que cresceu"
    y "Tudo continua igual..."
    mom "Sim, as coisas não mudam muito por aqui"
    mom "Eu imagino que seja diferente de onde você está, você foi pra São Paulo afinal"
    y "Sim, é bem diferente, mas eu gosto daqui"
    hide isabella_normal
    "Vocês chegam em casa e você se instala no seu antigo quarto"
    y "Nada mudou mesmo..."
    "Você vê uma foto antiga de você e seus amigos na época"
    
    $renpy.notify("Galeria Desbloqueada")
    show screen Gallery_UI
    show foto_1 at center:    
        yoffset -200
    ## This is how you unlock the CG.
    ## This "persistent.foto" is the condition used for "foto" button.
    $ persistent.foto = True
    y "É... Isso mudou..."
    mom "[yn], preciso ir no mercado, você quer vir comigo?"
    y "Ok!"
    hide foto_1
    "Vocês vão para o mercado"
    "Você está pegando itens na lista que sua mãe pediu"
    anon "[yn]??"
    anon "[yn]? Nossa quanto tempo!"
    $renpy.notify("Bloco de Notas Desbloqueado")
    show screen Stats_UI
    show alice_normal

    if main_1.name == "Alice":
        $alice_1.name = "Aline"
    else:
        $alice_1.name = "Alice"

    y "Uau... [alice_1.name!u]!"
    $renpy.notify("Você Descobriu Algo Novo")
    alice "Meu deus, você não tinha ido pra USP?"
    y "Sim! E você não tinha ido pra UFMG? A nova mediciner do grupo"
    $renpy.notify("Você Descobriu Algo Novo")
    $ alice_1.major = "Médica"
    alice "Sim, estou passando as férias agora na casa dos meus pais, eu cheguei tem uma semana"
    y "Ah eu também, cheguei hoje mais cedo"
    alice "Nossa, que legal a gente se encontrar"
    y "É mesmo"
    hide alice_normal
    show alice_normal at right
    show isabella_normal at left
    mom "Olá [alice_1.name]! Quanto tempo"

    if main_1.name == "Isabella" or main_1.name == "Isabela":
        $isabella_1.name = "Isadora"
    else:
        $isabella_1.name = "Isabella"

    alice "Oi dona [isabella_1.name]!"
    $renpy.notify("Você Descobriu Algo Novo")
    $isabella_1.sobrenome = main_1.sobrenome
    $isabella_1.imageName = "images/Characters/Isabella/normal.png"
    $alice_1.imageName = "/images/Characters/Alice/normal.png"
    mom "Que bom ver você"
    alice "Sim, é ótimo te ver"
    mom "Bom, vou deixar vocês à sós pra conversar"
    hide alice_normal
    hide isabella_normal
    show alice_normal
    if main_1.name == "Pedro":
        $pedro_1.name = "Jorge"
    else:
        $pedro_1.name = "Pedro"

    alice "Você se lembra do [pedro_1.name]?"
    if main_1.sobrenome == "Silva":
        $pedro_1.sobrenome = "Souza"
    else:
        $pedro_1.sobrenome = "Silva"
    y "[pedro_1.name] [pedro_1.sobrenome]? Lembro sim"
    $renpy.notify("Você Descobriu Algo Novo")
    alice "Ele está dando uma festa hoje na casa dele, e me chamou pra ir, quer ir junto de surpresa?"
    y "Ele ainda mora no mesmo lugar?"
    alice "Sim, ele nunca saiu. Ele tentou seguir a carreira de jogador mas nunca deu certo, agora ele é eletricista"
    y "Puxa, não sabia. Mas sobre a festa, aceito ir sim, acho que vai ser bom rever todo mundo"
    alice "Que ótimo! Te busco amanhã mais tarde então"
    hide alice_normal
    #mapa da cidade desbloqueado


    "[alice_1.name] te busca em casa e vocês vão para a festa"
    "Chegando na festa, está muita gente lá"
    "Você reconhece alguns amigos antigos"

    if main_1.name == "Lucas":
        $lucas_1.name = "Jorge"
    else:
        $lucas_1.name = "Lucas"

    if main_1.name == "Luana" or main_1.name == "Luanna":
        $anna_1.name = "Lúcia"
    else:
        $anna_1.name = "Luana"

    if main_1.name == "Miguel":
        $miguel_1.name = "Jorge"
    else:
        $miguel_1.name = "Miguel"

    label primeiro_menu:
    if var_lucas and var_anna and var_miguel and var_pedro: 
        jump choice_scene
    menu:
        "Com quem você fala primeiro?"

        "[lucas_1.name]" if not var_lucas:
            $var_lucas = True
            jump c1_lucas

        "[anna_1.name]" if not var_anna:
            $var_anna = True
            jump c1_anna

        "[miguel_1.name]" if not var_miguel:
            $var_miguel = True
            jump c1_miguel

        "[pedro_1.name]" if not var_pedro:
            $var_pedro = True
            jump c1_pedro

    label c1_lucas:
    show lucas_normal
    y "Oi [lucas_1.name], quanto tempo"
    $lucas_1.imageName = "/images/Characters/Lucas/normal.png"
    $renpy.notify("Você Descobriu Algo Novo")
    lucas "É, não o suficiente"
    y "Nossa, o que aconteceu"
    lucas "Olha, eu queria poder falar com você, mas a [anna_1.name] tem razão"
    $renpy.notify("Você Descobriu Algo Novo")
    lucas "A gente juntos, só causa problemas"
    "Ele vira de costas e vai embora..."
    hide lucas_normal

    menu:
        "Tentar chamar ele":
            jump c2_lucas
        "Deixar ele ir":
            jump primeiro_menu
    
    label c2_lucas:
    show lucas_normal
    y "[lucas_1.name], espera..."
    "Você tenta puxar ele pelo braço"
    y "Eu só queria reencontrar todo mundo, nós éramos tão amigos, tão próximos"
    y "Eu queria ter isso de novo..."
    $renpy.notify("+1 ponto")
    $lucas_1.affection +=1
    lucas "Eu..."
    "Lucas tenta falar, mas você vê ao longe uma mulher encarando vocês dois"
    lucas "Só é melhor a gente ficar longe"
    "Ele vai embora"
    hide lucas_normal
    jump primeiro_menu

    label c1_anna:
    show anna_normal
    y "Oi [anna_1.name]"
    $anna_1.imageName = "/images/Characters/Anna/normal.png"
    $renpy.notify("Você Descobriu Algo Novo")
    "Ela finge que não escutou você"
    "Você encosta no braço dela"
    anna "Você não entende mesmo quando alguém não quer conversar com você"
    y "Olha, eu só queria conversar"
    anna "E eu não quero"
    y "Espera..."
    anna "Não! Para de tentar"
    anna "Ninguém quer você aqui"
    if var_lucas == True:
        anna "E fica longe do meu namorado também, a gente quer distância de vocês todos"
        if anna_1.name == "Anna":
            $lucas_1.relation = "Namorado de Anna"
        else:
            $lucas_1.relation = "Namorado de Anita"
        
        if lucas_1.name == "Lucas":
            $anna_1.relation = "Namorada de Lucas"
        else:
            $anna_1.relation = "Namorada de Jorge"
        
        $renpy.notify("Você Descobriu Algo Novo")
    "Ela vai embora"
    hide anna_normal
    jump primeiro_menu

    label c1_miguel:
    show miguel_normal
    $miguel_1.imageName = "/images/Characters/Miguel/normal.png"
    y "Oi [miguel_1.name]"
    $renpy.notify("Você Descobriu Algo Novo")
    miguel "Oi [yn], quanto tempo"
    y "Sim, bastante tempo"
    if var_lucas == True or var_anna == True:
        y "Pelo menos uma pessoa nessa festa quer conversar comigo..."
        miguel "É, as pessoas costumam ser rancorosas por aqui"
        y "É... nada mudou"
    miguel "Entâo, o que você veio fazer aqui? Achei que tinha saído daqui de vez"
    y "É, eu to morando em São Paulo agora, vim visitar minha mãe agora no final de ano"
    miguel "É, eu fiquei sabendo, sua mãe contou que você está fazendo direito em São Paulo"
    miguel "Bom, fiquei sabendo por ela, já que você bloqueou todo mundo no instagram"

    menu:
        "É... Me desculpa por isso":
            $miguel_pontos = 1
        "É, é faria de novo":
            $miguel_pontos = 0

    if miguel_pontos == 1:
        y "É... Me dewsculpa por isso"
        y "Acho que eu precisava de um recomeço"
        $ renpy.notify("+1 ponto")
        $miguel_1.affection += 1
        miguel "Compreensível..."
        miguel "Eu acho que faria a mesma coisa se tivesse saído daqui"
        y "E você, o que faz da vida?"
        miguel "Bom, eu sou chaveiro, não é nada tão interessante quanto o que você faz, mas paga as contas"
        $renpy.notify("Você Descobriu Algo Novo")
        $miguel_1.major = "Chaveiro"
        miguel "Depois que meus pais morreram eu a casa deles ficou pra mim, e as dividas também"
        $miguel_1.history = "Pais mortos, cheio de dívidas"
        miguel "Fiz alguns cursos e agora trabalho por aqui"
        miguel "Então não sairia dessa cidade nem se eu pudesse"
        y "Entendi"
        miguel "Bom, boa festa pra você"
        y "Pra você também, bom te ver"
        miguel "Igualmente"
    if miguel_pontos ==0:
        y "É, e faria de novo"
        $ renpy.notify("-1 ponto")
        miguel "Bom, quando você não se importa com ninguém, é muito dificil esperar que os outros se importem também"
        miguel "Até outro dia"
        
    hide miguel_normal
    jump primeiro_menu

    label c1_pedro:
    show pedro_feliz
    $pedro_1.imageName = "/images/Characters/Pedro/normal.png"
    y "Oi [pedro_1.name]"
    pedro "[yn]! Nooossa"
    "Pedro vem te abraçar, quando ele chega perto você sente o cheiro de cigarro e bebida"
    $pedro_1.history = "Alcoolatra "
    $renpy.notify("Você Descobriu Algo Novo")
    pedro "Que bom que eu te convidei pra festa"
    pedro "Eu te convidei pra festa né?"
    menu:
        "Sim":
            $pedro_pontos = 2

        "Não, vim com a [alice_1.name]":
            $pedro_pontos = 1

        "Você está bebendo muito":
            $pedro_pontos = 0
    
    if pedro_pontos ==1:
        "Não, vim com a [alice_1.name]"
        $ renpy.notify("+1 ponto")
        $pedro_1.affection += 1
        pedro "[alice_1.name] veio também??? Que legaaal"
        y "Sim, ela está por aí"
        
    if pedro_pontos == 2:
        y "Sim"
        $ renpy.notify("+2 pontos")
        $pedro_1.affection += 2
        pedro "Ah eu sabia, eu sou muito bom"

    if pedro_pontos >0:
        pedro "Mas me fala, você finalmente saiu desse ninho de rato que é essa cidade"
        y "Sim, eu saí"
        pedro "É, você ta vivendo o sonho"
        y "Você nunca saiu?"
        pedro "Não, eu nunca fui tão bom na escola quanto você"
        pedro "De acordo com meus pais, eu nunca fui bom em nada"
        pedro "E aparentemente eles tinham razão"
        y "Não fale assim, você era ótimo nos esportes, sempre achei que você ia virar profissional"
        pedro "Era o sonho, até que eu tive o acidente"
        $pedro_1.history = pedro_1.history + "Bom nos esportes, sofreu acidente"
        $renpy.notify("Você Descobriu Algo Novo")
        y "Desculpa... Eu não sabia"
        pedro "Tá tudo bem"
        pedro "Mas fico feliz que pelo menos um de nós está fazendo o que queria"
        pedro "Você veio com a [alice_1.name] né? Vou procurar ela então"
        pedro "Muito bom ver você"
        "Ele sai cambaleando"
    if pedro_pontos == 0:
        y "Você está bebendo demais"
        $ renpy.notify("-1 pontos")
        pedro "Calma [yn], é uma festa"
        pedro "Mas acho que pra você é fácil julgar o que fazemos aqui"
        pedro "Você deixou tudo pra trás, mas nem todo mundo pode fazer isso"
        "Ele vai embora"
    
    hide pedro_feliz
    jump primeiro_menu

    label choice_scene:
    "Você falou com todo mundo"
    "Você se encontra novamente com [alice_1.name] e [pedro_1.name]"
    "Eles estão conversando e se divertindo"
    "A noite vai passando, você bebe um pouco"
    "cerca de 1 da manhã, poucas pessoas continuam na festa"
    "Vocês escutam um barulho vindo da garagem"
    pedro "Que bosta, alguem deve ter quebrado a porta saindo com o carro"
    pedro "Vem em ajudar a ver o que é"
    "Você, [alice_1.name], [pedro_1.name] e [anna_1.name] vão até a garagem"
    anna "Tem alguma coisa embaixo da porta, ela não consegue fechar"
    "A garage está escura, ninguem consegue identificar o que é"
    "Vocês chegam mais perto"
    "É uma mochila"
    pedro "ok, quem deixou a mochila no meio da porta da garagem?"
    anna "Pera. Essa mochila é do [lucas_1.name]"
    pedro "Ele já foi embora? E deixou a mochila aqui? Que merda"
    anna "Não, ele não foi, ele veio comigo, está sem carro"
    alice "Estranho, e onde ele está?"
    anna "Ele tinha ido no banheiro... Mas pensando bem já tem bastante tempo"
    pedro "Será que ele foi embora com outra pessoa?"
    anna "Você é idiota? Claro que não!"
    
    menu:
        "Ele pode ter ido com outra pessoa sem te avisar":
            $anna_1.affection += 0
        "Ele deve estar por aqui, fiquem tranquilos":
            $anna_1.affection += 1
    
    if anna_1.affection == 0:
        y "Ele pode ter ido com outra pessoa sem te avisar"
        $renpy.notify("-1 pontos")
        anna "O que você quer dizer com isso?"
        y "Nada... Só digo que ele pode ter saído com outra pessoa"
        anna "Ele não saiu com ninguém!"
        alice "Calma, Anna. A gente ta só considerando a possibilidade"
        anna "Cala a boca você também, sua piranha"
        alice "Vai se fuder!"
        pedro "Calma vocês duas!"
        pedro "Vamos procurar ele então"
        anna "Tá"
    
    if anna_1.affection == 1:
        y "Ele deve estar por aqui, fiquem tranquilos"
        $renpy.notify("+1 pontos")
        anna "Exatamente, obrigada [yn]"
        alice "Bom, vamos procurar ele então"

    "Vocês olham um pouco pela garagem"
    "Até que..."
    pedro "[lucas_1.name!u]!"
    "Vocês encontram [lucas_1.name] dormindo encostado na parede"
    anna "Meu deus, você me assustou!"
    "Ele não responde"

    "Você tenta acordá-lo encostando em seu ombro"
    y "[lucas_1.name]... Acorda..."
    "Você encosta a mão em seu ombro"
    "Está rígido e frio"
    alice "Alguém acende a luz por favor?"
    "Pedro acende a luz da garagem"
    anna "[lucas_1.name!u]!"
    "Quando a luz acende vocês veem, que tem uma faca na barriga de Lucas"
    "Você dá um pulo para trás e o corpo cai, revelando uma grande macha de sangue na parede atrás do corpo"
    $lucas_1.vivo = 0
    $lucas_1.imageName = "images/Characters/Lucas/morto.png"
    alice "O QUE ESTÁ ACONTECENDO?"
    pedro "Alguem liga pra ambulância, polícia, sei lá"
    anna "MEU DEUS O QUE ACONTECEU!"
    "[alice_1.name] tenta confortar Anna"
    anna "Eu vou ligar pra polícia!"
    "[anna_1.name] sai da garagem acompanhada por [pedro_1.name]"
    "Você e [alice_1.name] permanecem na garagem observando o corpo"
    "Vocês chegam perto e na ponta da faca tem uma mensagem"
    "Ele mereceu, e vocês todos também"
    "[alice_1.name] olha pra você e rapidamente tira a mensagem da faca e a guarda no bolso"
    "alguns minutos depois você escuta a sirene"
    "a policia vem e leva o corpo"
    "Eles fazem algumas perguntas para você e Alice"
    policial "Entâo... Vocês viram mais alguma coisa que pode ajudar no caso?"
    alice "Não... Mais nada..."
    "Após o interrogatório, [alice_1.name] leva você , [pedro_1.name],[anna_1.name] e [miguel_1.name] para seus respectivos destinos"
    miguel "Vocês acham que o que aconteceu com o [lucas_1.name] tem a ver com aquilo que aconteceu?"
    pedro "Cala a boca!"
    miguel "Mas a gente precisa falar sobre isso"
    pedro "Não, a gente não precisa"
    pedro "É a última coisa que a gente precisa falar"
    anna "Eu sabia que quando a gente fica juntos coisas ruins acontecem"
    alice "Então a culpa é nossa?"
    anna "De quem seria?"
    alice "Você esquece que vocês também estavam lá, ninguém obrigou vocês a fazer nada"
    anna "Não?? Claro que obrigaram, vocês todos são pessoas horríveis"
    anna "Por isso eu e o [lucas_1.name] fizemos o máximo pra ficar longe de você"
    anna "No dia que ficamos todos juntos... Olha o que acontece"
    pedro "Cala a boca vocês todos!"
    pedro "O que aconteceu hoje foi um incidente separado"
    pedro "Não tem nada a ver com o que aconteceu"
    pedro "E ninguém mais vai falar sobre isso"
    pedro "Não tem nada que prove que tem alguma relação"
    menu:
        "Contar sobre a mensagem":
            $segredo = 1
        "Não falar nada":
            $segredo = 0
    if segredo == 1:
        y "Na verdade tem uma coisa"
        alice "[yn]..."
        y "Não, eles precisam saber"
        alice "..."
        anna "Que porra vocês sabem?"
        y "Tinha uma mensagem no corpo hoje"
        y "Estava escrito 'Ele mereceu, e vocês todos também' "
        "..."
        anna "E vocês esconderam isso da gente?"
        alice "Eu escondi da polícia"
        alice "De nada, inclusive"
        anna "A gente precisa mostrar pra polícia"
        pedro "Você ta ficando doida?"
        pedro "[alice_1.name] fez a coisa certa"
        anna "Do que você ta falando? É a nossa segurança que estamos falando"
        pedro "Cala a boca, se a gente mostra isso pra polícia, vamos ter que explicar o motivo"
        alice "E o motivo de eu ter escondido a mensagem"
        anna "Isso não é problema meu"
        anna "É a minha segurança que estamos falando"
        anna "Eu não to nem aí pro que acontece com vocês"
        pedro "É mesmo? Você se esqueceu do que você fez?"
        anna "..."
        anna "Não, eu nunca esqueci, você sabe muito bem disso"
        anna "Eu só estou preocupada"
        alice "Todos nós estamos"
    
    miguel "E se vierem atrás da gente?"
    pedro "Ninguém vai vir fazer nada"
    miguel "Vieram atrás do [lucas_1.name]..."
    pedro "Ele estava despreparado"
    pedro "Nós não estamos"
    "Alice chega na casa de [pedro_1.name], deixando ele e [anna_1.name]"
    "Agora se dirige para sua casa"
    alice "Tenham cuidado a partir de agora"
    if segredo == 1:
        miguel "E se a mensagem tinha razão?"
        miguel "E se a gente realmente merece tudo isso?"
        alice "A gente merece muita coisa..."
        alice "Mas o [lucas_1.name] não merecia isso"
        alice "Ele era uma pessoa boa"
        miguel "Ninguém é totalmente bom"
        miguel "A gente devia saber disso"
    "Vocês chegam em sua casa"
    alice "Tchau [yn]"
    y "Tchau pessoal"

    #ep 2

    mom "[yn], você não comeu nada..."
    mom "Eu entendo que o que aconteceu ontem foi muito dificil para você, mas você precisa comer"
    y "É, eu sei..."
    mom "Eu sabia que aquela familia voltar pra cidade era uma coisa ruim"
    y "Quem voltou?"

    if main_1.name == "Luiz":
        $luiz_1.name = "Jorge"
    else:
        $luiz_1.name = "Luiz"

    mom "Ah eu não devia ter comentado..."
    y "Não, agora eu preciso saber"
    mom "Certo... Tudo bem"
    mom "Eu não queria trazer isso a tona, ainda mais com você aqui tão pouco tempo"
    y "Mãe... Me conta por favor"
    mom "Você se lembra daquele homem horrível, o [luiz_1.name]"
    y "..."
    y "Infelizmente eu me lembro"
    mom "Então, você se lembra como ele... Desapareceu anos atrás"
    mom "A filha dele nunca aceitou o desaparecimento, ela está morando na antiga casa dele"
    mom "A Sabrina, mãe daquele seu amigo [pedro_1.name] disse que ela está investigando o que aconteceu com o pai"
    y "Investigando?"
    mom "Sim, ela acha que ele ainda está por aí"
    mom "Felizmente pra nós, ele não está por aí"
    mom "Aquele homem horrível"
    mom "Se a filha dele soubesse das coisas que ele fez, ela não estaria tentando encontra-lo"
    if main_1 == "Julia" or main_1.name == "Júlia":
        $julia_1.name = "Gabriela"
    else:
        $julia_1.name = "Júlia"
    mom "Fazer aquilo com a [julia_1.name], uma criança"
    y "Sim..."
    y "Mas não podemos culpar ela, ela não sabe o que aconteceu"
    mom "É, mas mesmo assim. Me dá calafrios"
    mom "Desculpe falar sobre isso, eu sei que deve te trazer memórias ruins"
    mom "Mas eu só não consigo acreditar que ela está na cidade"
    mom "E pouco tempo depois, acontece essa tragédia"
    mom "Só... Tome cuidado, [yn]"
    mom "Por favor... Por mim..."
    y "Sim, mãe, eu vou tomar"
    "Seu telefone toca"
    call phone_start

    call message_start("[alice_1.name]", "Ei [yn], precisamos conversar")

    call reply_message("Tudo bem")
    call message("[alice_1.name]", "Todos nós")

    call message_img("[alice_1.name]", "Algo aconteceu","images/phone/pic1.png")

    call screen phone_reply("não acredito!","choice1","eu sei quem está fazendo isso","choice2")
    # i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
##call screen phone_reply3("awesome!","choice1","lame","choice2","im gay","choice3")

    label choice1:    
    # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
        call phone_after_menu
    
    # whenever you put the sender name to be "me" it is the player characters own message!
        call message_start("[main_1.name]", "não acredito!")
        call message("[alice_1.name]", "Vem pra cá agora")

        jump aftermenu
    
    label choice2:
        call phone_after_menu
        call message_start("[main_1.name]", "eu sei quem está fazendo isso")
        call message("[alice_1.name]", "então conte pra todo mundo hoje a tarde")
    
        jump aftermenu

    
    label aftermenu:
        call message("[alice_1.name]", "Precisamos conversar")
    
        # this one puts away the phone!
        call phone_end
    
    "Você vai até o lugar encontrar em [alice_1.name]"
    y "[alice_1.name]... Onde você está?"


    # This ends the game.

    return
