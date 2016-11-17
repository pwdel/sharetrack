
import urllib3, random, time
coord = [-93.2650, 44.9778];

baseUrl = "https://5fitl01xw0.execute-api.us-west-2.amazonaws.com/prod/gps-pull";
# baseUrl = "https://f5v4mh3e3d.execute-api.us-east-1.amazonaws.com/prod/tracker2";

http = urllib3.PoolManager();

while True:
   coord = [coord[0] + random.random()-0.5, coord[1] + random.random()-0.5]
   url = baseUrl + "?lat="+str(coord[1])+"&lon="+str(coord[0])+"&operation=push_location&testMode=1&time="+str(int(time.time()))
   print(url)
   r= http.request("GET", url)
   print(r.data)
   time.sleep(10)
