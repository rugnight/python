# -*- coding: utf-8 -*-

# ==================================================
# 
#   �g����
#       convert_media SRC DST SETTING_FILE
# 
#   �ݒ�t�@�C��
#       TITLE_VALID_DURATION    00:00:10
#       CHAPTER_SPRIT           4
# ==================================================

import sys
import commands
import handbrake_media as HB

Usage = "Usage: python convert_media.py SRC DST_DIR SETTING_FILE"

# �����̏���
argvs = sys.argv;
argc  = len(argvs)

if argc < 4:
    print Usage 
    exit()

TARGET_FILE  = argvs[1]      # �ϊ��Ώۃt�@�C����
OUTPUT_DIR   = argvs[2]      # �o�͐�f�B���N�g����
SETTING_FILE = argvs[3]      # �ݒ�t�@�C��

# �f�����f�B�A�̏����擾
HB_RESEARCH_COMMAND = "HandBrakeCLI -i %s -t %s" % (TARGET_FILE, "0")
research_cmd_return = commands.getstatusoutput(HB_RESEARCH_COMMAND)
research_result = research_cmd_return[0]
research_lines  = research_cmd_return[1]

# �Ȃ񂩎��s
if research_result == 0:
    print "DVD���̎擾�Ɏ��s���܂���\n"
    exit()

# ���f�B�A�̏��
media = HB.HandBrakeMedia()
media.set(research_lines)
media.dump()

exit()

#HB_COMMAND = "HandBrakeCLI -i %s -t %s" % (TARGET_FILE, "0")
HB_COMMAND = "ls"

results    = commands.getstatusoutput(HB_COMMAND)
media_info = results[1]
print media_info 

media = HB.HandBrakeMedia()
media.set(f)

# ���f�B�A���ǂ����������H
analyse = HandBrakeMediaAnalyser()
