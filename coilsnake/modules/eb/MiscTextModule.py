from coilsnake.model.eb.table import EbStandardTextTableEntry
from coilsnake.modules.eb.EbModule import EbModule
from coilsnake.util.common.yml import yml_load, yml_dump


MISC_TEXT_OFFSETS = {
    "Starting Text": {
        "Start New Game": (0x004c060, 14),
        "Text Speed": (0x04c074, 11),
        "Text Speed Fast": (0x04c07f, 6),
        "Text Speed Medium": (0x04c086, 6),
        "Text Speed Slow": (0x04c08d, 6),
        "Continue": (0x04c094, 9),
        "Copy": (0x04c09d, 5),
        "Delete": (0x04c0a2, 6),
        "Set Up": (0x04c0a9, 7),
        "Copy to where?": (0x04c0b0, 14),
        "Confirm Delete": (0x04c0be, 32),
        "Confirm Delete No": (0x04c0de, 2),
        "Confirm Delete Yes": (0x04c0e1, 3),
        "Select Speed": (0x04c0e5, 25),
        "Select Sound": (0x04c0fe, 28),
        "Select Sound Stereo": (0x04c11a, 6),
        "Select Sound Mono": (0x04c121, 6),
        "Select Style": (0x04c128, 37),
        "Ask Name 1": (0x04c194, 40),
        "Ask Name 2": (0x04c1bc, 40),
        "Ask Name 3": (0x04c1e4, 40),
        "Ask Name 4": (0x04c20c, 40),
        "Ask Name Pet": (0x04c234, 40),
        "Ask Name Food": (0x04c25c, 40),
        "Ask Name PSI": (0x04c284, 40),
        "Confirm Food": (0x04c2ac, 14),
        "Confirm PSI": (0x04c2ba, 14),
        "Confirm All": (0x04c2c8, 13),
        "Confirm All Yes": (0x04c2d5, 3),
        "Confirm All No": (0x04c2d9, 4)
    },
    "Ailments": {
        "Ailment 01": (0x045b70, 16),
        "Ailment 02": (0x045b80, 16),
        "Ailment 03": (0x045b90, 16),
        "Ailment 04": (0x045ba0, 16),
        "Ailment 05": (0x045bb0, 16),
        "Ailment 06": (0x045bc0, 16),
        "Ailment 07": (0x045bd0, 16),
        "Ailment 08": (0x045be0, 16),
        "Ailment 09": (0x045bf0, 16),
        "Ailment 10": (0x045c00, 16)
    },
    "Battle Menu": {
        "Bash": (0x049fe1, 16),
        "Goods": (0x049ff1, 16),
        "Auto Fight": (0x04a001, 16),
        "PSI": (0x04a011, 16),
        "Defend": (0x04a021, 16),
        "Pray": (0x04a031, 16),
        "Shoot": (0x04a041, 16),
        "Spy": (0x04a051, 16),
        "Run Away": (0x04a061, 16),
        "Mirror": (0x04a071, 16),
        "Do Nothing": (0x04a081, 11)  # New in CoilSnake 2.0
    },
    "Out of Battle Menu": {
        "Talk to": (0x2fa37a, 9),
        "Goods": (0x2fa384, 9),
        "PSI": (0x2fa38e, 9),
        "Equip": (0x2fa398, 9),
        "Check": (0x2fa3a2, 9),
        "Status": (0x2fa3ac, 9)
    },
    "Status Window": {
        "Level": (0x2fa3ba, 6),
        "Hit Points": (0x2fa3c4, 11),
        "Psychic Points": (0x2fa3d3, 15),
        "Experience Points": (0x2fa3e6, 18),
        "Exp. for next level": (0x2fa3fc, 20),
        "Offense": (0x2fa414, 8),
        "Defense": (0x2fa420, 8),
        "Speed": (0x2fa42c, 6),
        "Guts": (0x2fa436, 5),
        "Vitality": (0x2fa43f, 9),
        "IQ": (0x2fa44c, 3),
        "Luck": (0x2fa453, 5),
        "PSI Prompt": (0x045b4d, 35)  # From HS
    },
    "Other": {
        "Player Name Prompt": (0x03fb2b, 36),  # From HS
        "Lumine Hall Text": (0x048037, 213)
    },
    # From HS
    "PSI Types": {
        "Offense": (0x03f090, 7),
        "Recover": (0x03f098, 7),
        "Assist": (0x03f0a0, 7),
        "Other": (0x03f0a8, 7)
    },
    "PSI Menu": {
        "PP Cost": (0x03f11c, 7),
        "To enemy": (0x03f124, 19),
        "To one enemy": (0x03f138, 19),
        "To one enemy 2": (0x03f14c, 19),
        "To row of foes": (0x03f160, 19),
        "To all enemies": (0x03f174, 19),
        "himself": (0x03f188, 19),
        "To one of us": (0x03f19c, 19),
        "To one of us 2": (0x03f1b0, 19),
        "To all of us": (0x03f1c4, 19),
        "To all of us 2": (0x03f1d8, 19),
        "Row To": (0x0454f2, 3),
        "Row Front": (0x0454f5, 13),
        "Row Back": (0x45502, 15)
    },
    "Equip Menu": {
        "Offense": (0x045c1c, 7),
        "Defense": (0x045c24, 7),
        "Weapon": (0x045c2c, 10),
        "Body": (0x045c37, 10),
        "Arms": (0x045c42, 10),
        "Other": (0x045c4d, 10),
        "Weapon Window Title": (0x045c58, 7),
        "Body Window Title": (0x045c60, 7),
        "Arms Window Title": (0x045c68, 7),
        "Other Window Title": (0x045c70, 7),
        "No Equip": (0x045c78, 9),
        "Unequip": (0x045c82, 4),
        "To": (0x045c87, 2)
    },
    "Item Menu": {
        "Use": (0x043550, 5),
        "Give": (0x043556, 5),
        "Drop": (0x04355c, 5),
        "Help": (0x043562, 5)
    },
    "Menu Action Targets": {
        "Who": (0x045963, 9),
        "Which": (0x04596d, 9),
        "Where": (0x045977, 9),
        "Whom": (0x045981, 9),
        "Where 2": (0x04598b, 9)
    },
    "Window Titles": {
        "Escargo Express Window Title": (0x045c10, 12),
        "Phone Window Title": (0x045995, 4)
    }
}

