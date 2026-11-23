# Playable Entities

# Interactive embodied agents

We've created a range of interactive agents to address different training needs, like object tracking, autonomous driving, indoor/outdoor navigation, and drone tasks. Researchers can easily choose the agent types and environments they need for training. Our platform covers six main types of agents: virtual humans, animals, cars, motorcycles, and drones.

Each agent type shares most API interfaces, including control of movement, navigation, and texture adjustments. Plus, we are developing interaction features among agents.

# Showcase of different agents

## Human Character 🚶🏻‍♂️🚶🏻‍♀️

 A diverse range of mesh bodies for virtual characters are used to construct rich and highly realistic environments. These virtual characters can be employed to create dense crowds and simulate real urban scenes, and each character can be controlled and randomly change appearance through our API interfaces.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/770c9d95-2e0b-4b80-914d-4233b5c02b32/8053ac76164eb85556855d05dacea84.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K724F5Q%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2qTsMC28Y3wq3KBQkuPYTXns4IFWNWGu6vcrmv8XNhAIgRdcA0VlWjaz%2Bpacc4i87wIQ21EeLrpNBxMrotxUI1X8q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAfVqQwT3lnUM0CeDCrcAzcY6%2BpkZEwCEVynu9ALNs69zjv6OoJLLhQAdf%2FRT33g5Mj4u2zB2pUT3QiHzWAmz9sEQGH19v3NFSQCyswTsYQV2iWFfqIwsfhrsFufpkr4hYJmGPnLuWhwfCq8%2FMCpcN9kWknZGXzhJSExmZwjyL4CcXIiZdgGmk4vrn5XnXskJb2iOqc90Or1d9RIYelBwzLthDTWkKveTOtl%2FAO2JyQCQAbBUGXRpsmjxiyiaOwk4lIRjLIB17207iI3lGRl53751%2FX%2B1lG%2FFtj%2FVbk89qchOoJUdamls8xPH%2BmstfTg3FLyapGjlgmm1BAoZWuJMw8%2FNg40SQ1PMYRGt1aQpoC%2B3%2Fc1fIBfR%2F6Y5ygucVhmlJ5jQI7s7v%2BK5POhpD4efjJeR%2B2YafoikOBCjRvryJPOzBPkucHRsOeeiXPr%2BZt6K4z01nMgeqkq31v76gYqRe7F6vpmcEXl7gJhEgpiEmeTwV%2Fg3qh0jOu7MFdeeuZ7dYpAQUrjUStR%2BGtBpmb5gWeEqLz7A02BvhcrKM%2BpMqmGkovl2SxPMdE9K9YHdY%2B57CU8xmvC%2FeIB1bdo3GHF5Z8ddqJBgYlFrQ3stm%2BcRFlt9AnSTrzDYV7HaVgKiM%2BN6Y7JJMieLo2CmMJcML%2BUj9gGOqUBZOUBS6Sd12rZYhv31hNz0eIDLHN5skCrRppzGWnmK4ecym6VsdaDoUE3W1mc6dh%2Bl%2F1xabnVmawMPkRGti0BW3p2cMTM7Up%2BTh0T9rWSpSLarSmh1n07fzxn1NEJknL99BkQ18HcDKS%2Bc1rqxNjIjOnuNXuD17pRfccsWTOyTQcEX90iqxufzW6bFI86yJ4Vrcs5Ks%2Fh%2Fe3uifxzv0b7U9T2XJ%2Fe&X-Amz-Signature=602498f9360754c77300c2085d09a352bc9491205e58ec4b76bb4628c02fcd9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


