#coding:utf-8

def GetStrFromUnicode(ustr):
        '''
        把类似u'\xca\xd3\xc6\xb5\xd7\xa5\xc8\xa1'的内容转为中文字符串
        :param ustr: u'\xca\xd3\xc6\xb5\xd7\xa5\xc8\xa1'
        :return:
        '''
        result = ustr.encode('raw_unicode_escape')
        # result = ustr.encode('unicode_escape').decode('string_escape')
        uresult = unicode(eval(repr(result)), "gbk")
        return uresult.encode('utf8')