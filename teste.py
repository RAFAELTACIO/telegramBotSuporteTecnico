import telebot

CHAVE_API = "CONSIGA A CHAVE API FALANDO COM O BOTFATHER NO TELEGRAM"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
QUAL DAS OPÇÕES MAIS SE ADEQUA AO SEU PROBLEMA?
Digite o número ou clique na opção desejada:

/internet ESTOU TENDO PROBLEMAS COM A INTERNET

/impressora ESTOU TENDO PROBLEMAS COM A IMPRESSORA

/computador MEU COMPUTADOR NÃO ESTÁ LIGANDO

/pastas NÃO TENHO ACESSO AS PASTAS QUE PRECISO

/hardware MEU MOUSE PAROU DE PEGAR

/pclento MEU COMPUTADOR ESTÁ LENTO """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
PARA ENTRAR EM CONTATO COM UM PROFISSONAL DE T.I.:

MANDE UM EMAIL PARA: PROFISSIONALDETI@TIAGORA.COM.BR
LIGUE (16) 0404-6886 - RAFAEL OU EMERSON
MANDE UMA MENSAGEM VIA WHATSAPP: 16988707270
    """
    bot.send_message(mensagem.chat.id,texto)
    
@bot.message_handler(commands=["internet"])
def internet(mensagem):
    texto = """
/roteador Desligue e ligue seu roteador
/dispositivos Teste vários dispositivos
/problemaswifi Solucione problemas de Wi-Fi
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["roteador"])
def roteador(mensagem):
    texto = """
É um clichê de solução de problemas de TI, mas é porque geralmente funciona. 
Desligar e ligar o roteador (ou modem ou qualquer outro dispositivo que traga a internet para sua casa) 
deve eliminar falhas e bugs temporários da conexão, forçando o dispositivo a se reconectar do zero.

A maioria dos roteadores possui um botão de reset para esse fim específico, mas você também pode sempre tirar o aparelho da tomada.
Aguarde cerca de 30 segundos antes de reiniciar o dispositivo e aguarde alguns minutos para voltar a funcionar. Resolveu? Bom, você pode parar de ler aqui.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/dispositivos Teste vários dispositivos
/problemaswifi Solucione problemas de Wi-Fi

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["dispositivos"])
def dispositivos(mensagem):
    texto = """
Se a reinicialização do roteador não funcionar, 
a próxima etapa é determinar se o problema está dentro ou fora de sua casa.
Uma maneira rápida de fazer isso é verificar se seu smartphone, tablet ou qualquer outro computador consegue se conectar.
Se possível, conecte um laptop diretamente ao roteador usando um cabo de rede Ethernet.

Se nenhum dos seus dispositivos puder ficar online,
pode haver um problema no seu provedor. Confira o site oficial e o 
feed do Twitter para ver se há algum problema atualmente relatado (usando o 4G, é claro) 
ou ligue para eles para saber se eles têm alguma previsão de quando a situação será resolvida.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/roteador Desligue e ligue seu roteador
/problemaswifi Solucione problemas de Wi-Fi

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["problemaswifi"])
def problemaswifi(mensagem):
    texto = """
Nem todo mundo tem um laptop e um cabo Ethernet em casa, mas se você tiver, você pode conectar o laptop diretamente ao roteador para verificar se o problema está na sua internet como um todo (veja acima) ou no Wi-Fi em particular. Existem várias formas de melhorar o Wi-Fi em sua casa, mas geralmente elas não têm nada a ver com uma queda repentina e inexplicável.

Se o seu Wi-Fi estava funcionando, mas não está mais (e o problema persiste em vários dispositivos), é difícil identificar o problema. Você deve verificar as configurações do seu roteador em busca de pistas, reverter quaisquer modificações recentes na rede e ter certeza de que ninguém na casa alterou a senha da rede.

