import json
import interactions

from flask import Flask, request, redirect, render_template
from multiprocessing import Process

with open("./config/scopes.json") as scopes:
    scopes = json.load(scopes)
    testing = scopes["testing"]

class flask(interactions.Extension):
    def __init__(self, Tsumugi):
        self.Tsumugi = Tsumugi
        self.server = None

    @interactions.extension_command(
        name = "flask",
        description = "hosting a flask server",
        scope = [testing],
        options = [
            interactions.Option(
                name = "operation",
                description = "type of operation",
                type = interactions.OptionType.STRING,
                required = True,
                choices = [
                    interactions.Choice(
                        name = "Start",
                        value = "Start"
                    ),
                    interactions.Choice(
                        name = "Terminate",
                        value = "Terminate"
                    )
                ]
            )
        ]
    )

    async def flask(self, ctx: interactions.CommandContext, operation: str):
        if operation == "Start":
            await ctx.send(f"Start hosting server!\nhttp://127.0.0.1:5000", ephemeral=True)

            app = Flask(
                __name__,
                template_folder = "../templates"
            )

            @app.route("/")
            def index():
                return "Tsumugi is here!"

            @app.route("/upload", methods=["GET", "POST"])
            def upload():
                if request.method == "POST":
                    file = request.files["file"]
                    if file.filename == "":
                        print("No file selected.")
                        return redirect(request.url)
                    file.save(f"./upload/{file.filename}")
                return render_template("upload.html")

            server = Process(target=app.run)
            self.server = server
            server.start()

        elif operation == "Terminate":
            self.server.terminate()
            await ctx.send("Server terminated!", ephemeral=True)
            print("terminated successfully.")

def setup(Tsumugi):
    flask(Tsumugi)
