# -*- coding: utf-8 -*-

# ==================================================
#   �g����
#       convert_media SRC DST SETTING_FILE
# 
#   �ݒ�t�@�C��
#       TITLE_VALID_DURATION    00:00:10
#       CHAPTER_SPRIT           4
# ==================================================

import sys
import commands
import handbrake_media as HB_MEDIA
import handbrake_setting as HB_SETTING
import handbrake_commander as HB_COMMANDER

Usage = "Usage: python convert_media.py SRC_MEDIA DST_DIR SETTING_FILE"

# �����̏���
argvs = sys.argv;
argc  = len(argvs)

if argc < 4:
    print Usage 
    exit()

TARGET_FILE  = argvs[1]      # �ϊ��Ώۃt�@�C����
OUTPUT_DIR   = argvs[2]      # �o�͐�f�B���N�g����
SETTING_FILE = argvs[3]      # �ݒ�t�@�C��

# ���f�B�A�̏��
media = HB_MEDIA.HandBrakeMedia()
if media.set(TARGET_FILE) == False:
    print "this media have no titles"
    exit()

# �ݒ�t�@�C���ǂݍ���
setting = HB_SETTING.HandBrakeSetting()
if setting.set(SETTING_FILE) == False:
    print "invalid setting file"
    exit()

# HandBrake���s�R�}���h�𐶐�
commands = HB_COMMANDER.HandBrakeCommander()
if commands.set(media, setting, OUTPUT_DIR) == False:
    print "command generate failed"
    exit()

commands.dump()    
print "done..."
exit()