Se as conexões de internet com fio estiverem funcionando, mas as de Wi-Fi não estiverem em nenhum dispositivo, é um mistério — a menos que seu roteador tenha quebrado ou dado defeito. Se você decidiu colocar um dispositivo sem fio, como uma babá eletrônica, ou um micro-ondas ao lado do seu roteador, essa pode ser uma causa potencial — você realmente precisa colocar dispositivos como esses o mais afastados possível para evitar interferência no sinal.

O uso intenso da largura de banda por um dispositivo específico pode diminuir a velocidade da conexão com a internet, mas você provavelmente também verá isso em uma conexão com fio. O uso de um site ou aplicativo de teste de velocidade pode fornecer mais algumas dicas sobre o que está fazendo com que o Wi-Fi fique lento ou caia completamente.
    
SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/roteador Desligue e ligue seu roteador
/dispositivos Teste vários dispositivos

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["impressora"])
def impressora(mensagem):
    texto = """
/papel O papel engasgou e travou a impressora
/filaimpressao  A Fila de Impressão Parou ou Não Responde
/manchasdetinta Vazamentos de tinta ou manchas indevidas de impressão
/energia A energia elétrica acabou no meio de uma impressão
/papelfotografico Problemas com impressão no papel fotográfico
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["papel"])
def naoliga(mensagem):
    texto = """
Isto é um problema comum e ocorre quando algo obstrui a passagem do papel ou a impressora tem dificuldades de mover a folha para realizar a impressão.

Quando isto acontece, o equipamento pode devolver uma folha toda amassada com erros de impressão ou até mesmo travar todo o processo.

Caso isto aconteça, o primeiro passo é desligar a impressora para evitar posteriores desgastes.

Abra o compartimento onde o papel é disponibilizado ou, dependendo do equipamento, acesse a bandeja de papel. Tente verificar onde o papel travou, desde a entrada da folha até onde o papel é impresso. Libere as travas se existirem.

Tire com cuidado o papel agarrado e possíveis fragmentos que estejam impedindo este de correr livremente. Tenha cuidado para não danificar motores ou engrenagens. Opte pelo sentido natural de impressão para fazer a retirada do papel, caso seja possível.

Após retirar todo o material preso, reinicie a impressora com papel novo, liso e seco. Evite inserir papeis com dobras ou irregularidades que impeçam o equipamento de efetuar o procedimento corretamente.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/filaimpressao  A Fila de Impressão Parou ou Não Responde
/manchasdetinta Vazamentos de tinta ou manchas indevidas de impressão
/energia A energia elétrica acabou no meio de uma impressão
/papelfotografico Problemas com impressão no papel fotográfico

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora

"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["filaimpressao"])
def filaimpressao(mensagem):
    texto = """
Por mais moderno que seja a sua impressora, ela ainda tem uma limitação básica que é atender somente um projeto de cada vez.

Desta forma, a fila de impressão tem como objetivo organizar os trabalhos que foram enviados para o sistema, afim de priorizar as tarefas que são enviadas de forma linear para o equipamento.

A fila de impressão pode travar se há um projeto que ocupou toda a memória disponível do equipamento, se por ventura um dos projetos contém algum erro ou até mesmo por falta de papel.

Para resolver este problema em uma impressora dedicada, acesso o painel de controle da impressora (utilitário de impressão) no sistema operacional.

Cancele todas as operações ou identifique aquele projeto que contém erro. Pode ser necessário, em alguns casos, reiniciar a máquina.

Em casos em que a impressora é compartilhada por vários computadores, o mais indicado é chamar um assistente responsável para realizar o devido procedimento.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/papel O papel engasgou e travou a impressora
/manchasdetinta Vazamentos de tinta ou manchas indevidas de impressão
/energia A energia elétrica acabou no meio de uma impressão
/papelfotografico Problemas com impressão no papel fotográfico

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora

"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["manchasdetinta"])
def manchasdetinta(mensagem):
    texto = """
Ao identificar algum vazamento de tinta ou mancha de impressão, primeiro desligue o aparelho.

Seque o local com um pano seco ou papel absorventes. Pode ser utilizado um produto de limpeza comum para fazer a limpeza. Tenha cuidado para não inalar o produto. Evite utilizar aspiradores de pó.

