from src import DATA_DIR

hex_to_binary = lambda hex_chr: bin(int(hex_chr, 16))[2:].zfill(4)


def load_data():
    day_sixteen_file = DATA_DIR / "day16"
    with open(day_sixteen_file, "r") as f:
        return f.read()


def day16():
    print("--- Day 16: Packet Decoder ---")
    hex_data = load_data()
    print("HEX DATA", hex_data, sep="\n")
    print("BIN DATA", "".join([hex_to_binary(hex_chr) for hex_chr in hex_data]), sep="\n")


if __name__ == "__main__":
    day16()
