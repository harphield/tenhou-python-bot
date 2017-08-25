# -*- coding: utf-8 -*-
from mahjong.hand_calculating.yaku import Yaku


class Chiihou(Yaku):

    def set_attributes(self):
        self.yaku_id = 38
        self.name = 'Chiihou'

        self.han_open = None
        self.han_closed = 13

        self.is_yakuman = True

    def is_condition_met(self, hand):
        return True
