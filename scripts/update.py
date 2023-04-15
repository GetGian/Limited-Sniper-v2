import requests as r

print("Checking for updates...")
script = r.get("").text
with open("main.py", "r") as f:
   if f.read() != script:
        print("Updating...")
        with open("main.py", "w") as f:
            f.write(script)
            exit(0)
