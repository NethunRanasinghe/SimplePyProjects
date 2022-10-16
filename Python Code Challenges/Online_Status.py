def online_count(status):
    count = 0
    
    for i in status.values():
        if(i.lower() == "online"):
            count+=1

    return count

online_count({'Alice': 'online', 'Bob': 'online'})