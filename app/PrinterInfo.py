import urequests
import lvgl as lv

class PrinterInfo():
    def __init__(self, url, update_interval = 5000):
        self.url = url
        self.stats = {}
        self.fetch()
        self.timer = lv.timer_create(self.update, update_interval, None)

    def update(self, timer):
        self.fetch()

    def fetch(self):
        # print(lv.tick_get())
        response = urequests.get(self.url)
        # print(lv.tick_get())
        parsed = response.json()
        # print(lv.tick_get())
        response.close()

        duration = parsed['result']['status']['print_stats']['print_duration']

        progress = parsed['result']['status']['display_status']['progress']
        # print(parsed)

        if (progress == 0):
            totalTime = 0
        else:
            totalTime = duration / progress
        eta = totalTime - duration
        
        self.stats = {
            "state": parsed['result']['status']['print_stats']['state'],
            "filename": parsed['result']['status']['print_stats']['filename'],
            "print_duration": round(duration, 2),
            "progress": round(progress, 2),
            "totalTime": totalTime,
            "eta": eta,
            "bed": parsed['result']['status']['heater_bed'],
            "extruder": parsed['result']['status']['extruder']
        }

        # print(self.stats["filename"])
        
# def get_stats():
#     response = urequests.get(quickStatsURL)
# #     print(response.status_code)
# #     print(response.reason)
#     parsed = response.json()
#     response.close()
    
#     duration = parsed['result']['status']['print_stats']['print_duration']

#     progress = parsed['result']['status']['display_status']['progress']
# #     print(parsed)

#     if (progress == 0):
#         totalTime = 0
#     else:
#         totalTime = duration / progress
#     eta = totalTime - duration
    
#     stats = {
#         "state": parsed['result']['status']['print_stats']['state'],
#         "filename": parsed['result']['status']['print_stats']['filename'],
#         "print_duration": round(duration, 2),
#         "progress": round(progress, 2),
#         "totalTime": totalTime,
#         "eta": eta,
#         "bed": parsed['result']['status']['heater_bed'],
#         "extruder": parsed['result']['status']['extruder']
#     }
    
#     return stats

