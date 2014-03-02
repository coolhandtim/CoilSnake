from coilsnake.model.eb.map_enemy_groups import MapEnemyGroupPointerTableEntry
from coilsnake.model.eb.table import eb_table_from_offset

from coilsnake.modules.eb import EbModule
from coilsnake.util.eb.pointer import from_snes_address


GROUP_POINTER_TABLE_OFFSET = 0xD0B880
GROUP_PLACEMENT_TABLE_OFFSET = 0xD01880


class MapEnemyModule(EbModule.EbModule):
    NAME = "Enemy Groups"
    FREE_RANGES = [(0x10BBAC, 0x10C60C)]  # Groups data

    def __init__(self):
        EbModule.EbModule.__init__(self)
        self.group_pointer_table = eb_table_from_offset(
            offset=GROUP_POINTER_TABLE_OFFSET,
            single_column=MapEnemyGroupPointerTableEntry)
        self.group_placement_table = eb_table_from_offset(offset=GROUP_PLACEMENT_TABLE_OFFSET)

    def read_from_rom(self, rom):
        self.group_pointer_table.from_block(rom, from_snes_address(GROUP_POINTER_TABLE_OFFSET))
        self.group_placement_table.from_block(rom, from_snes_address(GROUP_PLACEMENT_TABLE_OFFSET))

    def write_to_rom(self, rom):
        self.group_pointer_table.to_block(rom, from_snes_address(GROUP_POINTER_TABLE_OFFSET))
        self.group_placement_table.to_block(rom, from_snes_address(GROUP_PLACEMENT_TABLE_OFFSET))

    def write_to_project(self, resource_open):
        with resource_open("map_enemy_groups", "yml") as f:
            self.group_pointer_table.to_yml_file(f, default_flow_style=None)
        with resource_open(self.group_placement_table.name.lower(), "yml") as f:
            self.group_placement_table.to_yml_file(f)

    def read_from_project(self, resource_open):
        with resource_open("map_enemy_groups", "yml") as f:
            self.group_pointer_table.from_yml_file(f)
        with resource_open(self.group_placement_table.name.lower(), "yml") as f:
            self.group_placement_table.from_yml_file(f)