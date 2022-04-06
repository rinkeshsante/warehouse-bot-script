import requests


class Bot:
    def __init__(self, id: str, location_X: int, location_Y: int, server_URL: str) -> None:
        self.id = id
        self.location_X = location_X
        self.location_Y = location_Y
        self.server_URL = server_URL

    def getNewTask(self):
        payload = {}
        payload["data"] = {
            'bot_id': self.id,
            'location': {
                "X": self.location_X,
                "Y": self.location_Y
            }
        }

        headers = {'content-type': 'application/json'}

        r = requests.get(self.server_URL, data=payload)
        data = r.json()
        print(data)

        self.destination_X = data["destination"]["X"]
        self.destination_Y = data["destination"]["Y"]

    def move(self):
        if self.location_X == self.destination_X and self.location_Y == self.destination_Y:
            print("already on destination")
            return

        start_location = (self.location_x, self.location_Y)
        end_location = (self.destination_X, self.destination_Y)

        print(f"moving from {start_location} to {end_location}")
        # add navigation here

        self.location_X = self.destination_X
        self.location_Y = self.destination_Y

    def showLocation(self):
        print(f"x:{self.location_x}, y:{self.location_y}")

    def __str__(self) -> str:
        return f"{self.id}"
