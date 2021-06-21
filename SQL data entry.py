for i in range(1,2039):
    print("INSERT INTO login_admin (userID,password,centreID) VALUES ({},'password',{});".format(i,i));