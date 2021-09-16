import justpy as jp 

def app():
	wp = jp.QuasarPage()
	h1 = jp.QDiv(a=wp, text="analysis of course reviews",classes="text-h3 text-center q-pa-md")
	p1 = jp.QDiv(a=wp, text="there is graphs represent course reviews analysis")
	return wp

jp.justpy(app)