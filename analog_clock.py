import tkinter as tk
import math
from datetime import datetime

class AnalogClock(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, width=400, height=400, bg='#f0f0f0', highlightthickness=0)
        self.center = (200, 200)
        self.radius = 190
        self.draw_face()
        # Create clock hands with high-contrast colors for readability
        self.hands = {
            'hour': self.create_line(0, 0, 0, 0, width=8, fill='#000000', capstyle=tk.ROUND),
            'minute': self.create_line(0, 0, 0, 0, width=5, fill='#000000', capstyle=tk.ROUND),
            'second': self.create_line(0, 0, 0, 0, width=2, fill='#d40000', capstyle=tk.ROUND)
        }
        self.update_clock()

    def draw_face(self):
        cx, cy = self.center
        # Metallic radial gradient with lighter tones for better contrast
        for r in range(self.radius, 0, -1):
            shade = 200 + int(55 * (r / self.radius))
            color = f'#{shade:02x}{shade:02x}{shade:02x}'
            self.create_oval(cx - r, cy - r, cx + r, cy + r, outline=color)
        # Tick marks with strong contrast
        for i in range(60):
            angle = math.pi / 30 * i
            inner = self.radius - 15 if i % 5 == 0 else self.radius - 10
            outer = self.radius - 5
            x0 = cx + inner * math.sin(angle)
            y0 = cy - inner * math.cos(angle)
            x1 = cx + outer * math.sin(angle)
            y1 = cy - outer * math.cos(angle)
            width = 4 if i % 5 == 0 else 1
            color = '#000000' if i % 5 == 0 else '#666666'
            self.create_line(x0, y0, x1, y1, fill=color, width=width)
        # Center cap
        self.create_oval(cx - 8, cy - 8, cx + 8, cy + 8, fill='#000000', outline='')

    def update_clock(self):
        now = datetime.now()
        hour = (now.hour % 12) + now.minute / 60.0
        minute = now.minute + now.second / 60.0
        second = now.second + now.microsecond / 1e6

        self.set_hand('hour', hour / 12 * 2 * math.pi, length=100)
        self.set_hand('minute', minute / 60 * 2 * math.pi, length=150)
        self.set_hand('second', second / 60 * 2 * math.pi, length=170)

        self.after(1000, self.update_clock)

    def set_hand(self, hand, angle, length):
        cx, cy = self.center
        x = cx + length * math.sin(angle)
        y = cy - length * math.cos(angle)
        self.coords(self.hands[hand], cx, cy, x, y)


def main():
    root = tk.Tk()
    root.title('Analog Clock')
    clock = AnalogClock(root)
    clock.pack()
    root.mainloop()


if __name__ == '__main__':
    main()