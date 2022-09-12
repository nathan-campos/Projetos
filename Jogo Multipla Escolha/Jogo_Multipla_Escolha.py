from subprocess import BELOW_NORMAL_PRIORITY_CLASS


print('Bom te ver por aqui!')
name = input('Qual o seu nickname?')
age = int(input('Quantos anos você tem?'))
#ans = resposta
# if ans=='': ans = input('')  
#colocar Hp do personagem
#fazer o restante da historia seguinte ao rato


print('Muito prazer', name, 'você tem', age, 'anos')
health = 10


if age >= 14:
    print('Você tem idade suficiente para jogar!')
    print('***AS RESPOSTAS DEVEM SER ESCRITAS EXATAMENTE COMO ESTÃO NOS EXEMPLOS***')
    print('>Você começa com 10 pontos de vida<')

    left_right = input('Vou te contar uma história um pouco diferente, cada uma das suas escolhas no meio do caminho vão influênciar no que vai acontecer, e como a vida do seu personagem vai se desenrolar daqui pra frente. Vou te dar um pequeno esboço de como anda a vida desse nosso pequeno personagem. Nosso herói anda com vários problemas em sua vida pessoal, onde pra começar ele está em um serviço meia boca, onde parece que vai morrer trabalhando em um hambiente hostíl e nada interessante. Em casa, ele não tem tempo para fazer muitas coisas desde que sua mãe adoeceu, além de ter que pagar o tratamento absurdamente caro, ela também precisa dos seus cuidados. Em uma das poucas oportunidades de sair com seus amigos, sua turma acaba passando um pouco dos limites e começam a se desafiar de maneiras que não há possibilide de terminar bem. Você é o último a ser desafiado, na sua vez, após todos os desafios terem sido concluídos, te desafiam a tomar o que parecem ser uma nova droga. Nisso um dos seus amigos tem o contato de um fornecedor, chegando até ele, ele apenas te dá duas opções. Sem saber das consequências qual será a sua escolha?\nPrimeira pergunta: Você terá duas opções, escolhe a pílula vermelha ou azul? (v/a)')
    
    if left_right == 'v':
        ans=input('Boa escolha! Nesse momento sua conciência começa a questionar o senso de realidade.Seus amigos te deixam em casa, sua conciência está afetada. Você caiu no sono, ao acordar, se depara com uma sala escura, a luz não está funcionando. Vê que há duas portas, uma à esquerda, outra à direita, qual delas você decide encarar? (esquerda/direita) ')
        
        if ans == 'esquerda':
            ans=input('Você se vê nos fundos da casa, de cara ao sair você já vê que essa casa não é a sua, e ainda é noite, observando o local você não para de encarar uma uma grande árvore,ela parece ser muito antiga de acordo com a largura de seu tronco. Sua curiosidade não o deixa parar de encará-la quer chegar mais perto, ou segue no caminho? (observa/segue) ')
            
        if ans=='observa':
            ans=input('Ao se aproximar, você se depara com uma antiga casa na árvore, logo decide subir e ver o que tem ali. As escadas estão sujas e não parecem seguras, mas você termina de subir. Ao forçar o alçapão, algo repentinamente cai na sua cabeça, te tirando o equilíbrio. Você caiu! perde *2 de HP. Logo após a queda, você vê que a casa tem o que parecem ser pequenas armadilhas para evitar invasores. Após a subida, vê que a casa teve várias coisas tiradas fora do lugar a pouco tempo, e se apressa para sair dali. Seguindo seu caminho, você se depara com uma encruzilhada e bem no meio há uma placa que indica dois caminhos, o primeiro parece te levar  em direção à floresta, ou a segundo, que indica um caminho para uma antiga usina. (floresta/usina)')
            health -= 2
            #perde 2 de HP
           

        if ans=='floresta':
            ans=input('Você tem agora tem *8* pontos de vida.\n Seguindo o caminho da floresta, os sons de pássaros parecem que estão ficando cada vez mais fortes ')     

        if ans=='usina':
            ans=input('Você tem ', health,'de vida.\n ')    


        if ans=='segue':
            ans=input('Você anda alguns metros sem notar, mas parece ter alguem que estava te observando desde que chegou nesse lugar... Seguindo o caminho, você se depara com uma estrada de terra que vai em direção à floresta, ou a segunda, que parece o levar para uma antiga usina. (floresta/usina)')    

        if ans == 'direita':
            ans=input('Ao abrir a a porta você dá de cara com um rato gigantesco que está extremamente furioso! Logo percebe algo em seu bolso, mas o seu instinto o diz para fugir, a decisão precisa ser feita logo! (bolso/correr) ')
        
        if ans == 'bolso':
            ans = input('Rapidamente você coloca a mão em seu bolso e pega o que parece ser uma lanterna. Você logo ascende e vê que nem sempre as coisas são o que parecem. O que parecia ser um rato furioso, é na verdade uma mãe que estava querendo apenas proteger seus filhotes. você os deixa em paz e passa pela saída. Sua mente parece estar pregando peças em você, porque aparentemente não deveria ser possível seu cachorrinho de infância estar logo a sua frente, -"Hanz morreu a mais de 5 anos", disse consigo, mas a emoção foi tanta que deixou a incredulidade de lado e logo foi em lágrimas para o abraçar. Agora você tem o seu companheiro de volta , e estão juntos em uma aventura. Hanz te chama para o seguir por entre os aburtos. Você o seguirá ou o chama para seguir pela estrada ao seu lado? (segue ele/chamar de volta) ')

        if ans=='segue ele':
            ans = input('Mesmo desconfiado com toda a situação ainda assim você segue Hanz. Ele passa primeiro pelos arbustos e late lhe chamando, sem se precipitar, você logo vai atrás... Ao passar pela folhagem, você se depara com um lugar que lhe parece familiar, onde suas memórias lentemante vão retornando, como se de repente sua mente houvesse aberto um baú onde havia toda aquelas lindas lembranças, mas junto, voltaram também tudo aquilo que você não queria mais se lembrar. Nesse breve momento, que em sua cabeça foram anos de lembranças vindo à tona, sua mente se volta para um detalhe: -"esse lugar não é exatamente como eu me lembrava".\n Parece que aquela mesma casa está diferente, os objetos estão organizados de uma maneira estranha, onde eu não me recordava. \n DIGITE "continuar" PARA SEGUIR COM A HISTÓRIA...')

        if ans=='continuar':
            ans = input('')    

        if ans=='chamar de volta':
            ans = input('')          

        if ans== 'correr':
            ans=input('O rato começa a correr atrás de você a toda velocidade, ele morde seu calcanhar, o fazendo perder *2 de HP, sua vida continuará a cair a cada rodada, de 2 em 2 pontos, até que não consiga reverter a infecção. Após a mordida, você vê a saída. Ao sair, se depara com uma rua totalmente deserta, onde caminhando por pouco tempo, logo vê o que parece ser um cachorrinho que está preso em uma cerca, ele emperrou e precisa da sua ajuda para sair. Você o ajuda e logo faz amizade, qual nome você dará ao seu novo amiguinho? (snoopy/doguinho)')
            #Perde vida 2 em 2
            health -= 2

            if ans== 'snoopy':
                ans=input('')

            if ans== 'doguinho':
                ans=input('')      

    #PILULA AZUL
    if left_right=='a':
        ans=input('Sua cabeça começa a doer e você desmaia. Acorda no dia seguinte se sentindo estranho, "Será que foi apenas um sonho?". Segue para o serviço, onde encontra seu chefe perdendo a cabeça por ter acabado de receber uma ligação ruim da esposa. Você decide... Tenta animá-lo, ou o deixa pra lá? (vou/deixo)')  
        
        if ans== 'vou':
            ans=input('Você decide levar um café para o seu chefe, parece ter sido uma boa idéia afinal... ao chegar em seu escritório você entra sem bater, e pega ele no flagra dando amaços com a antiga secretária, ele se desespera e te tranca com os dois, nesse momento você percebe que sua carreira nessa empresa pode estar por um fio... O seu chefe ameaça demiti-lo caso conte o que viu ali para alguém. Passa pela sua cabeça dois planos, no primeiro você o suborna para ele te dar uma promoção "Quanto maiores os riscos, maiores as recompensas". E na segunda você promete nunca falar nada. É um momento muito delicado, escolha sabiamente.(suborno/prometo)')
        
        if ans=='deixo':
            ans=input('Você sobrevive mais um dia no trabalho. No dia seguinte ao Voltar para trabalhar, esquece a carteira e celular na jaqueta, que estão em casa. Volta para pegar ou segue para o serviço? (volto/sigo)')      
if health <= 0:
    print('Sua jornada se encerra por aqui, se gostou do game, pensa na quantidade de opções que ainda falta explorar!!')
    print('Continue essa jornada reiniciando o jogo...')


else: 
    print('Você ainda não tem idade suficiente para este jogo...')