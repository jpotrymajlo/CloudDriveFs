import pyfuse3

logger = logging.getLogger(__name__)

class FuseHandlers(pyfuse3.Operations):
    def init(self):
        super(FuseHandlers, self).__init__()
    
    async def access(inode, mode, ctx):
        logger.info("access")
    
    async def create(parent_inode, name, mode, flags, ctx):
        logger.info("create")

    async def flush(fh):
        logger.info("flush")

    async def forget(inode_list):
        logger.info("forget")
    
    async def fsync(fh, datasync):
        logger.info("fsync")
    
    async def fsyncdir(fs, datasync):
        logger.info("fsyncdir")
    
    async def getattr(inode, ctx):
        logger.info("getattr")

    async def getxattr(inode, name, ctx):
        logger.info("getxattr")

    async def listxattr(inode, ctx):
        logger.info("listxattr")
    
    async def lookup(parent_inode, name, ctx):
        logger.info("lookup")
    
    async def mkdir(parent_inode, name, mode, ctx):
        logger.info("mkdir")
    
    async def mknod(parent_inode, name, mode, ctx):
        logger.info("mknod")
    
    async def open(inode, flags, ctx):
        logger.info("open")
        
    async def opendir(inode, ctx):
        logger.info("opendir")
    
    async def read(fh, off, size):
        logger.info("read")
    
    async def readdir(fs, start_id, token):
        logger.info("readdir")

    async def readlink(inode, ctx):
        logger.info("readlink")
    
    async def release(fh):
        logger.info("releasedir")
    
    async def removexattr(inode, name, ctx):
        logger.info("removexattr")
    
    async def rename(parent_inode_old, name_old, parent_inode_new, name_new, flags, ctx):
        logger.info("rename")
    
    async def rmdir(parent_inode, name, ctx):
        logger.info("rmdir")
    
    async def setattr(indoe, attr, fields, fh, ctx):
        logger.info("setattr")
    
    async def setxattr(inode, name, value, ctx):
        logger.info("setxattr")
    
    async def statfs(ctx):
        logger.info("statfs")

    async def symlink(parent_inode, name, target, ctx)
        logger.info("symlink")
    
    async def unlink(parent_inode, name, ctx)
        logger.info("unlink")
    
    async def write(fs, off, buf):
        logger.info("write")