## Animals 🐘 🐕 🐎 🐧 🐢 🐖 🐏 🐂


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/32bd9b38-56d3-4d61-898f-a0b7c8149fbf/bbf0fa8c2237b1140eb85a8bcd25fcb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K724F5Q%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2qTsMC28Y3wq3KBQkuPYTXns4IFWNWGu6vcrmv8XNhAIgRdcA0VlWjaz%2Bpacc4i87wIQ21EeLrpNBxMrotxUI1X8q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAfVqQwT3lnUM0CeDCrcAzcY6%2BpkZEwCEVynu9ALNs69zjv6OoJLLhQAdf%2FRT33g5Mj4u2zB2pUT3QiHzWAmz9sEQGH19v3NFSQCyswTsYQV2iWFfqIwsfhrsFufpkr4hYJmGPnLuWhwfCq8%2FMCpcN9kWknZGXzhJSExmZwjyL4CcXIiZdgGmk4vrn5XnXskJb2iOqc90Or1d9RIYelBwzLthDTWkKveTOtl%2FAO2JyQCQAbBUGXRpsmjxiyiaOwk4lIRjLIB17207iI3lGRl53751%2FX%2B1lG%2FFtj%2FVbk89qchOoJUdamls8xPH%2BmstfTg3FLyapGjlgmm1BAoZWuJMw8%2FNg40SQ1PMYRGt1aQpoC%2B3%2Fc1fIBfR%2F6Y5ygucVhmlJ5jQI7s7v%2BK5POhpD4efjJeR%2B2YafoikOBCjRvryJPOzBPkucHRsOeeiXPr%2BZt6K4z01nMgeqkq31v76gYqRe7F6vpmcEXl7gJhEgpiEmeTwV%2Fg3qh0jOu7MFdeeuZ7dYpAQUrjUStR%2BGtBpmb5gWeEqLz7A02BvhcrKM%2BpMqmGkovl2SxPMdE9K9YHdY%2B57CU8xmvC%2FeIB1bdo3GHF5Z8ddqJBgYlFrQ3stm%2BcRFlt9AnSTrzDYV7HaVgKiM%2BN6Y7JJMieLo2CmMJcML%2BUj9gGOqUBZOUBS6Sd12rZYhv31hNz0eIDLHN5skCrRppzGWnmK4ecym6VsdaDoUE3W1mc6dh%2Bl%2F1xabnVmawMPkRGti0BW3p2cMTM7Up%2BTh0T9rWSpSLarSmh1n07fzxn1NEJknL99BkQ18HcDKS%2Bc1rqxNjIjOnuNXuD17pRfccsWTOyTQcEX90iqxufzW6bFI86yJ4Vrcs5Ks%2Fh%2Fe3uifxzv0b7U9T2XJ%2Fe&X-Amz-Signature=39877201d43be0f7ac98902ab6607eb26c49bf8a7e432a2ec05f11ed2dfecf33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Vehicle 🏍️ 🚗

We also have developed various types of vehicles including cars and motorcycles. These can be utilized for additional tasks such as autonomous driving and simulating dynamic traffic scenes.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/1af0dd08-c87e-4614-be43-0f1196431928/e2b28bdef79dd1988b8a29621e91b8c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634TAASFU%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FHbddxRqVWuyKny0X0ExQfAFOWthFTAyTfUXScdG8MAIhALD1hW6V5NR2PLdpa%2FtzirSVbh4OU5Mj7cpcHX5L254HKv8DCG4QABoMNjM3NDIzMTgzODA1Igzf4ypD76RGNFSdoWEq3AOBvC%2B5ZE0s6xD9zr2c5wltwDgXXrlvWR46y0Ooi%2BjyWtnNre005fKGDgqPjaBQe3mElXscGQEnaZvwaFNPZcpgE8Of8t5I2NXNRUxjkLq1iqoAgdcAbmNZEFMULYzEHApcRtPAWCymrs0p78FgJYFzeHRbkdttWL%2BrKO6paFSeyV0YlQXXfDnTAEegAXJXfakWq5bbYIZ9XTI3LRj%2BzhMUAjNkDidr5k8x%2FCMuph4U%2FwypnvYkZ987KHxTwzW5HG%2BSr5hXIXb66JDv7OZBn8qq%2Bt1RIYRxkSO8FsRrlz4%2BOGsZuxxPKqhGnFFoLxp5ubB8TpBxswAlt0EP%2BO%2FrCvShGNvhTW4EICpjokCQl49%2BvF9tU1a2F6RhEXnDiiN%2FWlDiUFeSr2mBkfVKgApv8jQysrwtZ376b1%2BCU1edaYIO9GvsZR6xQlYaM0dCbF%2F7oqbksfuvx7wbykwefplzk%2BZBtS%2BC%2BqvIFlEr37IgthWhOzo6TGPzzR3IJG25XNP7EjO2WDAcJTXk11IZbw8W22NyEKWaLTLne4I3ZhF9Gr6WLjOHsQN1X7EdI1xGnxIjkOGy%2Baqgovyb5sJxOtEtyJk7UJUDdWoKG3ABX67WUzAaerMWTBMnNn3YR1ObWTDwlI%2FYBjqkAXP8bRVr5uSRekPUEJjLs37oY01zs8PuK%2FyeNyFl8gtS2b2leRpn8qsIRrJtMyQVdS%2Bl07IAFu40Q0oHjPsoz5fV70fjxkwjst27vleg6J%2B%2FzaXIteUug1dPphUGJAGTF3%2Bp4xsiVPh2UTLYVewVqfGZjDY9gZeyWyyqh1GDcbZbMOSPLNPtBxu%2FJ8OCGrDeZ8lO4arx8FN6QS3ohrFvjszq4IpJ&X-Amz-Signature=b4c8b7cc7294d58318fbff332092ede2aa23caea14f637338009deec2adcbb4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

