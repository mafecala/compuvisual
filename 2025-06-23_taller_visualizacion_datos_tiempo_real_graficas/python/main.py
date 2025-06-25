import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import threading
from queue import Queue

class DataGenerator:
    def __init__(self, data_type="sine", queue=None):
        self.data_type = data_type
        self.t = 0
        self.queue = queue
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.data_type == "sine":
            value = np.sin(self.t)
        elif self.data_type == "random":
            value = np.random.normal(0, 1)
        else:
            value = np.random.randint(0, 100)
            
        self.t += 0.1
        
        # Put value in queue for console display
        if self.queue is not None:
            self.queue.put((self.data_type, value))
            
        return value

def console_printer(queue):
    """Print data values in console"""
    while True:
        if not queue.empty():
            data_type, value = queue.get()
            print(f"{data_type}: {value:.3f}")
        time.sleep(0.1)

class RealtimeLinePlot:
    def __init__(self, max_points=100, title="Real-time Data", subplot_pos=None):
        self.max_points = max_points
        self.times = np.array([])
        self.values = np.array([])
        
        if subplot_pos:
            self.fig = plt.figure(figsize=(12, 5))
            self.ax = self.fig.add_subplot(subplot_pos)
        else:
            self.fig, self.ax = plt.subplots()
            
        self.line, = self.ax.plot([], [], 'b-', lw=2)
        
        self.ax.set_xlim(0, 30)
        self.ax.set_ylim(-1.5, 1.5)
        self.ax.grid(True)
        self.ax.set_title(title)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Value')
        
    def init(self):
        self.line.set_data([], [])
        return self.line,
        
    def update(self, frame):
        current_time = time.time()
        new_value = frame
        
        self.times = np.append(self.times, current_time)
        self.values = np.append(self.values, new_value)
        
        if len(self.times) > self.max_points:
            self.times = self.times[-self.max_points:]
            self.values = self.values[-self.max_points:]
            
        self.line.set_data(self.times - self.times[0], self.values)
        self.ax.set_xlim(0, max(30, self.times[-1] - self.times[0]))
        
        return self.line,
        
    def animate(self, data_generator, interval=50):
        anim = FuncAnimation(self.fig, self.update,
                           init_func=self.init,
                           frames=data_generator,
                           interval=interval,
                           cache_frame_data=False,
                           blit=True)
        plt.show()

def demo_both_with_console():
    # Create queue for console output
    data_queue = Queue()
    
    # Create data generators with queue
    sine_gen = DataGenerator(data_type="sine", queue=data_queue)
    random_gen = DataGenerator(data_type="random", queue=data_queue)
    
    # Start console printer thread
    console_thread = threading.Thread(target=console_printer, args=(data_queue,))
    console_thread.daemon = True
    console_thread.start()
    
    # Create two plots side by side
    plot1 = RealtimeLinePlot(title="Real-time Sine Wave", subplot_pos=121)
    plot2 = RealtimeLinePlot(title="Real-time Random Data", subplot_pos=122)
    
    # Adjust layout
    plt.tight_layout()
    
    # Create two animation objects
    anim1 = FuncAnimation(plot1.fig, plot1.update,
                         init_func=plot1.init,
                         frames=sine_gen,
                         interval=50,
                         cache_frame_data=False,
                         blit=True)
                         
    anim2 = FuncAnimation(plot1.fig, plot2.update,
                         init_func=plot2.init,
                         frames=random_gen,
                         interval=50,
                         cache_frame_data=False,
                         blit=True)
    
    plt.show()

def main():
    print("Visualizing data with console output...")
    print("Press Ctrl+C to exit")
    print("\nData values:")
    demo_both_with_console()

if __name__ == "__main__":
    main()