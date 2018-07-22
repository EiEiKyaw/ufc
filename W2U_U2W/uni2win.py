# -*- coding: utf-8 -*-

import re


def replace(input):
    output = input

    output = re.sub(u'\u1000', u'\u0075', output) # Ka...
    output = re.sub(u'\u1001', u'\u0063', output) # Kha...
    output = re.sub(u'\u1002', u'\u002A', output) # Ga...
    output = re.sub(u'\u1003', u'\u0043', output) # GaGyi...
    output = re.sub(u'\u1004', u'\u0069', output) # Nga...
    output = re.sub(u'\u1005', u'\u0070', output) # SaLone...
    output = re.sub(u'\u1006', u'\u0071', output) # SaLai...
    output = re.sub(u'\u1007', u'\u005A', output) # ZaGwe...
    output = re.sub(u'\u1008', u'\u0070\u0073', output) # ZaMyinZwe...
    output = re.sub(u'\u1009', u'\u006E', output) # NyaLay...
    output = re.sub(u'\u100A', u'\u00DA', output) # Nya...
    output = re.sub(u'\u100B', u'\u0023', output) # TaTaLin...
    output = re.sub(u'\u100C', u'\u0058', output) # HtaWan...
    output = re.sub(u'\u100D', u'\u0021', output) # DaYinGaut...
    output = re.sub(u'\u100E', u'\u00A1', output) # DaYinMote...
    output = re.sub(u'\u100F', u'\u0050', output) # NaGyi...
    output = re.sub(u'\u1010', u'\u0077', output) # Ta...
    output = re.sub(u'\u1011', u'\u0078', output) # Hta...
    output = re.sub(u'\u1012', u'\u0027', output) # DaDway...
    output = re.sub(u'\u1013', u'\u0022', output) # DaOut...
    output = re.sub(u'\u1014', u'\u0065', output) # NaNge...
    output = re.sub(u'\u1015', u'\u0079', output) # Pa...
    output = re.sub(u'\u1016', u'\u007A', output) # PhaWaHtote...
    output = re.sub(u'\u1017', u'\u0041', output) # BaHtaChite...
    output = re.sub(u'\u1018', u'\u0062', output) # Ba...
    output = re.sub(u'\u1019', u'\u0072', output) # Ma...
    output = re.sub(u'\u101A', u'\u002C', output) # YaPaLat...
    output = re.sub(u'\u101B', u'\u0026', output) # Ya...
    output = re.sub(u'\u101C', u'\u0076', output) # La...
    output = re.sub(u'\u101D', u'\u0030', output) # Wa...
    output = re.sub(u'\u101E', u'\u006F', output) # Tha...
    output = re.sub(u'\u101F', u'\u005B', output) # Ha...
    output = re.sub(u'\u1020', u'\u0056', output) # LaGyi...
    output = re.sub(u'\u1021', u'\u0074', output) # Aa...
    output = re.sub(u'\u1023', u'\u00A3', output) # Kasint...
    output = re.sub(u'\u1024', u'\u00FE', output) # AKaYarEi...
    output = re.sub(u'\u1025', u'\u004F', output) # Ou...
    output = re.sub(u'\u1026', u'\u004F\u0044', output) # OuLoneGyi...
    output = re.sub(u'\u1027', u'\u007B', output) # Aye...
    output = re.sub(u'\u1029', u'\u004D\u006F', output) # All...
    output = re.sub(u'\u102A', u'\u0061\u004D\u006F\u006D\u0066', output)  # Aww...
    output = re.sub(u'\u102B', u'\u0067', output) # YaCha.Shae...
    output = re.sub(u'\u102C', u'\u006D', output) # YaCha...
    output = re.sub(u'\u102D', u'\u0064', output) # LoneGyiTin...
    output = re.sub(u'\u102E', u'\u0044', output) # LGT.San...
    output = re.sub(u'\u102F', u'\u004B', output) # TCN.Shae...
    output = re.sub(u'\u1030', u'\u004C', output) # NaCN.Shae...
    output = re.sub(u'\u1031', u'\u0061', output) # ThaWayHtoe...
    output = re.sub(u'\u1032', u'\u004A', output) # NautSoneMyint...
    output = re.sub(u'\u1036', u'\u0048', output) # ThayThayTin...
    output = re.sub(u'\u1037', u'\u0059', output) # OutMyint...
    output = re.sub(u'\u1038', u'\u003B', output) # WutSaNaLone...
    output = re.sub(u'\u103A', u'\u0066', output) # AThet...
    output = re.sub(u'\u103B', u'\u0073', output) # YaPint...
    output = re.sub(u'\u103C', u'\u006A', output) # YaYit...
    output = re.sub(u'\u103D', u'\u0047', output) # WaSwe...
    output = re.sub(u'\u103E', u'\u0053', output) # HaHtoe...
    output = re.sub(u'\u103F', u'\u00F3', output) # ThaGyi...
    output = re.sub(u'\u1040', u'\u0030', output) # 0...
    output = re.sub(u'\u1041', u'\u0031', output) # 1...
    output = re.sub(u'\u1042', u'\u0032', output) # 2...
    output = re.sub(u'\u1043', u'\u0033', output) # 3...
    output = re.sub(u'\u1044', u'\u0034', output) # 4...
    output = re.sub(u'\u1045', u'\u0035', output) # 5...
    output = re.sub(u'\u1046', u'\u0036', output) # 6...
    output = re.sub(u'\u1047', u'\u0037', output) # 7...
    output = re.sub(u'\u1048', u'\u0038', output) # 8...
    output = re.sub(u'\u1049', u'\u0039', output) # 9...
    output = re.sub(u'\u104A', u'\u003F', output) # PoteHte...
    output = re.sub(u'\u104B', u'\u002F', output) # PoteMa...
    output = re.sub(u'\u104C', u'\u00FC', output) # Nhite...
    output = re.sub(u'\u104D', u'\u00ED', output) # Ywae...
    output = re.sub(u'\u104E', u'\u00A4', output) # Ngu...
    output = output.replace(u'\u104F', u'\u005C') # Ei...
    #---------------------------------------------------------------------------------------------------
    output = re.sub(u'\u0069\u0066\u00A2', u'\u0043\u0046', output) # GaGyi...
    output = re.sub(u'\u0069\u00669([\u00A6\u00AC])', u'\u0078\u0046', output) # Hta...
    output = re.sub(u'\u0069\u0066\u00A8', u'\u0022\u0046', output) # DaOut...
    output = re.sub(u'\u0069\u0066\u00A9', u'\u0063\u0046', output) # Kha...
    output = re.sub(u'\u0069\u0066\u00AE', u'\u0072\u0046', output) # Ma...
    output = re.sub(u'\u0069\u0066\u00B4', u'\u0027\u0046', output) # DaDway...
    output = re.sub(u'\u0069\u0066\u00BE', u'\u002A\u0046', output) # GaNge...
    output = re.sub(u'\u0069\u0066\u00C1', u'\u0041\u0046', output) # BaHtat...
    output = re.sub(u'\u0069\u0066([\u00C5\u00E5])', u'\u0077\u0046', output) # TaWan...
    output = re.sub(u'\u0069\u0066\u00C6', u'\u005A\u0046', output) # Za...
    output = re.sub(u'\u0069\u0066\u00C7', u'\u0062\u0046', output) # BaGone...
    output = re.sub(u'\u0069\u0066\u00D6', u'\u0050\u0046', output) # NaGyi...
    output = re.sub(u'\u0069\u0066\u00DC', u'\u0079\u0046', output) # Pa...
    output = re.sub(u'\u0069\u0066\u00E4', u'\u0071\u0046', output) # SaLai...
    output = re.sub(u'\u0069\u0066\u00E6', u'\u007A\u0046', output) # Pha...
    output = re.sub(u'\u0069\u0066\u00F6', u'\u0070\u0046', output) # SaLone...
    output = re.sub(u'\u0069\u0066\u00FA', u'\u0075\u0046', output) # Ka...
    #--------------------------------------- Nga Thet --------------------------------------------------
    return output

