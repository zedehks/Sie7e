#Sie7e

#Miembros del grupo:

#Waldo Navas 21441158
#Roberto Hernandez 21441008
#Osman Oliva 21441050




image bg phonescene = "phonescene.jpg"
image bg nortonroom = "nortonroom.jpg"
image bg battle = "battle.jpg"
image bg white = "white.jpg"
image bg black = "black.jpg"
#fotos de uso libre tomadas de wikipedia.

define d = Character('Detective', color="#c8ffc8")
define a = Character('Asistente', color="#fd5f5f")
define b = Character('Beatriz', color="#fd5f5f")
#define v = Character('Víctima', color="#3b3535")
define m = Character('Mapes Norton', color="#3b3535")
define e = Character('Escorpión', color="#3d1e1e")
define s = Character('Sombra', color="#3b3535")

image beatriz happy = "feliz.png"
image beatriz madtalk = "mad talk.png"
image beatriz salty = "molesta.png"
image beatriz phone = "phone.png"
image beatriz phone2 = "phone 2.png"
image beatriz phone3 = "phone 3.png"
image beatriz worrytalk = "preocupada habla.png"
image beatriz preocupada = "preocupada.png"
image beatriz smug = "smug.png"
image beatriz topmad = "top mad.png"
image beatriz shame = "verguenza.png"
image norton calla = "nortoncalla.png"
image norton habla1 = "nortonhabla1.png"
image norton habla2 = "nortonhabla2.png"

