import time


class TrafficLight(object):
    def __init__(self):
        self.color = None
        self._traffic_states = [{"color": "red",
                                 "duration": 7},
                                {"color": "yellow",
                                 "duration": 2},
                                {"color": "green",
                                 "duration": 5}
                                ]

    def _traffic_run_state(self, duration):
        for t in range(duration, 0, -1):
            print("{color} light: {time_left}".format(color=self.color, time_left=t))
            time.sleep(1)

    def running(self):
        for state in self._traffic_states:
            self.color = state["color"]
            self._traffic_run_state(state["duration"])


traffic_light = TrafficLight()
traffic_light.running()
