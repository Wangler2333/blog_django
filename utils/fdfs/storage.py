from django.core.files.storage import Storage
# conf.settings在启动后会自动加载项目的settings
from django.conf import settings
from fdfs_client.client import Fdfs_client


class FDFSStorage(Storage):
    """
    FastDFS文件存储类，需要settings中将文件存储方式指向此类
    """

    def __init__(self, client_conf=None, base_url=None):
        """
        初始化
        :param client_conf: FastDFS服务器的client.conf文件
        :param base_url: FastDFS服务器的url地址
        """
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        """
        打开文件时使用
        :param name: 文件名字
        :param mode: 打开方式
        :return: 直接a标签指向地址，无需打开文件
        """
        pass

    def _save(self, name, content):
        """
        保存文件时使用
        :param name: 你选择上传文件的名字
        :param content: 包含你上传文件内容的File对象
        :return: FastDFS服务器上保存的文件的名字
        """

        # 创建一个Fdfs_client对象
        client = Fdfs_client(self.client_conf)

        # 上传文件到fast dfs系统中
        res = client.upload_by_buffer(content.read())

        # res = dict()
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fast dfs失败')

        # 获取返回的文件ID
        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        """
        Django判断文件名是否可用
        :param name: 文件名
        :return: False，不存在
        """
        return False

    def url(self, name):
        """
        返回访问文件的url路径
        :param name: FastDFS服务器上文件名字
        :return: 完整的访问链接
        """
        return self.base_url + name
