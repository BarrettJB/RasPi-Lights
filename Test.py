from bootstrap import 
anim = Rainbow(led)
for i in range(384):
	anim.step()
	led.update()*
led.all_off()