Para limpar sujeira de tinta dentro da impressora, tome cuidado. Veja se realmente é necessário fazer esta limpeza.

Desligue o aparelho e utilize pano ou papel seco para fazer a limpeza. Não se esqueça de remover o cartucho ou toner para realizar o procedimento.

Após a limpeza ser realizada, ligue novamente o aparelho e realize o procedimento de limpeza padrão do cabeçote do cartucho ou do toner. Na maioria das impressoras, este procedimento já é feito ao ligar o equipamento.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/papel O papel engasgou e travou a impressora
/filaimpressao  A Fila de Impressão Parou ou Não Responde
/energia A energia elétrica acabou no meio de uma impressão
/papelfotografico Problemas com impressão no papel fotográfico

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["energia"])
def energia(mensagem):
    texto = """
Não é algo para se preocupar. Pode ser resolvido de forma semelhante ao procedimento com o papel engasgado. Ou então siga os passos abaixo:

Desligue a impressora, mesmo sem energia.

Após o retorno da energia, ligue novamente o aparelho e note se ele por si só irá soltar o papel. Caso não aconteça, em algumas impressoras você pode realizar o comando manualmente em algum botão, consulte o manual.

Se ainda sim o papel não for removido, tente o procedimento indicado para o papel engasgado indicado acima.

Em alguns casos é necessário ler o manual de instruções. A sigla “RTFM” significa: “por favor usuário, leia o manual de instruções”.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/papel O papel engasgou e travou a impressora
/filaimpressao  A Fila de Impressão Parou ou Não Responde
/manchasdetinta Vazamentos de tinta ou manchas indevidas de impressão
/papelfotografico Problemas com impressão no papel fotográfico

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["papelfotografico"])
def papelfotografico(mensagem):
    texto = """
O papel fotográfico possui um lado específico para impressão que absorve corretamente a tinta. Portanto, antes de realizar a impressão, certifique-se de que o lado do papel está correto. Observe ser a tinta não está sendo absorvida corretamente e interrompa o processo, caso não esteja.

Se tiver impresso no lado errado, verifique a posição correta do papel para que a tinta seja impressa corretamente e reinicie a operação.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/papel O papel engasgou e travou a impressora
/filaimpressao  A Fila de Impressão Parou ou Não Responde
/manchasdetinta Vazamentos de tinta ou manchas indevidas de impressão
/energia A energia elétrica acabou no meio de uma impressão

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["computador"])
def computador(mensagem):
    texto = """
/sinal Confira se dá qualquer sinal de vida
/verifique Verifique se ele tem energia
/conectores Dê uma olhada nos conectores de imagem
/tenteligar Tente ligá-lo em outro lugar
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["sinal"])
def sinal(mensagem):
    texto = """
A primeira etapa é verificar se o computador nem mesmo liga, ou se liga mas não mostra imagem.
Para isso, é necessário ficar de olho para qualquer sinal que ele dê.
Por exemplo, verifique se alguma luz se acende quando você liga ele, ou coloque o ouvido próximo para verificar se ele faz barulho.
Se esse for o caso, pode ser um problema do monitor, dos cabos ou da saída de vídeo.
Senão, o mais provável é que se trate de uma questão relacionada a energia.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/verifique Verifique se ele tem energia
/conectores Dê uma olhada nos conectores de imagem
/tenteligar Tente ligá-lo em outro lugar

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["verifique"])
def verifique(mensagem):
    texto = """
Pode parecer uma dica besta, mas confira se o computador está de fato ligado na tomada.
Se for um notebook, experimente plugá-lo para garantir que o problema não seja falta de bateria mesmo.
Se o seu computador tiver uma fonte (aquele “tijolinho” que faz parte do cabo), confira se ela está bem conectada, e faça o mesmo com a do seu notebook.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/sinal Confira se dá qualquer sinal de vida
/conectores Dê uma olhada nos conectores de imagem
/tenteligar Tente ligá-lo em outro lugar

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["conectores"])
def conectores(mensagem):
    texto = """
