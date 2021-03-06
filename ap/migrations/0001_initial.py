# Generated by Django 2.0.6 on 2018-07-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AP',
            fields=[
                ('apIndex', models.AutoField(db_column='apIndex', primary_key=True, serialize=False)),
                ('basemac', models.CharField(max_length=17, unique=True)),
                ('radio_basemac_offset', models.PositiveIntegerField()),
                ('radio_basemac2', models.CharField(max_length=17)),
                ('radio_basemac5', models.CharField(max_length=17)),
                ('apname', models.CharField(max_length=128, unique=True)),
                ('profileversion', models.CharField(max_length=128)),
                ('apversion', models.CharField(max_length=128)),
                ('bootversion', models.CharField(max_length=128)),
                ('vlanId', models.PositiveIntegerField(db_column='vlanId')),
                ('vlanId1', models.PositiveIntegerField(db_column='vlanId1')),
                ('vlanId2', models.PositiveIntegerField(db_column='vlanId2')),
                ('vlanId3', models.PositiveIntegerField(db_column='vlanId3')),
                ('vlanId4', models.PositiveIntegerField(db_column='vlanId4')),
                ('lan_disable1', models.PositiveIntegerField()),
                ('lan_disable2', models.PositiveIntegerField()),
                ('lan_disable3', models.PositiveIntegerField()),
                ('lan_disable4', models.PositiveIntegerField()),
                ('forwardmode1', models.PositiveIntegerField()),
                ('forwardmode2', models.PositiveIntegerField()),
                ('forwardmode3', models.PositiveIntegerField()),
                ('forwardmode4', models.PositiveIntegerField()),
                ('portal_enable1', models.PositiveIntegerField()),
                ('portal_enable2', models.PositiveIntegerField()),
                ('portal_enable3', models.PositiveIntegerField()),
                ('portal_enable4', models.PositiveIntegerField()),
                ('apMemo', models.CharField(db_column='apMemo', max_length=128)),
                ('location', models.CharField(blank=True, max_length=512, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('binIndex', models.PositiveIntegerField(blank=True, db_column='binIndex', null=True)),
                ('apOnline', models.PositiveIntegerField(db_column='apOnline')),
                ('apStatus', models.PositiveIntegerField(db_column='apStatus')),
                ('apPreConf', models.PositiveIntegerField(db_column='apPreConf')),
                ('apUptime', models.DateTimeField(db_column='apUptime')),
                ('rogue_ap_detect', models.PositiveIntegerField()),
                ('balance_enable', models.PositiveIntegerField()),
                ('balance_mode', models.PositiveIntegerField()),
                ('users_threshold', models.PositiveIntegerField()),
                ('users_offset', models.PositiveIntegerField()),
                ('flow_threshold', models.PositiveIntegerField()),
                ('flow_offset', models.PositiveIntegerField()),
                ('dband_balance', models.PositiveIntegerField()),
                ('user_maxretries', models.PositiveIntegerField()),
                ('log_level', models.PositiveIntegerField()),
                ('local_file_level', models.PositiveIntegerField()),
                ('remote_server_level', models.PositiveIntegerField()),
                ('remote_server_addr', models.PositiveIntegerField()),
                ('remote_server_port', models.PositiveIntegerField()),
                ('log_cloud', models.PositiveIntegerField()),
                ('log_cloud_url', models.CharField(max_length=200)),
                ('check_addr', models.PositiveIntegerField()),
                ('check_switch', models.IntegerField()),
                ('apLocalIp', models.PositiveIntegerField(db_column='apLocalIp')),
                ('apGwIp', models.PositiveIntegerField(db_column='apGwIp')),
                ('acIp', models.PositiveIntegerField(db_column='acIp')),
                ('ap_flag', models.PositiveIntegerField()),
                ('portal_audit_enable', models.PositiveIntegerField()),
                ('portal_audit_ip', models.PositiveIntegerField()),
                ('portal_audit_port', models.PositiveIntegerField()),
                ('portal_audit_type', models.PositiveIntegerField()),
                ('portal_audit_key', models.CharField(max_length=8)),
                ('rtls_enable', models.PositiveIntegerField()),
                ('rtls_ip', models.PositiveIntegerField()),
                ('rtls_port', models.PositiveIntegerField()),
                ('rtls_token', models.CharField(max_length=16)),
                ('rtls_appkey', models.CharField(max_length=64)),
                ('rtls_servers', models.CharField(max_length=256)),
                ('rtls_engine', models.PositiveIntegerField()),
                ('rtls_timeout', models.PositiveIntegerField()),
                ('capwap_data_sport', models.PositiveIntegerField()),
                ('capwap_data_dport', models.PositiveIntegerField()),
                ('capwap_data_local_sport', models.PositiveIntegerField()),
                ('capwap_ac_local_ip', models.PositiveIntegerField()),
                ('binUrl', models.CharField(db_column='binUrl', max_length=1024)),
                ('saveConfig', models.PositiveIntegerField(db_column='saveConfig')),
                ('binMd5', models.CharField(db_column='binMd5', max_length=100)),
                ('updateState', models.CharField(db_column='updateState', max_length=200)),
                ('uplink_detect_switch', models.PositiveIntegerField()),
                ('uplink_detect_action', models.PositiveIntegerField()),
                ('uplink_detect_ip', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'tb_ap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='APType',
            fields=[
                ('apType', models.PositiveSmallIntegerField(db_column='apType', primary_key=True, serialize=False)),
                ('hwtype', models.CharField(max_length=128)),
                ('typeName', models.CharField(db_column='typeName', max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('wans', models.PositiveSmallIntegerField()),
                ('lans', models.PositiveSmallIntegerField()),
                ('radios', models.PositiveSmallIntegerField()),
                ('radio_basemac_offset', models.PositiveSmallIntegerField()),
                ('cpu', models.CharField(max_length=128)),
                ('testMac', models.CharField(db_column='testMac', max_length=128)),
            ],
            options={
                'db_table': 'tb_ap_type',
                'managed': False,
            },
        ),
    ]
