# Main Script


#Main Character
define yn = Character("[yn]",color="#0000FF")
define y = Character("??",color="#0000FF")
define y = yn



#Auxiliar
define anon = Character("??",color="#fff")

#NPC
define mom = Character("Mãe")
define lucas = Character("Lucas")
define anna = Character("Anna")
define miguel = Character("Miguel")
define alice = Character("Alice")
define pedro = Character("Pedro")
define policial = Character("Policial")

image pink = "#FFC1D7"

#Definição de variaveis

default var_anna = False
default var_miguel = False
default var_pedro = False
default var_lucas = False
default var_alice = False
default var_mauricio = False

$anna_pontos = -2
$miguel_pontos = 0
$pedro_pontos = 0
$lucas_pontos = -1
$alice_pontos = 1
$mauricio_pontos = 0

# images

#mapa
image mapa_cidade = "/images/mapa.png"

# xiong
image xiong_normal = "/images/Characters/xiong_xue/normal.png"
image xiong_feliz = "/images/Characters/xiong_xue/feliz.png"
image xiong_confusa = "/images/Characters/xiong_xue/confusa.png"
image xiong_medo = "/images/Characters/xiong_xue/medo.png"
image xiong_neko = "/images/Characters/xiong_xue/neko.png"
image xiong_sexy = "/images/Characters/xiong_xue/sexy.png"
image xiong_apaixonada = "/images/Characters/xiong_xue/apaixonada.png"
image xiong_raiva = "/images/Characters/xiong_xue/raiva.png"

# alice
image alice_normal = "/images/Characters/alice_guerrero/normal.png"
image alice_feliz = "/images/Characters/alice_guerrero/feliz.png"
image alice_confusa = "/images/Characters/alice_guerrero/confusa.png"
image alice_medo = "/images/Characters/alice_guerrero/medo.png"
image alice_neko = "/images/Characters/alice_guerrero/neko.png"
image alice_sexy = "/images/Characters/alice_guerrero/sexy.png"
image alice_apaixonada = "/images/Characters/alice_guerrero/apaixonada.png"
image alice_raiva = "/images/Characters/alice_guerrero/raiva.png"

# ayisha
image ayisha_normal = "/images/Characters/ayisha_okoye/normal.png"
image ayisha_feliz = "/images/Characters/ayisha_okoye/feliz.png"
image ayisha_confusa = "/images/Characters/ayisha_okoye/confusa.png"
image ayisha_medo = "/images/Characters/ayisha_okoye/medo.png"
image ayisha_neko = "/images/Characters/ayisha_okoye/neko.png"
image ayisha_sexy = "/images/Characters/ayisha_okoye/sexy.png"
image ayisha_apaixonada = "/images/Characters/ayisha_okoye/apaixonada.png"
image ayisha_raiva = "/images/Characters/ayisha_okoye/raiva.png"

# beatriz
image beatriz_normal = "/images/Characters/beatriz_souza/normal.png"
image beatriz_feliz = "/images/Characters/beatriz_souza/feliz.png"
image beatriz_confusa = "/images/Characters/beatriz_souza/confusa.png"
image beatriz_medo = "/images/Characters/beatriz_souza/medo.png"
image beatriz_neko = "/images/Characters/beatriz_souza/neko.png"
image beatriz_sexy = "/images/Characters/beatriz_souza/sexy.png"
image beatriz_apaixonada = "/images/Characters/beatriz_souza/apaixonada.png"
image beatriz_raiva = "/images/Characters/beatriz_souza/raiva.png"

# genevieve
image genevieve_normal = "/images/Characters/genevieve_dubois/normal.png"
image genevieve_feliz = "/images/Characters/genevieve_dubois/feliz.png"
image genevieve_confusa = "/images/Characters/genevieve_dubois/confusa.png"
image genevieve_medo = "/images/Characters/genevieve_dubois/medo.png"
image genevieve_neko = "/images/Characters/genevieve_dubois/neko.png"
image genevieve_sexy = "/images/Characters/genevieve_dubois/sexy.png"
image genevieve_apaixonada = "/images/Characters/genevieve_dubois/apaixonada.png"
image genevieve_raiva = "/images/Characters/genevieve_dubois/raiva.png"

# helena
image helena_normal = "/images/Characters/helena_lawson/normal.png"
image helena_feliz = "/images/Characters/helena_lawson/feliz.png"
image helena_confusa = "/images/Characters/helena_lawson/confusa.png"
image helena_medo = "/images/Characters/helena_lawson/medo.png"
image helena_neko = "/images/Characters/helena_lawson/neko.png"
image helena_sexy = "/images/Characters/helena_lawson/sexy.png"
image helena_apaixonada = "/images/Characters/helena_lawson/apaixonada.png"
image helena_raiva = "/images/Characters/helena_lawson/raiva.png"

