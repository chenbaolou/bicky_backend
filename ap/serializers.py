from rest_framework import serializers
from ap.models import AP, APType
from group.serializers import GroupSerializer

class APTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = APType
        fields = ('apType','hwtype','typeName','model','wans','lans','radios','radio_basemac_offset','cpu','testMac',)

class APSerializer(serializers.ModelSerializer):
    apType = APTypeSerializer(many=False, read_only=True)
    group = GroupSerializer(many=False, read_only=True)
    class Meta:
        model = AP
        fields = ('apIndex','basemac','radio_basemac_offset','radio_basemac2','radio_basemac5','apname',
        'profileversion','apversion','bootversion','group','vlanId','vlanId1','vlanId2','vlanId3','vlanId4',
        'lan_disable1','lan_disable2','lan_disable3','lan_disable4','forwardmode1','forwardmode2','forwardmode3','forwardmode4',
        'portal_enable1','portal_enable2','portal_enable3','portal_enable4','apMemo','location','city','binIndex','apType','apOnline',
        'apStatus','apPreConf','apUptime','rogue_ap_detect','balance_enable','balance_mode','users_threshold','users_offset',
        'flow_threshold','flow_offset','dband_balance','user_maxretries','log_level','local_file_level','remote_server_level',
        'remote_server_addr','remote_server_port','log_cloud','log_cloud_url','check_addr','check_switch','apLocalIp','apGwIp','acIp',
        'ap_flag','portal_audit_enable','portal_audit_ip','portal_audit_port','portal_audit_type','portal_audit_key','rtls_enable',
        'rtls_ip','rtls_port','rtls_token','rtls_appkey','rtls_servers','rtls_engine','rtls_timeout','capwap_data_sport',
        'capwap_data_dport','capwap_data_local_sport','capwap_ac_local_ip','binUrl','saveConfig','binMd5','updateState',
        'uplink_detect_switch','uplink_detect_action','uplink_detect_ip')
