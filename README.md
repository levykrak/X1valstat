# X1valstat

![2024-04-02](https://github.com/levykrak/X1valstat/assets/44068840/422d135c-cd19-4930-b1a7-437d56164cf8)

Simple tool to automaticly generate chart for x1-testnet, it generates info about previouse day

requirements:
python3
```bash
python3 -m pip install matplotlib py-cpuinfo
```

git clone https://github.com/levykrak/X1valstat.git
chmod +x gen_stats.sh

edit logrotate:

```bash
root@m25039:/etc/logrotate.d# cat rsyslog
/var/log/syslog
{
        rotate 7
        daily
        missingok
        notifempty
        delaycompress
        compress
        postrotate
                /usr/lib/rsyslog/rsyslog-rotate
        endscript
}
```

edit crontab to generate at 00:05

```bash
05 00 * * * /CUSTOM_DIRECTORY/gen_stats.sh >/dev/null 2>&1
```
