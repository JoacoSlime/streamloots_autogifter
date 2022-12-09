import json
import os
import sys
import requests
from tkinter import *
from tkinter import ttk


class Config:
    def get_packs(self):
        url = f"https://api.streamloots.com/sets?slug={self.data['CHANNEL_NAME']}"
        headers = {"Authorization": "Bearer " + self.data["AUTH_TOKEN"]}
        packs = requests.get(url=url, headers=headers)
        if packs.status_code == 403:
            raise Exception(
                "Insufficient permissions, "
                "probably the name and token are from different accounts."
            )
        packs = json.loads(packs.text)
        packs = packs["data"]
        return packs

    # Updates token before closing.
    def confirm_auth(self):
        self.data["AUTH_TOKEN"] = self.auth_input.get()
        self.auth_window.destroy()
    
    # Updates ID before closing.
    def confirm_name(self):
        self.data["CHANNEL_NAME"] = self.name_input.get().lower()
        self.name_window.destroy()

    # Updates ID before closing.
    def confirm_id(self):
        self.data["ITEM_ID"] = self.packs_names.get(self.clicked.get())
        self.id_window.destroy()

    def configure(self):

        # Opens a window and waits for an auth token.
        self.auth_window = Tk()
        self.auth_window.title("Authentication")
        frm = ttk.Frame(self.auth_window, padding=15)
        frm.grid()
        ttk.Label(frm, text="Copy the AUTH_TOKEN value from the cookies.").grid(
            column=0, row=0, pady=(0, 15)
        )
        ttk.Label(
            frm, text="Follow step 2 on the README for instructions to scrap it."
        ).grid(column=0, row=1, pady=(0, 15))
        self.auth_input = ttk.Entry(frm)
        self.auth_input.grid(column=0, row=2, ipadx=50, pady=15)
        ttk.Button(frm, text="Confirm", command=lambda: self.confirm_auth()).grid(
            column=0, row=3, pady=(15, 0)
        )

        self.auth_window.mainloop()
        frm.quit()

        # Opens a window and waits for an auth token.
        self.name_window = Tk()
        self.name_window.title("Select channel")
        frm = ttk.Frame(self.name_window, padding=15)
        frm.grid()
        ttk.Label(frm, text="Insert the name of your channel.").grid(
            column=0, row=0, pady=(0, 15)
        )
        self.name_input = ttk.Entry(frm)
        self.name_input.grid(column=0, row=1, ipadx=50, pady=15)
        ttk.Button(frm, text="Confirm", command=lambda: self.confirm_name()).grid(
            column=0, row=2, pady=(15, 0)
        )

        self.name_window.mainloop()
        frm.quit()

        # Requests the list of collections.
        packs = self.get_packs()
        self.packs_names = dict()
        item_name = ""
        for i in packs:
            self.packs_names.update({i["name"]: i["_id"]})

        # Opens a window with a dropdown of the collections.
        self.id_window = Tk()
        self.id_window.title("Select Pack")
        frm = ttk.Frame(self.id_window, padding=15)
        frm.grid()
        ttk.Label(frm, text="Select the Collection you want to give.").grid(
            column=0, row=0, pady=(0, 15)
        )
        self.clicked = StringVar()
        OptionMenu(frm, self.clicked, *list(self.packs_names.keys())).grid(
            column=0, row=1, pady=(15, 0)
        )
        ttk.Button(frm, text="Confirm", command=lambda: self.confirm_id()).grid(
            column=0, row=2, pady=(15, 0)
        )
        self.id_window.mainloop()
        frm.quit()

        f = open(self.file, "w")
        f.write(json.dumps(self.data, indent=4))
        f.close()


    def load_config(self):
        return self.data

    def __init__(self, file):
        self.file = file
        f = open(file, "r")
        self.data = json.load(f)
        f.close()


def give_chest(data, user):
    url = "https://api.streamloots.com/loot-orders"
    headers = {
        "Authorization": "Bearer " + data["AUTH_TOKEN"],
        "Content-Type": "application/json",
    }
    obj = json.dumps(
        {
            "items": [
                {
                    "item": {
                        "setId": data["ITEM_ID"],
                        "cardAmount": data["CARDS"],
                    },
                    "quantity": data["TIMES"],
                }
            ],
            "gifteeUsername": user,
            "type": "FREE_GIFT",
        }
    )
    request = requests.post(url=url, data=obj, headers=headers)
    if request.status_code == 403:
        raise Exception(
            "Insufficient permissions, probably the name and token are from different accounts."
        )
    return request


if __name__ == "__main__":
    if len(sys.argv) == 2:
        data_file_path = os.path.join(os.path.dirname(__file__), "config.json")

        # Restore config.json when asked
        if sys.argv[1] == "--reset":
            default = {
                "AUTH_TOKEN": "Insert your auth token here",
                "ITEM_ID": "Insert your pack id here or configure it on first start",
                "CARDS": 3,
                "TIMES": 1,
                "CHANNEL_NAME": "Insert your channel name here",
            }
            f = open(data_file_path, "w")
            f.write(json.dumps(default, indent=4))
            f.close()
            print(0)
        elif sys.argv[1] == "--configure":
            config = Config(data_file_path)
            config.configure()
            print("Script configurado!")
            print("Modifica la cantidad de cartas por pack y la cantidad de packs enviados en config.json")
        else:
            config = Config(data_file_path)
            response = give_chest(config.load_config(), user=sys.argv[1])
            print(response.status_code)
    else:
        print(401)
