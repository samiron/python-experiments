import io
import ftplib as ftp
import boto3

s3 = boto3.client('s3', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)


def progress_update(bytes):
    print "Bytes: %s\n" % bytes
    
#ftp = ftp.FTP('localhost', 'spaul', 'spaul') 
#myfile=io.BytesIO()
#ftp.retrbinary ('RETR b.PNG', myfile.write)
#myfile.seek(0)
#s3.upload_fileobj(myfile, 'mybucket', 'spu_test.png', Callback=progress_update, Config=boto3.s3.transfer.TransferConfig())
#myfile.close()

downloadfile = io.BytesIO()
#s3.download_fileobj('mybucket', 'spu_test.PNG', downloadfile, Callback=progress_update, Config=boto3.s3.transfer.TransferConfig())
s3.download_fileobj('mybucket', 'spu_test.PNG', downloadfile, ExtraArgs={"Range":"bytes=0-19"}, Callback=progress_update, Config=boto3.s3.transfer.TransferConfig())
downloadfile.seek(0)
ftp.storbinary ('STOR partial_downloaded.PNG', downloadfile)
downloadfile.close()

#http://stackoverflow.com/questions/36436057/s3-how-to-do-a-partial-read-seek-without-downloading-the-complete-file

ftp.close()    
input("Press Enter to continue...")
