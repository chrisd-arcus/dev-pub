export HISTTIMEFORMAT='%F %T '

#date=`date --iso-8601=seconds`
date=`date "+%Y-%m-%d_%H-%M-%S"`
string=$1

## LOCAL:
#history | gzip -c > history-$date---$string.gz
## REMOTE:
#history | gzip -c >  ~/History.dir/history-$date---$string.gz

## or BOTH if using TEE:
history | gzip -c | tee history-$date---$string.gz ~/History.dir/history-$date---$string.gz >& /dev/null




#### HELP for search:
# zgrep bowtie2 History.dir/*gz |cut -f2- -d':'|sed 's/^ *//g'|cut -f2- -d' '|sort -k1,1 -k2,2|uniq|less
### OR, if multiple search terms:
###  gzcat ~/History.dir/*gz | egrep "blastn|midline" | sed 's/^ *//g' | cut -f2- -d ' ' | sort -k1,1 -k2,2 | uniq | less
