from xml.etree.ElementTree import Element, tostring, SubElement, Comment, XML
from xml.etree import ElementTree
from xml.dom import minidom
import re
def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def snake_to_camel_case(snake_name):
    return re.sub(r'_.', lambda x : x.group()[1].upper(), snake_name)
def snake_to_camel_case(name):
    list_name = name.split('_')
    first, rest = list_name[0], list_name[1:]
    return first + ''.join(word.capitalize() for word in rest)
#".format(colJavaName=snake_to_camel_case(col), colName=col))
def getSqlCommonCondition(parentNode, columns):
    sql = Element('sql')
    sql.set('id', 'COMMON_CONDITION')
    for col in columns:
        isNotEmpty = XML("""
        <isNotEmpty >
            {colName} = {colJavaName}
        </isNotEmpty>""")
        sql.extend(isNotEmpty)
    return sql
modelJavaName = snake_to_camel_case('cae_biz_message')
columns = ['name', 'sex', 'email_box']
sqlMap = Element('sqlMap')
sqlMap.set('namespace', modelJavaName)
typeAlias = SubElement(sqlMap, 'typeAlias')
typeAlias.set('alias', modelJavaName)
typeAlias.set('type', 'com.ali.caesar.platform.foundation.entity.'+modelJavaName)
resultMap = SubElement(sqlMap, 'resultMap')
resultMap.set('id', 'RM-'+modelJavaName)
resultMap.set('class', modelJavaName)
result = [
            Element('result', property=snake_to_camel_case(col), column=col)
            for col in columns
                    ]
resultMap.extend(result)
sql = getSqlCommonCondition(sqlMap, columns)
sql = Element('sql')
sql.set('id', 'COMMON_CONDITION')
for col in columns:
    isNotEmpty = XML("""
    <isNotEmpty >
        {colName} = {colJavaName}
    </isNotEmpty>""")
    sql.extend(isNotEmpty)
sqlMap.extend(sql)
print prettify(sqlMap)