💡Please note that, in the latest UE5 version, to support more realistic chaos system, each vehicle has its own class name, set_app cannot change the appearance anymore. If you want to use another vehicle, please spawn a new instance vehicle.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/de38a37d-fff1-461b-bd64-0996a1f1777c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGMNOZF4%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAX0XUtBlevlOJhZEKRwYzelpmYbVE8egvOWY%2FFzIxm2AiBHO6fdjFesV9SVKDnxsNrZKoGJ7bqm5LzeVHeyqAo%2B8ir%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMfneorNM5OURTumt9KtwDOtuSNSmOImgRyYj1gOPcOSqP0KgIUQGu234TEMQI4FrZkTDBKgdo9%2Bwa7EcXA1XXgK9GfNG9tiLVqtIEareP%2Fice2tluxKj%2FNze5Bx84B%2BlRDa7rIL9cq42UXrSuKXJpd4nLRNJUoWarXbf7%2BTAhUcChQiSArpj8RwwdjssBo5UYoQfLf6HKxDkgo4YuMcshOIzY%2FqVrFnqT%2FleXTA5CAv6vbAvL0gIwb8v3ooX2T5sX0oqd0kP0xYwcY2NmkZojgWyQxlMS7Q3CWeozt8XvBC5V14g%2Fag1t%2FayvT4AKjRFUpFKg3zm3mamQ15dmEHxT9jbAua%2BvRygaku5aQHCIEz2eZfIuc5lsesE0KQlsm5E1o9Klyr59MBq9TmtSS8kzCAEx7cMd685f8FclGdim%2FNEfZAScN%2F9q7FETCUCaCs41Q1YdZdkV%2B9%2BpwK6%2BOaCD0fo13SCzuYXmKBXynZ%2BbRSUfFFSpR4wxfLySzlA1nkjCxfjpLGm30Wtb%2B2agewmzPSGfALp40wvNNvz5XmThCGZYVqwH3LCp9O8DAfWcoQVWlR36so6j8fJOyO5bZ6am8y3mny3SKsozWj55NgHQDMzJUzbcTBREoZ9I6fHTEekGiLaW1DYyF6%2BITRYwqZWP2AY6pgGwDrgPONxAp10u7a5BIpbi3CJG%2B4TKWH8E%2B5Z9Q0eim3sc1mJhfNxNb6wZby4TqeY%2FrPRuQkqLp4i610J%2BfU72SI%2FbOJqQin3NLPFLX7JRzw69UxWmvh8R0nTFG66ljY8c5j8nY6DKGWlD1UDZJ02cpfQ96bIlOKfZEWi0Yc3B7Adf7KO%2FO43mTuJ1%2F9S7MQMDak9fvHjazZWaRPgbWgqxWkKObwz0&X-Amz-Signature=bf71139cfd92de87492a01f2095db3f843be7c2fe33b89365dcadf8dfa2cd574&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Drone 🛩️

