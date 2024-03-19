# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
 
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

export JAVA_HOME=/root/java-1.8.0
export HADOOP_HOME=/root/hadoop-3.3.6
export HIVE_HOME=/root/apache-hive-3.1.3-bin
export PATH=$PATH:$HADOOP_HOME/bin:$JAVA_HOME/bin:$HIVE_HOME/bin:$SQOOP_HOME/bin

export SQOOP_HOME=/root/sqoop-1.4.7
export SQOOP_CONF_DIR=$SQOOP_HOME/conf