# priya
image priya_normal = "/images/Characters/priya_chaudhari/normal.png"
image priya_feliz = "/images/Characters/priya_chaudhari/feliz.png"
image priya_confusa = "/images/Characters/priya_chaudhari/confusa.png"
image priya_medo = "/images/Characters/priya_chaudhari/medo.png"
image priya_neko = "/images/Characters/priya_chaudhari/neko.png"
image priya_sexy = "/images/Characters/priya_chaudhari/sexy.png"
image priya_apaixonada = "/images/Characters/priya_chaudhari/apaixonada.png"
image priya_raiva = "/images/Characters/priya_chaudhari/raiva.png"

# sasha
image sasha_normal = "/images/Characters/sasha_petrova/normal.png"
image sasha_feliz = "/images/Characters/sasha_petrova/feliz.png"
image sasha_confusa = "/images/Characters/sasha_petrova/confusa.png"
image sasha_medo = "/images/Characters/sasha_petrova/medo.png"
image sasha_neko = "/images/Characters/sasha_petrova/neko.png"
image sasha_sexy = "/images/Characters/sasha_petrova/sexy.png"
image sasha_apaixonada = "/images/Characters/sasha_petrova/apaixonada.png"
image sasha_raiva = "/images/Characters/sasha_petrova/raiva.png"

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
    $ yn = yn.strip()
    if yn == "Clara":
        "Você de novo... Sentimos sua falta..."

    mom "[yn] que saudade!"
    y "Oi mãe!"
    "Vocês duas se abraçam"
    "Vocês vão indo para casa"
    "Pela janela você ve a cidade que cresceu"
    y "Tudo continua igual..."
    mom "Sim, as coisas não mudam muito por aqui"
    mom "Eu imagino que seja diferente de onde você está, você foi pra São Paulo afinal"
    y "Sim, é bem diferente, mas eu gosto daqui"
    "Vocês chegam em casa e você se instala no seu antigo quarto"
    y "Nada mudou mesmo..."
    "Você vê uma foto antiga de você e seus amigos na época"
    y "É... Isso mudou..."
    mom "[yn], preciso ir no mercado, você quer vir comigo?"
    y "Ok!"
    "Vocês vão para o mercado"
    "Você está pegando itens na lista que sua mãe pediu"
    anon "[yn]??"
    anon "[yn]? Nossa quanto tempo!"
    y "Uau... Alice!"
    alice "Meu deus, você não tinha ido pra USP?"
    y "Sim! E você não tinha ido pra UFMG?"
    alice "Sim, estou passando as férias agora na casa dos meus pais, eu cheguei tem uma semana"
    y "Ah eu também, cheguei hoje mais cedo"
    alice "Nossa, que legal a gente se encontrar"
    y "É mesmo"
    alice "Você se lembra do Pedro?"
    y "Pedro Silva? Lembro sim"
    alice "Ele está dando uma festa hoje na casa dele, e me chamou pra ir, quer ir junto de surpresa?"
    y "Ele ainda mora no mesmo lugar?"
    alice "Sim, ele nunca saiu. Ele tentou seguir a carreira de jogador mas nunca deu certo, agora ele é eletricista"
    y "Puxa, não sabia. Mas sobre a festa, aceito ir sim, acho que vai ser bom rever todo mundo"
    alice "Que ótimo! Te busco amanhã mais tarde então"
    #mapa da cidade desbloqueado


    "Alice te busca em casa e vocês vão para a festa"
    "Chegando na festa, esta muita gente lá"
    "Você reconhece alguns amigos antigos"

    label primeiro_menu:
    if var_lucas and var_anna and var_miguel and var_pedro: 
        jump choice_scene
    menu:
        "Com quem você fala primeiro?"

        "Lucas" if not var_lucas:
            $var_lucas = True
            jump c1_lucas

        "Anna" if not var_anna:
            $var_anna = True
            jump c1_anna

        "Miguel" if not var_miguel:
            $var_miguel = True
            jump c1_miguel

        "Pedro" if not var_pedro:
            $var_pedro = True
            jump c1_pedro

    label c1_lucas:
    y "Oi Lucas, quanto tempo"
    lucas "É, não o suficiente"
    y "Nossa, o que aconteceu"
    lucas "Olha, eu queria poder falar com você, mas a Anna tem razão"
    lucas "A gente juntos, só causa problemas"
    "Ele vira de costas e vai embora..."

    menu:
        "Tentar chamar ele":
            jump c2_lucas
        "Deixar ele ir":
            jump primeiro_menu
    
    label c2_lucas:
    y "Lucas, espera..."
    "Você tenta puxar ele pelo braço"
    y "Eu só queria reencontrar todo mundo, nós éramos tão amigos, tão próximos"
    y "Eu queria ter isso de novo..."
    lucas "Eu..."
    "Lucas tenta falar, mas você vê ao longe uma mulher encarando vocês dois"
    lucas "Só é melhor a gente ficar longe"
    "Ele vai embora"
    jump primeiro_menu

    label c1_anna:
    y "Oi Anna"
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
    "Ela vai embora"
    jump primeiro_menu

    label c1_miguel:
    y "Oi Miguel"
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
        miguel "Compreensível..."
        miguel "Eu acho que faria a mesma coisa se tivesse saído daqui"
        y "E você, o que faz da vida?"
        miguel "Bom, eu sou chaveiro, não é nada tão interessante quanto o que você faz, mas paga as contas"
        miguel "Depois que meus pais morreram eu a casa deles ficou pra mim, e as dividas também"
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
    
    jump primeiro_menu

    label c1_pedro:
    y "Oi Pedro"
    pedro "[yn]! Nooossa"
    "Pedro vem te abraçar, quando ele chega perto você sente o cheiro de cigarro e bebida"
    pedro "Que bom que eu te convidei pra festa"
    pedro "Eu te convidei pra festa né?"
    menu:
        "Sim":
            $pedro_pontos = 2

        "Não, vim com a Alice":
            $pedro_pontos = 1

        "Você está bebendo muito":
            $pedro_pontos = 0
    
    if pedro_pontos ==1:
        "Não, vim com a Alice"
        $ renpy.notify("+1 ponto")
        pedro "Alice veio também??? Que legaaal"
        y "Sim, ela está por aí"
        
    if pedro_pontos == 2:
        y "Sim"
        $ renpy.notify("+2 pontos")
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
        y "Desculpa... Eu não sabia"
        pedro "Tá tudo bem"
        pedro "Mas fico feliz que pelo menos um de nós está fazendo o que queria"
        pedro "Você veio com a Alice né? Vou procurar ela então"
        pedro "Muito bom ver você"
        "Ele sai cambaleando"
        jump primeiro_menu
    if pedro_pontos == 0:
        y "Você está bebendo demais"
        $ renpy.notify("-1 pontos")
        pedro "Calma [yn], é uma festa"
        pedro "Mas acho que pra você é fácil julgar o que fazemos aqui"
        pedro "Você deixou tudo pra trás, mas nem todo mundo pode fazer isso"
        "Ele vai embora"
        jump primeiro_menu


    label choice_scene:
    "Você falou com todo mundo"
    "Você se encontra novamente com Alice e Pedro"
    "Eles estão conversando e se divertindo"
    "A noite vai passando, você bebe um pouco"
    "cerca de 1 da manhã, poucas pessoas continuam na festa"
    "Vocês escutam um barulho vindo da garagem"
    pedro "Que bosta, alguem deve ter quebrado a porta saindo com o carro"
    pedro "Vem em ajudar a ver o que é"
    "Você, Alice, Pedro e Anna vão até a garagem"
    anna "Tem alguma coisa embaixo da porta, ela não consegue fechar"
    "A garage está escura, ninguem consegue identificar o que é"
    "Vocês chegam mais perto"
    "É uma mochila"
    pedro "ok, quem deixou a mochila no meio da porta da garagem?"
    anna "Pera. Essa mochila é do Lucas"
    pedro "Ele já foi embora? E deixou a mochila aqui? Que merda"
    anna "Não, ele não foi, ele veio comigo, está sem carro"
    alice "Estranho, e onde ele está?"
    anna "Ele tinha ido no banheiro... Mas pensando bem já tem bastante tempo"
    pedro "Será que ele foi embora com outra pessoa?"
    anna "Você é idiota? Claro que não!"
    
    menu:
        "Ele pode ter ido com outra pessoa sem te avisar":
            $anna_pontos = 0
        "Ele deve estar por aqui, fiquem tranquilos":
            $anna_pontos = 1
    
    if anna_pontos == 0:
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
    
    if anna_pontos == 1:
        y "Ele deve estar por aqui, fiquem tranquilos"
        $renpy.notify("+1 pontos")
        anna "Exatamente, obrigada [yn]"
        alice "Bom, vamos procurar ele então"

    "Vocês olham um pouco pela garagem"
    "Até que..."
    pedro "LUCAS!"
    "Vocês encontram Lucas dormindo encostado na parede"
    anna "Meu deus, você me assustou!"
    "Ele não responde"

    "Você tenta acordá-lo encostando em seu ombro"
    y "Lucas... Acorda..."
    "Você encosta a mão em seu ombro"
    "Está rígido e frio"
    alice "Alguém acende a luz por favor?"
    "Pedro acende a luz da garagem"
    anna "LUCAS!"
    "Quando a luz acende vocês veem, que tem uma faca na barriga de Lucas"
    "Você dá um pulo para trás e o corpo cai, revelando uma grande macha de sangue na parede atrás do corpo"
    alice "O QUE ESTÁ ACONTECENDO?"
    pedro "Alguem liga pra ambulância, polícia, sei lá"
    anna "MEU DEUS O QUE ACONTECEU!"
    "Alice tenta confortar Anna"
    anna "Eu vou ligar pra polícia!"
    "Anna sai da garagem acompanhada por Pedro"
    "Você e Alice permanecem na garagem observando o corpo"
    "Vocês chegam perto e na ponta da faca tem uma mensagem"
    "Ele mereceu, e vocês todos também"
    "Alice olha pra você e rapidamente tira a mensagem da faca e a guarda no bolso"
    "alguns minutos depois você escuta a sirene"
    "a policia vem e leva o corpo"
    "Eles fazem algumas perguntas para você e Alice"
    policial "Entâo... Vocês viram mais alguma coisa que pode ajudar no caso?"
    alice "Não... Mais nada..."




    # This ends the game.

    return
