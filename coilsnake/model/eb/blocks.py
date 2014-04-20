import logging

from coilsnake.model.common.blocks import Block
from coilsnake.modules.eb import EbModule
from coilsnake.exceptions.eb.exceptions import InvalidEbCompressedDataError


log = logging.getLogger(__name__)


class EbCompressibleBlock(Block):
    def from_compressed_block(self, block, offset=0):
        self.data = EbModule.decomp(block, offset)
        if self.data[0] < 0:
            raise InvalidEbCompressedDataError("Couldn't decompress invalid data")
        self.size = len(self.data)

    def compress(self):
        compressed_data = EbModule.comp(self.to_list())
        self.from_list(compressed_data)