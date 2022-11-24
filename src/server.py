import json

from multiprocessing import Process

import interactions

from flask import Flask, request, redirect, render_template

with open("./config.json") as scopes:
    scopes = json.load(scopes)["scopes"]

class server(interactions.Extension):
    def __init__(self, Tsumugi):
        self.Tsumugi = Tsumugi
        self.message = [interactions.Message]
        self.serevr = None

    @interactions.extension_command(
        name = "server",
        description = "hosting server",
        scope = scopes,
    )

    async def server(self, ctx: interactions.CommandContext):
        
        start = interactions.Button(
            style = interactions.ButtonStyle.PRIMARY,
            label = "Start",
            custom_id = "button_start"
        )
        stop = interactions.Button(
            style = interactions.ButtonStyle.DANGER,
            label = "Shutdown",
            custom_id = "button_shutdown"
        )

        self.message[0] = await ctx.send(content="Server console", components=[start, stop], ephemeral=False)

    @interactions.extension_component("button_start")
    async def start(self, ctx: interactions.CommandContext):
        
        app = Flask(__name__, template_folder="../templates")
        
        @app.route("/", methods=["GET", "POST"])
        def index():
            
            if request.method == "POST":
                file = request.files["file"]
                
                if file.filename == "":
                    print("No file selected.")
                    return redirect(request.url)

                file.save(f"./upload/{file.filename}")
                print("File uploaded!")

            return render_template("upload.html")

        self.server = Process(target=app.run, kwargs={"host": "0.0.0.0", "port": "80"})
        self.server.start()
        self.message.append(await ctx.send(f"Hosting server!\n> http://127.0.0.1:80/", ephemeral=False))

    @interactions.extension_component("button_shutdown")
    async def shutdown(self, ctx: interactions.CommandContext):
        
        if self.server != None:
            self.server.terminate()
            print("Server shutdown!")
        
        for message in self.message:
            await message.delete()
        
        self.message = [interactions.Message]
        
        await ctx.send("Shutdown successfully!", ephemeral=True)

def setup(Tsumugi):
    server(Tsumugi)