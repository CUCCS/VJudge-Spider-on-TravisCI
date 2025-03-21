#之前师哥通过从网页上爬去比赛链接，大部分挂题的同学都不能根据要求起名字
#并且这种方法受到密码，外界因素（如其他同学挂出来了名字类似的题目，以及太早的比赛爬不下来）
#现在改成手动输入比赛链接，只爬all_url.txt里面的比赛
import run
from selenium import webdriver
#爬取所有比赛
def get_all(url_path : str, out_path : str):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_page_load_timeout(30)  # 设置页面加载超时时间为60秒

    with open(url_path, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.rstrip("\n")
            f = open("url.txt", 'w',encoding="UTF-8").close()  # 先清空文件
            f = open("url.txt", 'w',encoding="UTF-8")
            print(f'cur_url: {line}')
            f.write(f'{line}#rank\n')
            f.write(f'{line}#rank\n') 
            f.close()
            while True:
                try:
                    run.Crawl_and_save(browser,out_path)
                    # print(f"done: {line}")
                    break
                except Exception as e:
                    print(e,"retry")

#只爬取url的比赛
def get_lastest(url : str , out_path : str):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_page_load_timeout(30)  # 设置页面加载超时时间为60秒

    f = open("url.txt", 'w',encoding="UTF-8").close()  # 先清空文件
    f = open("url.txt", 'w',encoding="UTF-8")
    f.write(f'{url}#rank\n')
    f.write(f'{url}#rank\n') 
    f.close()
    f = open(out_path, 'w',encoding="UTF-8")
    f.close()
    #这里加入了重新申请机制，防止网络问题引起中途报错
    while True:
        try:
            run.Crawl_and_save(browser,out_path)
            # print(f"done: {line}")
            break
        except Exception as e:
            print(e,"retry")

if __name__ == "__main__":
    #get_all("./url/all_url.txt","./outs/all_result.csv")
    get_all("./url/div1.txt","./outs/div1.csv")
    get_all("./url/div2.txt","./outs/div2.csv")
    get_all("./url/div3.txt","./outs/div3.csv")
    #get_lastest("https://vjudge.net/contest/695643")