Se o computador recebe energia mas não mostra nada, pode ser também um mau contato dos cabos que levam informação até o monitor.
Encontre o conector de imagem do monitor e reforce a conexão dele nas duas pontas.
Se for um notebook, experimente ir abrindo lentamente a tela e veja se ele de repente não se acende em algum ângulo.
Tente também conectá-lo via cabo HDMI ou semelhante a outro display, para ver se o problema não está na tela.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/sinal Confira se dá qualquer sinal de vida
/verifique Verifique se ele tem energia
/tenteligar Tente ligá-lo em outro lugar

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["tenteligar"])
def tenteligar(mensagem):
    texto = """
Se ele não estiver nem mesmo recebendo energia e o problema não é da bateria ou dos cabos, pode ainda ser da sua tomada.
Tente ligar outro aparelho naquela tomada para ver se ele funciona, e tente também ligar o computador em outra tomada.
Se estiver usando uma régua ou algo do tipo, tente removê-la e ligar o PC direto na tomada para ver o que acontece.
No caso de um notebook, pode ser ainda um problema da bateria específica que você está usando.
Se possível, tente trocá-la para ver se ele liga.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/sinal Confira se dá qualquer sinal de vida
/verifique Verifique se ele tem energia
/conectores Dê uma olhada nos conectores de imagem

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pastas"])
def pastas(mensagem):
    texto = """
ESSE É UM PROBLEMA DE ACESSO A PASTAS RESTRITAS, QUE SÓ PODE SER RESOLVIDO TENDO A SENHA DO ADMINISTRADOR, ENTRE EM CONTATO COM O ADMINISTRADOR,
OU ENTRE EM CONTATO CONTATO COM UM PROFISSONAL DE T.I,

PARA ENTRAR EM CONTATO COM UM PROFISSONAL DE T.I.:

MANDE UM EMAIL PARA: PROFISSIONALDETI@TIAGORA.COM.BR
LIGUE (16) 0404-6886 - RAFAEL OU EMERSON
MANDE UMA MENSAGEM VIA WHATSAPP: 16988707270
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["hardware"])
def hardware(mensagem):
    texto = """
    
/maucontato  Veja se é mau contato
/verifycabos Verifique os cabos
/pilhas Troque a pilha (ou o receptor)
/mousepad Use um mousepad
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["maucontato"])
def maucontato(mensagem):
    texto = """
Muitos mouses podem apresentar problemas de mau contato, principalmente os paralelos.
Ao usar o computador e notar que o mouse para de repente, ou simplesmente não se move, verificar se ele está bem conectado na porta USB é uma das primeiras coisas a se fazer.
Caso ele esteja bem conectado e mesmo assim o problema não for resolvido, desligue o computador, troque o mouse para outra entrada USB e ligue a máquina novamente.
Assim, o sistema operacional pode reconhecer o mouse.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/verifycabos Verifique os cabos
/pilhas Troque a pilha (ou o receptor)
/mousepad Use um mousepad

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["verifycabos"])
def verifycabos(mensagem):
    texto = """
Se o seu mouse for com fio, provavelmente ele deve estar embolado na bagunça de fios que um computador pode ter. Com certa frequência, o cabo fica preso e a gente tem que dar aquele "puxãozinho" para dar uma folga ao mouse.
Só que esses pequenos puxões danificam os fios que estão dentro do cabo que, por sua vez, são muito finos, fazendo com que eles se rompam e isso prejudique o funcionamento do mouse, podendo até inutilizá-lo. Deixar o fio do mouse sempre livre é uma ótima opção, evita danos ao cabo e prolonga a vida útil do mouse.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/maucontato  Veja se é mau contato
/pilhas Troque a pilha (ou o receptor)
/mousepad Use um mousepad

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pilhas"])
def pilhas(mensagem):
    texto = """