The drone can be controlled like vehicles through our APIs. It can be used for multi-agent collaboration or anomaly detection tasks, etc.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/2f7a9d4e-01b8-45b6-81fe-0c75efbda3f4/6bb42da16d76f3d2235b7176c6acb4a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K724F5Q%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2qTsMC28Y3wq3KBQkuPYTXns4IFWNWGu6vcrmv8XNhAIgRdcA0VlWjaz%2Bpacc4i87wIQ21EeLrpNBxMrotxUI1X8q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAfVqQwT3lnUM0CeDCrcAzcY6%2BpkZEwCEVynu9ALNs69zjv6OoJLLhQAdf%2FRT33g5Mj4u2zB2pUT3QiHzWAmz9sEQGH19v3NFSQCyswTsYQV2iWFfqIwsfhrsFufpkr4hYJmGPnLuWhwfCq8%2FMCpcN9kWknZGXzhJSExmZwjyL4CcXIiZdgGmk4vrn5XnXskJb2iOqc90Or1d9RIYelBwzLthDTWkKveTOtl%2FAO2JyQCQAbBUGXRpsmjxiyiaOwk4lIRjLIB17207iI3lGRl53751%2FX%2B1lG%2FFtj%2FVbk89qchOoJUdamls8xPH%2BmstfTg3FLyapGjlgmm1BAoZWuJMw8%2FNg40SQ1PMYRGt1aQpoC%2B3%2Fc1fIBfR%2F6Y5ygucVhmlJ5jQI7s7v%2BK5POhpD4efjJeR%2B2YafoikOBCjRvryJPOzBPkucHRsOeeiXPr%2BZt6K4z01nMgeqkq31v76gYqRe7F6vpmcEXl7gJhEgpiEmeTwV%2Fg3qh0jOu7MFdeeuZ7dYpAQUrjUStR%2BGtBpmb5gWeEqLz7A02BvhcrKM%2BpMqmGkovl2SxPMdE9K9YHdY%2B57CU8xmvC%2FeIB1bdo3GHF5Z8ddqJBgYlFrQ3stm%2BcRFlt9AnSTrzDYV7HaVgKiM%2BN6Y7JJMieLo2CmMJcML%2BUj9gGOqUBZOUBS6Sd12rZYhv31hNz0eIDLHN5skCrRppzGWnmK4ecym6VsdaDoUE3W1mc6dh%2Bl%2F1xabnVmawMPkRGti0BW3p2cMTM7Up%2BTh0T9rWSpSLarSmh1n07fzxn1NEJknL99BkQ18HcDKS%2Bc1rqxNjIjOnuNXuD17pRfccsWTOyTQcEX90iqxufzW6bFI86yJ4Vrcs5Ks%2Fh%2Fe3uifxzv0b7U9T2XJ%2Fe&X-Amz-Signature=84ba0d3af7ebfe9a3a985e30d3985bc6251e0f27a36468a61cee59df55633def&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


## Mobile Robot 🤖


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/5cadb75c-89b0-4d17-8657-cd66a684b79b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K724F5Q%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2qTsMC28Y3wq3KBQkuPYTXns4IFWNWGu6vcrmv8XNhAIgRdcA0VlWjaz%2Bpacc4i87wIQ21EeLrpNBxMrotxUI1X8q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAfVqQwT3lnUM0CeDCrcAzcY6%2BpkZEwCEVynu9ALNs69zjv6OoJLLhQAdf%2FRT33g5Mj4u2zB2pUT3QiHzWAmz9sEQGH19v3NFSQCyswTsYQV2iWFfqIwsfhrsFufpkr4hYJmGPnLuWhwfCq8%2FMCpcN9kWknZGXzhJSExmZwjyL4CcXIiZdgGmk4vrn5XnXskJb2iOqc90Or1d9RIYelBwzLthDTWkKveTOtl%2FAO2JyQCQAbBUGXRpsmjxiyiaOwk4lIRjLIB17207iI3lGRl53751%2FX%2B1lG%2FFtj%2FVbk89qchOoJUdamls8xPH%2BmstfTg3FLyapGjlgmm1BAoZWuJMw8%2FNg40SQ1PMYRGt1aQpoC%2B3%2Fc1fIBfR%2F6Y5ygucVhmlJ5jQI7s7v%2BK5POhpD4efjJeR%2B2YafoikOBCjRvryJPOzBPkucHRsOeeiXPr%2BZt6K4z01nMgeqkq31v76gYqRe7F6vpmcEXl7gJhEgpiEmeTwV%2Fg3qh0jOu7MFdeeuZ7dYpAQUrjUStR%2BGtBpmb5gWeEqLz7A02BvhcrKM%2BpMqmGkovl2SxPMdE9K9YHdY%2B57CU8xmvC%2FeIB1bdo3GHF5Z8ddqJBgYlFrQ3stm%2BcRFlt9AnSTrzDYV7HaVgKiM%2BN6Y7JJMieLo2CmMJcML%2BUj9gGOqUBZOUBS6Sd12rZYhv31hNz0eIDLHN5skCrRppzGWnmK4ecym6VsdaDoUE3W1mc6dh%2Bl%2F1xabnVmawMPkRGti0BW3p2cMTM7Up%2BTh0T9rWSpSLarSmh1n07fzxn1NEJknL99BkQ18HcDKS%2Bc1rqxNjIjOnuNXuD17pRfccsWTOyTQcEX90iqxufzW6bFI86yJ4Vrcs5Ks%2Fh%2Fe3uifxzv0b7U9T2XJ%2Fe&X-Amz-Signature=686d0f3e2cfd13509782f705fb449db4a4ddcc3b553ccac7547f0b6528c89f8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


