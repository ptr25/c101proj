import dropbox
import os 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for (root,dirs,files) in os.walk(file_from):
             print (root)
             print (dirs)
             print (files)
             relativePath = os.path.relpath(local_path,file_from)
             dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path,'rb') as f :
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
      

def main():
    access_token = '8iJVa0jHfwYAAAAAAAAAAVhWoz7nIfqS-wqYw2lfQg3auednfJRfB7hlnNMa0rsw'
    transferData = TransferData(access_token)
  

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()

