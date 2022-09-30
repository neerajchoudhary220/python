import json, webbrowser
class actions:
    def opensite(site_name):
        # file_dir = os.path.dirname(os.path.realpath('__file__'))
        # json_file = os.path.join(file_dir,'../my.json')
        with open('my.json') as f: 
            try:
                    json_data = json.load(f)
                    url = json_data['url'][site_name]
                    path = json_data['chrome']+' %s'
                    webbrowser.get(path).open(url)
            except:
                print(site_name+" is not found in your list !")
            finally:
                print(site_name+" is opening")
               
    

                

           

   
      
