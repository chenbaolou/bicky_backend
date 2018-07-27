"""
AP类型和AP数据模型
"""
from django.db import models


class APType(models.Model):
    """
    AP类型数据模型
    """
    apType = models.PositiveSmallIntegerField(db_column='apType', primary_key=True)
    hwtype = models.CharField(max_length=128)
    typeName = models.CharField(db_column='typeName', max_length=128)
    model = models.CharField(max_length=128)
    wans = models.PositiveSmallIntegerField()
    lans = models.PositiveSmallIntegerField()
    radios = models.PositiveSmallIntegerField()
    radio_basemac_offset = models.PositiveSmallIntegerField()
    cpu = models.CharField(max_length=128)
    testMac = models.CharField(db_column='testMac', max_length=128)

    class Meta:
        managed = False
        db_table = 'tb_ap_type'


class AP(models.Model):
    """
    AP数据类型
    """
    apIndex = models.AutoField(db_column='apIndex', primary_key=True)
    basemac = models.CharField(unique=True, max_length=17)
    radio_basemac_offset = models.PositiveIntegerField(default=2)
    radio_basemac2 = models.CharField(max_length=17, default='FF:FF:FF:FF:FF:FF')
    radio_basemac5 = models.CharField(max_length=17, default='FF:FF:FF:FF:FF:FF')
    apname = models.CharField(unique=True, max_length=128, default='')
    profileversion = models.CharField(max_length=128, default='')
    apversion = models.CharField(max_length=128, default='')
    bootversion = models.CharField(max_length=128, default='')
    group = models.ForeignKey('group.Group', models.CASCADE, db_column='groupIndex', default=999)
    vlanId = models.PositiveIntegerField(db_column='vlanId', default=1)
    vlanId1 = models.PositiveIntegerField(db_column='vlanId1', default=1)
    vlanId2 = models.PositiveIntegerField(db_column='vlanId2', default=1)
    vlanId3 = models.PositiveIntegerField(db_column='vlanId3', default=1)
    vlanId4 = models.PositiveIntegerField(db_column='vlanId4', default=1)
    lan_disable1 = models.PositiveIntegerField(default=0)
    lan_disable2 = models.PositiveIntegerField(default=0)
    lan_disable3 = models.PositiveIntegerField(default=0)
    lan_disable4 = models.PositiveIntegerField(default=0)
    forwardmode1 = models.PositiveIntegerField(default=0)
    forwardmode2 = models.PositiveIntegerField(default=0)
    forwardmode3 = models.PositiveIntegerField(default=0)
    forwardmode4 = models.PositiveIntegerField(default=0)
    portal_enable1 = models.PositiveIntegerField(default=0)
    portal_enable2 = models.PositiveIntegerField(default=0)
    portal_enable3 = models.PositiveIntegerField(default=0)
    portal_enable4 = models.PositiveIntegerField(default=0)
    apMemo = models.CharField(db_column='apMemo', max_length=128, default='')
    location = models.CharField(max_length=512, blank=True, null=True, default='')
    city = models.CharField(max_length=20, blank=True, null=True, default='')
    binIndex = models.PositiveIntegerField(db_column='binIndex', blank=True, null=True, default=1)
    apType = models.ForeignKey(APType, models.CASCADE, db_column='apType', default=1)
    apOnline = models.PositiveIntegerField(db_column='apOnline', default=0)
    apStatus = models.PositiveIntegerField(db_column='apStatus', default=0)
    apPreConf = models.PositiveIntegerField(db_column='apPreConf', default=0)
    apUptime = models.DateTimeField(db_column='apUptime', default=None, null=True)
    rogue_ap_detect = models.PositiveIntegerField(default=0)
    balance_enable = models.PositiveIntegerField(default=1)
    balance_mode = models.PositiveIntegerField(default=3)
    users_threshold = models.PositiveIntegerField(default=22)
    users_offset = models.PositiveIntegerField(default=11)
    flow_threshold = models.PositiveIntegerField(default=44)
    flow_offset = models.PositiveIntegerField(default=55)
    dband_balance = models.PositiveIntegerField(default=66)
    user_maxretries = models.PositiveIntegerField(default=77)
    log_level = models.PositiveIntegerField(default=0)
    local_file_level = models.PositiveIntegerField(default=0)
    remote_server_level = models.PositiveIntegerField(default=0)
    remote_server_addr = models.PositiveIntegerField(default=0)
    remote_server_port = models.PositiveIntegerField(default=0)
    log_cloud = models.PositiveIntegerField(default=0)
    log_cloud_url = models.CharField(max_length=200, default='syslog.ap.bdcom.com.cn:514')
    check_addr = models.PositiveIntegerField(default=0)
    check_switch = models.IntegerField(default=0)
    apLocalIp = models.PositiveIntegerField(db_column='apLocalIp', default=0)
    apGwIp = models.PositiveIntegerField(db_column='apGwIp', default=0)
    acIp = models.PositiveIntegerField(db_column='acIp', default=0)
    ap_flag = models.PositiveIntegerField(default=0)
    portal_audit_enable = models.PositiveIntegerField(default=0)
    portal_audit_ip = models.PositiveIntegerField(default=0)
    portal_audit_port = models.PositiveIntegerField(default=0)
    portal_audit_type = models.PositiveIntegerField(default=0)
    portal_audit_key = models.CharField(max_length=8, default='12345678')
    rtls_enable = models.PositiveIntegerField(default=0)
    rtls_ip = models.PositiveIntegerField(default=0)
    rtls_port = models.PositiveIntegerField(default=0)
    rtls_token = models.CharField(max_length=16, default='')
    rtls_appkey = models.CharField(max_length=64, default='')
    rtls_servers = models.CharField(max_length=256, default='')
    rtls_engine = models.PositiveIntegerField(default=0)
    rtls_timeout = models.PositiveIntegerField(default=0)
    capwap_data_sport = models.PositiveIntegerField(default=0)
    capwap_data_dport = models.PositiveIntegerField(default=0)
    capwap_data_local_sport = models.PositiveIntegerField(default=0)
    capwap_ac_local_ip = models.PositiveIntegerField(default=0)
    binUrl = models.CharField(db_column='binUrl', max_length=1024, default='')
    saveConfig = models.PositiveIntegerField(db_column='saveConfig', default=0)
    binMd5 = models.CharField(db_column='binMd5', max_length=100, default='')
    updateState = models.CharField(db_column='updateState', max_length=200, default='')
    uplink_detect_switch = models.PositiveIntegerField(default=0)
    uplink_detect_action = models.PositiveIntegerField(default=1)
    uplink_detect_ip = models.PositiveIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'tb_ap'
