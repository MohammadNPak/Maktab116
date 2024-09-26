from xml.etree import ElementTree as Et
import requests
import sqlite3


class Author:
    url = "https://thetestrequest.com/authors.xml"
    _table_name = "author"
    _db_name = "db.sqlite3"

    def __init__(self, id, name, email, avatar,
                 created_at, updated_at) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.avatar = avatar
        self.created_at = created_at
        self.update_at = updated_at

    def __repr__(self) -> str:
        return f"Author(id:{self.id},name:{self.name}...)"

    @classmethod
    def get_remote_data(cls, result_path="data.xml"):
        res = requests.get(url=cls.url)
        if res.status_code == 200:
            # print(res.text)
            with open(result_path, 'w', encoding='utf-8') as fp:
                fp.write(res.text)
                print("data has written successfully!")
        else:
            print("invalid request!")

    @classmethod
    def from_xml(cls, xml_path="data.xml"):
        tree = Et.parse(xml_path)
        root = tree.getroot()
        result = []
        for o in root.findall('object'):
            result.append(cls(
                id=o.find('id').text,
                name=o.find('name').text,
                email=o.find('email').text,
                avatar=o.find('avatar').text,
                created_at=o.find('created-at').text,
                updated_at=o.find('updated-at').text
            ))
        return result

    def save(self):
        conn = sqlite3.connect(self._db_name)
        cur = conn.cursor()
        cur.execute("insert into author (id,name,email,avatar,created_at"
                    ",update_at) values (:id,:name,:email,:avatar,:created_at,:update_at)"
                    , self.__dict__)
        conn.commit()

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect(cls._db_name)
        cur = conn.cursor()
        # CREATE TABLE IF NOT EXISTS
        cur.execute("create table if not exists author (id,name,email,avatar,created_at,update_at);")
        conn.commit()

Author.create_table()
Author.get_remote_data()
res = Author.from_xml()
for r in res:
    r.save()
    
print(res)