## Pickable Object 🧸

human character could use set_pickup to pick/drop the item, researchers could use api to set them anywhere in the map and use set_app to change its appearance. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/55e42301-d67e-4239-ad5b-9daaabf6aa3a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K724F5Q%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2qTsMC28Y3wq3KBQkuPYTXns4IFWNWGu6vcrmv8XNhAIgRdcA0VlWjaz%2Bpacc4i87wIQ21EeLrpNBxMrotxUI1X8q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDAfVqQwT3lnUM0CeDCrcAzcY6%2BpkZEwCEVynu9ALNs69zjv6OoJLLhQAdf%2FRT33g5Mj4u2zB2pUT3QiHzWAmz9sEQGH19v3NFSQCyswTsYQV2iWFfqIwsfhrsFufpkr4hYJmGPnLuWhwfCq8%2FMCpcN9kWknZGXzhJSExmZwjyL4CcXIiZdgGmk4vrn5XnXskJb2iOqc90Or1d9RIYelBwzLthDTWkKveTOtl%2FAO2JyQCQAbBUGXRpsmjxiyiaOwk4lIRjLIB17207iI3lGRl53751%2FX%2B1lG%2FFtj%2FVbk89qchOoJUdamls8xPH%2BmstfTg3FLyapGjlgmm1BAoZWuJMw8%2FNg40SQ1PMYRGt1aQpoC%2B3%2Fc1fIBfR%2F6Y5ygucVhmlJ5jQI7s7v%2BK5POhpD4efjJeR%2B2YafoikOBCjRvryJPOzBPkucHRsOeeiXPr%2BZt6K4z01nMgeqkq31v76gYqRe7F6vpmcEXl7gJhEgpiEmeTwV%2Fg3qh0jOu7MFdeeuZ7dYpAQUrjUStR%2BGtBpmb5gWeEqLz7A02BvhcrKM%2BpMqmGkovl2SxPMdE9K9YHdY%2B57CU8xmvC%2FeIB1bdo3GHF5Z8ddqJBgYlFrQ3stm%2BcRFlt9AnSTrzDYV7HaVgKiM%2BN6Y7JJMieLo2CmMJcML%2BUj9gGOqUBZOUBS6Sd12rZYhv31hNz0eIDLHN5skCrRppzGWnmK4ecym6VsdaDoUE3W1mc6dh%2Bl%2F1xabnVmawMPkRGti0BW3p2cMTM7Up%2BTh0T9rWSpSLarSmh1n07fzxn1NEJknL99BkQ18HcDKS%2Bc1rqxNjIjOnuNXuD17pRfccsWTOyTQcEX90iqxufzW6bFI86yJ4Vrcs5Ks%2Fh%2Fe3uifxzv0b7U9T2XJ%2Fe&X-Amz-Signature=88699c4deabb554bc2339388f0e195e79e716b4ad8fa84a23ca4f7436d5a3f19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# APIs: 

We utilize the BluePrint Function in Unreal Engine to construct these APIs for controlling the agent. Developers could directly call them via UnrealCV in the built-in console or Python code, following the UnrealCV command system:

```python
vbp [obj_name] [func_name] [arg1] [arg2] …
```

