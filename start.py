from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import logging
import base64
import hashlib
import json
import os
from info import config
import handlers
from subprocess import (PIPE, Popen)

hls = handlers

updater = Updater(config.token)
updater.dispatcher.add_handler(CommandHandler('help', hls.help))

updater.dispatcher.add_handler(CommandHandler('stop', hls.stop))

updater.dispatcher.add_handler(CommandHandler('enc', hls.md5))

updater.dispatcher.add_handler(CommandHandler('hello', hls.hello))

updater.dispatcher.add_handler(CommandHandler('date', hls.date))

updater.dispatcher.add_handler(CommandHandler('reply', hls.reply))

updater.dispatcher.add_handler(CommandHandler('start', hls.start))

updater.dispatcher.add_handler(CommandHandler('dec', hls.dec))

updater.dispatcher.add_handler(CommandHandler('clsd', hls.clsd))

updater.dispatcher.add_handler(CommandHandler('users',
hls.users))

updater.dispatcher.add_handler(CommandHandler('clslog',
hls.clslog))

updater.dispatcher.add_handler(CommandHandler('read',
hls.read))

updater.dispatcher.add_handler(CommandHandler('perm',
hls.perm))

updater.dispatcher.add_handler(CommandHandler('sperm',
hls.stopperm))

updater.dispatcher.add_handler(CommandHandler('log',
hls.log))

updater.dispatcher.add_handler(CommandHandler('send',
hls.send))

updater.dispatcher.add_handler(CommandHandler('setid',
hls.setid))

updater.dispatcher.add_handler(CommandHandler('chid',
hls.chid))

updater.dispatcher.add_handler(CommandHandler('banapil',
hls.banapil))

updater.dispatcher.add_handler(CommandHandler('ban',
hls.ban))

updater.dispatcher.add_handler(CommandHandler('unban',
hls.unban))

updater.dispatcher.add_handler(CommandHandler('banlist',
hls.banlist))

updater.dispatcher.add_handler(CommandHandler('setreason',
hls.setreason))

updater.dispatcher.add_handler(CommandHandler('warn',
hls.warn))

updater.dispatcher.add_handler(CommandHandler('unwarn',
hls.unwarn))

updater.dispatcher.add_handler(CommandHandler('spermu',
hls.spermu))

updater.dispatcher.add_handler(CommandHandler('info',
hls.info))

updater.dispatcher.add_handler(CommandHandler('infoid',
hls.infoid))

updater.dispatcher.add_handler(CommandHandler('token',
hls.token))

updater.dispatcher.add_handler(MessageHandler(Filters.text,
hls.ai))


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater.start_polling()
updater.idle()


