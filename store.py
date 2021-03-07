import dropbox
#sl.Asi5i_7Qrvq9gGTsOmxTdi5IhCU6s3vwmrsVlNgIGSj1Nk1lmlGJpfxb3snLwJlZRXS9Eily7AyGLpBHwoSH7qa19C3E5qKFPZ0K9veI7kZA8F4UmqzZxHxMsqWSvwCMmWU7LtI
class Uploaddropbox:
    def __init__(self,accessessTocken):
        self.accessessTocken=accessessTocken
    def upload2dropbox(self,filesrc,filedes):
        dbx=dropbox.Dropbox(self.accessessTocken)
        f=open(filesrc,'rb')
        dbx.files_upload(f.read(),filedes)

def main():
    accessessTocken="sl.AsicDl30ZBUmTUl29sUrJJlsPfMvK0-3WCIOM1T3gMSabxMOWzLgj7J0f8C2wJ1wqqRPDEQt9BaqPJf9HEi-rtxh7bIfx2RrWPG_JfbT0g0IQetNJjzsiWMWS9clFlsxmOamSUrE-Nw"
    a=Uploaddropbox(accessessTocken)
    src=input('Which file to pick')
    des=input('Where to drop')
    a.upload2dropbox(src,des)
    print('file uploaded')

main()