def decompose(input):
    output = input
    output = re.sub(u'\u1039\u1003', u'\u00A2', output) # GaGyi...
    #output = re.sub(u'\u1039\u1011', u'\u00A6', output) # ...Hta...
    output = re.sub(u'\u1039\u1013', u'\u00A8', output) # DaOut...
    output = re.sub(u'\u1039\u1001', u'\u00A9', output) # Kha...
    output = re.sub(u'\u1039\u1011', u'\u00AC', output) # Hta...
    output = re.sub(u'\u1039\u1019', u'\u00AE', output) # Ma...
    output = re.sub(u'\u1039\u100B', u'\u00B3', output) # TaTaLin...
    output = re.sub(u'\u1039\u1012', u'\u00B4', output) # DaDway...
    output = re.sub(u'\u1039\u1002', u'\u00BE', output) # Ga...
    output = re.sub(u'\u1039\u1017', u'\u00C1', output) # BaHtaChite...
    #output = re.sub(u'\u1039\u1010', u'\u00C5', output) # ...TaWan...
    output = re.sub(u'\u1039\u1007', u'\u00C6', output) # Za...
    output = re.sub(u'\u1039\u1018', u'\u00C7', output) # Ba...
    output = re.sub(u'\u1039\u1010\u103D', u'\u00C9', output) # Twa...
    output = re.sub(u'\u1039\u1009', u'\u00D1', output) # ZaMyinZwe...
    output = re.sub(u'\u1039\u100F', u'\u00D6', output) # NaGyi...
    output = re.sub(u'\u1039\u1015', u'\u00DC', output) # Pa...
    output = re.sub(u'\u1039\u1006', u'\u00E4', output) # SaLai...
    output = re.sub(u'\u1039\u1010', u'\u00E5', output) # TaWan...
    output = re.sub(u'\u1039\u1016', u'\u00E6', output) # Pha...
    output = re.sub(u'\u1039\u1014', u'\u00E9', output) # Na...
    output = re.sub(u'\u1039\u1005', u'\u00F6', output) # SaLone...
    output = re.sub(u'\u1039\u1000', u'\u00FA', output) # Ka...
    #output = re.sub(u'\u103A\u1006', u'\u00E4', output) # SaLai...
    return output

