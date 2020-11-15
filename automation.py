import os
import subprocess as sp
from hadoopsetup import *
#####add speak feature
print("\n\n")
print("\t\tWelcome To Sriw World")
#os.system("tput setaf 3")
print("\t\t--------------------")
print("\t\tI am your assistant")
print("\t\tHow can I help you")


    
while True:

	print("\n")
	#os.system("tput setaf 5")
	print("\t\tPress 1 to perform general task")
	print("\t\tPress 2 to play with docker")
	print("\t\tPress 3 to Configure Webserver")
	print("\t\tPress 4 to Launch python Interpreter inside container")
	print("\t\tPress 5 to Configure AWS Cloud")
	print("\t\tPress 6 to Implement Hadoop Concepts")
	print("\t\tPress 7 to Implement LVM Concepts")

	#os.system("tput setaf 6")
	print("\t\tPress 8 to exit")
	#os.system("tput setaf 1")
		
	inp = input("Enter your choice : ")
	inp = int(inp)	
	if inp == 1:
		print()
		print("\t\tReady to perform General task")
		print()
		print("\t\tPress 1 to know date")
		print("\t\tPress 2 to open calender")
		print("\t\tPress 3 to open firefox")
		print("\t\tPress 4 to open gedit")
		print("\t\tPress 5 to add new user")
		print("\t\tPress 6 to delete new user")
		print("\t\tPress 7 to check IP")
		print("\t\tPress 8 to Ping")		
		print("\t\tPress 9 to view all Partition")
		print("\t\tPress 10 to install a software using yum")
		print("\t\tPress 11 to uninstall a software using yum")
		print("\t\tPress 12 to move back")

		while True:
			inp1 = int(input("Enter your choice : "))
			if inp1 == 1:
				print("\t\tToday's date coming up")
				os.system("date")
			if inp1 == 2:
				print("\t\tCalender coming up")
				os.system("cal")
			if inp1 == 3:
				print("\t\tOpening firefox...Wait")
				os.system("firefox")
			if inp1 == 4:
				print("\t\tOpening gedit...Wait")
				os.system("gedit")
			if inp1 == 5:
				user_name=input("Enter the username : ")
				os.system(f"useradd {user_name};id {user_name}")
			if inp1 == 6:
				user_name=input("Enter the username To Delete : ")
				os.system(f"userdel {user_name}")
			if inp1 == 7:
				print("\t\tIp of system is : ")
				os.system("ifconfig enp0s3")
			if inp1 == 8:
				ip = input("\t\tEnter IP or Hostname you want to ping : ")
				os.system("ping {}".format(ip))
			if inp1 == 9:
				os.system("fdisk -l")
			if inp1 == 10:
				soft = input("\t\tEnter package you want to install ")
				os.system(f"yum install {soft}")
			if inp1 == 11:
				soft = input("\t\tEnter package you want to uninstall ")
				os.system(f"yum remove {soft}")
			if inp1 == 12:
				print("\t\tReach out to  me to perform general task")
				print("\t\tExit performing  General task")
				break
		
	elif inp == 2:
		print()
		print("\t\tReady to perform Docker task")
		print("\t\tPress 1 to View all images")
		print("\t\tPress 2 to View all containers")
		print("\t\tPress 3 to Pull a docker image")
		print("\t\tPress 4 to Launch a container")
		print("\t\tPress 5 to delete all container")
		print("\t\tPress 6 to move out")

		while True:
			inp2 = int(input("Enter your choice : "))

			if inp2 == 1:
				print("\t\tAll Docker Images")
				os.system('docker images')
			if inp2 == 2:
				print("\t\tAll running containers")
				os.system('docker ps')
			if inp2 == 3:
				image = input("\t\tEnter image to pull ")
				cmd = 'docker pull {}'.format(image)
				os.system(cmd)
				os.system('docker images')
			if inp2 == 4:
				image = input("\t\tEnter image to pull ")
				name = input("\t\tEnter name of container ")
				cmd = 'docker run -it --name {} {}'.format(name,image)
				print("\t\tLaunching a containers")
				os.system(cmd)
			if inp2 == 5:
				print("\t\tDeleting containers")
				os.system(f"docker rm $(docker  ps –a -q)")
			if inp2 == 6:
				print("\t\tAgain Reach out to play with docker")
				break

	elif inp == 3:
		os.system('systemctl start docker')
		name = input("\t\tEnter name of container : ")
		print()
		print('\t\tStarting Configuring WebServer')
		print()
		print()
		cmd = 'docker create -it --name {}  ubuntu'.format(name)		
		os.system(cmd)
		os.system('docker start {}'.format(name))
		os.system('docker exec -it {} apt-get update'.format(name))
		os.system('docker exec -it {} apt-get install apache2 -y'.format(name))
		os.system('docker exec -it {} apt-get install wget'.format(name))
		os.system('docker exec -it {} apt-get install net-tools'.format(name))
		os.system('docker exec -it {} wget -O /var/www/html/home.html https://sarthak-arth-storage.s3.amazonaws.com/home.html'.format(name))
		os.system('docker exec -it {} service apache2 start'.format(name))
		os.system('docker exec -it {} ifconfig eth0'.format(name))		
		print()		
		print('\t\tConfiguration of WebServer Complete')
		print()
		print()

	elif inp == 4:
		os.system('systemctl start docker')
		name = input("\t\tEnter name of container : ")
		print()
		print('\t\tInstalling Python Interpretor')
		print()
		print()
		os.system('docker create -it --name {} ubuntu'.format(name))
		os.system('docker start {}'.format(name))
		os.system('docker exec -it {} apt-get update'.format(name))
		os.system('docker exec -it {} apt-get install python3 -y'.format(name))
		os.system('docker exec -it  {} python3'.format(name))

	elif inp == 5:
		print()
		print('\t\tPress 1 to Create Key Pair')
		print('\t\ttPress 2 to Create Security Group')
		print('\t\tPress 3 to Launch Instance on AWS Cloud')
		print('\t\tPress 4 to Create EBS Volume')
		print('\t\ttPress 5 to Attach EBS Volume to EC2 Instance')
		print('\t\tPress 6 to Create S3 Bucket')
		print('\t\tPress 7 to copy files inside S3 bucket')
		print('\t\tPress 8 to create Cloudfront distribution providing S3 as Origin')
		print('\t\tPress 9 to Stop EC2-Instances')
		print('\t\tPress 10 to terminate Ec2-Instances')
		print('\t\tPress 11 to delete S3 Bucket')
		print("\t\tPress 12 to move out")

		
		while True:
			
			inp5 = int(input('Input your choice : '))
			if inp5 == 1:
				print()
				key_name = input("\t\tEnter Key Name : ")
				os.system('aws ec2 create-key-pair --key-name {}  --region us-east-1'.format(key_name))
				print()
				print()
				print('\t\tKey Pair Created.. Kindly remember the Key Pair name')
				print()
				print()

			if inp5 == 2:
				sg_name = input("\t\tEnter Security Group Name : ")
				desc = input("\t\tEnter Description : ")
				os.system('aws ec2 create-security-group --group-name  {}  --description {} --region us-east-1'.format(sg_name,desc))
				os.system('aws ec2 authorize-security-group-ingress --group-name {}  --protocol all --cidr 0.0.0.0/0 --region us-east-1'.format(sg_name))				
				print()
				print()
				print('\t\tSecurity Group Created.. Kindly remember the Security Group ID ')
				print()
				print()
	
		
			if inp5 == 3 : 
				print()
				ami = input('\t\tEnter AMI id to Launch Instance : ')
				itype = input("\t\tEnter Instance type : ")
				count = input('\t\tEnter Number of Instances to launch : ')
				sg_id = input('\t\tEnter Security Group Id to attach to the Instance : ')
				key_name = input('\t\tEnter Key to attach to ec2 Instance : ')
				os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {} --region us-east-1 '.format(ami , itype , count , sg_id , key_name))
				print()
				print()
				print('\t\tInstance Launched.. ')
				print()
				print()


			if inp5 == 4:
				print()
				az = input('\t\tEnter Availablity Zone to Create EBS Volume : ')
				ebs_size = input('\t\tEnter Size of EBS Volume :-  ')
				os.system('aws ec2 create-volume --availability-zone {} --size {} --region us-east-1'.format(az , ebs_size))
				print()
				print()
				print('\t\tEBS Volume Created. Kindly note the volume ID ')
				print()
				print()
			
			if inp5 == 5:
				print()
				ebs_vid = input('\t\tEnter EBS Volume ID to Attach to EC2 Instance : ')
				ec2_id = input('\t\tEnter EC2 Instance ID to attach EBS Volume : ')
				os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf --region us-east-1'.format(ebs_vid , ec2_id))
				print()
				print('\t\tEBS Volume Attached ')
				print()
				print()

	
			if inp5 == 6 :
				print()
				s3_name = input("\t\tEnter S3 bucket name : ")
				os.system('aws s3api create-bucket --bucket {} --region us-east-1 '.format(s3_name))
				
				print()
				print('\t\tS3 Bucket Created ')
				print()
				print()

			if inp5 == 7 :
				print()
				s3_name = input("\t\tEnter S3 bucket name : ")
				path = input('\t\tEnter Location of File or Folder To Copy :')
				os.system('aws s3 cp {} s3://{} --acl public-read'.format(path,s3_name))
				print()
				print('\t\tFiles Copied to S3 Bucket ')
				print()
				print()
			
			if inp5 == 8 :
				print()
				s3_name = input("\t\tEnter S3 bucket name : ")
				os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --region us-east-1'.format(s3_name))
				print()
				print('\t\tCloudFront Initiated ')
				print()
				print()
		
			if inp5 == 9 :
				print()
				id = input("\t\tEnter Instance Id to stop Instance")
				os.system('aws ec2 stop-instances --instance-ids {}  --region us-east-1'.format(id))
				print()
				print('\t\Instance Stopped ')
				print()
				print()
		
			if inp5 == 10 :
				print()
				id = input("\t\tEnter Instance Id to Terminate Instance : ")
				os.system('aws ec2 terminate-instances --instance-ids {} --region us-east-1'.format(id))
				print()
				print('\t\tnstance Terminated ')
				print()
				print()
			
			if inp5 == 11 :
				print()
				s3_name = input("\t\tEnter S3 bucket name to delete : ")
				os.system('aws s3 rm --recursive s3://{}'.format(s3_name))
				os.system('aws s3api delete-bucket --bucket {} --region us-east-1'.format(s3_name))
				print()
				print('\t\tBucket deleted ')
				print()
				print()
			
			if inp5 == 12:
				print("\t\tAgain Reach out to play with AWS")
				break
			
	elif inp == 6:
		print()
		print('\t\tPress 1 to Configure NameNode')
		print('\t\ttPress 2 to Configure DataNode')
		print('\t\tPress 3 for Client Services')
		print('\t\ttPress 4 to Check Cluster Report ')
		print('\t\tPress 5 to Stop NameNode')
		print('\t\tPress 6 to Stop DataNode')
		print('\t\tPress 7 to Move Back')
		print()
		
		while True:

			inp6 = int(input('Input your choice : '))
			if inp6 == 1:
				print()
				print('\t\tConfiguring NameNode.. This may take some time')
				print()
				hadoop()
				print()
				
			if inp6 == 2:
				print()
				os.system('sudo su - root')
				print('\t\tConfiguring DataNode.. This may take some time')
				print()
				hadoopset()
				print()
			
			if inp6 == 3:
				print()
				os.system('sudo su - root')
				print('\t\tConfiguring Client.. This may take some time')
				print()
				hadoopset()
				print()

			if inp6 == 4:			
				os.system("hadoop dfsadmin -report")
			if inp6 == 5:
				os.system("hadoop-daemon.sh stop datanode;jps")
			if inp6 == 6:
				os.system("hadoop-daemon.sh stop namenode;jps")
			if inp6 == 7:
				print("\t\tAgain Reach out to  configure hadoop")
				break
				

	elif inp == 7:
		print()
		print('\t\tPress 1 to convert For Static To Dynamic Volume')
		print('\t\tPress 2 to Extend Your LVM Size  ')
		print('\t\tPress 3 to  Reduce Your LVM Size')
		print('\t\tPress 4 to Remove LVM ')
		print('\t\tPress 5 to Remove Volume Group')
		print('\t\tPress 6 to Remove Physical Volume')
		print('\t\tPress 7 to Move Back')
		print()
		
		while True:

			inp7 = int(input('Input your choice : '))
			if inp7 == 1:
				static_volume=input("\t\tEnter hard disk name : ")
				print()
				
				dynamic_size =int(input("\t\tEnter size to share : "))
				print()

				user_vg=input("\t\tEnter Volume Group Name : ")
				print()

				user_lv=input("\t\tEnter Logical Volume Name : ")
				print()

				user_dir = input("\t\tEnter New Directry Name to mount Volume : ")
				os.system(f"pvcreate {static_volume};vgcreate {user_vg} {static_volume};lvcreate --size +{dynamic_size}G --name {user_lv} {user_vg};mkfs.ext4 /dev/{user_vg}/{user_lv};mkdir /user_dir;mount /dev/{user_vg}/{user_lv} /user_dir;df -h")
				print("\n\t\t----LVM Created----")
			
			if inp7 == 2:
				lv_name=input("\t\tGive Your LV Path : ")
				print()
				lv_extend_size=int(input("\t\tEnter Size to Extend in GB : "))
				print()
				os.system(f"e2fsck -ff {lv_name};lvextend --size +{lv_extend_size}G {lv_name};fsadm resize {lv_name}")
				
			if inp7 == 3:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print()
				lv_reduce_size=int(input("How much You Want To Reduce In GB : "))
				print()
				final_size=int(input("How Much Size DO You Want After Reducing :"))
				print() 
				os.system(f"umount {lv_name} {mounting_point};e2fsck -ff {lv_name};resize2fs {lv_name} {final_size}G;lvreduce --size -{lv_reduce_size}G {lv_name};resize2fs {lv_name};mount {lv_name} {mounting_point}")
		
			if inp7 == 4:			
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				os.system(f"umount -v {mounting_point};lvremove {lv_name}")
			if inp7 == 5:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				vg_name=input("Give Your VG Name : ")
				print()
				os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name}")
			if inp7 == 6:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				vg_name=input("Give Your VG Name : ")
				print()
				pv_name=input("Give Your PV Name : ")
				print()
				os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name};pvremove {pv_name}")
			if inp7 == 7:
				print("\t\tAgain Reach out to  configure hadoop")
				break


				
	elif inp == 8:
		print("\t\tSee you again")
		break
	
	else:
		print('\t\tInvalid Input')
		print('\t\tPlease Input Valid Number')	

	
