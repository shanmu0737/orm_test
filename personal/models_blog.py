from datetime import datetime
from mybolg import db

class Mylog(db.Model):
    """创建 日志表"""
    __tablename__ = 'mylog'
    id = db.Column(db.Integer,primary_key=True)     #主键
    sortname = db.Column(db.String(50))             #分类名称
    queue = db.Column(db.String)                    #排序

    def __init__(self,sortname,queue):
        self.sortname = sortname
        self.queue = queue

    #表现函数
    def __repr__(self):
        return '日志分类{}：名称：{}，排序：{}'.format(self.id,self.sortname,self.queue)

class Article(db.Model):
    """博客内容表"""
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)       #作者
    summary = db.Column(db.Text)        #摘要
    image = db.Column(db.Text)
    main_body =db.Column(db.Text)       #正文
    label_n = db.Column(db.String)      #标签
    is_show = db.Column(db.Boolean)     #是否显示
    is_recom = db.Column(db.Boolean)    #是否推荐
    browse_num = db.Column(db.Integer)  #浏览数量
    release_time = db.Column(db.DATETIME)   #发布时间

    def __init__(self,title,author,summary,image,main_body,label_n,is_show,
                 is_recom,browse_num,release_time=None):
        self.title = title
        self.author = author
        self.summary = summary
        self.image = image
        self.main_body = main_body
        self.label_n = label_n
        self.is_show = is_show
        self.is_recom = is_recom
        self.browse_num = browse_num
        self.release_time = release_time if release_time else datetime.now()

    #表类别和表博客之间的关联
    mylogs_id = db.Column(db.Integer,db.ForeignKey('mylog.id'))
    #类成员关系
    mylogs = db.relationship('Mylog',backref=db.backref('articles',lazy='dynamic'))

    def __repr__(self):
        return '<博客{}：标题：{}，作者：{}，标签：{}>'.format(self.id,self.title,self.author,self.label_n)

class Comment(db.Model):
    """评论表名"""
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    comm_user = db.Column(db.String)        #评论用户名
    ip = db.Column(db.Float)
    body = db.Column(db.String)             #评论内容
    comment_time = db.Column(db.DateTime)   #评论时间
    is_audit = db.Column(db.String)         #审核状态

    def __init__(self,comm_user,ip,body,is_audit,comment_time=None):
        self.comm_user = comm_user
        self.ip = ip
        self.body = body                #评论内容
        self.is_audit = is_audit        #审核状态
        self.comment_time = comment_time    #时间

    #评论表关联博客表,#表现部门表和员工表之间的关联,#外键，department表名，id
    comment_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    comments = db.relationship('Article',backref=db.backref('comments',lazy='dynamic'))

    def __repr__(self):
        return '<评论用户{}：{}>'.format(self.comm_user,self.body)