Com a evolução da tecnologia wireless, alguns mouses ganharam um ótimo upgrade e passaram a ser sem fios.
Isso facilitou muito a vida de quem já estava cansado dos fios e precisava de mais liberdade para trabalhar ou jogar.
Só que, para funcionar, os mouses precisam de baterias, que podem ser uma ou duas pilhas.
Com o uso, as pilhas vão perdendo força e o mouse também perde desempenho.
Caso seu mouse esteja travado ou dando saltos na tela, verifique se a pilha está carregada.
Alguns deles possuem indicadores luminosos para alertar que a bateria está fraca. Caso a bateria esteja carregada, verifique se o receptor está corretamente ligado na porta USB. 
Trocar o plug de porta também é uma opção caso não resolva o problema.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/maucontato  Veja se é mau contato
/verifycabos Verifique os cabos
/mousepad Use um mousepad

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagorav
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["mousepad"])
def mousepad(mensagem):
    texto = """
Pode não parecer, mas o mousepad tem função importantíssima na performance do seu mouse. Para quem faz trabalhos que exijam precisão, um bom mousepad faz toda a diferença na hora de executar a ação.
Cada mouse tem uma quantidade de DPIs (dots per inch) ou pontos por polegadas.
Se um mouse tem 1000 DPIs, isso significa que ele lerá 1000 pontos por polegada.
Se você não usa mousepad, pode estar perdendo toda a precisão que seu produto tem a oferecer.
A dica é usar mousepads escuros, pois eles não refletem a luz óptica, assim, evitará pequenos travamentos ou imprecisões durante suas atividades.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/maucontato  Veja se é mau contato
/verifycabos Verifique os cabos
/pilhas Troque a pilha (ou o receptor)

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pclento"])
def pclento(mensagem):
    texto = """
/programaspesados Encontrar os programas sugadores de recursos
/desativar Desativar programas que iniciam com o Windows
/navegador Verificar Malware e Adware
/espaço Liberar espaço em disco
/programasnaousados Desinstalar programas que você não usa
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["programaspesados"])
def programaspesados(mensagem):
    texto = """
Seu PC está lento porque algo está usando seus recursos.

Se, de repente, a execução for mais lenta, um processo de fuga pode estar usando 99% dos recursos da CPU, por exemplo.

Ou, um aplicativo pode estar sofrendo um erro de memória e usando uma grande quantidade dela, fazendo com que o seu PC troque para o disco. Como alternativa, um aplicativo pode estar usando muito o disco, fazendo com que outros aplicativos diminuam a velocidade quando precisam carregar dados ou salvá-los.

Para descobrir, abra o Gerenciador de Tarefas. Você pode clicar com o botão direito do mouse na sua barra de tarefas e selecionar a opção “Gerenciador de Tarefas” ou pressione Ctrl + Shift + Esc para abri-lo.

No Windows 8, 8.1 e 10, o novo Gerenciador de Tarefas fornece uma interface atualizada que informa com uso de cores os aplicativos que estão usando muitos recursos.

Clique nos cabeçalhos “CPU”, “Memória” e “Disco” para classificar a lista pelos aplicativos que usam a maioria dos recursos.

Se algum aplicativo estiver usando muitos recursos, convém fechá-lo normalmente. Se não for possível, selecione-o aqui e clique em “Finalizar tarefa” para forçar o fechamento.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/desativar Desativar programas que iniciam com o Windows
/navegador Verificar Malware e Adware
/espaço Liberar espaço em disco
/programasnaousados Desinstalar programas que você não usa

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["desativar"])
def desativar(mensagem):
    texto = """
Após você identificar na dica anterior, os aplicativos que você normalmente não precisa usar assim que o Windows inicia, você pode desativar sua inicialização automática de uma vez por todas.

Isso evita que esses aplicativos sejam iniciados junto com o Windows economizando memória e uso de CPU, além de acelerar o processo de inicialização.

No Windows 8, 8.1 e 10, há um gerenciador de inicialização no Gerenciador de Tarefas que você pode usar para gerenciar seus programas de inicialização.

Clique com o botão direito do mouse na barra de tarefas e selecione “Gerenciador de Tarefas” ou pressione Ctrl + Shift + Esc para iniciá-lo.

