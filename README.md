# Coding Bowl training bot

This bot serves the purpos of having an easy base for working together on one bot without having to much merge conflicts. Therefore it in designed in a way that modules can be simply added by inheriting from a the ModuleBase class.


## Contributing

In order to contribute to this project you need to do the follwing steps:

1. Have python3, pip and git installed on your system
2. Create a working directory for this project
3. [Optional but recommended] Create a python venv in your wd and activate it
4. Install the dependencies
```
pip install discord python-dotenv
```
5. Fork this repository and clone your fork
```
git clone <https://github.com/YOUR-FORK-ADDRESS.git>
```
6. Create a new branch for your feature
```
git checkout -b <ExampleFeatureBranchName>
```
7. Create a new module or make changes to the existing code base
8. Commit all changes
 ```
git add .
git commit -m "change description"
 ```
9. Merge new changes from master into your branch
```
git pull
git merge master
```
10. Push your feature
```
git push origin <ExampleFeatureBranchName>
```
11. Create a merde request from feature into master on github
12. Wait for approval

To be a bit faster, use `git commit -a -m "change description"` when no new files need to be added.

### Create a new module
To create a new module follow these steps:

1. Create a new .py in the modules folder
2. Import nessecary libraries
```
from ModuleBase import ModuleBase
```
3. Create a new class in your .py and inherite from `ModuleBase`
```
class ModuleIndex(ModuleBase):
    def __init__(self, bot):
        self.bot = bot
```
4. Add funcionality
5. Add your module to config.json (True or False indicates wether a module gets leaded or not)
```
{
  "modules" :
    {
      "modules.<.pyName>" : <true/false>
    }
}
```

If your module uses other custom classes/files put them in a subfolder within the modules folder together with your .py
```
{
  "modules" :
    {
      "modules.<subfolder>.<.pyName>" : <true/false>
    }
}
```

For more information please refere to the `ModuleIndex` as an example.
## Testing

To test your modele/bot you need to:

1. [Creat a discord server](https://support.discord.com/hc/en-us/articles/204849977-How-do-I-create-a-server-)
2. [Create a bot account and invite it to your server](https://discordpy.readthedocs.io/en/stable/discord.html)
3. Create a .env file in the same folder where the botMain.py is and add the following line (replace <TOKEN> with your token)
```
DISCORD_TOKEN=<TOKEN>
```
4. Start your bot with:
```
cd bowlBot
python bowlMain.py
```

For the sake of testing you can give your bot admin rights and activate all intents.
## Documentation

For now there will be no docmentation for this bot. So please add the getInformation() method to your module and add docstrings.
For an example please refere to `bowlBot/modules/ModuleIndex.py.


## References

[Discord bot documentation](https://discord.com/developers/docs/intro)

[discord.py documentation](https://discordpy.readthedocs.io/en/stable/index.html#)