def shape(input):
    output = input
    output = re.sub(u'\u1000\u103B\u1015\u1039', u'\u0024', output) # Kyat...
    output = re.sub(u'\u102B\u103A', u'\u003A', output) # YaCha.ShaeHtoe...
    output = re.sub(u'\u103C([\u1000\u1003\1006\u100F\u1010\u1011\u1018\u101A\u101C\u101E\u101F\u1021])\u103D',
                    u'\u003C\\1', output) # YitKyi.Swe...
    output = re.sub(u'\u103C([\u1001\u1002\1004\u1005\u1007\u100E\u1012\u1013\u1015\u1016\u1017\u1019\u101D])\u103D',
                    u'\u003E\\1', output)  # YitLay.Swe...
    output = re.sub(u'\u100D\u1039\u100D', u'\u00D7', output) # DaYin.Sint.DaYin...
    output = re.sub(u'\u100F\u1039\u100D', u'\u0040', output) # NaGyi.Sint.DaYin...
    output = re.sub(u'\u100B\u1039\u100B', u'\u00A5', output) # TaTa.Sint.TaTa...
    output = re.sub(u'\u103C([\u1000\u1003\1006\u100F\u1010\u1011\u1018\u101A\u101C\u101E\u101F\u1021])',
                    u'\u004D\\1', output) # YitKyi...
    output = re.sub(u'\u103C([\u1000\u1003\1006\u100F\u1010\u1011\u1018\u101A\u101C\u101E\u101F\u1021])([\u102D\u102E])',
                    u'\u0042\\1\\2', output) # YitKyi.Lone...
    output = re.sub(u'\u103C([\u1001\u1002\1004\u1005\u1007\u100E\u1012\u1013\u1015\u1016\u1017\u1019\u101D])([\u102D\u102E])',
                    u'\u004E\\1\\2', output) # YitLay.Lone...
    #output = re.sub(u'([\u1000-\u1021])\u103E\u103B', u'\\1\u0051', output)  # Pint...Htoe...
    #output = re.sub(u'([\u1000-\u1021])\u103B\u103E', u'\\1\u0051', output)  # Pint...Htoe...
    return output

def visual2logical(input):
    output = input
    output = re.sub(u'([\u1000-\u1021])((?:\u103B)?)((?:\u103C)?)((?:\u103D)?)((?:\u103E)?)(\u1031)',
                    '\\6\\1\\2\\3\\4\\5', output) # ThaWayHtoe...Pint/Yit/Swe/Htoe...
    output = re.sub(u'([\u1000-\u1021])\u103C', u'\u103C\\1', output)  # Yit...Byee...
    output = re.sub(u'((?:\u103C)?)\u1014((?:\u103B)?)((?:\u103D)?)((?:\u103E)?)((?:\u102F)?)((?:\u1030)?)((?:\u102C)?)((?:\u102D)?)((?:\u102E)?)',
                    '\\1\u0045\\2\\3\\4\\8\\9\\5\\6\\7', output)
    # NaPyat...1(Pint)/2(Yit)/3(Swe)/4(Htoe)/5(TCN)/6(NaCN)/7(YaCha)/8(LoneGyi)/9(LoneTinSan)...

    return output

def convert(input):
    output = input

    output = decompose(output)
    output = visual2logical(output)
    output = shape(output)
    output = replace(output)

    return output