Clique na guia Inicializar e desative os aplicativos de inicialização que você não precisa.

O Windows lhe informará quais aplicativos atrasam mais o processo de inicialização. Esse é um dos principais passos de o que fazer quando o computador está muito lento.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/programaspesados Encontrar os programas sugadores de recursos
/navegador Verificar Malware e Adware
/espaço Liberar espaço em disco
/programasnaousados Desinstalar programas que você não usa

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["navegador"])
def navegador(mensagem):
    texto = """
Também há a chance do seu computador ficar lento porque um software mal-intencionado está diminuindo a velocidade e sendo executado em segundo plano.

Um software que interfere na sua navegação na Web para rastreá-lo e adicionar anúncios adicionais, por exemplo.

Para ficar mais seguro, verifique sempre seu computador com um programa de antivírus atualizado.

Você também deve verificar com algum programa específico contra malware, que captura com mais precisão que a maioria dos programas de antivírus que tendem a ignorar algumas ameaças.

Esses programas tentam infiltrar-se no seu computador quando você instala outro software e sem perceber acaba instalando eles juntamente.

Execute uma varredura usando o AntiVirus no seu computador.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/programaspesados Encontrar os programas sugadores de recursos
/desativar Desativar programas que iniciam com o Windows
/espaço Liberar espaço em disco
/programasnaousados Desinstalar programas que você não usa

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["espaço"])
def espaço(mensagem):
    texto = """
Se o seu disco rígido estiver quase cheio, o seu computador ficará visivelmente mais lento.

Você precisa deixar algum espaço para seu computador trabalhar.

Para isso você não precisa de nenhum software de terceiros. Basta executar a ferramenta Limpeza de Disco incluída no Windows. Isso já pode ajudar bastante.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/programaspesados Encontrar os programas sugadores de recursos
/desativar Desativar programas que iniciam com o Windows
/navegador Verificar Malware e Adware
/programasnaousados Desinstalar programas que você não usa

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["programasnaousados"])
def programasnaousados(mensagem):
    texto = """
Se o seu disco rígido estiver quase cheio, o seu computador ficará visivelmente mais lento.

Você precisa deixar algum espaço para seu computador trabalhar.

Para isso você não precisa de nenhum software de terceiros. Basta executar a ferramenta Limpeza de Disco incluída no Windows. Isso já pode ajudar bastante.

SEU PROBLEMA FOI RESOLVIDO? SE NÃO, QUE TAL TENTAR MAIS UMA DAS OUTRAS OPÇÕES:

/programaspesados Encontrar os programas sugadores de recursos
/desativar Desativar programas que iniciam com o Windows
/navegador Verificar Malware e Adware
/espaço Liberar espaço em disco

SE O SEU PROBLEMA NÃO FOI RESOLVIDO, ENTRE EM CONTATO COM A NOSSA EMPRESA, E TENHA SEU PROBLEMA RESOLVIDO POR UM PROFISSONAL DE T.I
/profissionaldetiagora
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["profissionaldetiagora"])
def profissionaldetiagora(mensagem):
    texto = """
    PARA ENTRAR EM CONTATO COM UM PROFISSONAL DE T.I.:

    MANDE UM EMAIL PARA: PROFISSIONALDETI@TIAGORA.COM.BR
    LIGUE (16) 0404-6886 - RAFAEL OU EMERSON
    MANDE UMA MENSAGEM VIA WHATSAPP: 16988707270
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler()
def responder(mensagem):
    texto = """
Eu sou a 🙋🏻‍♀️ JÚLIA, sua assistente virtual.

Você prefere tentar encontrar a resposta para o seu problema aqui mesmo nesse chat,
ou prefere um com um profissional de TI?
Para iniciar seu atendimento digite o comando ou clique na opção desejada:
/opcao1 TENTAR RESOLVER PELO CHAT
/opcao2 ATENDIMENTO PRESENCIAL
Responder qualquer outra coisa não vai funcionar, clique em uma das opções."""
    bot.reply_to(mensagem, texto)

bot.polling()