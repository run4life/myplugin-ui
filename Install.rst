
# yum install -y git
# yum install nss-devel nspr-devel -y
# yum install -y libvirt-devel
# yum -y install gcc intltool gperf glib2-devel libcap-devel xz-devel
# yum -y install systemd-devel libsystemd-dev

构建horizonrpm包需要的依赖装包：
# yum install python2-django python2-django-nos python2-pycodestyle python-nose-exclude python-selenium python-anyjso python2-django-debreac python2-django-compressor python2-django-pyscss python2-XStatic python2-XStatic-* python2-scss python-django-appconf python-lesscpy python-semantic_version python-pint
# yum install python2-django-nose python-selenium python-anyjson python2-django-debreach python-XStatic-*
# yum install python2-openstackclient python2-swiftclient python2-oslo-concurrency python2-osprofiler python2-oslo-policy fontawesome-fonts python2-XStatic-Font-Awesome fontawesome-fonts-web
# yum install https://cbs.centos.org/kojifiles/packages/python-django-nose/1.4.5/1.el7/noarch/python2-django-nose-1.4.5-1.el7.noarch.rpm
# yum install http://rpmfind.net/linux/openmandriva/cooker/repository/x86_64/unsupported/release/python-selenium-3.141.0-1-omv4001.x86_64.rpm

# git clone https://github.com/openstack/horizon.git -b stable/rocky  --depth=1
# cd horizon

# cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py
# vi openstack_dashboard/local/local_settings.py
ALLOWED_HOSTS = ['*', ]

OPENSTACK_HOST = "172.16.197.130"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "admin"

# python manage.py collectstatic --noinput --clear # 静态文件收集(js、css文件)
# python manage.py compress --force # 将收集的静态文件进行压缩
# python manage.py runserver 172.16.197.12:8000

# git clone https://github.com/run4life/myplugin-ui.git
# cd myplugin-ui
# python setup.py build
# python setup.py install
# cp myplugin_ui/enabled/_31000_myplugin.py /root/horizon/openstack_dashboard/enabled/
# 重启horizon


horizon中文配置
# cd /root/svn/horizon/openstack_dashboard/
# django-admin compilemessages --locale=zh_CN
