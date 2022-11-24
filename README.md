# TsumugiShiraishi

A basic templates used for hosting a flask server and operates with discord bot.

## Configurations

### Required libraries/packages

```shell
discord-py-interactions
flask
```

### Secrets and hosting port

Edit `./config.json`

```python
{
    "port": str,
    "scopes": [*str],
    "token": str
}
```

## Usage

### Launch discord bot

If you're using non-privilege port just type the following command

```shell
$ python3 main.py
...
Tsumugi is ready!
```

Otherwise (unix for example, just using administrator mode depends on your operating system)

```shell
$ sudo python3 main.py
...
Tsumugi is ready!
```

If you don't want create `__pycache__` everytime you runs bot, type

```shell
$ python3 -B main.py
...
Tsumugi is ready!
```

### Launch server

Once you have launched the bot, enter `/server` on your discord server and the bot will send a server console on the chat.  

Click the `Start` button to hosting server, or click `Shutdown` to shutdown server then delete all the message that sent by the bot.

## License

Licensed under [MIT](LICENSE).