obj_name is the name of the instance of the entity, such as bp_character_2

func_name is the name of the blueprint function, such as nav_to_object

arg  is the input parameter for the blueprint function, such as the goal location coordinates. 


> 💡The following linked pages detail the Blueprint APIs for each type of playable entity


Class Name：BP_Character_C 

New added animation (lie down, climb, crouch, slide, etc)

vbp {instance_name} {bp_function} {args 1} {args2}…

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Navmesh and AI-controller built-in plugin to automatically control its movement to reach the goal via the shortest path. (The goal has to be reachable in the environment.) |
| nav_random | {radius} {loop} | { ”random_location”:  “X=0.00 Y=0.00 Z=0.00” } | control agent randomly wandering around. Agent randomly selects a point within its own radius range for navigation. The loop parameter controls whether continuous navigation is performed.（True for continuous navigation). Return with the randomly sampled location. |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~19 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |
| generate_nav_goal | {radius} | { ”nav_goal”: “X=0.00 Y=0.00 Z=0.00” } | generate a reachable goal location around the agent radius, return the location. |
|  |  |  |  |
| get_hit |  | { ”hitresult”: “true(or false)” } | get the hit flag(with other target or static object) of the agent object, return true or false. |
| get_speed |  | { ”speed”: “0.000” } | get the agent’s linear velocity, return value |
| get_angle |  | { ”angle”: “0.000” } | get the agent’s angular velocity, return value |
|  set_jump |  |  | The agent displays a jumping animation, demonstrating a crossing motion when encountering obstacles that can be overcome. |
| set_crouch |  |  | The agent demonstrates a crouching animation, which, when paired with the set_move action, enables a crouching walking animation. |
| set_liedown | {Direction_Frontback} {Direction_Rightleft} |  | The agent displays a near-death falling animation, with the direction of the fall controlled by two parameters: "Direction_Frontback" and "Direction_Rightleft". For example, (100, 0) indicates falling forward, while (-100, 0) indicates falling backward. |
| set_standup |  |  | The agent demonstrates an animation transitioning from a near-death fallen state to standing up, with the direction of the stand-up automatically matching the previous fall direction. |
| set_open_door | {1/0} |  | The agent open/close the door.(1 for open, 0 for close) |
| set_pickup |  |  | The agent pick/drop a item. |




Class Name: BP_animal_C


| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Navmesh and AI-controller built-in plugin to automatically control its movement to reach the goal via the shortest path. (The goal has to be reachable in the environment.) |
| nav_random |  |  | control agent randomly wandering around |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~27 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |




# 🚗Cars

Class Name: BP_BaseCar_C

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| set_stop |  |  | stop the car with handbrake |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Nav mesh to calculate the legal path and control the target moving to the goal. (The goal has to be reachable in the environment.) |
|  |  |  |  |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~2 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |
| enter_exit_car | {player index} |  | Human character interactions with cars involve standing near the car door. When the character stands close to the door and executes the corresponding command with the character index, it triggers animations for entering and exiting the car, which can be repeated by executing the command again |



# 🏍️Motorbikes

Class Name: MotorBikes_C

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Nav mesh to calculate the legal path and control the target moving to the goal. (The goal has to be reachable in the environment.) |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~8 |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |




Mobile Rbots share the same class with human characters (BP_character_C), developers could directly use set_app to change the mesh into robotdog(id:20~33).


| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {angular} {velocity} |  | control the object for a single step with angle and linear velocity: |
| nav_to_goal | {x} {y} {z} |  | Assign the agent a navigation goal, and use Navmesh and AI-controller built-in plugin to automatically control its movement to reach the goal via the shortest path. (The goal has to be reachable in the environment.) |
| nav_to_target | {target_object} {distance} |  | Assign the current agent to a target_object, utilize Navmesh and AI controller to dynamically follow the target_object, stopping at a specified distance from it |
| nav_random |  |  | control agent randomly wandering around |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam  | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_app  | {id} |  | set the appearance of the agent object, id: 20~33 |
| set_photo_mode |  |  | Switch the perspective to the first-person view of the agent. Change it back to the third-person view while executing the command a second time. |
| generate_nav_goal |  | { ”nav_goal”: “X=0.00 Y=0.00 Z=0.00” } | generate a reachable goal location around the agent, return the location. |
|  |  |  |  |
| get_hit |  | { ”hitresult”: “true(or false)” } | get the hit flag(with other target or static object) of the agent object, return true or false. |
| get_speed |  | { ”speed”: “0.000” } | get the agent’s linear velocity, return value |
| get_angle |  | { ”angle”: “0.000” } | get the agent’s angular velocity, return value |
|  |  |  |  |



