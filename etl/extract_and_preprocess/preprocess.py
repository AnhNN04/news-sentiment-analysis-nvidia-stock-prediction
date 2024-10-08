# For news1_txt
def news_1():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
    with open('./data/raw_data/raw_news_1.txt','r',encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if 1 < (len(line)) <= 20:
                if 'January' in line:
                    date = line.replace('January','01').replace(', ','-').replace(' ','-')
                if 'February' in line:
                    date = line.replace('February','02').replace(', ','-').replace(' ','-')
                if 'March' in line:
                    date = line.replace('March','03').replace(', ','-').replace(' ','-')
                if 'April' in line:
                    date = line.replace('April','04').replace(', ','-').replace(' ','-')
                if 'May' in line:
                    date = line.replace('May','05').replace(', ','-').replace(' ','-')
                if 'June' in line:
                    date = line.replace('June','06').replace(', ','-').replace(' ','-')
                if 'July' in line:
                    date = line.replace('July','07').replace(', ','-').replace(' ','-')
                if 'August' in line:
                    date = line.replace('August','08').replace(', ','-').replace(' ','-')
                if 'September' in line:
                    date = line.replace('September','09').replace(', ','-').replace(' ','-')
                if 'October' in line:
                    date = line.replace('October','10').replace(', ','-').replace(' ','-')
                if 'November' in line:
                    date = line.replace('November','11').replace(', ','-').replace(' ','-')
                if 'December' in line:
                    date = line.replace('December','12').replace(', ','-').replace(' ','-')
                with open('./data/raw_data/preprocess_data/news_1_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(date)
            else:
                with open('./data/raw_data/preprocess_data/news_1_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(line)

# For news_2.txt:
def news_2():
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
    with open('./data/raw_data/raw_news_2.txt','r',encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if 1 < (len(line)) <= 13:
                if 'Jan' in line:
                    date = line.replace('Jan','01').replace(', ','-').replace(' ','-')
                if 'Feb' in line:
                    date = line.replace('Feb','02').replace(', ','-').replace(' ','-')
                if 'Mar' in line:
                    date = line.replace('Mar','03').replace(', ','-').replace(' ','-')
                if 'Apr' in line:
                    date = line.replace('Apr','04').replace(', ','-').replace(' ','-')
                if 'May' in line:
                    date = line.replace('May','05').replace(', ','-').replace(' ','-')
                if 'Jun' in line:
                    date = line.replace('Jun','06').replace(', ','-').replace(' ','-')
                if 'Jul' in line:
                    date = line.replace('Jul','07').replace(', ','-').replace(' ','-')
                if 'Aug' in line:
                    date = line.replace('Aug','08').replace(', ','-').replace(' ','-')
                if 'Sep' in line:
                    date = line.replace('Sep','09').replace(', ','-').replace(' ','-')
                if 'Oct' in line:
                    date = line.replace('Oct','10').replace(', ','-').replace(' ','-')
                if 'Nov' in line:
                    date = line.replace('Nov','11').replace(', ','-').replace(' ','-')
                if 'Dec' in line:
                    date = line.replace('Dec','12').replace(', ','-').replace(' ','-')
                with open('./data/raw_data/preprocess_data/news_2_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(date)
            else:
                with open('./data/raw_data/preprocess_data/news_2_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(line)


# For news_3.txt:
def news_3():
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    with open('./data/raw_data/raw_news_3.txt','r',encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if 1 < (len(line)) <= 14:
                if 'Jan' in line:
                    date = line.replace(line[:4],'2024').replace('Jan','01').replace(' ','-').replace('.-','-')
                if 'Feb' in line:
                    date = line.replace(line[:4],'2024').replace('Feb','02').replace(' ','-').replace('.-','-')
                if 'Mar' in line:
                    date = line.replace(line[:4],'2024').replace('Mar','03').replace(' ','-').replace('.-','-')
                if 'Apr' in line:
                    date = line.replace(line[:4],'2024').replace('Apr','04').replace(' ','-').replace('.-','-')
                if 'May' in line:
                    date = line.replace(line[:4],'2024').replace('May','05').replace(' ','-').replace('.-','-')
                if 'Jun' in line:
                    date = line.replace(line[:4],'2024').replace('Jun','06').replace(' ','-').replace('.-','-')
                if 'Jul' in line:
                    date = line.replace(line[:4],'2024').replace('Jul','07').replace(' ','-').replace('.-','-')
                if 'Aug' in line:
                    date = line.replace(line[:4],'2024').replace('Aug','08').replace(' ','-').replace('.-','-')
                if 'Sep' in line:
                    date = line.replace(line[:4],'2024').replace('Sep','09').replace(' ','-').replace('.-','-')
                if 'Oct' in line:
                    date = line.replace(line[:4],'2024').replace('Oct','10').replace(' ','-').replace('.-','-')
                if 'Nov' in line:
                    date = line.replace(line[:4],'2024').replace('Nov','11').replace(' ','-').replace('.-','-')
                if 'Dec' in line:
                    date = line.replace(line[:4],'2024').replace('Dec','12').replace(' ','-').replace('.-','-')
                with open('./data/raw_data/preprocess_data/news_3_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(date)
            else:
                with open('./data/raw_data/preprocess_data/news_3_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(line)

# For news_4.txt:
def news_4():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
    with open('./data/raw_data/raw_news_4.txt','r',encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if 1 < (len(line)) <= 20:
                if 'January' in line:
                    clean = line.replace('January','01').replace(', ','-').replace(' ','-')
                if 'February' in line:
                    clean = line.replace('February','02').replace(', ','-').replace(' ','-')
                if 'March' in line:
                    clean = line.replace('March','03').replace(', ','-').replace(' ','-')
                if 'April' in line:
                    clean = line.replace('April','04').replace(', ','-').replace(' ','-')
                if 'May' in line:
                    clean = line.replace('May','05').replace(', ','-').replace(' ','-')
                if 'June' in line:
                    clean = line.replace('June','06').replace(', ','-').replace(' ','-')
                if 'July' in line:
                    clean = line.replace('July','07').replace(', ','-').replace(' ','-')
                if 'August' in line:
                    clean = line.replace('August','08').replace(', ','-').replace(' ','-')
                if 'September' in line:
                    clean = line.replace('September','09').replace(', ','-').replace(' ','-')
                if 'October' in line:
                    clean = line.replace('October','10').replace(', ','-').replace(' ','-')
                if 'November' in line:
                    clean = line.replace('November','11').replace(', ','-').replace(' ','-')
                if 'December' in line:
                    clean = line.replace('December','12').replace(', ','-').replace(' ','-')
                with open('./data/raw_data/preprocess_data/news_4_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(clean)
            else:
                with open('./data/raw_data/preprocess_data/news_4_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(line)

# For news_5.txt:
def news_5():
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec']
    with open('./data/raw_data/raw_news_5.txt','r',encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        for line in lines:
            if 1 < (len(line)) <= 14:
                if 'Jan' in line:
                    date = line.replace('Jan','01').replace(', ','-').replace(' ','-')
                if 'Feb' in line:
                    date = line.replace('Feb','02').replace(', ','-').replace(' ','-')
                if 'Mar' in line:
                    date = line.replace('Mar','03').replace(', ','-').replace(' ','-')
                if 'Apr' in line:
                    date = line.replace('Apr','04').replace(', ','-').replace(' ','-')
                if 'May' in line:
                    date = line.replace('May','05').replace(', ','-').replace(' ','-')
                if 'Jun' in line:
                    date = line.replace('Jun','06').replace(', ','-').replace(' ','-')
                if 'Jul' in line:
                    date = line.replace('Jul','07').replace(', ','-').replace(' ','-')
                if 'Aug' in line:
                    date = line.replace('Aug','08').replace(', ','-').replace(' ','-')
                if 'Sep' in line:
                    date = line.replace('Sep','09').replace(', ','-').replace(' ','-')
                if 'Oct' in line:
                    date = line.replace('Oct','10').replace(', ','-').replace(' ','-')
                if 'Nov' in line:
                    date = line.replace('Nov','11').replace(', ','-').replace(' ','-')
                if 'Dec' in line:
                    date = line.replace('Dec','12').replace(', ','-').replace(' ','-')
                with open('./data/raw_data/preprocess_data/news_5_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(date)
            else:
                with open('./data/raw_data/preprocess_data/news_5_clean.txt','a',encoding='utf-8', errors='replace') as file:
                    file.write(line)

if __name__ == "__main__":
    print(f"Cleaning all raw news file from 1 to 5...")

    news_1()
    print(f"Finished file 1")
    news_2()
    print(f"Finished file 2")
    news_3()
    print(f"Finished file 3")
    news_4()
    print(f"Finished file 4")
    news_5()
    print(f"Finished file 5")

    print(f"Cleaning Finished")


            
