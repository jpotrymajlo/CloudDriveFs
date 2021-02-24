import pyfuse3
import logging
import os
import errno
import stat

logger = logging.getLogger(__name__)

class FuseHandlers(pyfuse3.Operations):
    def __init__(self):
        super(FuseHandlers, self).__init__()
        self.hello_name = b"message"
        self.hello_inode = pyfuse3.ROOT_INODE+1
        self.hello_data = b"hello world\n"

#    async def access(self, inode, mode, ctx):
#        logger.info("access")
    
#    async def create(self, parent_inode, name, mode, flags, ctx):
#        logger.info("create")

#    async def flush(self, fh):
#        logger.info("flush")

#    async def forget(self, inode_list):
#        logger.info("forget")
    
#    async def fsync(self, fh, datasync):
#        logger.info("fsync")
    
#    async def fsyncdir(self, fs, datasync):
#        logger.info("fsyncdir")
 
    async def getattr(self, inode, ctx=None):
        entry = pyfuse3.EntryAttributes()
        if inode == pyfuse3.ROOT_INODE:
            entry.st_mode = (stat.S_IFDIR | 0o755)
            entry.st_size = 0
        elif inode == self.hello_inode:
            entry.st_mode = (stat.S_IFREG | 0o644)
            entry.st_size = len(self.hello_data)
        else:
            raise pyfuse3.FUSEError(errno.ENOENT)

        stamp = int(1438467123.985654 * 1e9)
        entry.st_atime_ns = stamp
        entry.st_ctime_ns = stamp
        entry.st_mtime_ns = stamp
        entry.st_gid = os.getgid()
        entry.st_uid = os.getuid()
        entry.st_ino = inode

        return entry

#    async def getxattr(self, inode, name, ctx):
#        logger.info("getxattr"

#    async def listxattr(self, inode, ctx):
#        logger.info("listxattr")
    
   
    async def lookup(self, parent_inode, name, ctx=None):
        if parent_inode != pyfuse3.ROOT_INODE or name != self.hello_name:
            raise pyfuse3.FUSEError(errno.ENOENT)
        return await self.getattr(self.hello_inode)
#    async def mkdir(self, parent_inode, name, mode, ctx):
#        logger.info("mkdir")
    
#    async def mknod(self, parent_inode, name, mode, ctx):
#        logger.info("mknod")

    async def open(self, inode, flags, ctx):
        if inode != self.hello_inode:
            raise pyfuse3.FUSEError(errno.ENOENT)
        if flags & os.O_RDWR or flags & os.O_WRONLY:
            raise pyfuse3.FUSEError(errno.EACCES)
        return pyfuse3.FileInfo(fh=inode)

    async def opendir(self, inode, ctx):
        if inode != pyfuse3.ROOT_INODE:
            raise pyfuse3.FUSEError(errno.ENOENT)
        return inode

    async def read(self, fh, off, size):
        assert fh == self.hello_inode
        return self.hello_data[off:off+size]

    async def readdir(self, fh, start_id, token):
        assert fh == pyfuse3.ROOT_INODE

        # only one entry
        if start_id == 0:
            pyfuse3.readdir_reply(
                token, self.hello_name, await self.getattr(self.hello_inode), 1)
        return

#    async def readlink(self, inode, ctx):
#        logger.info("readlink")
    
#    async def release(self, fh):
#        logger.info("releasedir")
    
#    async def removexattr(self, inode, name, ctx):
#        logger.info("removexattr")
    
#    async def rename(self, parent_inode_old, name_old, parent_inode_new, name_new, flags, ctx):
#        logger.info("rename")
    
#    async def rmdir(self, parent_inode, name, ctx):
#        logger.info("rmdir")
    
#    async def setattr(self, inode, attr, fields, fh, ctx):
#        logger.info("setattr")

    async def setxattr(self, inode, name, value, ctx):
        if inode != pyfuse3.ROOT_INODE or name != b'command':
            raise pyfuse3.FUSEError(errno.ENOTSUP)

        if value == b'terminate':
            pyfuse3.terminate()
        else:
            raise pyfuse3.FUSEError(errno.EINVAL)
   
#    async def statfs(self, ctx):
#        logger.info("statfs")

#    async def symlink(self, parent_inode, name, target, ctx):
#        logger.info("symlink")
    
#    async def unlink(self, parent_inode, name, ctx):
#        logger.info("unlink")
    
#    async def write(self, fs, off, buf):
#        logger.info("write")

