#!/usr/bin/env python3
#-*- encode:utf-8 -*-

#in some linux distributions is required to install using pip
# pip install pywinrm[kerberos]
# sys module could be uncomented in order to use CLI to pass host, login and password as arguments

# Make sure in the target windows machine the network connection type is "private", if it is "public" winrm would not get configured.
# Open command prompt and type:

# winrm qc
# winrm set winrm/config/service @{AllowUnencrypted="true"}

# Open Powershell and type:

# enable-psremoting
# set-item WSMan:\localhost\Client\TrustedHosts * # ('*' is for all hosts, you may specify the host you want)

#create 2 lists, one is the server lists, and the second the powershell commands to run on the remote hosts

import winrm, sys

def main():
	#host = sys.argv[5] #'YourWindowsHost' uncoment if you want to use it individually
	domain = sys.argv[2] #'YourDomain'
	user = sys.argv[3] #'YourDomainUser'
	password = sys.argv[4] #'YourPassword'

	hosts = open(sys.argv[1], "r") # provide list of hosts
	#cmds = open(sys.argv[2], "r") # provide list of powershell commands to run on remote host

	for host in hosts.readlines():
		session = winrm.Session(host, auth=('{}@{}'.format(user,domain), password), transport='ntlm')
		#result = session.run_cmd('ipconfig', ['/all']) # To run command in cmd
		com(host)

	hosts.close()


def com(host):
		cmds = open(sys.argv[2], "r")
		log = open(host,'w')
		for c in cmds.readlines():
			#result = session.run_ps('Get-Acl') # To run Powershell block
			result = session.run_ps(c)
			#print result.std_out
			log.writelines(result.std_out)

		log.close()
		cmds.close()


if __name__ == '__main__':
	main()
