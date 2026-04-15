from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

# Many-to-Many relationship between Files and Tags
file_tags = Table('file_tags', Base.metadata,
    Column('file_id', Integer, ForeignKey('files.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    path = Column(String, unique=True, nullable=False)
    size = Column(Integer)
    file_type = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    tags = relationship("Tag", secondary=file_tags, back_populates="files")

class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)
    
    files = relationship("File", secondary=file_tags, back_populates="tags")

class Rule(Base):
    __tablename__ = 'rules'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    condition_type = Column(String)  # e.g., 'extension', 'content', 'size'
    condition_value = Column(String)
    action_type = Column(String)     # e.g., 'move', 'copy', 'tag'
    action_value = Column(String)
    priority = Column(Integer, default=0)
    is_active = Column(Integer, default=1)

class AIDecision(Base):
    __tablename__ = 'ai_decisions'
    
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    suggestion = Column(String)  # JSON string of AI suggestion
    user_action = Column(String) # 'accept', 'reject', 'modify'
    correction = Column(String)  # JSON string of user correction if any
    confidence = Column(Integer) # scaled 0-100
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class ActionHistory(Base):
    __tablename__ = 'action_history'
    
    id = Column(Integer, primary_key=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    action_type = Column(String) # 'move', 'rename', 'copy'
    src_path = Column(String)
    dest_path = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    is_undone = Column(Integer, default=0)
