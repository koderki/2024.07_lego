from buildhat import Hat

hat = Hat()
dev = hat.get()
[print(value, dev[value]) for value in dev]
