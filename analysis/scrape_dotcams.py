import time
import requests
import os

cams_dict = {'Queensboro_60thst' : 'https://webcams.nyctmc.org/api/cameras/d83aed40-b117-424b-8caf-35c3afe82527/image?t=1697576091936',
             'BB25' : 'https://webcams.nyctmc.org/api/cameras/4f688c33-672c-4bac-bf2b-98438d464ccd/image?t=1697548827548',
             '7thave_23st': 'https://webcams.nyctmc.org/api/cameras/fcfbaa3d-13e5-4687-9688-ae1eab37c723/image?t=1697727190132',
             '8ave_49st' : 'https://webcams.nyctmc.org/api/cameras/4850e464-1111-4b5d-a72d-f54a0e12a789/image?t=1698153162583',
             'bway_46stN': 'https://webcams.nyctmc.org/api/cameras/f3d82b25-6b10-44c7-ae89-30df075a7ac8/image?t=1698759465348',
             'bway_51st': 'https://webcams.nyctmc.org/api/cameras/3d8e276f-b179-414d-a506-679d5e559d3e/image?t=1698759641304',
             'atlantic_vanderbilt' : 'https://webcams.nyctmc.org/api/cameras/b5d8fe4f-1cf5-4cd8-8211-8353e68da1cb/image?t=1698759748728',
             '4ave_union' : 'https://webcams.nyctmc.org/api/cameras/53d62ac5-34f9-4d8f-82b9-0cecebc9c55a/image?t=1698759703981',
             'BB44': 'https://webcams.nyctmc.org/api/cameras/26136ff4-a399-4cce-9a37-4d6331f5f1fb/image?t=1699148658436',
             'BB39': 'https://webcams.nyctmc.org/api/cameras/32651453-d9de-4cde-af4b-be42b8de2775/image?t=1699148698081'
}

start_time = time.time()
run_time = 60 * 180     #three hours
end_time = start_time + run_time  

while time.time() < end_time:
    
    for cam in cams_dict.keys():
        url = cams_dict[cam]    
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_filename = f"{cam}/image_{timestamp}.jpg"
            
            if not os.path.exists(f"{cam}/"):
                os.makedirs(f"{cam}/")
            with open(image_filename, "wb") as file:
                file.write(response.content)
                
            print(f"Saved {image_filename}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
            
        time.sleep(1)