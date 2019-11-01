import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()

numkits = 2
kit = 1

snare_sound = pygame.mixer.Sound('kit1-snare.wav')
tom1_sound = pygame.mixer.Sound('kit1-tom1.wav')
tom2_sound = pygame.mixer.Sound('kit1-tom2.wav')
tom3_sound = pygame.mixer.Sound('kit1-tom3.wav')

snare_sound2 = pygame.mixer.Sound('kit2-snare.wav')
tom1_sound2 = pygame.mixer.Sound('kit2-tom1.wav')
tom2_sound2 = pygame.mixer.Sound('kit2-tom2.wav')
tom3_sound2 = pygame.mixer.Sound('kit2-tom3.wav')

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(1):
		    if kit == 1:
                    	snare_sound.play()
		    elif kit == 2:
                    	snare_sound2.play()
			print("kit 2!")

                if j.get_button(3):
		    if kit == 1:
                    	tom1_sound.play()
		    elif kit == 2:
                    	tom1_sound2.play()

                if j.get_button(2):
		    if kit == 1:                    
			tom2_sound.play()
		    elif kit == 2:
                    	tom2_sound2.play()

                if j.get_button(0):
		    if kit == 1:
                    	tom3_sound.play()
		    elif kit == 2:
                    	tom3_sound2.play()

		if j.get_button(11):
		    print("left")
		    if kit == 1:
			kit = numkits
		    else:
			kit = kit - 1

		if j.get_button(12):
		    print("right")
		    if kit == numkits:
			kit = 1
		    else:
			kit = kit + 1

		if j.get_button(13):
		    print("up")

		if j.get_button(14):
		    print("down")
		
		print(kit)
except KeyboardInterrupt:
    j.quit()
