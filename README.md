# FormulaCarbon

This is a repository for Sam and Ethan to coordinate code for our Formula Carbon cars.

1. $CO_2$ Cartridge
2. EV

# Useful Resources
* [Git Cheat Sheet](https://git-scm.com/cheat-sheet)
* [Git Install Link](https://git-scm.com/install/windows)


# ESP32 Useful Commands
### Install mpremote
```pip install mpremote```

### Connect to REPL (interactive console)
```mpremote connect COM7 repl```

### Copy a single file to the board
```mpremote connect COM7 cp main.py :main.py```

### Copy entire project folder to the board
```mpremote connect COM7 cp -r src/. :```

### Run a file without uploading it
```mpremote connect COM7 run main.py```

### Reset the board
```mpremote connect COM7 reset```

### List files on the board
```mpremote connect COM7 fs ls```

### Delete a file from the board
```mpremote connect COM7 fs rm :main.py```