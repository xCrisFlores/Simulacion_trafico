import json 
from app.simulacion import Simulacion


def load_config():
    with open("config.json", "r") as file:
        return json.load(file)


def main():
    config = load_config()

    simulation = Simulacion(config)

    simulation.run()


if __name__ == "__main__":
    main()