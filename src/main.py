import os
import shutil
from textnode import TextNode, TextType

from generate_page import generate_page
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
pages = ["blog/glorfindel","blog/majesty","blog/tom","contact"]



def copy_contents(source, destination):
    if (not os.path.exists(source)) or (not os.path.exists(destination)):
        if not os.path.exists(destination):
            os.mkdir(destination)
        
    else:
        #print("BOTH PATHS FOUND")
        shutil.rmtree(destination)        
        os.mkdir(destination)
    
    
    
    
    def recurse(source,destination):
        if(os.path.isfile(source)):
            #print('---FILE DETECTED', source)
            file_name = os.path.basename(source)
            target_file_path = os.path.join(destination, file_name)
            #print("===> Destination", destination)

            
            shutil.copy(source, target_file_path)
            return
        else:
            
            #print('FOLDER DETECTED', source)
            
            files = os.listdir(source)
            for file in files:
                fpath = os.path.join(source, file)
                if os.path.isfile(fpath) == False:
                    #print("CREATING DIRECTORY", fpath)
                    dir = os.path.join(destination,file)
                    
                    os.mkdir(dir)
                    recurse(fpath, dir)
                else:
                    #print("FILE DETECTED:", file, source, destination)
                    #print("FILE WILL BE COPIED")
                    file_path = os.path.join(source, file)
                    recurse(file_path,destination)
                    
                
                #print('FOLDER',path)
                
        
    
    recurse(source, destination)
    
    #create htmls recursively
    recurse_content(dir_path_content, dir_path_public)
    
    
def recurse_content(source,destination):
        if(os.path.isfile(source)):            
            file_name = os.path.basename(source)
            #print('FILE SPOTTED', file_name)
            if file_name.endswith('.md'):
                new_file_name = file_name.replace('.md','.html')
                #print("ON", source)
                #print('DEST',destination)
                content_path = source
                dest_path = os.path.join(destination,new_file_name)
                generate_page(content_path, "template.html", dest_path)
            
            return
        else:
            
            
            
            files = os.listdir(source)
            for file in files:
                fpath = os.path.join(source, file)
                if os.path.isfile(fpath) == False:
                    #print("CREATING DIRECTORY", fpath)
                    dir = os.path.join(destination,file)
                    
                    #os.mkdir(dir)
                    recurse_content(fpath, dir)
                else:
                    #print("FILE DETECTED:", file, source, destination)
                    #print("FILE WILL BE COPIED")
                    file_path = os.path.join(source, file)
                    recurse_content(file_path,destination)            


def main():
    copy_contents(dir_path_static, dir_path_public)
    
    
    
if __name__ == "__main__":
    main()
    
    
