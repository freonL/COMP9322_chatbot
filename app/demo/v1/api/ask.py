# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from rivescript import RiveScript

from . import Resource
from .. import schemas


class Ask(Resource):

    def post(self):
        print(g.json)
        bot = RiveScript()
        bot.load_directory("app/demo/v1/api/brain")
        bot.sort_replies()
        reply = bot.reply("localuser", g.json['message'])
        output = {"message": reply}

        return output, 200, None