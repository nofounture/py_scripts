#!/bin/bash
ver_last=$(cat /alidata/www/jobs/scripts/svn_ver.txt)
echo "ver_last : $ver_last"
ver=$(svn info svn://xxxche.wicp.net/jobs |grep Revision: |cut -c11-)
echo "ver : $ver"
#let ver_last=ver-5
echo $ver > /alidata/www/jobs/scripts/svn_ver.txt

svn diff --summarize -r $ver_last:$ver svn://xxxche.wicp.net/jobs > /alidata/www/jobs/scripts/svn.txt

python /alidata/www/jobs/scripts/svn.py
/bin/bash /alidata/www/jobs/scripts/svn_commands.sh
#scp /opt/lampp/htdocs/jobs/scripts/svn_commands.sh lucky@jwall.hk:/alidata/www/jobs/scripts/svn_commands.sh