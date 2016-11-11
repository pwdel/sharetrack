# sharetrack
Share Tracking Demo for Kenya, Minnesota &amp; Sweden, Using Particle Asset Tracker

# Background

Better Transportation infrastructure in developing countries improves the efficiency and speed of the transfer of goods and people while reducing the unit cost which favors growth of the country.  Poor infrastructure, particularly highway and road infrastructure, as well as institutional finance problems mean that roads in developing countries will continue to be risky, which also entails that the insurance industries and overall economies will not grow at their full potential rate.  

Being able to track assets such as trucks, cargo bicycles or other transportation methods via a cellular-data monitoring GPS asset trackers opens up an entire world of possibilities for economic growth.  Apps and visualizations can be built using this technology which decrease risks of purchasing, using and renting transportation assets.  Much as increased mobile phone penetration increases productivity[1], internet-connected devices can do the same.


## Transportation Issues & Opportunities

### Transportation Issues

Traffic jams, potholes and accidents are huge problems on the road in developing nations, particularly in either dense city or remote areas in Kenya, and Africa overall.

![Traffic Jam](/../master/images/trafficjam.jpg?raw=true "Traffic Jam")

![Potholes](/../master/images/potholes.jpg?raw=true "Potholes")

![Truck Crash](/../master/images/truckcrash.jpg?raw=true "Truck Crash")

### Transportation Opportunities

While the above problems represent major issues in developing nations, one opportunity that exists is that there tend to be significant labor forces which are looking for work, temporary labor forces, and a large amount of that work is in the transportation and logistics sector.

For example, in this picture below, a bicycle is shown which was used to transport wood for heating in a smaller city in Kenya.

![Bicycle Wood Transportation](/../master/images/bikewood.jpg?raw=true "Bicycle Wood Transportation")

In other countries, such as China, large amounts of recycling and lightweight goods can be seen to be transported by bicycle for lower income citizens to use to generate income.

![Bicycle Bottle Transportation](/../master/images/bottletransport.png?raw=true "Bicycle Bottle Transportation")

In a place like Sweden, or various countries in Europe, you can actually find Cargo Bicycles as a specific service which are used today.  This is essentially a more developed version of transport that has been co-opted from developing countries into more developed countries as the bicycling culture has grown and people have attempted to innovate ways to integrate bicycling and transportation.

![Cargo Bike](/../master/images/cargobike.png?raw=true "Cargo Bike")

![Move Bikes Now](/../master/images/movebikesnow.png?raw=true "Move Bikes Now")

![Move By Bike Back](/../master/images/movebybikeback.png?raw=true "Move By Bike Back")

![Move By Bike Side](/../master/images/movebybikeside.png?raw=true "Move By Bike Side")


## Hardware Overview ##

### Particle Electron ###

The Particle Electron is an open-source cellular data prototyping platform which allows individuals to build Internet-Enabled Sensing Applications quickly and easily.  Particle.io is a company which began in Minneapolis, Minnesota as a hobbyist electronics platform, and has expanded to serve prototypers around the world due to its high ease of use and cloud integration.

Basically, the way to work with Particle.io is to use an IDE which is similar to the Arduino IDE to write firmware which goes on the Particle Electron device.  This firmware is written in C++.  There are pre-written commands, including, "publish()" which allows one to publish whichever data that was captured to the Particle cloud platform.

#### Why Particle?  Why Not Just Arduino?  ####

While you can purchase an Arduino cellular shield, and a variety of different components for Arduino which allow you to build a GPS reporting device from scratch, we have built this particular tech stack with ease of prototyping in mind while balancing customization - e.g. we were willing to pay more for components which were already available, while allowing us to put the data anywhere we wanted to be able to focus on building a cooler data visualization, or to be able to fork the data visuzalization and build superior apps on the web in the future.  In short, we wanted to spend the least amount of time on the hardware that we thought we could, while still delivering a fast way to put data on the web.

![Particle Electron World Coverage Map](/../master/images/worldcoveragemap.png?raw=true "Particle Electron World Coverage Map")

### GPS Shield with Antenna vs Without Antenna ###

![10 Meter Clustering With Antenna](/../master/images/map10m.png?raw=true "10 Meter Clustering With Antenna")

![50 Meter Clustering With Antenna](/../master/images/map50m.png?raw=true "50 Meter Clustering With Antenna")

## Software Overview ##

Particle WebHooks
http://www.webhooks.org

GeoJSon
http://geojson.org/

Amazon Lambda
https://aws.amazon.com/lambda/

Mapbox
https://www.mapbox.com 


## Reference ##

[1] http://www.gsma.com/publicpolicy/wp-content/uploads/2012/11/gsma-deloitte-impact-mobile-telephony-economic-growth.pdf
