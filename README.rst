

yum install -y git
yum install -y python3 python3-devel python3-pip

mkdir /root/.pip
# vi /root/.pip/pip.conf
[global] 
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = https://mirrors.aliyun.com


# yum install nss-devel nspr-devel -y
# yum install -y libvirt-devel
# yum -y install gcc intltool gperf glib2-devel libcap-devel xz-devel
# yum -y install systemd-devel libsystemd-dev

# git clone https://github.com/openstack/horizon.git -b stable/rocky  --depth=1
# cd horizon
# pip3 install -r requirements.txt
# pip3 install -r test-requirements.txt


# cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py
# vi openstack_dashboard/local/local_settings.py
ALLOWED_HOSTS = ['*', ]

OPENSTACK_HOST = "172.16.197.9"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "admin"

# python3 manage.py collectstatic # 静态文件收集(js、css文件)
# python3 manage.py compress --force # 将收集的静态文件进行压缩
# python3 manage.py runserver 172.16.197.12:8000

启动报错，需要卸载掉高版本novaclient
  File "/usr/lib64/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/root/horizon/openstack_dashboard/urls.py", line 35, in <module>
    from openstack_dashboard.api import rest
  File "/root/horizon/openstack_dashboard/api/__init__.py", line 35, in <module>
    from openstack_dashboard.api import cinder
  File "/root/horizon/openstack_dashboard/api/cinder.py", line 41, in <module>
    from openstack_dashboard.api import nova
  File "/root/horizon/openstack_dashboard/api/nova.py", line 34, in <module>
    from novaclient.v2 import list_extensions as nova_list_extensions
ImportError: cannot import name 'list_extensions'
# pip3 uninstall python-novaclient
# pip3 install python-novaclient==11.0.1
ERROR openstack_dashboard.dashboards.project.cgroups.panel Call to list enabled services failed. This is likely due to a problem communicating with the Cinder endpoint. Consistency Group panel will not be displayed.
ERROR openstack_dashboard.dashboards.project.cg_snapshots.panel Call to list enabled services failed. This is likely due to a problem communicating with the Cinder endpoint. Consistency Group Snapshot panel will not be displayed.
ERROR openstack_dashboard.dashboards.project.volume_groups.panel Call to list enabled services failed. This is likely due to a problem communicating with the Cinder endpoint. Volume Group panel will not be displayed.
ERROR openstack_dashboard.dashboards.project.vg_snapshots.panel Call to list enabled services failed. This is likely due to a problem communicating with the Cinder endpoint. Volume Group Snapshot panel will not be displayed.

python-cinderclient (7.3.0)
pip3 uninstall python-cinderclient
pip3 install python-cinderclient==4.0.3
# git clone https://github.com/run4life/myplugin-ui.git
# cd myplugin-ui
# python3 setup.py build
# python3 setup.py install
# cp myplugin_ui/enabled/_31000_myplugin.py /root/horizon/openstack_dashboard/enabled/
# 重启horizon