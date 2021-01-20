import pyfuse3
import logging
import os
import errno

logger = logging.getLogger(__name__)

class FuseHandlers(pyfuse3.Operations):
    def init(self):
        super(FuseHandlers, self).__init__()
    
    async def access(self, inode, mode, ctx):
        logger.info("access")
    
    async def create(self, parent_inode, name, mode, flags, ctx):
        logger.info("create")

    async def flush(self, fh):
        logger.info("flush")

    async def forget(self, inode_list):
        logger.info("forget")
    
    async def fsync(self, fh, datasync):
        logger.info("fsync")
    
    async def fsyncdir(self, fs, datasync):
        logger.info("fsyncdir")
    
    async def getattr(self, inode, ctx):
        logger.info("getattr")
        attributes = pyfuse3.EntryAttributes()
        return attributes

    async def getxattr(self, inode, name, ctx):
        logger.info("getxattr")

    async def listxattr(self, inode, ctx):
        logger.info("listxattr")
    
    async def lookup(self, parent_inode, name, ctx):
        logger.info("lookup")
    
    async def mkdir(self, parent_inode, name, mode, ctx):
        logger.info("mkdir")
    
    async def mknod(self, parent_inode, name, mode, ctx):
        logger.info("mknod")
    
    async def open(self, inode, flags, ctx):
        logger.info("open")
        
    async def opendir(self, inode, ctx):
        logger.info("opendir")
    
    async def read(self, fh, off, size):
        logger.info("read")
    
    async def readdir(self, fs, start_id, token):
        logger.info("readdir")

    async def readlink(self, inode, ctx):
        logger.info("readlink")
    
    async def release(self, fh):
        logger.info("releasedir")
    
    async def removexattr(self, inode, name, ctx):
        logger.info("removexattr")
    
    async def rename(self, parent_inode_old, name_old, parent_inode_new, name_new, flags, ctx):
        logger.info("rename")
    
    async def rmdir(self, parent_inode, name, ctx):
        logger.info("rmdir")
    
    async def setattr(self, inode, attr, fields, fh, ctx):
        logger.info("setattr")
    
    async def setxattr(self, inode, name, value, ctx):
        logger.info("setxattr")
    
    async def statfs(self, ctx):
        logger.info("statfs")

    async def symlink(self, parent_inode, name, target, ctx):
        logger.info("symlink")
    
    async def unlink(self, parent_inode, name, ctx):
        logger.info("unlink")
    
    async def write(self, fs, off, buf):
        logger.info("write")

