import numpy as np
from scipy import signal


def search_closest_match(vec,center,tolerance):
    for i in range(tolerance*2):
        j = i / 2 if i % 2 == 0 else (i - 1) / (-2)
        if center + j in vec:
            return center + j
    return -1



class peakTracker():

    def __init__(self):
        self.peaks = []
        self.tick = 0
        self.hr = -1
        self.hr_candidates = []
        self.hr_window = 2
        self.hr_history = np.zeros(self.hr_window)
        self.tolerance = 5


    def _find_peaks(self,frequencies):
        return signal.find_peaks_cwt(frequencies,np.arange(1,10))


    def _extract_heart_rate(self):
        last_signal = self.peaks[self.tick]
        if self.hr == -1:
            # searching for initial hr
            print('dont know yet. For now:')
            HR = 25
            proposed_hr = search_closest_match(last_signal, HR, self.tolerance*5)
        else:
            # hr is already known - track changes
            proposed_hr = search_closest_match(last_signal, self.hr, self.tolerance*5)
        if proposed_hr != -1:
            if np.abs(proposed_hr - self.hr) > self.tolerance and self.hr != -1:
                print('HR jumped from '+str(int(self.hr))+' to '+str(int(proposed_hr)))
            self.hr_history[self.tick%self.hr_window] = proposed_hr
            if self.tick+1 >= self.hr_window:
                self.hr = np.average(self.hr_history)
            else:
                self.hr = np.average(self.hr_history[0:self.tick+1])
            return self.hr
        # hr changed more that tolerant or no hr yet


    def peak_tracker(self,frequencies):
        peakid = self._find_peaks(frequencies)
        self.peaks.append(peakid)
        self._extract_heart_rate()
        self.tick += 1


# 9,24,40
Data =[[0,0,0,1,2,2,3,7,19,55,32,17,5,1,0,0,0,0,0,1,2,6,10,26,93,74,52,14,1,0,0,0,0,0,1,4,7,4,19,43,69,56,32,57,11,1,0],
       [0, 0, 0, 1, 2, 2, 3, 7, 19, 34, 44, 17, 5, 1, 0, 0, 0, 0, 0, 1, 2, 6, 10, 26, 82, 95, 52, 14, 1, 0, 0, 0, 0, 0,
        1, 4, 7, 4, 19, 43, 56, 87, 32, 57, 11, 1, 0],
       [0, 0, 0, 1, 2, 2, 3, 7, 19, 55, 32, 17, 5, 1, 0, 0, 0, 0, 0, 1, 2, 6, 10, 26, 93, 74, 52, 14, 1, 0, 0, 0, 0, 0,
        1, 4, 7, 4, 19, 43, 69, 56, 32, 57, 11, 1, 0],
       [0, 0, 0, 1, 2, 2, 3, 7, 19, 55, 32, 17, 5, 1, 0, 0, 0, 0, 0, 1, 2, 6, 6, 6, 7, 7, 7, 14, 16,19,34, 45, 56, 78,
        99, 4, 7, 4, 19, 43, 69, 56, 32, 57, 11, 1, 0]]

      # Data = [[50,77,155],[52,79,200],[33,53,70,100],[56,94]]

def main():
    # xs = np.arange(0, np.pi*5, 0.05)
    # data = np.sin(xs)
    p = peakTracker()
    for data in Data:
        peakind = p.peak_tracker(data)
        #print(peakind)
        # print(peakind, xs[peakind], data[peakind])




if __name__ == '__main__':
    main()