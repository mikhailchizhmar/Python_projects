import sys
import time


class Main:
    def custom_range(self, start, stop, step):
        """
        custom function for range
        :param start:
        :param stop:
        :param step:
        :return:
        """
        i = start
        while i < stop:
            yield i
            i += step

    def run(self):
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
        step = int(sys.argv[3])
        if len(sys.argv) < 5:
            time_delay = 3
            number_of_starts = 2
        else:
            time_delay = int(sys.argv[4])
            number_of_starts = int(sys.argv[5])
        count = 0

        while count < number_of_starts:
            for i in self.custom_range(start, stop, step):
                print(i)
            time.sleep(time_delay)
            count += 1


if __name__ == "__main__":
    main1 = Main()
    main1.run()
