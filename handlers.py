from datetime import datetime
from telegram.ext import Updater
import bot
import logging
import base64
import hashlib
import apiai, json
import os
import random
from info import config
from lang.ru import ru
from lang.en import en
from lang.uk import uk
from subprocess import (PIPE, Popen)

updater = Updater(config.token)
b = bot.Bot(config.token)


def log(bot, update):
    if update.message.from_user.language_code == 'uk':
        lang = 'uk'
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lang = 'ru'
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
        lang = 'en'
    else:
        lng = en
        lang = 'en'
    mess = update.message.text
    mess = mess[5:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        if os.path.exists('info/perm' + update.message.from_user.username):
            if mess == 'true':
                update.message.reply_text(lng.logstart)
                open('info/logtool', 'w').write(mess).close()
            elif mess == 'false':
                os.remove('info/logtool')
                update.message.reply_text(lng.logstop)
            else:
                update.message.reply_text('Error')
        else:
            update.message.reply_text(lng.perms)


def dates():
    return datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")


def invoke(userhah, loltext):
    if os.path.exists('info/logtool'):
        b.send_message(168434295, '[ ' + dates() + ' ] ' + userhah + ': ' + loltext)
    l = open("info/log.txt", 'a')
    l.write('[ ' + dates() + ' ] ' + userhah + ': ' + loltext + '\n')
    l.close()


def stop(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        f = open('music/1.ogg', 'rb')
        bot.send_voice(update.message.chat.id, f, None)
        messp = update.message.text
        mess = messp[6:]
        passw = config.adminpass
        invoke(update.message.from_user.username, update.message.text)
        # update.message.reply_text(enc + ' ' + passw)
        if os.path.exists('info/perm' + update.message.from_user.username):
            update.message.reply_text("Its a prank Bro)0))0)")
        else:
            update.message.reply_text("Its a prank Bro)0))0)")


def hello(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    user = update.message.from_user.username
    name = update.message.from_user.first_name
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if user == config.admin:
            update.message.reply_text(lng.helloadm)
        else:
            update.message.reply_text(lng.hello + name + '!')


def date(bot, update):
    update.message.reply_text(dates())


def reply(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        rpm = update.message.text
        rpm = rpm[6:]
        invoke(update.message.from_user.username, update.message.text)
        f = open('info/replies.txt', 'a')
        f.write(
            rpm + ' [Username: ' + update.message.from_user.username + ', Date: ' + datetime.strftime(datetime.now(),
                                                                                                      "%d.%m.%Y %H:%M:%S") + ' ]' + '\n')
        f.close()
        update.message.reply_text(lng.reply_text)


def start(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        update.message.reply_text(lng.start)
        uname = update.message.from_user.username
        fname = update.message.from_user.first_name
        lname = update.message.from_user.last_name
        invoke(update.message.from_user.username, update.message.text)
        w = open('info/users.txt', 'w')
        w.write('@' + update.message.from_user.username + '\n')
        w.close()
        k = open('info/users/' + update.message.from_user.username, 'w')
        k.write(
            uname + ', ' + fname + ', ' + lname + ', lang: ' + update.message.from_user.language_code + ', id: ' + str(
                update.message.chat_id))
        k.close()
        t = open('info/chid/' + update.message.from_user.username, 'w')
        t.write(str(update.message.chat_id))
        t.close()
        t = open('info/chid/ids/' + str(update.message.chat_id), 'w')
        t.write(update.message.from_user.username)
        t.close()


def md5(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        mes = update.message.text
        mes = mes[5:]
        cod = hashlib.md5(mes.encode("UTF-8")).hexdigest()
        invoke(update.message.from_user.username, update.message.text)
        update.message.reply_text(cod + ' ' + mes)
        d = open('info/md5/' + cod, 'a')
        d.write(mes)
        d.close()


def dec(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        me = update.message.text
        me = me[5:]
        invoke(update.message.from_user.username, update.message.text)
        h = open('info/md5/' + me, 'r')
        update.message.reply_text(h.read())
        h.close()


def clsd(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        msg = update.message.text
        msg = msg[6:]
        pwd = config.adminpass
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            update.message.reply_text(lng.clsd)
            os.system("rm -rf ./info/md5/* && rm ./info/users.txt")
        else:
            update.message.reply_text(lng.perms)


def help(bot, update):
    if update.message.from_user.language_code == 'uk':
        lang = 'uk'
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lang = 'ru'
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
        lang = 'en'
    else:
        lng = en
        lang = 'en'
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        mmsg = update.message.text
        mmsg = mmsg[6:]
        invoke(update.message.from_user.username, update.message.text)
        u = open('lang/' + lang + '/help/' + mmsg + '.txt', 'r')
        update.message.reply_text(u.read())
        u.close()


def users(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        message = update.message.text
        message = message[7:]
        pwds = config.adminpass
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            update.message.reply_text(os.listdir("info/users"))
            update.message.reply_text('Done')
        else:
            update.message.reply_text(lng.perms)


def clslog(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        messager = update.message.text
        messager = messager[8:]
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            os.system('rm -rf ./info/log.txt')
            update.message.reply_text('Done')
        else:
            update.message.reply_text(lng.perms)


def read(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        mesege = update.message.text
        mesege = mesege[6:]
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            if os.path.exists(mesege):
                io = open(mesege, 'r')
                update.message.reply_text(io.read())
                io.close()
            else:
                update.message.reply_text(lng.ioerr)
        else:
            update.message.reply_text(lng.perms)


def perm(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[6:]
    pwdrs = config.adminpass
    invoke(update.message.from_user.username, update.message.text)
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        encodre = hashlib.md5(meseger.encode("UTF-8")).hexdigest()
        if pwdrs == encodre:
            ios = open('info/perm' + update.message.from_user.username, 'w')
            ios.write(encodre)
            ios.close()
        else:
            if os.path.exists('info/warns/' + update.message.from_user.username):
                open('info/ban/' + update.message.from_user.username, 'w').close()
                update.message.reply_text(lng.banned)
                io = open('info/chid/' + update.message.from_user.username)
                chids = io.read()
                io.close()
                b.send_message(chids, lng.sysbanumess)
            else:
                update.message.reply_text(lng.inv_pass)
                open('info/warns/' + update.message.from_user.username, 'w').close()


def stopperm(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            os.remove('info/perm' + update.message.from_user.username)
            update.message.reply_text('Done.')
        else:
            update.message.reply_text(lng.ioerr)


def setid(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        meseger = update.message.text
        meseger = meseger[7:]
        s = open('info/ids/setid' + update.message.from_user.username, 'w')
        s.write(meseger)
        s.close()
        update.message.reply_text('Done')


def send(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[6:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        num = random.randint(0, 10000)
        if os.path.exists('info/perm' + update.message.from_user.username):
            if os.path.exists('info/ids/setid' + update.message.from_user.username):
                s = open('info/ids/setid' + update.message.from_user.username, 'r')
                id = s.read()
                s.close()
                ids = open('info/numess', 'a')
                ids.write(str(id) + ' ' + str(update.message.chat_id) +  ' [ ' + str(num) + ', ' + dates() + ' ]: ' + meseger + "\n")
                b.send_message(id, '[ Sended by admin (' + str(num) + ') ]: ' + meseger + '\n')
                update.message.reply_text('Ok')
            else:
                update.message.reply_text(lng.setid)
        else:
            update.message.reply_text(lng.perms)


def chid(bot, update):
    update.message.reply_text(update.message.chat_id)
    invoke(update.message.from_user.username, update.message.text)


def banapil(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        rpm = update.message.text
        rpm = rpm[9:]
        invoke(update.message.from_user.username, update.message.text)
        f = open('info/banapils.txt', 'a')
        f.write(
            rpm + ' [Username: ' + update.message.from_user.username + ', Date: ' + datetime.strftime(datetime.now(),
                                                                                                      "%d.%m.%Y %H:%M:%S") + ' ]' + '\n')
        f.close()
        update.message.reply_text(lng.reply_text)
    else:
        update.message.reply_text('Доступ к этой команде имеют только забаненные пользователи')


def ban(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[5:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            open('info/ban/' + meseger, 'w').close()
            update.message.reply_text(meseger + lng.banmess)
            io = open('info/chid/' + meseger)
            chids = io.read()
            io.close()
            io = open('info/reasons/reason' + update.message.from_user.username)
            reason = io.read()
            io.close
            b.send_message(chids, lng.adminbanumess + reason)
        else:
            update.message.reply_text(lng.perms)


def unban(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[7:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            os.remove('info/ban/' + meseger)
            update.message.reply_text(meseger + lng.unbanmess)
            io = open('info/chid/' + meseger)
            chids = io.read()
            io.close()
            b.send_message(chids, lng.adminunbanumess)
        else:
            update.message.reply_text(lng.perms)


def banlist(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            update.message.reply_text(os.listdir("info/ban"))
            update.message.reply_text('Done')
        else:
            update.message.reply_text(lng.perms)


def spermu(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    mess = update.message.text
    mess = mess[8:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            os.remove('info\perm' + mess)
            update.message.reply_text('Done.')
        else:
            update.message.reply_text(lng.ioerr)


def warn(bot, update):
    global lng
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[6:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            io = open('info/chid/' + meseger)
            chids = io.read()
            io.close()
            if os.path.exists('info/warns/' + meseger):
                open('info/ban/' + meseger, 'w').close()
                b.send_message(chids, lng.sysbanumess)
            open('info/warns/' + meseger, 'w').close()
            update.message.reply_text(meseger)
            io = open('info/reasons/reason' + update.message.from_user.username)
            reason = io.read()
            io.close()
            b.send_message(chids, lng.adminwarnmess + reason)
        else:
            update.message.reply_text(lng.perms)


def unwarn(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    meseger = update.message.text
    meseger = meseger[8:]
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        if os.path.exists('info/perm' + update.message.from_user.username):
            os.remove('info/warns/' + meseger)
            io = open('info/chid/' + meseger)
            chids = io.read()
            io.close()
            b.send_message(chids, lng.adminunwarnmess)

        else:
            update.message.reply_text(lng.perms)


def setreason(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        invoke(update.message.from_user.username, update.message.text)
        meseger = update.message.text
        meseger = meseger[11:]
        s = open('info/reasons/reason' + update.message.from_user.username, 'w')
        s.write(meseger)
        s.close()
        update.message.reply_text('Done')


def info(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
     if os.path.exists('info/perm' + update.message.from_user.username):
        invoke(update.message.from_user.username, update.message.text)
        meseger = update.message.text
        meseger = meseger[6:]
        k = open('info/users/' + meseger, 'r')
        uname = k.read()
        k.close()
        update.message.reply_text(uname)
     else:
      update.message.reply_text(lng.perms)



def infoid(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
      if os.path.exists('info/perm' + update.message.from_user.username):
        invoke(update.message.from_user.username, update.message.text)
        meseger = update.message.text
        meseger = meseger[8:]
        k = open('info/chid/ids/' + meseger, 'r')
        nick = k.read()
        k.close()
        u = open('info/users/' + nick, 'r')
        uname = u.read()
        u.close()
        update.message.reply_text(uname)
      else:
        update.message.reply_text(lng.perms)



def token(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        meseger = update.message.text
        token = meseger[7:]
        genid = token[:4]
        yeid1 = token[4:]
        yeid = yeid1[:4]
        naid1 = token[8:]
        naid = naid1[:4]
        whoid1 = token[12:]
        whoid = whoid1[:3]
        checknum = token[15:]
        if genid == '5741':
            genname = "Official Service of MashDB"
        elif genid == '1234':
            genname = "Unknown"
        elif genid == '6811':
            genname = "SevenBot"
        else:
            genname = "Unofficial"

        if yeid < '2015':
            year = "Unsecured Token"
        else:
            year = yeid

        if naid == '6751':
            namegen = "MashDB Security Service"
        elif naid == '7124':
            namegen = "Telegram SevenBot Generator"
        else:
            namegen = "Unofficial"

        if whoid == '444':
            whouse = "MashDB License"
        elif whoid == '616':
            whouse = "NsUO Frame Code"
        elif whoid == '532':
            whouse = "DPFs Protect"
        else:
            whouse = "Unofficial"


        a1 = int(genid)
        a2 = int(naid)
        a3 = int(whoid)
        a4 = int(yeid)
        ch1 = int(checknum)

        chknum = a1 + a2 - a3 + a4
        print(chknum)
        print(ch1)
        if ch1 == chknum:
            correct = "Token Correct"
        else:
            correct = "Token Incorrect"

        update.message.reply_text("Generated by: "+genname+"\nYear: "+year+"\nName: "+namegen+"\nPurpose: "+whouse+"\nIs Correct: "+correct)

def ai(bot, update):
    if update.message.from_user.language_code == 'uk':
        lng = uk
    elif update.message.from_user.language_code == 'ru':
        lng = ru
    elif update.message.from_user.language_code == 'en':
        lng = en
    else:
        lng = en
    if os.path.exists('info/ban/' + update.message.from_user.username):
        update.message.reply_text(lng.ban)
    else:
        request = apiai.ApiAI('f0d8dbdcf1534f6d99123bca2cafaa51').text_request() # Токен API к Dialogflow
        request.lang = 'ru' # На каком языке будет послан запрос
        request.session_id = 'AIMASHDB' # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(update.message.chat_id, response)
        else:
            bot.send_message(update.message.chat_id, 'Я Вас не совсем поняла!')







