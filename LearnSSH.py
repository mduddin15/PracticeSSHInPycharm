#add some general code

import os
import sys
import time
import paramiko
import threading
import subprocess
import getpass
import socket
import re
import logging
import logging.handlers

class LearnSSH:

    def __init__(self, host, user, password, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.password)
        self.channel = self.ssh.invoke_shell()
        self.channel.settimeout(0.0)
        self.channel.setblocking(0)
        self.buffer = ''
        self.prompt = ''
        self.logger = logging.getLogger('LearnSSH')
        self.logger.setLevel(logging.DEBUG)
        self.logfile = 'LearnSSH.log'
        self.fh = logging.handlers.RotatingFileHandler(self.logfile, maxBytes=1000000, backupCount=5)
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.info('LearnSSH object created')

    def close(self):
        self.channel.close()
        self.ssh.close()
        self.logger.info('LearnSSH object closed')

    def send(self, command):
        self.channel.send(command + '\n')
        self.logger.info('Command sent: ' + command)

    def recv(self):
        while not self.channel.recv_ready():
            time.sleep(1)
        self.buffer = self.channel.recv(1024)
        self.logger.info('Data received: ' + self.buffer)
        return self.buffer

    def recvall(self):
        while not self.channel.recv_ready():
            time.sleep(1)
        while self.channel.recv_ready():
            self.buffer += self.channel.recv(1024)
        self.logger.info('Data received: ' + self.buffer)
        return self.buffer

    def set_prompt(self, prompt):
        self.prompt = prompt
        self.logger.info('Prompt set to: ' + self.prompt)

    def expect(self, prompt):
        self.set_prompt(prompt)
        while not self.prompt in self.buffer:
            self.recvall()
        self.logger.info('Prompt found: ' + self.prompt)

    def login(self):
        self.expect('login:')
        self.send(self.user)
        self.expect('assword:')
        self.send(self.password)
        self

    def run(self, command):
        self.send(command)
        self.expect(self.prompt)
        return self.buffer

    def runall(self, command):
        self.send(command)
        return self.recvall()

    def run2(self, command):
        self.send(command)
        return self.recv()

    def run3(self, command):
        self.send(command)
        return self.recvall()

    def run4(self, command):
        self.send(command)
        return self.recvall()

    def run5(self, command):
        self.send(command)
        return self.recvall()

    def run6(self, command):
        self.send(command)
        return self.recvall()

    def run7(self, command):
        self.send(command)
        return self.recvall()

    def run8(self, command):

        self.send(command)
        return self.recvall()


