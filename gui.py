from guizero import App, Text, Picture, Text  
count = 1
def switch():
    global count
    count =+ 1
    



app = App()

app.title = "Wanted App"
app.bg = "yellow"
text = Text(app, text="Wanted",size=34)
text.text_color = "black"

picture = Picture(app, image="maine_coon.png", width=600)

app.display()