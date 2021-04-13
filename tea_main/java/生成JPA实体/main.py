import os
import sys
import user
import pymysql
import re
sys.path.append(r'D:\python_project\my_toolbox')
import common

config = common.Dict(**user.config())
field = re.compile(r"^\s+`(.*?)`\s+(\S+?)[\s(].*$")
pk = re.compile(r'^\s*PRIMARY KEY.*?`(\S+?)`.*,')
bean = []
fields = []
imps = []

id = None
types = {'varchar': 'String',
         'mediumtext': 'String',
         'int': 'Integer',
         'smallint': 'Integer',
         'datetime': 'Date',
         'double': 'Double',
         'float': 'Float'}

def main():

    conn = pymysql.connect(**config['mysql'])
    cur = conn.cursor()
    cur.execute("show create table %s" %config['table_name'])
    row = cur.fetchone()
    if row != None:
        
        if config.use_lombok:
            imps.append('import lombok.Getter;')
            imps.append('import lombok.Setter;')
            bean.append('@Setter')
            bean.append('@Getter')

        imps.append('import javax.persistence.Entrity;')
        imps.append('import javax.persistence.id;')
        imps.append('import javax.persistence.Table;')
        
        

        bean.append('@Entity')
        bean.append('@Table(name = "%s")' % row['Table'])
        bean.append('public class %s {' % common.to_class_name(row['Table']))
        
        sql_to_bean(row['Create Table'])
        print("\n".join(imps))
        print()
        print()
        print("\n".join(bean))


    cur.close()    
    conn.close()

def sql_to_bean(sql):
    global bean
    for i in sql.split("\n"):
        m = field.match(i)
        if m:
            fields.append((m.group(1),m.group(2)))
        m1 = pk.match(i)
        if m1:
            id = m1.group(1)
    
    
    for i in fields:
        if i[0] == id:
            bean.append('    @Id')
            if types[i[1]] == 'Integer':
                imps.append('javax.persistence.GeneratedValue;')
                imps.append('javax.persistence.GenerationType;')
                bean.append('    @GeneratedValue(strategy = GenerationType.IDENTITY)')
        if types[i[1]] == 'Date':
            if 'import java.util.Date;' not in imps:
                imps.insert(0, 'import java.util.Date;')
        bean.append('    @Column(name = "%s")' % i[0])
        bean.append('    private %s %s;' % (types[i[1]], common.to_field_name(i[0])))
        bean.append('')
    
    if not config.use_lombok:
        for i in fields:
            bean.append('    public void set%s(%s %s) {'%(common.to_class_name(i[0]), types[i[1]], common.to_field_name(i[0])))
            bean.append('        this.%s = %s;'%(common.to_field_name(i[0]), common.to_field_name(i[0])))
            bean.append('    }')
            bean.append('')
            bean.append('    public %s get%s() {'%(types[i[1]], common.to_class_name(i[0])))
            bean.append('        return %s;' % common.to_field_name(i[0]))
            bean.append('    }')
            bean.append('')
    
    bean.append('}')
if __name__ == "__main__":
    main()    
