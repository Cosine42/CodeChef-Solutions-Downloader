import requests
import os
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

username='cosine1509'
# creating the download folder
os.makedirs(username)

# function to fetch the solution and store in .txt file
def write(link,ques):
    
    
    # fetching the unique solution code
    res = requests.get(link,headers=headers)
    soup = bs(res.text,'html.parser')
    code = soup.select('.tablebox-section>table>tbody>tr>td')[0].text
            
        
    # accessing the solution content
    res = requests.get('https://www.codechef.com/viewplaintext/'+code,headers=headers)
    res.raise_for_status()
    soup = bs(res.text,'html.parser')
    answer = soup.select('pre')[0].text
    # creating the file with filename as 'questioncode_solutioncode.txt'
    file=os.path.join(username, ques+"_"+code+".txt")
    # writing contents to the .txt file
    with open(file,'w') as f:
        f.write(answer)
    print(ques+"_"+code)
 
    

# accessing the user profile page
res = requests.get('https://www.codechef.com/users/'+username,headers=headers)
res.raise_for_status()
soup = bs(res.text,'html.parser')
elems = soup.select('.rating-data-section.problems-solved>.content>article>p>span>a')
links=[]
# fetching the solution links and question codes
for e in elems:
    links.append([e['href'],e.text])

# processing each solution link
for l in links:
    f=1
    i=5
    while f==1:
        try:
            write('https://www.codechef.com'+l[0],l[1])
            f=0
        # retrying (upto 5 times) if processing somehow failed
        except:
            i-=1
            if i==0:
                break
    
    

