from main import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Numeric, String
from uuid import uuid4

db = SQLAlchemy(app)

# A资产标签号
# B资产名称
# C规格型号
# D生产厂商
# E供应商
# F责任人名称
# G使用人名称
# H责任部门
# I资产地点编码
# J资产地点

class Asset(db.Model):
    __tablename__ = 'assets'

    uid = Column(String, primary_key=True)  # id
    sid = Column(db.Integer)  # 序号
    id = Column(String)  # A资产标签号
    assetName = Column(String)  # B资产名称
    modelName = Column(String)  # C规格型号
    product = Column(String)  # D生产厂商
    vender = Column(String)  # E供应商
    liable = Column(String)  # F责任人名称
    user = Column(String)  # G使用人名称
    depart = Column(String)  # H责任部门
    locCode = Column(String)  # I资产地点编码
    locName = Column(String)  # J资产地点
    locCodeOld = Column(String)  # I资产地点编码 old
    locNameOld = Column(String)  # J卡特或远供 old
    clazz = Column(String)
    editor = Column(String)

    def __init__(self, row):
        self.uid = str(uuid4())
        self.id = row[0]  # A资产标签号
        self.assetName = row[1]  # B资产名称
        self.modelName = row[2]  # C规格型号
        self.product = row[3]  # D生产厂商
        self.vender = row[4]  # E供应商
        self.liable = row[5]  # F责任人名称
        self.user = row[6]  # G使用人名称
        self.depart = row[7]  # H责任部门
        self.locCode = row[8]  # I资产地点编码
        self.locName = row[9]  # J资产地点
        self.locCodeOld = ''  # I资产地点编码 old
        self.locNameOld = ''  # J卡特或远供 old
        self.clazz = ''
        self.editor = ''

    def removeLoc(self):
        # self.locCodeOld = self.locCode
        # self.locNameOld = self.locName
        self.locCode = ""
        self.locName = ""

    def setNewloc(self, code, name, clazz, editor):
        self.locCodeOld = self.locCode
        self.locNameOld = self.locName
        self.locCode = code
        self.locName = name
        self.editor = code
        self.clazz = clazz
        self.editor = editor

    def to_json(self):
        return {
            'id': self.id,  # A资产标签号
            'assetName': self.assetName,  # B资产名称
            'modelName': self.modelName,  # C规格型号
            'product': self.product,  # D生产厂商
            'vender': self.vender,  # E供应商
            'liable': self.liable,  # F责任人名称
            'user': self.user,  # G使用人名称
            'depart': self.depart,  # H责任部门
            'locCode': self.locCode,  # I资产地点编码
            'locName': self.locName,  # J资产地点
            'locCodeOld': self.locCodeOld,
            'locNameOld': self.locNameOld,
            'editor': self.editor,
            'clazz': self.clazz
        }

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


class Address(db.Model):
    __tablename__ = 'address'

    uuid = Column(String, primary_key=True)
    id = Column(String)
    name = Column(String)

    def __init__(self, name, id):
        self.uuid = str(uuid4())
        self.name = name
        self.id = id

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
