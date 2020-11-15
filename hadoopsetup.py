def hadoopset():

	if inp6 == 1:
		
		jdk = sp.getstatusoutput("jps")

		if jdk[0]==127:
			print("\t\tjdk installing")
			sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
		else:
			pass

		hadoop = sp.getstatusoutput("hadoop version")
		if hadoop[0]==127:
			sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		else:
			pass

		print()
		
		nameip=input(" \t\tEnter IP of NameNode: ")

		print()

		nameport=int(input("\t\tEnter Port No :"))
		print()

		namedir=input("\t\tEnter Directry : ")


		sp.getoutput(f"rm -rf /{namedir};mkdir /{namedir}")  

		datafile=open("/etc/hadoop/hdfs-site.xml", 'w')

		datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{namedir}</value>
</property>
</configuration>''')

		datafile.close()

		datafile1=open("/etc/hadoop/core-site.xml", 'w')

		datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{nameip}:{nameport}</value>
</property>
</configuration>''')

		datafile1.close()
		sp.getoutput("echo Y |hadoop namenode -format;echo 3>/proc/sys/vm/drop_caches;systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start namenode")
									
		print("\n\n--------------Namenode Is Started----------")

	if inp6 == 2:
		
		jdk = sp.getstatusoutput("jps")
		if jdk[0]==127:
			print("jdk installing")
			sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
		else:
			pass
		
		hadoop = sp.getstatusoutput("hadoop version")
		if hadoop[0]==127:
			sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		else:
			pass

		print()

		disk_name=input("\t\tEnter the hard disk name : ")
		print()

		storage_size=int(input("\t\tEnter hard disk size you want to share : "))
		os.system(f"pvcreate {disk_name};vgcreate user_vg {disk_name};lvcreate --size +{storage_size}G ---name user_LVM user_vg;mkfs.ext4 /dev/user_vg/user_LVM")

		print()

		dataip=input("\t\tEnter IP of NameNode : ")

		print()

		dataport=int(input("\t\tEnter Port No :"))
		print()

		datadir=input("\t\tEnter directry name you want to share : ")
		
		sp.getoutput(f"rm -rf /{datadir};mkdir /{datadir};mount /dev/user_vg/user_LVM /{datadir};df -h;echo 3 >/proc/sys/vm/drop_caches")  

		datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
		datafile.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	<!-- Put site-specific property overrides in this file. -->
	<configuration>
	<property>
	<name>dfs.data.dir</name>
	<value>/{datadir}</value>
	</property>
	</configuration>''')

		datafile.close()

		datafile1=open("/etc/hadoop/core-site.xml", 'w')
		datafile1.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
			
	<!-- Put site-specific property overrides in this file. -->
	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://{dataip}:{dataport}</value>
	</property>
	</configuration>''')

		datafile1.close()

		sp.getoutput("hadoop-daemon.sh start datanode;hadoop-daemon.sh stop datanode;hadoop-daemon.sh start datanode;systemctl stop firewalld;setenforce 0")			

		os.system("jps")			
		print("\n\n------------------Datanode Is Started--------------")
			

	if inp6 == 3 :
	
		jdk = sp.getstatusoutput("jps")
		if jdk[0]==127:
			print("jdk installing")
			sp.getoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
		else:
			pass

		hadoop = sp.getstatusoutput("hadoop version")
		if hadoop[0]==127:
			sp.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		else:
			pass
		print()

		dataip=input("\t\tEnter Ip of NameNode : ")
		print()
		dataport=int(input("\t\tEnter Port No :"))


		datafile1=open("/etc/hadoop/core-site.xml", 'w')

		datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')

		datafile1.close()			
		os.system("systemctl stop firewalld;setenforce 0")			
		print("\n\n--------------Client Service Started----------")





