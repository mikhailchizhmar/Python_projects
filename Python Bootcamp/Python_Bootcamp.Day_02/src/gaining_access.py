class Key:
    def __init__(self):
        self.passphrase = "zax2rulez"

    def __len__(self):
        return 1337

    def __getitem__(self, item):
        return 3

    def __gt__(self, other):
        if isinstance(other, (int, float)) and other <= 9000:
            return True
        return False

    def __str__(self):
        return "GeneralTsoKeycard"


if __name__ == '__main__':
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