# - El juego comienza aquí.
label start:
    #Escena 1
   play music "ghost9.ogg"
   scene black
   with dissolve 
   "Nunca supuse que terminaría así, pero bueno, la vida es así de cruel..."

   "La vida de un detective no es una vida noble."
   "Tampoco es una vida larga."
   "Si no estuviera al final de este túnel, diría que esta situación es ridículamente cliché. Jeh."
   "…Solo me arrepiento que ella nunca supo…"
   "…"
   d"“Que Dios tenga merced con su alma.”"
   
   #Escena 2
   #play music "ghost9"
   scene bg phonescene
   with fade
   show beatriz preocupada
   with dissolve  
   show beatriz worrytalk
   a"”¿…es…?”"
   show beatriz preocupada

   d"”Si, es aquí. Sigamos.”"

   show beatriz preocupada

   "Entramos dentro de aquel lugar destartalado, nuestros ojos abiertos y alertos por cualquier sorpresa. Nunca supuse que un caso tan mundano abriría una caja de Pandora tan siniestra."

   "No debía haber estado ahí. Solo seguí haciendo esto por varias razones, mitad estupidez y mitad una sensación ingenua de idealismo que rápidamente se pudrió y murió."

   "“Es un caso sencillo, tómalo y te podrás retirar con un poco de dignidad. Oh, antes que se me olvide, te asignaré alguien. Tal vez le podrías dar unas cuantas canas tuyas.” ¿Qué diablos estaba pensando?"
   
   "De pronto la pesadez de todo me cayó en los hombros."

   "Quisiera estar en mi casa jugando en mi laptop y comiendo chatarra. Odio el afuera. Odio la gente. Odio el todo."

   "Todo momento que vivo es miserable. Diez años en la fuerza policial, solo para terminar como niñera de novatos."
   #hide beatriz

   "Supongo que me la estaba ganando; solo la juventud perdona la rebeldía. Tal comportamiento se vuelve inexcusable cuando uno crece las canas de sabiduría. Era inevitable que el Jefe me buscaría apaciguar. Le he causado estrés por años; sería su manera de desquitarse." 
   hide beatriz
   with dissolve 
   scene black
   with dissolve
   "En fin, Saturno no perdona a nadie. La arena siempre cae. Constante, finitamente, ominosamente…"


   pause

   scene bg phonescene

  
   show beatriz worrytalk
   with hpunch
   a"“¡Señor!”"


   show beatriz preocupada 

   "Cierto. Tú sigues aquí. Diablos."
   
   d"“Sí, eh…”"
   show beatriz madtalk

   a"“Beatriz.”"
   show beatriz salty

   d"“Cierto, cierto… Beatriz.”"

   "Oye, Saturno, ¿no quisieras abrir un agujero más grande en ese reloj? O por lo menos envíame unos frascos de veneno de rata y te hago el favor de gratis."
   show beatriz madtalk

   b"“Por lo menos podría fingir interés. Tampoco estoy emocionada que me tocó un fósil paleolítico como instructor.”"

   show beatriz salty
   "…"
   show beatriz madtalk

   b"”Increíble. Le vale pi…”"
   show beatriz phone

   "Bajó la voz y prosiguió a distraerse con su teléfono, ocasionalmente mirando a su alrededor con miedo parcialmente oculto."

   "Estamos en una situación riesgosa e igual decide usar su maldito teléfono. Brillante. “Strike one” para la novata. Por lo menos es un Nokia. Se lo avienta a alguien, capaz le raja el cráneo. Aún así, preferiría no tomar el riesgo. Le debería decir que lo guarde."

   "Sutileza es la clave…"
   
   menu:
      "“Ey, guarda esa cosa… estamos en patrulla.”":
          #Respuesta amable:
          
          d"”Beatriz, por favor, guarda esa cosa. Dos pares de ojos protegen más que uno.”"
          show beatriz shame

          "Con vergüenza visible en la cara, inmediatamente guardó el bloque de plomo en sus manos."
          show beatriz worrytalk

          b"“… Discúlpeme. No me imaginaba que esto iba a ser tan… estresante.”"
          show beatriz preocupada

          "Entonces hubieras escogido otra carrera, cariño."

          d"“No te estreses; la vida va cuesta arriba. Solo acéptalo y verás como se vuelve más fácil de masticar.”"
          show beatriz madtalk

          b"“¿Eso se supone que me motivaría?”"
          show beatriz salty

          d"“Es lo mejor que obtendrás de mi. Tómalo o déjalo, cipota.”"
          show beatriz happy
          with Dissolve(.5)
          show beatriz salty
          with Dissolve(.5)

          "¿Fue eso que vi una sonrisa?" 

          "Digamos que sí y sigamos. Jeh."
          $ sheHappy = True
          $ sheBTFO = False

          
      "“Novata. Teléfono. Apágalo. Ya.”":
          #Respuesta “Neutra” (estricta):
          
          d"“Novata; teléfono; apágalo; Ya.”"
          

          "..."

          "Dios deme fuerza."
          show beatriz phone2

          "...."#pout

          d"“Apaga esa cosa. Te estoy hablando, cipota.”"
          show beatriz phone3

          "....."#top pout

          d"“¡Beatriz!”"
          show beatriz worrytalk
          with vpunch

          "El ladrillo de plomo subió por el aire, giró más radicalmente que Tony Hawk  y cayó majestuosamente al suelo como un zepelín de plomo, rajando la cerámica alrededor de sí. Okey, las leyes de la guerra deberían tener una prohibición sobre esto. Balas expansivas y armas químicas ni se acercan a esta capacidad destructiva."

          show beatriz preocupada
          "Tras los cinco segundos de silencio más ruidosos de mi vida, Beatriz se acercó y cautelosamente recogió el teléfono. Naturalmente, estaba intacto, pero lo mismo no podría decirse del piso. Oy vey." 

          
          "Sin decir ni una palabra, guardó el teléfono y siguió caminando."
          $ sheHappy = False
          $ sheBTFO = False

          
      "Agarra el teléfono de sus manos.":   
          #Respuesta  de Cerote:
          
          "Bueno, mi vida antes que su entretenimiento. Solo la tendré que aguantar hasta el final del caso."

          "Con Dios a mi lado, agarré el teléfono y lo metí en mi bolsillo."
          show beatriz worrytalk
          
          d"“Lo tendrás de vuelta después de salir de aquí, novata.”"
          show beatriz topmad

          "Fuego surgió de sus ojos mientras su cara de indignación rápidamente se volvió en una de ira y odio. Oy gevalt, quizás no fue una idea brillante. Sentí una sensación frígida por mi espalda."
 
          "Cielos, sí esta furiosa. Tranquilízate, ¿sí?" 
          

          "¿No? No. La…"

          d"“… que me parió.”"
          show beatriz salty

          "…"

          d"“¿Vas a estar bien?”"

          "Me ignoró y solo siguió adelante. He visto este escenario en muchas de mis caricaturas chinas y usualmente termina el protagonista destripado, literalmente. Aquella sensación fría corrió por mi espalda nuevamente."

          "Mis instintos animales de supervivencia despiertos, hurgué mi chaqueta y sentí mi arma. El acero frio irónicamente me tranquilizó. Me siento cómodo solamente con mis únicos dos amigos: Smith y Wesson."
          $ sheHappy = False
          $ sheBTFO = True

   #Escena 3:
   scene bg nortonroom
   with fade

   show beatriz preocupada
   with dissolve
   #with dissolve
   "Uno siempre mira en las películas y videojuegos sitios como estos. Dado, usualmente son ubicaciones industriales abandonadas, pero esta sigue respirando y viviendo, como lo demuestran todas las botellas de cola en el piso." 
   "…"
   "Ojalá eso sea un chicle pegado a la pared." 
   show beatriz worrytalk
   b"“¿Dónde se supone que esta?”"
   show beatriz preocupada
   d"“Buena pregunta. Los gemidos que oyeron los albañiles ya no sonaban cuando yo llegué. Yo mantendría los ojos abiertos y la pistolera cerca.”"

   d"“Aquí. Subamos al sexto piso.”"
   show beatriz madtalk
   b"“Maldita sea; ¿cuántos pisos más son?”"
   show beatriz salty

   "Tantos como sean necesarios para matarme de una caída."

   d"“No sabría decirte. Solo aguanta. Para esto nos entrenan.”"
   show beatriz madtalk

   b"“Sin ofender, su entrenamiento con arcabuces y estoques no nos sirve mucho hoy en día.”"
   show beatriz salty

   d"Por lo menos sabe su historia. Alternativamente, podría ojear el diccionario como pasatiempo. Siempre existen raros que hacen eso." 

   d"“Mosquetes y sables, gracias. Hay una diferencia de cientos de años.”"

   show beatriz smug
   b"“Ah, ¿como la diferencia de edad entre usted y yo?”"

   "Nanosegundos antes que el insulto llegara a mi amígdala cerebral, nos encontramos con una sombra extraña al otro lado del cuarto, en una esquina iluminada solamente por el brillo de una linterna."

   show beatriz preocupada at left
   with move
   s"“¿…llegué a esto? No habría manera de saberlo, la vida como la conocemos es muy volátil, solo miren a Kennedy como él estalló aunque fue otro tipo quien encendió la mecha pero aun así no crea que la sopa sea necesaria en el espacio porque Dios es eterno aunque Dios no es comida no creo eso seria raro pero aun así ¿será Dios comida para ángeles en el cielo o es Dios quien se come a los ángeles? La vida es rara. ¿Cómo llegué a esto? No habría manera…”"

   d"“…Ahora estamos llegando a algo.”"
   show norton calla at right

   "A veces extraño ser un novato. Todo el mundo es un misterio por resolver, sin mencionar todas las emociones y experiencias que uno conoce; experiencias cómo escuchar a una persona perder la mente." 

   "Tan pragmático como suene, ya no había mucha sorpresa en un pobre tío como éste. Contando toda la gente que he visto así, ocuparía más manos."

   "Me pregunto si terminaré un día como él. ¿Será posible que mis múltiples experiencias con esto me prevenga de perder la mente así?"

   show beatriz worrytalk

   b"“Aquí está su cédula. Es Norton.”"
   show beatriz preocupada

   d"“Lotería. Es nuestro tipo. Revisa sus heridas.”"

   b"“…”"
   show beatriz worrytalk

   b"“Está intacto. Bueno, físicamente.”"
   show beatriz preocupada

   d"“Esto es nuevo. Nuestro otro amigo usualmente no dejaría a alguien intacto.”"
   show beatriz worrytalk

   b"“¿Lo conoce?”"
   show beatriz preocupada

   d"“Sería difícil hallar un veterano en la fuerza que no haya oído del Escorpión. Ese desgraciado nos ha dado angustia por seis años.”"

   d"“Solo digamos que los resultados usuales de una visita del Escorpión no ocupan paramédicos para limpiar; más de un par de trapeadores es necesario.”"

   "Okey novata, estos son los momentos donde debes fortalecer tu alma. Conviértete en hierro. Te ayudará a sobrevivir."
   show beatriz worrytalk
   

   b"“Llamaré a los paramédicos.”"
   show beatriz preocupada at left

   d"“Por favor. Veré si puedo ayudar a este tío.”"
   hide beatriz
   with dissolve

   "Con conocimiento pleno que era en vano, me acerque a Norton, dispuesto a probar y ver que podría sacar de él."

   show norton habla1 
   m"“Hombre misterioso, pelo gris y liso, se acerca al mata-virus, se acerca con miedo, el miedo se huele, el miedo te come, el miedo te cambia, el miedo me traga. “"

   show norton calla
   d"“¿Dónde está el miedo? ¿Lo quieres hallar junto a mí?”"

   show norton habla2
   m"“Tú eres el miedo. Tú eres un miedo pero no mi miedo. Mi miedo subió al cielo. No esta a la derecha de ningún padre, pero subió, subió.”"

   show norton calla
   "Miré para arriba. Solo quedaba un piso más por subir."

   d"“¿Cómo llego el miedo?”"

   show norton habla1
   m"“¿No viene de uno mismo? Bueno, quizás el miedo tuyo, mi miedo el miedo en negro el miedo con el fusil el miedo que me come viene de la sombra.”"

   show norton calla
   d"“Beatriz, mientras estas ahí, llama también por refuerzos.”"  

   
   show norton habla2
   m"“Si vas a buscar al miedo de la sombra, cuida de su aguijón, cuida de su veneno, cuida de mi, cuida de mi cuida de mi voz. Es muy tarde. No llegaré a la cena. No me gusta la paella. Callo, callo cayó callo callo cayo calló cayo cayó callo…”"

   hide norton
   with dissolve 
   d"“Mejor de lo que yo esperaba. Beatriz, subamos. Está en el último piso. Pistola desfundada y alerta.”"
   
  #Termina Escena 3
  #Escena 4:

   scene bg battle
   with fade
        
   "Sombras alrededor, el sol hace ratos muerto, la luna hace ratos mira, buscamos a un escorpión con veneno en la cola y sangre en sus manos."
   "Me gusta esta parte. Qué dulce es la vida."
        
   d"”Hagas lo que hagas, no te separes. Él tiene el elemento de la sorpresa. Además, desde ahora, silencio absoluto.”"
   "Difícil de ver en la penumbra, pero su pulgar erguido es suficiente."
   "Un resorte siempre esta más tenso en el momento previo a soltarse. El instante donde la energía potencial se convierte en cinética. Tal como el resorte que empuja el martillo de un arma. El martillo golpea un pin, el pin activa la carga explosiva, empuja un pedazo de plomo a la velocidad del sonido." 
        
   b"”¡Contacto!”"
   d"”¡Suelta el arma!”"
   e"”Eh, ¡es el viejo bigote! ¿Cómo te va? ¡Veamos si esta vez sí te mato!”"

   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)

   #pause(1.3)
        
   "Saltamos y nos cubrimos tras una pared interna. Siempre vuelve a esto, ¿no? No es a prueba de balas, pero nos esconde."
   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)
   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)
   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)
   "Una pelea sin la apariencia de una. Solo tres idiotas lanzando plomo uno a otro en la oscuridad."
   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)
   play sound "gun.ogg"  
   scene bg white
   with Dissolve(0.125)
   scene bg battle
   with Dissolve(0.125)

   "Tengo dos opciones: ataco por la izquierda, o voy por la derecha. Vida o muerte. Tiremos los dados:"

   menu:

            "A la Izquierda":

                jump izquierda

            "A la Derecha":

                jump derecha


   label izquierda:

        "Dicen lo que dicen, ¿no? El camino de la mano izquierda cosecha recompensas oscuras. Dedo en el gatillo, me lancé a la izquierda, y disparé a las sombras de ese lado."
        scene bg white
        play sound "gun.ogg"
        with Dissolve(0.125)
        scene bg battle
        with Dissolve(0.125)
        scene bg battle
        with hpunch
        play sound "gun.ogg"  
        scene bg white
        with Dissolve(0.125)
        scene bg battle
        with Dissolve(0.125)
        "De pronto, sentí la sensación caliente familiar de una bala. En el estrés del combate, la adrenalina trae sus beneficios. Uno no siente dolor hasta ratos después. Si es fatal, tal vez ni siente el dolor."
        "Por suerte, nuestro amigo artrópodo conoció un fin similar. Su grito resonó por las paredes vacías. Colapsó en un baño de su sangre, un fin apropiado para tal carnicero."
        "Sin embargo, un ataque de toz después, mis manos estaban cubiertas de sangre. Mierda."
        
        if sheBTFO:
          jump final3
        else:
          if sheHappy:
            jump final4
          else:
            jump final3


   label derecha:


        play sound "gun.ogg"
        scene bg white
        with Dissolve(0.125)
        scene bg battle
        with Dissolve(0.125)
        scene bg battle
        with hpunch
        "Cincuenta, cincuenta. Realmente es aleatorio. Por eso no me sentí tan mal cuando la bala entró a mi ser. Sin siquiera darme tiempo de reaccionar o contraatacar, estaba en el piso, la mente en blanco. Debes agradecer a la adrenalina; te puede evitar mucho dolor. Solo espero que Saturno llegue por mí primero."

        e "”Vaya, es lo mejor que podré hacer ahorita. Ni modo. Tengo que ir a mi Xbox. ¡Ciao!”"

        "Con esas palabras, salió corriendo, sus pasos resonando en mis oídos. Diablos, odio y dolor no combinan bien, como cerveza y pescado frito, pero en vez es horrible, como pasta dental después de una naranja."
        b "”¡Voy tras él!”"
        "Con  plomo en el abdomen, ni sé si salió ruido de mi boca. En fin, pronto desaparecieron los ecos de sus pasos aligerados."
        "¿No fue lo primero que enseñan que uno “jamás se separa de su compañero? Diablos, ¿qué conchas enseñan ahora en la academia?"
        "El dolor repentinamente me recordó que seguía aquí. También me acordó que tenia una bala de ocho milímetros en el intestino. Qué dulce es la vida."
        if sheBTFO:
          jump final2
        else:
          if sheHappy:
            jump final4
          else:
            jump final1


   label final1: # (B=1)
    
        "Nunca supuse que terminaría así, pero bueno, la vida es así de cruel."
        "La vida de un detective no es una vida noble."
        "Tampoco es una vida larga."
        "Si no estuviera al final de este túnel, diría que esta situación es ridículamente cliché. Jeh."
        "…Solo me arrepiento que ella nunca supo…"
        "…"
        "Sí, ella no volverá. Parece que los insultos por mi edad no eran por molestar. Eran sinceros."

        d "”Que Dios tenga merced con su alma.”"

        "La paz nunca dura. Pasos pesados hacían eco contra las paredes vacías. Él venía."
        "Es irónico, ¿no? El asesino termina siendo mi ángel. Ojalá me mate rápido. Me duele el vientre."
        "Se acerca. Siento su aura del mal. "
        "Qué dulce es la vida."
        scene black
        with fade
        
        return

   label final2: #(B=2)
    
        "Nunca supuse que terminaría así, pero bueno, la vida es así de cruel."
        "La vida de un detective no es una vida noble."
        "Tampoco es una vida larga."
        "Si no estuviera al final de este túnel, diría que esta situación es ridículamente cliché. Jeh."
        "…Solo me arrepiento que ella nunca supo…"
        "…"
        "Sí, ella no volverá. Parece que los insultos por mi edad no eran por molestar. Eran sinceros."
        "Que Dios tenga merced con su alma."
        "Mi última equivocación. Pasos lentos y deliberados hacían eco contra las paredes vacías. Ella venía."
        "Es casi mitológico, ¿no? El aprendiz mata al maestro. Ojalá lo haga rápido. Me duele el vientre."
        "Se acerca. Siento su aura de odio." 
        "Lo lamento tanto."
        scene black
        with fade
        
        return

        
   label final3:
        scene black
        with dissolve
        "Todo se vuelve borroso. Mi visión se oscurece." #Perfectamente seguro que azul y negro. Relámpago en el fondo hace que todo se vuelva blanco y dorado. No, es una ilusión. ¿Este dolor? No lo es."
        "Ella nunca supo. Nunca supo. No, yo rechazo esta realidad. Es un sueño y me voy a levantar."
        "Ya suena la alarma. Ya suena la alarma. Mi reloj se acaba. Saturno debe guardarlo. Hay que madrugar y alistarse. Ya voy, cinco minutos más."
        "De pronto un momento de lucidez. Todo esta negro. Se escucha una voz en el fondo."

        d "”Cállate mocosa; intento dormir.”"

        "Vaya. Que oscuro."
        scene black
        with fade
        
        return
 
   label final4: #(B=0)
    
        "Nunca supuse que terminaría así, pero bueno, la vida es así de cruel."
        "La vida de un detective no es una vida noble."
        "Tampoco es una vida larga."
        "Si no estuviera al final de este túnel, diría que esta situación es ridículamente cliché. Jeh. "
        " …Solo me arrepiento que ella nunca supo…"
        "…"
        " Oí el gran alboroto subiendo por las gradas. Venía la caballería."
        "Debo admitir, aún con mi disposición oculta sociópata, debo admitir: la vida puede no ser mala de vez en cuando."
        "Eso pensé, hasta acordarme que todavía no habría internet en la casa."
        "Qué dulce es la vida."
        scene white
        with fade
        
        return
