# -*- coding: utf-8 -*-

import psutil


class GlancesNetwork(object):

    def get(self):
        stats = []

        try:
            netiocounters = psutil.net_io_counters(pernic=True)
        except UnicodeDecodeError:
            return stats

        netstatus = {}
        try:
            netstatus = psutil.net_if_stats()
        except OSError:
            pass

        # Loop over interfaces
        network_new = netiocounters
        for net in network_new:
            try:
                rx = network_new[net].bytes_recv
                tx = network_new[net].bytes_sent
                cx = rx + tx
                netstat = {
                    'interface_name': net,
                    'rx': rx,
                    'tx': tx,
                    'cx': cx
                }
            except KeyError:
                continue
            else:
                # Interface status
                netstat['is_up'] = netstatus[net].isup
                # Interface speed in Mbps, convert it to bps
                # Can be always 0 on some OSes
                netstat['speed'] = netstatus[net].speed * 1048576

                stats.append(netstat)

        return stats


glances_network = GlancesNetwork()