TEXT_TABLE_ENTRIES = dict()
for category_name, category in MISC_TEXT_OFFSETS.iteritems():
    for item_name, item in category.iteritems():
        offset, size = item
        if size not in TEXT_TABLE_ENTRIES:
            TEXT_TABLE_ENTRIES[size] = type(
                "EbStandardTextTableEntry_Size{}".format(size),
                (EbStandardTextTableEntry,),
                {"size": size})


class MiscTextModule(EbModule):
    NAME = "Miscellaneous Text"

    def __init__(self):
        super(MiscTextModule, self).__init__()
        self.data = dict()

    def read_entry_from_rom(self, rom, offset, size):
        return TEXT_TABLE_ENTRIES[size].from_block(rom, offset)

    def read_from_rom(self, rom):
        for category_name, category in MISC_TEXT_OFFSETS.iteritems():
            category_data = dict()
            for item_name, item in category.iteritems():
                offset, size = item
                category_data[item_name] = self.read_entry_from_rom(rom, offset, size)
            self.data[category_name] = category_data

    def write_to_rom(self, rom):
        for category_name, category in MISC_TEXT_OFFSETS.iteritems():
            for item_name, item in category.iteritems():
                offset, size = item
                TEXT_TABLE_ENTRIES[size].to_block(rom, offset, self.data[category_name][item_name])
                if (category_name == "Status Window") and (len(self.data[category_name][item_name]) < size):
                    rom.write_multi(offset + len(self.data[category_name][item_name]),
                                    0,
                                    size - len(self.data[category_name][item_name]))

    def write_to_project(self, resource_open):
        with resource_open("text_misc", "yml") as f:
            yml_dump(self.data, f, default_flow_style=False)

    def read_from_project(self, resource_open):
        with resource_open("text_misc", "yml") as f:
            self.data = yml_load(f)

    def upgrade_project(self, old_version, new_version, rom, resource_open_r, resource_open_w, resource_delete):
        if old_version == new_version:
            return
        elif old_version == 4:
            self.read_from_project(resource_open_r)

            offset, size = MISC_TEXT_OFFSETS["Battle Menu"]["Do Nothing"]
            self.data["Battle Menu"]["Do Nothing"] = self.read_entry_from_rom(rom, offset, size)

            self.write_to_project(resource_open_w)

            self.upgrade_project(old_version + 1, new_version, rom, resource_open_r, resource_open_w, resource_delete)
        elif old_version <= 2:
            self.read_from_rom(rom)
            self.write_to_project(resource_open_w)
            self.upgrade_project(3, new_version, rom, resource_open_r, resource_open_w, resource_delete)
        else:
            self.upgrade_project(old_version + 1, new_version, rom, resource_open_r, resource_open_w, resource_delete)