Class Name: BP_Drone01_C

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| set_move | {x} {y} {z} {yaw} |  | control the object with force of each axis(x,y,z, yaw), between -1 and 1 |
| set_rotation | {yaw} |  | Set the absolute rotation position of the drone in the world coordinate system. |
| set_speed | {speed} |  | set the max velocity of the agent object |
| set_interval | {value} |  | set the interval of the time to simulate animation. value: 1 ~ 1000 |
| set_acc | {acceleration} |  | set the max acceleration of the agent object |
| set_phy  | {value} |  | simulate physics, 0: turn off, 1 :turn on |
| set_cam | {x} {y} {z} {row} {pitch} {yaw}  |  | set the camera pose relative to the actor |
| set_viewport |  |  | After executing this command, the Game window will display the agent's first-person perspective. Enter the command again to switch the window to display the free-roaming perspective. |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |




This interactive must be incorporated with a human character

vbp {character name} set_pickup 


Class Name： BP_GrabMoveDrop_C 

vbp {instance_name} {bp_function} {args1} {args2} ... 

| BP_function | input  | output  | help |
| --- | --- | --- | --- |
| is_picked |  | { “is_picked”：“0” } | return the object state, is picked or not (0/1) |
| set_app  | {id} |  | set the appearance of the agent object, id: 0~20 |



## 💡Hint

You could manually spawn pickable objects and set their location by calling the unrealcv api:

self.unrealcv.set_new_obj(self, class_name, obj_name) 

self.unrealcv.set_obj_location(self, obj, loc)

Example:

self.unrealcv.set_new_obj(self, BP_GrabMoveDrop_C, pickable_object_1)  

self.unrealcv.set_obj_location(self, pickable_object_1, [0,0,100])



# Examples

### 1. Basic movement control

```python
vbp bp_character_2 set_move 0 100
vbp bp_character_2 set_move 20 100
# Control the movement of the agent step by step, 
# specifying the movement speed and direction through given angle and speed parameters. 
# The interval time for single-step execution can be customized and adjusted using "set_interval" 
```


### 2. Advanced movement control

```python
# For further complex environment exploration task 

vbp bp_character_2 set_crouch 
vbp bp_character_2 set_move 0 100
# Set crouch and walk across some narrow obstacles
```

```python
vbp bp_character_2 set_move 45 100
vbp bp_character_2 set_jump 
# while agent faces some low obstacles, the agent could jump and climb over the obstacles
```

```python
vbp bp_character_2 set_liedown 100 0
vbp bp_character_2 set_standup 
# Simulate the actions of falling down， given the direction of falling, 
# as well as the recovery animation.
```

### 3. Control movement via navigation system

```python
vbp bp_character_2 nav_to_object bp_animal_2 200
# using navigation system control the bp_character move to a specific object (bp_animal_2),
# and stop when reaching a radius range of 200 
```

```python
vbp Sport_2 set_viewport
vbp bp_basecar_2 nav_to_goal -1620 -3071 487
vbp Sport_2 set_viewport
# Display the first-person view of motorbike agent.
# Using navigation system control the motorbike agent navigates to a given location in the environment, following the shortest path
# Display the free-roaming perspective 
```


### 4. Pick/Drop up an object

```python
vbp bp_character_2 set_pickup
# Display the Third-person view of human agent.
# When the human agent reached in the range of interactive object, 
#'set_pickup' command or press keyboard 'E' will trigger the object interaction animation. 
# call set_pickup again, the agent will drop the object. 

```


### 5. Open a door

```python
vbp bp_character_2 set_opendoor 1 #open door
vbp bp_character_2 set_opendoor 0 #close door

# Display the First-person view of human agent.
# When the human agent reached in the range of interactive door, 
#'set_opendoor' command or press keyboard 'E' will trigger the door interaction animation. 
```


